import { describe, expect, it } from 'vitest'

import type { Attachment } from '../../contract/attachments/Attachment'
import type { InteractiveWidget } from '../../contract/attachments/InteractiveWidget'
import type { Message } from '../../contract/messages/Message'
import type { Participant } from '../../contract/participants/Participant'
import type { Permission } from '../../contract/permissions/Permission'
import type { PermissionPrompt } from '../../contract/permissions/PermissionPrompt'

import { createHarness, flush } from './harness'

const empty: ReadonlyArray<Attachment> = []

function inboundMessage(senderID: string, text: string, localID: string, serverID: string): Message {
  return {
    id: serverID,
    localID,
    senderID,
    text,
    attachments: [],
    timestamp: new Date('2026-01-01T00:00:00Z'),
    deliveryStatus: { kind: 'received' },
  }
}

describe('DefaultOrchestrator — send + reply', () => {
  it('round-trips a non-streaming exchange and tracks delivery status', async () => {
    const h = createHarness()

    const localID = await h.orchestrator.submitMessage('hello', empty)
    expect(localID).toBe('local-1')
    expect(h.backend.sent).toEqual([{ localID: 'local-1', text: 'hello', attachments: [] }])
    expect(h.orchestrator.messages).toHaveLength(1)
    expect(h.orchestrator.messages[0]?.deliveryStatus).toEqual({ kind: 'sending' })

    h.backend.emit({ kind: 'messageAccepted', localID: 'local-1', serverID: 'srv-1', at: new Date() })
    await flush()
    expect(h.orchestrator.messages[0]?.id).toBe('srv-1')
    expect(h.orchestrator.messages[0]?.deliveryStatus).toEqual({ kind: 'sent' })

    h.backend.emit({ kind: 'messageDelivered', messageID: 'srv-1', at: new Date() })
    await flush()
    expect(h.orchestrator.messages[0]?.deliveryStatus).toEqual({ kind: 'delivered' })

    h.backend.emit({
      kind: 'messageReceived',
      message: inboundMessage(h.persona.id, 'hi there', 'persona-local-1', 'srv-2'),
    })
    await flush()
    expect(h.orchestrator.messages).toHaveLength(2)
    expect(h.orchestrator.messages[1]?.text).toBe('hi there')
    expect(h.orchestrator.messages[1]?.senderID).toBe(h.persona.id)
  })

  it('flips a message to failed when the bus rejects it', async () => {
    const h = createHarness()
    await h.orchestrator.submitMessage('hi', empty)
    h.backend.emit({ kind: 'messageFailed', localID: 'local-1', reason: 'rate-limited' })
    await flush()
    expect(h.orchestrator.messages[0]?.deliveryStatus).toEqual({ kind: 'failed', reason: 'rate-limited' })
  })
})

describe('DefaultOrchestrator — streaming via ActiveDraft', () => {
  it('buffers a streaming response in activeDrafts, then commits to messages on messageReceived', async () => {
    const h = createHarness()

    h.backend.emit({ kind: 'draftUpdated', participantID: h.persona.id, text: 'Th', attachments: [] })
    await flush()
    expect(h.orchestrator.activeDrafts).toHaveLength(1)
    expect(h.orchestrator.activeDrafts[0]?.text).toBe('Th')

    h.backend.emit({ kind: 'draftUpdated', participantID: h.persona.id, text: 'Thinki', attachments: [] })
    h.backend.emit({ kind: 'draftUpdated', participantID: h.persona.id, text: 'Thinking…', attachments: [] })
    await flush()
    expect(h.orchestrator.activeDrafts).toHaveLength(1)
    expect(h.orchestrator.activeDrafts[0]?.text).toBe('Thinking…')

    h.backend.emit({
      kind: 'messageReceived',
      message: inboundMessage(h.persona.id, 'Thinking… done.', 'persona-local-1', 'srv-99'),
    })
    await flush()
    expect(h.orchestrator.activeDrafts).toHaveLength(0)
    expect(h.orchestrator.messages).toHaveLength(1)
    expect(h.orchestrator.messages[0]?.text).toBe('Thinking… done.')
  })

  it('discards a draft on draftCleared without committing a message', async () => {
    const h = createHarness()
    h.backend.emit({ kind: 'draftUpdated', participantID: h.persona.id, text: 'wait…', attachments: [] })
    await flush()
    expect(h.orchestrator.activeDrafts).toHaveLength(1)
    h.backend.emit({ kind: 'draftCleared', participantID: h.persona.id })
    await flush()
    expect(h.orchestrator.activeDrafts).toHaveLength(0)
    expect(h.orchestrator.messages).toHaveLength(0)
  })
})

