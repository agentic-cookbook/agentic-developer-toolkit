import type { Attachment } from '../contract/attachments/Attachment'
import type { WidgetResponse } from '../contract/attachments/WidgetResponse'
import type { Backend } from '../contract/backend/Backend'
import type { InboundEvent } from '../contract/backend/InboundEvent'

export interface SentRecord {
  readonly localID: string
  readonly text: string
  readonly attachments: ReadonlyArray<Attachment>
}

/**
 * Backend implementation driven by explicit `emit()` calls and a script of
 * pre-canned responses. Records every `send` / `setLocalTyping` /
 * `submitWidgetResponse` invocation so tests can assert on them.
 *
 * Each `send` mints a deterministic localID of the form `${prefix}-${n}`
 * starting at 1. The matching `messageAccepted` event is the test's job to
 * emit — that's the whole point of a scripted backend.
 */
export class ScriptedBackend implements Backend {
  readonly sent: SentRecord[] = []
  readonly typingCalls: boolean[] = []
  readonly widgetResponses: WidgetResponse[] = []

  private localIDSeq = 0
  private readonly localIDPrefix: string
  private readonly queue: InboundEvent[] = []
  private readonly waiters: Array<(result: IteratorResult<InboundEvent>) => void> = []
  private closed = false

  constructor(options: { localIDPrefix?: string } = {}) {
    this.localIDPrefix = options.localIDPrefix ?? 'local'
  }

  async send(text: string, attachments: ReadonlyArray<Attachment>): Promise<string> {
    this.localIDSeq += 1
    const localID = `${this.localIDPrefix}-${this.localIDSeq}`
    this.sent.push({ localID, text, attachments })
    return localID
  }

  async setLocalTyping(isTyping: boolean): Promise<void> {
    this.typingCalls.push(isTyping)
  }

  async submitWidgetResponse(response: WidgetResponse): Promise<void> {
    this.widgetResponses.push(response)
  }

  emit(event: InboundEvent): void {
    if (this.closed) return
    const waiter = this.waiters.shift()
    if (waiter) {
      waiter({ value: event, done: false })
    } else {
      this.queue.push(event)
    }
  }

  close(): void {
    if (this.closed) return
    this.closed = true
    while (this.waiters.length > 0) {
      const waiter = this.waiters.shift()
      if (waiter) waiter({ value: undefined, done: true })
    }
  }

  get inboundEvents(): AsyncIterable<InboundEvent> {
    const queue = this.queue
    const waiters = this.waiters
    const isClosed = (): boolean => this.closed
    return {
      [Symbol.asyncIterator](): AsyncIterator<InboundEvent> {
        return {
          next(): Promise<IteratorResult<InboundEvent>> {
            const buffered = queue.shift()
            if (buffered !== undefined) {
              return Promise.resolve({ value: buffered, done: false })
            }
            if (isClosed()) {
              return Promise.resolve({ value: undefined, done: true })
            }
            return new Promise<IteratorResult<InboundEvent>>((resolve) => {
              waiters.push(resolve)
            })
          },
        }
      },
    }
  }
}
