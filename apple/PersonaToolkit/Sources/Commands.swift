import Foundation

public enum CommandInvoker: Sendable, Hashable {
    case user
    case other   // any non-local actor that may invoke commands locally
}

/// Slash-style commands invokable from the chat composer. Commands are
/// purely CLIENT-SIDE affordances. Server-side tool use by a remote
/// actor (e.g. a persona running on a backend) surfaces as `ToolCall`
/// metadata on Messages, not as Commands.
public protocol Command: Sendable {
    /// "clear", "poll", "question.publish".
    var name: String { get }
    var description: String { get }
    /// Who may invoke this command in this chat.
    var allowedInvokers: Set<CommandInvoker> { get }
    /// Permission gate. `nil` means no permission required.
    var permission: (any Permission)? { get }
    /// Schema describing the arguments, identified by media type.
    var argumentSchema: any MediaType { get }
}

/// Built-in command shipped by the toolkit (e.g. `/clear`, `/poll`).
public protocol Tool: Command {
    /// Stable identifier for the built-in implementation, versioned with
    /// the toolkit.
    var builtInIdentifier: String { get }
}

/// Developer-supplied command. The developer owns the implementation
/// and lifecycle.
public protocol Skill: Command {
    /// Stable identifier in the developer's namespace, e.g. "acme.weather".
    var skillIdentifier: String { get }
}

public protocol CommandInvocation: Sendable {
    var invocationID: String { get }
    var commandName: String { get }
    var rawInput: String { get }
    var argumentsJSON: String { get }
    var invokerParticipantID: String { get }
}

public protocol CommandResult: Sendable {
    var invocationID: String { get }
    var ok: Bool { get }
    /// Result JSON, or error message when `ok == false`.
    var payloadJSON: String { get }
}