describe('DefaultOrchestrator — read cursors', () => {
  it('local markRead advances the local cursor only', async () => {
    const h = createHarness()
    await h.orchestrator.markRead('srv-42')
    expect(h.orchestrator.readMarkers).toHaveLength(1)
    expect(h.orchestrator.readMarkers[0]?.participantID).toBe(h.localUser.id)
    expect(h.orchestrator.readMarkers[0]?.upToMessageID).toBe('srv-42')
  })

  it('inbound readMarkerAdvanced from a peer is recorded as a separate cursor', async () => {
    const h = createHarness()
    await h.orchestrator.markRead('srv-1')
    h.backend.emit({
      kind: 'readMarkerAdvanced',
      participantID: h.persona.id,
      upToMessageID: 'srv-3',
      at: new Date(),
    })
    await flush()
    expect(h.orchestrator.readMarkers).toHaveLength(2)
    const personaMarker = h.orchestrator.readMarkers.find((r) => r.participantID === h.persona.id)
    expect(personaMarker?.upToMessageID).toBe('srv-3')
  })

  it('a second cursor advance from the same participant overwrites the first', async () => {
    const h = createHarness()
    h.backend.emit({
      kind: 'readMarkerAdvanced',
      participantID: h.persona.id,
      upToMessageID: 'srv-1',
      at: new Date(),
    })
    h.backend.emit({
      kind: 'readMarkerAdvanced',
      participantID: h.persona.id,
      upToMessageID: 'srv-2',
      at: new Date(),
    })
    await flush()
    expect(h.orchestrator.readMarkers).toHaveLength(1)
    expect(h.orchestrator.readMarkers[0]?.upToMessageID).toBe('srv-2')
  })
})

describe('DefaultOrchestrator — typing indicators', () => {
  it('adds and removes typing participants on isTyping toggles', async () => {
    const h = createHarness()
    h.backend.emit({ kind: 'typing', participantID: h.persona.id, isTyping: true })
    await flush()
    expect(h.orchestrator.typingParticipants).toEqual([h.persona.id])
    h.backend.emit({ kind: 'typing', participantID: h.persona.id, isTyping: true })
    await flush()
    expect(h.orchestrator.typingParticipants).toEqual([h.persona.id])
    h.backend.emit({ kind: 'typing', participantID: h.persona.id, isTyping: false })
    await flush()
    expect(h.orchestrator.typingParticipants).toEqual([])
  })

  it('local setLocalTyping calls through to the backend', async () => {
    const h = createHarness()
    await h.orchestrator.setLocalTyping(true)
    await h.orchestrator.setLocalTyping(false)
    expect(h.backend.typingCalls).toEqual([true, false])
  })
})

describe('DefaultOrchestrator — widgets', () => {
  it('presents a widget and clears it on response', async () => {
    const h = createHarness()
    const widget: InteractiveWidget = {
      id: 'wid-1',
      mediaType: { identifier: 'application/json' },
      source: { kind: 'inline', data: new Uint8Array([0x7b, 0x7d]) },
      presentation: 'inline',
      hasResponse: true,
    }
    h.backend.emit({ kind: 'widgetPresented', messageID: 'srv-7', widget })
    await flush()
    expect(h.orchestrator.pendingWidgets).toHaveLength(1)

    await h.orchestrator.respondToWidget({
      widgetID: 'wid-1',
      respondingParticipantID: h.localUser.id,
      payloadJSON: '{"choice":"yes"}',
    })
    expect(h.orchestrator.pendingWidgets).toHaveLength(0)
    expect(h.backend.widgetResponses).toHaveLength(1)
    expect(h.backend.widgetResponses[0]?.payloadJSON).toBe('{"choice":"yes"}')
  })
})

