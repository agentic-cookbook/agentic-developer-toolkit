import Foundation

public protocol Attachment: Sendable {
    var id: String { get }
    var mediaType: any MediaType { get }
    var source: AttachmentSource { get }
    var presentation: AttachmentPresentation { get }
    var displayName: String? { get }
    var byteSize: Int? { get }
}

/// Structured content rendered inline (cards, embeds, rich blocks).
/// `presentation` MUST be `.inline`.
public protocol InlineDocument: Attachment {}

/// An InlineDocument that can collect a response from a participant
/// (poll, quiz, mini-game). The response, when collected, is delivered
/// back through the Backend via WidgetResponse.
public protocol InteractiveWidget: InlineDocument {
    /// True once any participant has supplied a response.
    var hasResponse: Bool { get }
}

public protocol WidgetResponse: Sendable {
    var widgetID: String { get }
    var respondingParticipantID: String { get }
    /// Payload schema is determined by the widget's `mediaType`.
    var payloadJSON: String { get }
}
