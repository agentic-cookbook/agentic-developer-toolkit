import type { Attachment } from '../attachments/Attachment'
import type { InteractiveWidget } from '../attachments/InteractiveWidget'
import type { Message } from '../messages/Message'
import type { Participant } from '../participants/Participant'

export type InboundEvent =
  | {
      readonly kind: 'messageAccepted'
      readonly localID: string
      readonly serverID: string
      readonly at: Date
    }
  | { readonly kind: 'messageDelivered'; readonly messageID: string; readonly at: Date }
  | { readonly kind: 'messageFailed'; readonly localID: string; readonly reason: string }
  | { readonly kind: 'messageReceived'; readonly message: Message }
  /**
   * A participant has advanced their read cursor to `upToMessageID`.
   * Everything before that point is considered read. There is exactly
   * one cursor per (conversation, participant). Mirrors Matrix `m.read`,
   * XMPP XEP-0333 `displayed`, Slack `conversations.mark`, Discord
   * `READ_STATE`.
   */
  | {
      readonly kind: 'readMarkerAdvanced'
      readonly participantID: string
      readonly upToMessageID: string
      readonly at: Date
    }
  /**
   * A streaming participant (typically an LLM persona) has appended to
   * their in-progress draft. The draft is NOT a message — it lives in
   * `ChatViewModel.activeDrafts` until it commits as an immutable
   * `Message` via `messageReceived`. Keeps `Message` immutable while
   * preserving the token-by-token UX.
   */
  | {
      readonly kind: 'draftUpdated'
      readonly participantID: string
      readonly text: string
      readonly attachments: ReadonlyArray<Attachment>
    }
  /**
   * The participant has aborted or finalized their draft. If finalized,
   * a `messageReceived` event will follow carrying the immutable
   * `Message`. If aborted, no message arrives.
   */
  | { readonly kind: 'draftCleared'; readonly participantID: string }
  | { readonly kind: 'participantJoined'; readonly participant: Participant }
  | { readonly kind: 'participantDeparted'; readonly participantID: string }
  | { readonly kind: 'typing'; readonly participantID: string; readonly isTyping: boolean }
  | {
      readonly kind: 'widgetPresented'
      readonly messageID: string
      readonly widget: InteractiveWidget
    }
  | { readonly kind: 'transportError'; readonly message: string }
