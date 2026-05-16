import type { InlineDocument } from './InlineDocument'

export interface InteractiveWidget extends InlineDocument {
  readonly hasResponse: boolean
}
