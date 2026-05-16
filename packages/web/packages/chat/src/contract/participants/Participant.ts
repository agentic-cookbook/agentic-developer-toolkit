import type { ParticipantKind } from './ParticipantKind'
import type { ParticipantConversationState } from './ParticipantConversationState'

export interface Participant {
  readonly id: string
  readonly displayName: string
  readonly avatarURL?: URL
  readonly profileURL?: URL
  readonly address: string
  readonly kinds: ReadonlySet<ParticipantKind>
  readonly conversationState: ParticipantConversationState
}
