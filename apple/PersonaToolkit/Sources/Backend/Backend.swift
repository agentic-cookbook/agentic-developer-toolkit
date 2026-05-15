import Foundation

public protocol Backend: AnyObject, Sendable {
    func send(text: String, attachments: [any Attachment]) async throws -> String
    func acknowledgeRead(messageID: String) async throws
    func setLocalTyping(_ isTyping: Bool) async throws
    func submitWidgetResponse(_ response: any WidgetResponse) async throws
    func subscribe(_ observer: any BackendObserver)
    func unsubscribe(_ observer: any BackendObserver)
}
