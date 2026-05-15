import Foundation

public protocol ReadReceipt: Sendable {
    var messageID: String { get }
    var participantID: String { get }
    var at: Date { get }
}
