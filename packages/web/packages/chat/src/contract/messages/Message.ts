import type { Attachment } from '../attachments/Attachment'
import type { MessageDeliveryStatus } from './MessageDeliveryStatus'

export interface Message {
  readonly id?: string
  readonly localID: string
  readonly senderID: string
  readonly text: string
  readonly timestamp?: Date
  readonly attachments: ReadonlyArray<Attachment>
  readonly deliveryStatus: MessageDeliveryStatus
}
