import Foundation

/// Points at which `ObservingHook`s fire. Observing hooks cannot affect
/// outcomes — pure telemetry, logging, audit, tracing.
public enum ObservingPoint: Sendable, Hashable {
    case didComposeMessage      // user typed + submitted
    case messageSent            // backend ack'd an outbound message
    case messageReceived        // a new inbound message arrived
    case messageRead            // a read receipt was observed
    case didExecuteCommand
    case willEmitUpdate
    case didEmitUpdate
    case participantJoined
    case participantDeparted
    case permissionResolved
}

/// Points at which `GatingHook`s fire. Gating hooks may veto the
/// orchestrator's next action by returning `.block(reason:)`.
public enum GatingPoint: Sendable, Hashable {
    case willSubmitMessage         // about to call Backend.send
    case willExecuteCommand
    case willEmitUpdate
    case willRequestPermission
    case willAcceptInboundMessage  // moderation hook on inbound traffic
}

public protocol HookContext: Sendable {
    var conversationID: String { get }
    /// Point-specific payload, JSON-encoded for portability.
    var payloadJSON: String { get }
}

public enum HookDecision: Sendable {
    case proceed
    case block(reason: String)
}

/// Pure telemetry. Return value is `Void`; cannot block.
public protocol ObservingHook: Sendable {
    var points: Set<ObservingPoint> { get }
    func observe(point: ObservingPoint, context: any HookContext) async
}

/// Policy enforcement. Returns a decision the orchestrator honors.
public protocol GatingHook: Sendable {
    var points: Set<GatingPoint> { get }
    func gate(point: GatingPoint, context: any HookContext) async -> HookDecision
}
