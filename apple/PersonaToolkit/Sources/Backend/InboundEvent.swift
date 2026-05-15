import Foundation

public enum InboundEvent: Sendable {
    case messageAccepted(localID: String, serverID: String, at: Date)
    case messageDelivered(messageID: String, at: Date)
    case messageRead(messageID: String, by: String, at: Date)
    case messageFailed(localID: String, reason: String)
    case messageReceived(any Message)
    case messageUpdated(messageID: String, deltaText: String?, addedAttachments: [any Attachment])
    case messageCompleted(messageID: String)
    case participantJoined(any Participant)
    case participantDeparted(participantID: String)
    case typing(participantID: String, isTyping: Bool)
    case widgetPresented(messageID: String, widget: any InteractiveWidget)
    case transportError(message: String)
}
