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

## Planning

Status, milestones, the open architectural decision, and design notes live in
[`docs/planning/planning.md`](docs/planning/planning.md).

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
