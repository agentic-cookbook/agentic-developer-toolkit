import type { Attachment } from '../attachments/Attachment'
import type { WidgetResponse } from '../attachments/WidgetResponse'
import type { InboundEvent } from './InboundEvent'

export interface Backend {
  /**
   * Submit a message to the bus. Returns the `localID` assigned by the
   * backend at submission time. The server-assigned id (if any) arrives
   * later as `InboundEvent` of kind `messageAccepted`.
   */
  send(text: string, attachments: ReadonlyArray<Attachment>): Promise<string>

  setLocalTyping(isTyping: boolean): Promise<void>
  submitWidgetResponse(response: WidgetResponse): Promise<void>

  /**
   * Cancellable stream of events from the bus. Each platform binds this
   * to its native cold-async-sequence type (Swift `AsyncStream`, Kotlin
   * `Flow`, JS async iterable). The orchestrator is the single consumer;
   * multiplexing to multiple observers is the orchestrator's
   * responsibility, not the backend's.
   */
  readonly inboundEvents: AsyncIterable<InboundEvent>
}
