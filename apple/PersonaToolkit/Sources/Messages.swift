import Foundation

/// Lifecycle of a Message owned by the local orchestrator.
///
/// Outbound (composed locally):
///   composing → sending → sent → delivered (per recipient) → read (per recipient)
///                             ↘ failed
/// Inbound (from a remote participant):
///   received (with isStreaming flag while updates are still arriving)
public enum MessageDeliveryStatus: Sendable, Hashable {
    case composing             // local-only, not yet submitted
    case sending               // submitted to Backend, awaiting ack
    case sent                  // Backend acknowledged receipt
    case delivered             // Backend confirmed delivery to ≥1 recipient
    case failed(reason: String)
    case received              // inbound message from another participant
}

public protocol ReadReceipt: Sendable {
    var messageID: String { get }
    var participantID: String { get }
    var at: Date { get }
}

public enum ToolCallStatus: String, Sendable {
    case started, completed, failed
}

/// Display-only summary of tool activity that happened on the other side
/// of the Backend (e.g. a server-side persona used a calendar tool).
/// The local chat does NOT invoke these — Tool/Skill are slash-style
/// commands the user invokes locally; ToolCalls are attribution data only.
public protocol ToolCall: Sendable {
    var name: String { get }
    var argumentsJSON: String { get }
    var status: ToolCallStatus { get }
    var resultJSON: String? { get }
    var ok: Bool? { get }
}

public protocol Message: Sendable {
    /// Server-assigned id once accepted. Until then, `nil`; correlate via
    /// `localID`.
    var id: String? { get }

    /// Locally-generated id, stable from the moment of composition.
    /// Used to match `InboundEvent.messageAccepted` back to the
    /// originating outbound message.
    var localID: String { get }

    /// Must match a `Participant.id` in the Conversation.
    var senderID: String { get }

    /// Display text. May be empty if the message is purely attachments
    /// or a widget.
    var text: String { get }

    /// Backend-assigned timestamp. `nil` while pending.
    var timestamp: Date? { get }

    var attachments: [any Attachment] { get }
    var toolCalls: [any ToolCall] { get }

    var deliveryStatus: MessageDeliveryStatus { get }

    /// Read receipts collected so far for this message.
    var readBy: [any ReadReceipt] { get }

    /// True while the message is being updated in place (token-by-token
    /// streaming from a remote actor). Flips to false on
    /// `InboundEvent.messageCompleted`.
    var isStreaming: Bool { get }
}

public protocol Conversation: Sendable {
    var id: String { get }
    var createdAt: Date { get }
    var title: String? { get }
    var participants: [any Participant] { get }
}
