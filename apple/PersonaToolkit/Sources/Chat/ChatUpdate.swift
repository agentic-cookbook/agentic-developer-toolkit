import Foundation

public enum ChatUpdate: Sendable {
    case messagesChanged
    case participantsChanged
    case typingChanged
    case pendingPermissionsChanged
    case pendingWidgetsChanged
    case displayConfigChanged
    case error(message: String)
}
