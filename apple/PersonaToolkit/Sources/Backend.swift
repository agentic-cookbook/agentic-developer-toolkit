import Foundation

/// The Backend is the orchestrator's single I/O abstraction. It hides
/// every difference between "fully local" configs (in-process bus,
/// possibly wrapping a local LLM call) and "remote" configs (HTTP+SSE,
/// WebSocket, gRPC, …).
///
/// Outbound flow:
///   user composes → orchestrator.submitMessage → Backend.send
///                 → eventually: InboundEvent.messageAccepted
/// Inbound flow:
///   remote actor posts → Backend emits InboundEvent.messageReceived
///                      → orchestrator updates state, notifies UI
///
/// The orchestrator is the ONLY caller of Backend methods. Consumer code
/// goes through `ChatViewModel`.
public protocol Backend: AnyObject, Sendable {

    /// Submit a composed message for transmission. Returns the local id
    /// immediately so the orchestrator can render the message as
    /// `.sending`. The actual ack arrives later via
    /// `InboundEvent.messageAccepted`.
    @discardableResult
    func send(text: String, attachments: [any Attachment]) async throws -> String

    /// Tell the backend the local user has read a received message;
    /// the backend forwards a read receipt to whoever sent it.
    func acknowledgeRead(messageID: String) async throws

    /// Local typing state changed.
    func setLocalTyping(_ isTyping: Bool) async

    /// Submit a response to an inline interactive widget.
    func submitWidgetResponse(_ response: any WidgetResponse) async throws

    /// Subscribe to inbound events. Multiple subscribers permitted; each
    /// receives every event.
    func subscribe(_ observer: any BackendObserver) async
    func unsubscribe(_ observer: any BackendObserver) async
}

public protocol BackendObserver: AnyObject, Sendable {
    func backendDidReceive(_ event: InboundEvent) async
}

/// The fixed alphabet of inbound events. Concrete Backend implementations
/// translate transport-specific events (SSE frames, WebSocket frames,
/// local-bus callbacks) into this vocabulary. The orchestrator handles
/// the rest — folding events into Message state, fanning to observers,
/// running hooks.
public enum InboundEvent: Sendable {

    // --- Outbound acknowledgments ------------------------------------

    /// Our outbound message has been accepted. Assigns a server-side id;
    /// the orchestrator looks up the pending message by `localID` and
    /// flips its status from `.sending` to `.sent`.
    case messageAccepted(localID: String, serverID: String, at: Date)

    /// Our outbound message was delivered to one recipient.
    case messageDelivered(messageID: String, toParticipantID: String, at: Date)

    /// A read receipt arrived. Used for both directions: receipts FOR our
    /// outbound messages, and confirmation that the backend registered
    /// our local read-acks for inbound messages.
    case messageRead(messageID: String, byParticipantID: String, at: Date)

    /// Our outbound message could not be sent.
    case messageFailed(localID: String, reason: String)

    // --- Inbound message lifecycle -----------------------------------

    /// A new inbound message has begun. May be partial — see updates.
    /// The Message's `isStreaming` will be true until messageCompleted.
    case messageReceived(any Message)

    /// Partial update to an in-flight inbound message (token streaming,
    /// late-arriving attachments, late-bound tool-call status changes).
    /// Orchestrator merges into the existing Message in place.
    case messageUpdated(
        messageID: String,
        deltaText: String?,
        addedAttachments: [any Attachment])

    /// The in-flight inbound message is finalized. Its `isStreaming`
    /// flips to false; no further `messageUpdated` events will follow.
    case messageCompleted(messageID: String)

    // --- Conversation lifecycle --------------------------------------

    case participantJoined(any Participant)
    case participantDeparted(participantID: String)

    /// A remote participant's typing state changed.
    case typing(participantID: String, isTyping: Bool)

    // --- Widgets / prompts -------------------------------------------

    /// The backend presents an inline widget out-of-band of any message
    /// (e.g. "please grant calendar access"). Widgets that arrive as
    /// part of a message come via `messageReceived` / `messageUpdated`
    /// in the message's `attachments`.
    case widgetPresented(any InteractiveWidget)

    // --- Transport ---------------------------------------------------

    /// The bus itself is in trouble (auth expired, network gone, …).
    /// Distinct from `messageFailed`, which is about a single send.
    case transportError(message: String)
}
