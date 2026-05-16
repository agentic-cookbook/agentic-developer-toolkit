import Foundation

public enum InboundEvent: Sendable {
    case messageAccepted(localID: String, serverID: String, at: Date)
    case messageDelivered(messageID: String, at: Date)
    case messageFailed(localID: String, reason: String)
    case messageReceived(any Message)

    /// A participant has advanced their read cursor to `upToMessageID`.
    /// Everything before that point is considered read. There is exactly
    /// one cursor per (conversation, participant). This event replaces
    /// per-message read acks — see Matrix `m.read`, XMPP XEP-0333
    /// `displayed`, Slack `conversations.mark`, Discord `READ_STATE`.
    case readMarkerAdvanced(participantID: String, upToMessageID: String, at: Date)

    /// A streaming participant (typically an LLM persona) has appended to
    /// their in-progress draft. The draft is NOT a message — it lives in
    /// `ChatViewModel.activeDrafts` until it commits as an immutable
    /// `Message` via `messageReceived`. This keeps `Message` immutable
    /// while preserving the token-by-token UX.
    case draftUpdated(participantID: String, text: String, attachments: [any Attachment])

    /// The participant has aborted or finalized their draft. If finalized,
    /// a `messageReceived` event will follow carrying the immutable
    /// `Message`. If aborted, no message arrives.
    case draftCleared(participantID: String)

    case participantJoined(any Participant)
    case participantDeparted(participantID: String)
    case typing(participantID: String, isTyping: Bool)
    case widgetPresented(messageID: String, widget: any InteractiveWidget)
    case transportError(message: String)
}
