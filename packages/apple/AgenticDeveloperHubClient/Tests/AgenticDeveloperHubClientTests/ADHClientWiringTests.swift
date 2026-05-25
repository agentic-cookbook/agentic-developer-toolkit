import HTTPTypes
import OpenAPIRuntime
import Testing

#if canImport(FoundationEssentials)
import FoundationEssentials
#else
import Foundation
#endif

@testable import AgenticDeveloperHubClient

/// Hermetic tests for the `ADHClient` façade: the generated typed client routes
/// through the chosen ``APITransport``, the ``AuthenticationMiddleware`` injects
/// the bearer, and a typed operation round-trips. No network — a
/// ``MockClientTransport`` stands in for the wire.
@Suite("ADHClient wiring")
struct ADHClientWiringTests {

    private func client(
        kind: TransportKind = .direct,
        serverURL: URL = DaemonContract.backendURL,
        token: String? = "tok-abc",
        transport: MockClientTransport
    ) -> ADHClient {
        let creds = InMemoryCredentialStore(token.map { Credentials(token: $0, kind: .jwt) })
        return ADHClient(
            transport: APITransport(kind: kind, serverURL: serverURL, transport: transport),
            credentials: creds
        )
    }

    @Test("direct factory targets the backend over HTTPS")
    func directFactoryTargetsBackend() {
        let t = APITransport.direct()
        #expect(t.kind == .direct)
        #expect(t.serverURL == DaemonContract.backendURL)
    }

    @Test("daemon factory targets loopback on the contract port")
    func daemonFactoryTargetsLoopback() {
        let t = APITransport.daemon()
        #expect(t.kind == .daemon)
        #expect(t.serverURL == DaemonContract.daemonURL())
        #expect(t.serverURL.absoluteString == "http://127.0.0.1:\(DaemonContract.port)")
    }

    @Test("a typed operation routes through the transport and decodes")
    func typedOperationRoundTrips() async throws {
        let mock = MockClientTransport()
        let adh = client(transport: mock)

        let output = try await adh.api.getHealth()

        // Decoded the 200 body the mock returned.
        let body = try output.ok.body.json
        #expect(body.additionalProperties["status"] == "ok")

        // The generated client produced the right request and handed it to our transport.
        let recorded = try #require(mock.recorded.last)
        #expect(recorded.request.method == .get)
        #expect(recorded.request.path == "/health")
        #expect(recorded.operationID == "get/health")
        #expect(recorded.baseURL == DaemonContract.backendURL)
    }

    @Test("auth middleware injects the bearer on outgoing requests")
    func authHeaderInjected() async throws {
        let mock = MockClientTransport()
        let adh = client(token: "tok-abc", transport: mock)

        _ = try await adh.api.getHealth()

        let request = try #require(mock.lastRequest)
        #expect(request.headerFields[.authorization] == "Bearer tok-abc")
    }

    @Test("no Authorization header when there is no credential")
    func noAuthHeaderWhenUnauthenticated() async throws {
        let mock = MockClientTransport()
        let adh = client(token: nil, transport: mock)

        _ = try await adh.api.getHealth()

        let request = try #require(mock.lastRequest)
        #expect(request.headerFields[.authorization] == nil)
    }

    @Test("Direct and Daemon differ only by base URL — same auth, same request")
    func transportsDifferOnlyByBaseURL() async throws {
        let directMock = MockClientTransport()
        let daemonMock = MockClientTransport()

        let direct = client(kind: .direct, serverURL: DaemonContract.backendURL, token: "tok-xyz", transport: directMock)
        let daemon = client(kind: .daemon, serverURL: DaemonContract.daemonURL(), token: "tok-xyz", transport: daemonMock)

        _ = try await direct.api.getHealth()
        _ = try await daemon.api.getHealth()

        let directReq = try #require(directMock.lastRequest)
        let daemonReq = try #require(daemonMock.lastRequest)

        // Identical request shape and identical auth on both transports …
        #expect(directReq.method == daemonReq.method)
        #expect(directReq.path == daemonReq.path)
        #expect(directReq.headerFields[.authorization] == daemonReq.headerFields[.authorization])
        #expect(directReq.headerFields[.authorization] == "Bearer tok-xyz")

        // … only the base URL the transport receives differs.
        #expect(directMock.lastBaseURL == DaemonContract.backendURL)
        #expect(daemonMock.lastBaseURL == DaemonContract.daemonURL())
        #expect(directMock.lastBaseURL != daemonMock.lastBaseURL)
    }

    @Test("transportKind is carried through from the transport")
    func transportKindCarried() {
        #expect(ADHClient(transport: .direct(transport: MockClientTransport())).transportKind == .direct)
        #expect(ADHClient(transport: .daemon(transport: MockClientTransport())).transportKind == .daemon)
    }
}
