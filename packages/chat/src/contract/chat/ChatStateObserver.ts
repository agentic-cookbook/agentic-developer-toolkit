import type { ChatUpdate } from './ChatUpdate'

export interface ChatStateObserver {
  chatDidUpdate(update: ChatUpdate): void
}
