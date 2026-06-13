import Foundation

/// A bearer credential for the Agentic Developer Hub API.
///
/// The backend accepts two token shapes on the same `Authorization: Bearer`
/// channel (security scheme `BearerAuth`): short-lived JWTs from
/// `POST /auth/login`, and long-lived API tokens from
/// `POST /auth/tokens`. ``kind`` is informational — both are sent
/// identically as `Authorization: Bearer <token>`.
public struct Credentials: Sendable, Equatable, Codable {

    /// Which flavor of token this is. Does not affect how it is transmitted.
    public enum Kind: String, Sendable, Codable {
        case jwt
        case apiToken
    }

    public var token: String
    public var kind: Kind

    public init(token: String, kind: Kind) {
        self.token = token
        self.kind = kind
    }
}
