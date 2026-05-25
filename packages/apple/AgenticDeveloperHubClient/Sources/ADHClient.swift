import OpenAPIRuntime

#if canImport(FoundationEssentials)
import FoundationEssentials
#else
import Foundation
#endif

/// The entry point to the Agentic Developer Hub API.
///
/// `ADHClient` is a thin façade over the generated `Client`: it wires a chosen
/// ``APITransport`` (Direct or Daemon) to the typed surface and attaches the
/// ``AuthenticationMiddleware`` so every request carries the bearer token. The
/// generated client is exposed directly as ``api`` — consumers call the full,
/// typed API through it (e.g. `client.api.postApiAuthLogin(...)`).
///
/// The transport is the only point of variation: Direct and Daemon produce an
/// identical `Client`, differing only by the `(serverURL, transport)` pair the
/// ``APITransport`` carries. Pick one explicitly via ``direct(credentials:)`` /
/// ``daemon(credentials:)``, or let ``TransportResolver`` choose at runtime.
public struct ADHClient: Sendable {

    /// The full generated typed API. Call any operation directly on this.
    public let api: Client

    /// Which endpoint this client is wired to — useful for diagnostics and for
    /// the resolver's caching.
    public let transportKind: TransportKind

    /// The credential store backing the attached ``AuthenticationMiddleware``.
    /// Held so the auth convenience wrappers can persist tokens through it.
    let credentials: any CredentialStore

    /// Builds a client over the given transport.
    /// - Parameters:
    ///   - transport: the Direct/Daemon transport seam to talk through.
    ///   - credentials: the credential store the auth middleware reads from and
    ///     the auth wrappers write to. Defaults to the Keychain-backed store.
    public init(
        transport: APITransport,
        credentials: any CredentialStore = KeychainCredentialStore()
    ) {
        self.transportKind = transport.kind
        self.credentials = credentials
        self.api = Client(
            serverURL: transport.serverURL,
            transport: transport.transport,
            middlewares: [AuthenticationMiddleware(credentials: credentials)]
        )
    }
}

extension ADHClient {

    /// A client wired straight to the backend over HTTPS.
    public static func direct(
        credentials: any CredentialStore = KeychainCredentialStore()
    ) -> ADHClient {
        ADHClient(transport: .direct(), credentials: credentials)
    }

    /// A client wired to the local `adhd` daemon. Use only when the daemon is
    /// known to be reachable — prefer ``TransportResolver`` to choose safely.
    public static func daemon(
        credentials: any CredentialStore = KeychainCredentialStore()
    ) -> ADHClient {
        ADHClient(transport: .daemon(), credentials: credentials)
    }

    /// The recommended entry point: ask a ``TransportResolver`` whether the
    /// daemon is reachable and wire the client to whichever transport it picks
    /// (Daemon if up, else Direct). Defaults to an auto-resolving probe.
    public static func resolved(
        using resolver: TransportResolver = TransportResolver(),
        credentials: any CredentialStore = KeychainCredentialStore()
    ) async -> ADHClient {
        let transport: APITransport = switch await resolver.resolve() {
        case .daemon: .daemon(port: resolver.port)
        case .direct: .direct()
        }
        return ADHClient(transport: transport, credentials: credentials)
    }
}
