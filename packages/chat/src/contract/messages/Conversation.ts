import type { Participant } from '../participants/Participant'

export interface Conversation {
  readonly id: string
  readonly createdAt: Date
  readonly title?: string
  readonly participants: ReadonlyArray<Participant>
}
