import Foundation

public enum PermissionDecision: Sendable, Hashable {
    case allowOnce
    case allowAlways
    case denyOnce
    case denyAlways
}

public protocol Permission: Sendable {
    var id: String { get }
    /// Human-facing template, e.g. "{actor} wants to read your calendar".
    var displayPromptTemplate: String { get }
    /// Applied when no stored decision exists; `nil` means always ask.
    var defaultDecision: PermissionDecision? { get }
}

public protocol PermissionPrompt: Sendable {
    var id: String { get }
    var permission: any Permission { get }
    var requesterParticipantID: String { get }
    var contextDescription: String { get }
}

public protocol PermissionStore: Sendable {
    func decision(for permissionID: String,
                  requesterID: String) async -> PermissionDecision?

    func remember(_ decision: PermissionDecision,
                  for permissionID: String,
                  requesterID: String) async
}
