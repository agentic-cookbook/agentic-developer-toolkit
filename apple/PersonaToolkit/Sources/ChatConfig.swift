import Foundation

/// Bootstraps an Orchestrator. The Backend instance is supplied here;
/// the orchestrator does not know how it was built. A wholly-local
/// config supplies an in-process Backend; a server-backed config
/// supplies an HTTP/SSE one. Same Orchestrator, same UI either way.
public protocol ChatConfig: Sendable {
    var conversationID: String { get }

    /// The Participant.id of the local user. Exactly one participant in
    /// `initialParticipants` must match.
    var localParticipantID: String { get }

    var initialParticipants: [any Participant] { get }

    var commands: [any Command] { get }
    var observingHooks: [any ObservingHook] { get }
    var gatingHooks: [any GatingHook] { get }
    var permissionStore: any PermissionStore { get }

    var backend: any Backend { get }
    var display: any DisplayConfig { get }
}
