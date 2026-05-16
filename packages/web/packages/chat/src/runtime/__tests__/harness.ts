import type { ChatStateObserver } from '../../contract/chat/ChatStateObserver'
import type { ChatUpdate } from '../../contract/chat/ChatUpdate'
import type { ChatConfig } from '../../contract/configuration/ChatConfig'
import type { Participant } from '../../contract/participants/Participant'
import { DefaultOrchestrator } from '../DefaultOrchestrator'
import { InMemoryPermissionStore } from '../InMemoryPermissionStore'
import { ScriptedBackend } from '../ScriptedBackend'

export interface Harness {
  readonly backend: ScriptedBackend
  readonly orchestrator: DefaultOrchestrator
  readonly permissionStore: InMemoryPermissionStore
  readonly localUser: Participant
  readonly persona: Participant
  readonly updates: ChatUpdate[]
}

const baseUser: Participant = {
  id: 'user-1',
  displayName: 'Alice',
  address: 'alice@local',
  kinds: new Set(['user']),
  conversationState: 'joined',
}

const basePersona: Participant = {
  id: 'persona-1',
  displayName: 'Aria',
  address: 'aria@registry',
  kinds: new Set(['persona']),
  conversationState: 'joined',
}

export function createHarness(overrides: Partial<ChatConfig> = {}): Harness {
  const backend = new ScriptedBackend()
  const permissionStore = new InMemoryPermissionStore()
  const config: ChatConfig = {
    conversationID: 'conv-1',
    localParticipantID: baseUser.id,
    initialParticipants: [baseUser, basePersona],
    commands: [],
    observingHooks: [],
    gatingHooks: [],
    permissionStore,
    backend,
    display: {
      showAvatars: true,
      showReadReceipts: true,
      showTypingIndicators: true,
      allowJoining: false,
      allowDeparting: false,
      reducedMotion: false,
    },
    ...overrides,
  }
  const orchestrator = new DefaultOrchestrator(config)
  const updates: ChatUpdate[] = []
  const observer: ChatStateObserver = {
    chatDidUpdate(update: ChatUpdate): void {
      updates.push(update)
    },
  }
  orchestrator.addObserver(observer)
  orchestrator.start()
  return { backend, orchestrator, permissionStore, localUser: baseUser, persona: basePersona, updates }
}

/**
 * Yield control so the orchestrator's async event loop can pick up
 * anything we just emitted. A few microtask ticks are enough — the loop
 * is `await iterator.next()` then a synchronous `handleEvent`.
 */
export async function flush(ticks = 5): Promise<void> {
  for (let i = 0; i < ticks; i += 1) {
    await Promise.resolve()
  }
}
