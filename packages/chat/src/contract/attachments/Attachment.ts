import type { MediaType } from '../media/MediaType'
import type { AttachmentSource } from '../media/AttachmentSource'
import type { AttachmentPresentation } from '../media/AttachmentPresentation'

export interface Attachment {
  readonly id: string
  readonly mediaType: MediaType
  readonly source: AttachmentSource
  readonly presentation: AttachmentPresentation
  readonly displayName?: string
  readonly byteSize?: number
}
