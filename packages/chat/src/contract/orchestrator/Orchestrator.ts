import type { ChatViewModel } from '../chat/ChatViewModel'
import type { PermissionStore } from '../permissions/PermissionStore'

export interface Orchestrator extends ChatViewModel {
  readonly permissionStore: PermissionStore
}
