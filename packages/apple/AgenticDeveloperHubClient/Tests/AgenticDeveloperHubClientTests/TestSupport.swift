import HTTPTypes
import OpenAPIRuntime

#if canImport(FoundationEssentials)
import FoundationEssentials
#else
import Foundation
#endif

/// A thread-safe mutable holder, so `@Sendable` test closures can record a value
/// under Swift 6 strict concurrency without data-race diagnostics.
final class Box<T>: @unchecked Sendable {
    private let lock = NSLock()
    private var value: T
    init(_ value: T) { self.value = value }
    var get: T { lock.withLock { value } }
    func set(_ newValue: T) { lock.withLock { value = newValue } }
}

/// A `ClientTransport` that records every request it receives and returns a
/// caller-supplied response. This is the hermetic seam under the generated
/// `Client`: it proves the codegen → middleware → transport chain wires up and
/// lets tests assert on the exact `HTTPRequest` the stack produced.
final class MockClientTransport: ClientTransport, @unchecked Sendable {

    struct Recorded: Sendable {
        var request: HTTPRequest
        var baseURL: URL
        var operationID: String
    }

    private let lock = NSLock()
    private var _recorded: [Recorded] = []
    private let responder: @Sendable (HTTPRequest) -> (HTTPResponse, HTTPBody?)

    /// - Parameter responder: produces the response for a given request.
    ///   Defaults to a `200` health payload (`{"status":"ok"}`).
    init(responder: @escaping @Sendable (HTTPRequest) -> (HTTPResponse, HTTPBody?) = { _ in MockClientTransport.healthOK() }) {
        self.responder = responder
    }

    var recorded: [Recorded] { lock.withLock { _recorded } }
    var lastRequest: HTTPRequest? { lock.withLock { _recorded.last?.request } }
    var lastBaseURL: URL? { lock.withLock { _recorded.last?.baseURL } }

    func send(
        _ request: HTTPRequest,
        body: HTTPBody?,
        baseURL: URL,
        operationID: String
    ) async throws -> (HTTPResponse, HTTPBody?) {
        lock.withLock {
            _recorded.append(.init(request: request, baseURL: baseURL, operationID: operationID))
        }
        return responder(request)
    }

    /// A valid `GET /health` 200 response the generated `getHealth` deserializer accepts.
    static func healthOK() -> (HTTPResponse, HTTPBody?) {
        var response = HTTPResponse(status: .ok)
        response.headerFields[.contentType] = "application/json"
        return (response, HTTPBody(Data(#"{"status":"ok"}"#.utf8)))
    }
}

/// A `URLProtocol` that intercepts `URLSession` traffic so a real
/// `URLSessionTransport` can be exercised end-to-end without a network. Install
/// it via `URLSessionConfiguration.protocolClasses` and set a handler.
final class StubURLProtocol: URLProtocol {

    struct Stub: Sendable {
        var statusCode: Int = 200
        var headers: [String: String] = ["Content-Type": "application/json"]
        var body: Data = Data(#"{"status":"ok"}"#.utf8)
        /// When set, `startLoading()` fails the request with this error instead of
        /// returning a response — simulates a `URLSession` transport failure (e.g.
        /// `URLError.notConnectedToInternet`) so callers can assert their mapping
        /// from transport errors to a domain failure.
        var error: (any Error)? = nil
    }

    private static let lock = NSLock()
    nonisolated(unsafe) private static var handler: (@Sendable (URLRequest) -> Stub)?
    nonisolated(unsafe) private static var captured: [URLRequest] = []

    static func install(_ handler: @escaping @Sendable (URLRequest) -> Stub) {
        lock.withLock {
            self.handler = handler
            self.captured = []
        }
    }

    static func reset() {
        lock.withLock {
            handler = nil
            captured = []
        }
    }

    static var capturedRequests: [URLRequest] {
        lock.withLock { captured }
    }

    override class func canInit(with request: URLRequest) -> Bool { true }
    override class func canonicalRequest(for request: URLRequest) -> URLRequest { request }

    override func startLoading() {
        let request = self.request
        let stub: Stub = Self.lock.withLock {
            Self.captured.append(request)
            return Self.handler?(request) ?? Stub()
        }
        if let error = stub.error {
            client?.urlProtocol(self, didFailWithError: error)
            return
        }
        let response = HTTPURLResponse(
            url: request.url!,
            statusCode: stub.statusCode,
            httpVersion: "HTTP/1.1",
            headerFields: stub.headers
        )!
        client?.urlProtocol(self, didReceive: response, cacheStoragePolicy: .notAllowed)
        client?.urlProtocol(self, didLoad: stub.body)
        client?.urlProtocolDidFinishLoading(self)
    }

    override func stopLoading() {}
}
