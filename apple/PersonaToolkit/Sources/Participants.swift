import Foundation

/// The role a participant plays in a Conversation. A Set so a single
/// participant can carry multiple roles simultaneously.
public enum ParticipantKind: Sendable, Hashable {
    case user        // the local human; UI renders on the right
    case persona     // a non-local actor (display attribution only)
    case observer    // present but cannot speak (read-only)
}

public enum ParticipantConversationState: Sendable, Hashable {
    case joining
    case joined
    case departing
    case departed
}

/// Pure attribution data: who is in this conversation, what to display,
/// and where to address messages. Participants have NO behavior — they do
/// not "take turns" or "produce responses." Active behavior lives behind
/// the Backend on whichever side actually runs the actor.
public protocol Participant: Sendable {
    var id: String { get }
    var displayName: String { get }
    var avatarURL: URL? { get }
    var profileURL: URL? { get }

    /// Routing address for the Backend (server-side persona slug, user
    /// account id, opaque token, …). Interpretation is backend-specific.
    var address: String { get }

    var kinds: Set<ParticipantKind> { get }
    var conversationState: ParticipantConversationState { get }
}
