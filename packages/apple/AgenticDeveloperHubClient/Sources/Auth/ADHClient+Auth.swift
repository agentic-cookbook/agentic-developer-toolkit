import OpenAPIRuntime

/// Thin convenience wrappers over the generated auth operations. They are just
/// ergonomics — the same calls are available on ``ADHClient/api`` directly — but
/// they save callers from spelling out the long generated request/response type
/// names and wire the result into the credential store.
extension ADHClient {

    /// The backend's auth payload returned by ``login(email:password:)``
    /// (contains `token`, `refreshToken`, and `user`).
    public typealias AuthResponse = Components.Schemas.Company_temporal_backend_routes_AuthResponse

    /// A freshly minted API token returned by ``createAPIToken(name:expiresAt:)``.
    /// Its `token` field is the only time the raw secret is exposed.
    public typealias CreatedAPIToken = Components.Schemas.Company_temporal_backend_routes_CreatedApiTokenResponse

    /// Email / password login (`POST /api/auth/login`). On success the returned
    /// JWT is persisted through the credential store, so every subsequent call
    /// on this client is authenticated.
    @discardableResult
    public func login(email: String, password: String) async throws -> AuthResponse {
        let output = try await api.postApiAuthLogin(body: .json(.init(email: email, password: password)))
        let auth = try output.ok.body.json
        credentials.save(Credentials(token: auth.token, kind: .jwt))
        return auth
    }

    /// Create a long-lived API token (`POST /api/auth/tokens`). Requires the
    /// client to already be authenticated (the middleware forwards the current
    /// credential).
    ///
    /// The raw token is returned for the caller to store wherever it belongs
    /// (e.g. handed to the daemon or a CI secret). It is deliberately **not**
    /// persisted here — minting a token must not silently replace the active
    /// session credential. Call ``adopt(_:)`` to switch this client to it.
    @discardableResult
    public func createAPIToken(name: String, expiresAt: String? = nil) async throws -> CreatedAPIToken {
        let output = try await api.postApiAuthTokens(body: .json(.init(expiresAt: expiresAt, name: name)))
        return try output.created.body.json
    }

    /// Persist a credential through the store, switching this client to it.
    public func adopt(_ credentials: Credentials) {
        self.credentials.save(credentials)
    }

    /// Forget the persisted credential (sign out). Subsequent calls are
    /// unauthenticated until the next ``login(email:password:)``.
    public func logout() {
        credentials.clear()
    }
}
