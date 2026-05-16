import type { Attachment } from '../attachments/Attachment'

/**
 * A participant's in-progress, uncommitted message. Drafts are a
 * view-model concept — they exist only while a streaming responder is
 * producing tokens or a human is composing. On commit, the draft is
 * replaced by an immutable `Message`; on abort, it is discarded. Drafts
 * never appear in `ChatViewModel.messages`.
 */
export interface ActiveDraft {
  readonly participantID: string
  readonly text: string
  readonly attachments: ReadonlyArray<Attachment>
}
