// Components
export { InlineChat, InlineChatView } from './modes/InlineChat'
export type {
  InlineChatSizing,
  ChatSizingBehavior,
  InactiveSizingBehavior,
  SizingTransition,
} from './modes/InlineChat'
export { ThreePaneChat, ThreePaneChatView } from './modes/ThreePaneChat'
export { MobileChat, MobileChatView } from './modes/MobileChat'
export { PersonaChat } from './modes/PersonaChat'
export { Transcript } from './components/Transcript'
export { ContentOverlay } from './components/ContentOverlay'
export type { ContentOverlayProps } from './components/ContentOverlay'
export { RegistryMark } from './components/RegistryMark'
export type { RegistryMarkProps } from './components/RegistryMark'

// Backends
export { MockBackend } from './backends/MockBackend'
export { FetchBackend } from './backends/FetchBackend'
export type { ChatBackend } from './backends/types'

// Types
export type {
  ChatParticipant,
  ChatMessage,
  ChatResponse,
  ChatStreamEvent,
  ToolCallInfo,
  ContentItem,
  LinkContent,
  ImageContent,
  PopoverData,
  ChatMode,
} from './types'

// Hooks (for advanced usage)
export { useChatSession } from './hooks/useChatSession'
export type { ChatSession } from './hooks/useChatSession'

// Cross-platform chat contract (mirrors apple/PersonaToolkit/Sources/).
export type * from './contract'

// Reference TS implementations of the cross-platform contract.
export { DefaultOrchestrator, ScriptedBackend, InMemoryPermissionStore } from './runtime'
export type { SentRecord } from './runtime'