describe('DefaultOrchestrator — participants', () => {
  it('handles participantJoined / participantDeparted events', async () => {
    const h = createHarness()
    const newcomer: Participant = {
      id: 'observer-1',
      displayName: 'Observer',
      address: 'obs@local',
      kinds: new Set(['observer']),
      conversationState: 'joined',
    }
    h.backend.emit({ kind: 'participantJoined', participant: newcomer })
    await flush()
    expect(h.orchestrator.participants).toHaveLength(3)
    expect(h.orchestrator.participants.find((p) => p.id === 'observer-1')).toBeDefined()

    h.backend.emit({ kind: 'participantDeparted', participantID: 'observer-1' })
    await flush()
    expect(h.orchestrator.participants).toHaveLength(2)
    expect(h.orchestrator.participants.find((p) => p.id === 'observer-1')).toBeUndefined()
  })
})

describe('DefaultOrchestrator — permissions', () => {
  const permission: Permission = {
    id: 'perm.read-files',
    displayPromptTemplate: 'Allow {{requester}} to read files?',
  }

  it('respondToPermission with allowAlways persists the decision', async () => {
    const h = createHarness()
    const prompt: PermissionPrompt = {
      id: 'prompt-1',
      permission,
      requesterID: h.persona.id,
      displayPrompt: 'Allow Aria to read files?',
      requestedAt: new Date(),
    }
    h.orchestrator.presentPermissionPrompt(prompt)
    expect(h.orchestrator.pendingPermissions).toHaveLength(1)

    await h.orchestrator.respondToPermission('prompt-1', 'allowAlways')
    expect(h.orchestrator.pendingPermissions).toHaveLength(0)
    expect(h.permissionStore.decision(permission, h.persona.id)).toBe('allowAlways')
  })

  it('respondToPermission with allowOnce does not persist', async () => {
    const h = createHarness()
    h.orchestrator.presentPermissionPrompt({
      id: 'prompt-2',
      permission,
      requesterID: h.persona.id,
      displayPrompt: '...',
      requestedAt: new Date(),
    })
    await h.orchestrator.respondToPermission('prompt-2', 'allowOnce')
    expect(h.permissionStore.decision(permission, h.persona.id)).toBeUndefined()
  })

  it('falls back to permission.defaultDecision when nothing is remembered', () => {
    const h = createHarness()
    const permWithDefault: Permission = {
      id: 'perm.harmless',
      displayPromptTemplate: 'ok?',
      defaultDecision: 'allowAlways',
    }
    expect(h.permissionStore.decision(permWithDefault, h.persona.id)).toBe('allowAlways')
  })
})

describe('DefaultOrchestrator — observer notifications', () => {
  it('notifies observers for each state-changing event kind', async () => {
    const h = createHarness()
    await h.orchestrator.submitMessage('hello', empty)
    h.backend.emit({ kind: 'typing', participantID: h.persona.id, isTyping: true })
    h.backend.emit({
      kind: 'participantJoined',
      participant: {
        id: 'observer-9',
        displayName: 'Lurker',
        address: 'lurker@local',
        kinds: new Set(['observer']),
        conversationState: 'joined',
      },
    })
    await flush()

    const kinds = h.updates.map((u) => u.kind)
    expect(kinds).toContain('messagesChanged')
    expect(kinds).toContain('typingChanged')
    expect(kinds).toContain('participantsChanged')
  })

  it('emits an error update on transportError events', async () => {
    const h = createHarness()
    h.backend.emit({ kind: 'transportError', message: 'socket closed' })
    await flush()
    const error = h.updates.find((u) => u.kind === 'error')
    expect(error).toBeDefined()
    if (error?.kind === 'error') expect(error.message).toBe('socket closed')
  })

  it('does not notify after removeObserver', async () => {
    const h = createHarness()
    const captured: string[] = []
    const obs = {
      chatDidUpdate(update: { kind: string }) {
        captured.push(update.kind)
      },
    }
    h.orchestrator.addObserver(obs)
    h.orchestrator.removeObserver(obs)
    h.backend.emit({ kind: 'typing', participantID: h.persona.id, isTyping: true })
    await flush()
    expect(captured).toEqual([])
  })
})

describe('DefaultOrchestrator — commands', () => {
  it('listCommands returns the commands handed in via ChatConfig', () => {
    const cmd = {
      name: '/help',
      description: 'show help',
      allowedInvokers: new Set(['user'] as const),
      argumentSchema: '{}',
    }
    const h = createHarness({ commands: [cmd] })
    expect(h.orchestrator.listCommands()).toEqual([cmd])
  })
})
