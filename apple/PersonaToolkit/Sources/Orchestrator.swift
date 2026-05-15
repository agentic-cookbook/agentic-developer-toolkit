import Foundation

/// The single toolkit front door.
///
/// Consumer code constructs an `Orchestrator` from a `ChatConfig`, hands
/// it to the UI as a `ChatViewModel`, and that's the entire interface.
/// The orchestrator owns:
///   • the Backend subscription
///   • the message-state machine (composing → sending → sent → … )
///   • read-receipt accounting
///   • hook execution (observing + gating)
///   • permission resolution
///   • command dispatch
///
/// `Orchestrator` adds nothing user-facing beyond `ChatViewModel`. The
/// accessors below are for diagnostics and setup-time wiring; consumer
/// code should not call into `backend` directly.
public protocol Orchestrator: ChatViewModel {

    var permissionStore: any PermissionStore { get }

    /// The Backend wired into this orchestrator.
    var backend: any Backend { get }
}
