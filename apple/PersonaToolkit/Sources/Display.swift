import Foundation

public protocol DisplayConfig: Sendable {
    var showAvatars: Bool { get }
    var showReadReceipts: Bool { get }
    var showTypingIndicators: Bool { get }
    var maxParticipants: Int? { get }
    var allowJoining: Bool { get }
    var allowDeparting: Bool { get }
    /// Identifier resolved by the themes package; the chat surface just
    /// passes the string through.
    var themeIdentifier: String? { get }
    var reducedMotion: Bool { get }
}
