import Network

#if canImport(FoundationEssentials)
import FoundationEssentials
#else
import Foundation
#endif

/// A minimal in-process HTTP/1.1 server on loopback, modeled on DaemonKit's
/// `HTTPServer` (NWListener, 127.0.0.1, no TLS, connection-close per response).
/// It stands in for the future `adhd` daemon so ``DaemonTransport`` can be
/// exercised over a real socket without the daemon existing.
///
/// It records every request it receives and answers from a supplied handler;
/// the default handler honors the ``DaemonContract`` `GET /health` and returns a
/// health-shaped 200 for anything else, so a typed operation round-trips.
final class MockDaemonServer: @unchecked Sendable {

    struct ReceivedRequest: Sendable {
        var method: String
        var path: String
        var headers: [String: String]   // lowercased names
        var body: Data
    }

    struct Response: Sendable {
        var status: Int = 200
        var headers: [String: String] = ["Content-Type": "application/json"]
        var body: Data = Data(#"{"status":"ok","version":"mock"}"#.utf8)
    }

    private let queue = DispatchQueue(label: "MockDaemonServer", qos: .utility)
    private let handler: @Sendable (ReceivedRequest) -> Response
    private let lock = NSLock()
    private var _requests: [ReceivedRequest] = []
    private var listener: NWListener?
    private let ready = DispatchSemaphore(value: 0)
    private(set) var port: UInt16 = 0

    init(handler: @escaping @Sendable (ReceivedRequest) -> Response = { _ in Response() }) {
        self.handler = handler
    }

    /// All requests received so far, in arrival order.
    var requests: [ReceivedRequest] { lock.withLock { _requests } }

    /// Bind an OS-assigned loopback port and block until ready. Returns the port.
    @discardableResult
    func start(timeout: TimeInterval = 5) throws -> UInt16 {
        let listener = try NWListener(using: .tcp)
        listener.newConnectionHandler = { [weak self] connection in self?.accept(connection) }
        listener.stateUpdateHandler = { [weak self] state in
            guard let self else { return }
            switch state {
            case .ready:
                self.port = self.listener?.port?.rawValue ?? 0
                self.ready.signal()
            case .failed:
                self.ready.signal()
            default:
                break
            }
        }
        self.listener = listener
        listener.start(queue: queue)
        _ = ready.wait(timeout: .now() + timeout)
        return port
    }

    func stop() {
        listener?.cancel()
        listener = nil
    }

    // MARK: - Connection handling

    private func accept(_ connection: NWConnection) {
        connection.start(queue: queue)
        receive(connection, buffer: Data())
    }

    private func receive(_ connection: NWConnection, buffer: Data) {
        connection.receive(minimumIncompleteLength: 1, maximumLength: 65536) { [weak self] data, _, isComplete, error in
            guard let self else { connection.cancel(); return }
            var buffer = buffer
            if let data { buffer.append(data) }

            if let request = Self.parse(buffer) {
                self.lock.withLock { self._requests.append(request) }
                self.send(self.handler(request), on: connection)
            } else if error != nil || isComplete {
                connection.cancel()
            } else {
                self.receive(connection, buffer: buffer)  // request not yet complete
            }
        }
    }

    /// Parse a complete HTTP/1.1 request, or `nil` if more bytes are needed.
    private static func parse(_ buffer: Data) -> ReceivedRequest? {
        let separator = Data("\r\n\r\n".utf8)
        guard let headerRange = buffer.range(of: separator),
              let headerText = String(data: buffer[..<headerRange.lowerBound], encoding: .utf8)
        else { return nil }

        let lines = headerText.components(separatedBy: "\r\n")
        let requestLine = lines.first?.split(separator: " ") ?? []
        guard requestLine.count >= 2 else { return nil }

        var headers: [String: String] = [:]
        for line in lines.dropFirst() {
            guard let colon = line.firstIndex(of: ":") else { continue }
            let name = line[..<colon].trimmingCharacters(in: .whitespaces).lowercased()
            let value = line[line.index(after: colon)...].trimmingCharacters(in: .whitespaces)
            headers[name] = value
        }

        let contentLength = headers["content-length"].flatMap(Int.init) ?? 0
        let bodyBytes = buffer[headerRange.upperBound...]
        guard bodyBytes.count >= contentLength else { return nil }

        return ReceivedRequest(
            method: String(requestLine[0]),
            path: String(requestLine[1]),
            headers: headers,
            body: contentLength > 0 ? Data(bodyBytes.prefix(contentLength)) : Data()
        )
    }

    private func send(_ response: Response, on connection: NWConnection) {
        var headers = response.headers
        headers["Content-Length"] = String(response.body.count)
        headers["Connection"] = "close"
        var head = "HTTP/1.1 \(response.status) \(Self.reason(response.status))\r\n"
        for (name, value) in headers { head += "\(name): \(value)\r\n" }
        head += "\r\n"

        var out = Data(head.utf8)
        out.append(response.body)
        connection.send(content: out, completion: .contentProcessed { _ in connection.cancel() })
    }

    private static func reason(_ status: Int) -> String {
        switch status {
        case 200: return "OK"
        case 404: return "Not Found"
        case 500: return "Internal Server Error"
        default: return "Status"
        }
    }
}
