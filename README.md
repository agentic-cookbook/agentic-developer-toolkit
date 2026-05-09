# agentic-persona-toolkit

A toolkit for wiring AI persona chats into apps using the [official agentic
registry](https://github.com/agentic-cookbook/agenticregistry) (persona
definitions + LLM provider integrations) and [my-agentic-storage](https://github.com/agentic-cookbook/my-agentic-storage)
(chat history + state). The **coordinator package** is the glue that splices both
services into the shape a chat UI expects, so each consumer site does not have to
re-implement orchestration.

This repo supersedes `agentic-persona-coordinator` (apc). The coordinator role
moves here alongside a broader set of tools (web chat package today; CLI/Python
tools, persona-authoring skills, and other-platform coordinators in later
milestones).

## Status

Brainstorming complete for **M1** (the web chat slice). Scope is locked. One
architectural decision is still open. See
[`docs/planning/planning.md`](docs/planning/planning.md) for the full picture.

## Milestones

| Milestone | Scope | Status |
|-----------|-------|--------|
| **M1** | Web chat slice: relocate the chat package from `agentic-web-toolkit`; build the coordinator package; switch `learntruefacts` from a vendored toolkit copy to a real apt dependency. | designing |
| M2 | Python persona-config scripts + a terminal try-out tool. | not started |
| M3 | Claude skills for persona authoring + a skill that populates the registry. | not started |
| M4 | Whimsical name / bio generator. | not started |
| M5 | Absorb `personacreator` into this repo. | not started |
| M6 | Apple / Windows / Android coordinator ports. | not started |

## How the chat backend works

The existing chat package's `FetchBackend` POSTs `{ message, history }` to a
configurable URL. apt's job is to make that URL backed by the **registry + storage**
pair:

- **Registry** owns the persona definition (`modelPrompt`, `voice`, `character`,
  `examples`), the user's connected LLM service (`serviceId`, `model`), and stored
  credentials. Provider integrations for Anthropic / OpenAI / Gemini already exist
  in `web/backend/src/lib/providers/`.
- **Storage** owns the chat history. The right primitive is `lists` or `events`
  in `my-agentic-storage`.
- **Coordinator package** wires the chat UI's `ChatBackend` interface to those two
  services.

How that orchestration is split between registry and coordinator (registry-as-chat-backend
vs coordinator-orchestrates-stateless-registry) is the open architectural decision —
see the planning doc.

## Layout

```
docs/
  planning/    # M1 plan, milestones, open decisions
  project/     # high-level project description
.claude/
  CLAUDE.md    # agent context for this repo
```

More directories will arrive once the architecture is decided and implementation
starts.
