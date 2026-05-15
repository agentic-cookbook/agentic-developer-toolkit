import Foundation

public protocol ChatViewModel: AnyObject, Sendable {
    var conversation: any Conversation { get }
    var participants: [any Participant] { get }
    var messages: [any Message] { get }
    var displayConfig: any DisplayConfig { get }
    var pendingPermissions: [any PermissionPrompt] { get }
    var pendingWidgets: [any InteractiveWidget] { get }
    var typingParticipants: [String] { get }

    func addObserver(_ observer: any ChatStateObserver)
    func removeObserver(_ observer: any ChatStateObserver)

    func submitMessage(text: String, attachments: [any Attachment]) async throws -> String
    func markRead(messageID: String) async throws
    func setLocalTyping(_ isTyping: Bool) async throws
    func respondToWidget(_ response: any WidgetResponse) async throws
    func respondToPermission(promptID: String, decision: PermissionDecision) async throws

    func listCommands() -> [any Command]
}
