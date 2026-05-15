import Foundation

/// What kind of change happened. The UI re-reads snapshot accessors on
/// the ChatViewModel to learn the new state.
public enum ChatUpdate: Sendable {
    case messagesChanged
    case messageStatusChanged(messageID: String)
    case participantsChanged
    case typingChanged
    case readReceiptsChanged
    case widgetPresented(widgetID: String)
    case widgetResolved(widgetID: String)
    case permissionRequested(promptID: String)
    case permissionResolved(promptID: String)
    case displayConfigChanged
    case error(message: String)
}

public protocol ChatStateObserver: AnyObject, Sendable {
    func chatStateDidChange(_ change: ChatUpdate) async
}

/// The single surface between the UI and the toolkit. UI binds to a
/// `ChatViewModel`; it never imports anything else from the toolkit
/// internals (Backend, Hooks, Commands, …).
///
/// State delivery is abstracted via `ChatStateObserver`: the UI registers
/// as an observer and re-reads snapshot accessors after each
/// `chatStateDidChange`. Concrete implementations may back this with
/// `@Observable`, Combine, AsyncStream, or anything else.
public protocol ChatViewModel: AnyObject, Sendable {

    // --- Snapshots (UI reads to render) ------------------------------

    var conversation: any Conversation { get async }
    var participants: [any Participant] { get async }
    var messages: [any Message] { get async }
    var displayConfig: any DisplayConfig { get async }

    var pendingPermissions: [any PermissionPrompt] { get async }
    var pendingWidgets: [any InteractiveWidget] { get async }

    /// Participants currently typing (excluding the local user).
    var typingParticipants: Set<String> { get async }

    // --- Observation -------------------------------------------------

    func addObserver(_ observer: any ChatStateObserver) async
    func removeObserver(_ observer: any ChatStateObserver) async

    // --- Actions from UI --------------------------------------------

    /// Compose and submit a message. Returns the local id immediately so
    /// the UI can correlate a transcript row with later status changes.
    @discardableResult
    func submitMessage(_ text: String,
                       attachments: [any Attachment]) async throws -> String

    /// The local user has visually seen a received message; the
    /// orchestrator forwards a read receipt through the Backend.
    func markRead(messageID: String) async

    /// Local user typing state changed.
    func setLocalTyping(_ isTyping: Bool) async

    func respondToWidget(_ response: any WidgetResponse) async

    func respondToPermission(promptID: String,
                             decision: PermissionDecision) async

    /// Discover available commands. Backs slash-command palettes / `/`
    /// auto-complete.
    func listCommands(matching filter: String?) async -> [any Command]
}
