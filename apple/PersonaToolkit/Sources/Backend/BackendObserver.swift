import Foundation

public protocol BackendObserver: AnyObject, Sendable {
    func backendDidReceive(_ event: InboundEvent)
}
