# agentic-persona-toolkit

Developer toolkit for wiring AI persona chats into apps using the official
agentic registry (persona definitions + LLM provider integrations) and
my-agentic-storage (chat history + state). Replaces the deprecated
`agentic-persona-coordinator`.

Authoritative planning: [`docs/planning/planning.md`](../docs/planning/planning.md).
README: [`README.md`](../README.md).

## Ecosystem map

- **`~/Development/projects/agenticregistry`** — registry service. Has
  per-user persona services (Anthropic / OpenAI / Gemini), provider
  integrations at `web/backend/src/lib/providers/`, persona records with
  `slug`, `modelPrompt`, `voice`, `character`, `examples`, `serviceId`,
  `model`. Public read at `/api/public/personas/:slug`. No chat-completion
  endpoint exists yet — M1 will add one.
- **`~/Development/projects/my-agentic-storage`** — storage service.
  Primitives: `buckets`, `lists`, `events`, `kv`, `counters`, `queues`,
  `memory`, `keywords`. Per-user API keys. Chat history is a fit for `lists`
  or `events`.
- **`~/Development/projects/agentic-web-toolkit`** — current home of the
  chat package at `packages/features/chat/`. M1 relocates it here.
- **`~/Development/projects/learntruefacts`** — dogfood site for apt.
  Currently vendors `agentic-web-toolkit/` under `vendor/`. M1's success
  criterion is replacing that vendor copy with a real apt dependency.
- **`~/Development/projects/agentic-persona-coordinator`** — deprecated.
  Do not change anything there.

## M1 scope (the only milestone designed so far)

1. Relocate `agentic-web-toolkit/packages/features/chat/` into this repo.
2. Build the coordinator package — the glue between the chat UI's
   `ChatBackend` interface and the registry + storage pair.
3. Switch `learntruefacts/sites/main/` from the vendored toolkit to a real
   apt dependency.

Later milestones (M2–M6) cover Python persona-config and try-out tools,
persona-authoring skills, registry population skills, a whimsical name/bio
generator, absorbing `personacreator`, and Apple/Windows/Android coordinator
ports. Each gets its own design spec when its turn comes.

## Open architectural decision (paused)

Where does chat orchestration live?

- **A1** — registry orchestrates a `POST /api/personas/:slug/chat` endpoint
  that handles persona lookup, history read/write to storage, and provider
  call. Coordinator is a thin client.
- **A2** — registry exposes a stateless `POST /api/personas/:slug/complete`.
  Coordinator package implements `ChatBackend`, reads history from storage,
  calls registry's `complete`, writes the new turn back to storage.

A2 was the tentative recommendation in brainstorming, not yet confirmed by
the user. **Do not write the design spec or scaffold the coordinator package
until the user picks one.** This is the brainstorming HARD-GATE.

## Tech stack

- TypeScript / Node throughout for M1 (matches registry, storage, chat
  package).
- Python arrives in M2 for the persona-config scripts and terminal try-out
  tool.
- Future platforms (Swift / Windows / Android) live in M6.

## Build

Not set up yet — depends on the architecture decision. Will mirror the
registry + storage repos' npm-workspaces layout.

## Conventions

- Follow the user's global instructions (see `~/.claude/CLAUDE.md`):
  Python over Bash for scripts, no `git add -A`, commit only what was
  touched in the session, ask before pull/merge/rebase/etc.
- The chat package's HTTP contract is fixed by what already exists: POST
  `{ message, history }` and either return `{ reply: string }` or stream
  `ChatStreamEvent` values. Do not redesign that.
- `learntruefacts` is the test bed. New apt features must demonstrate
  themselves in `learntruefacts/sites/main` before being considered done.
