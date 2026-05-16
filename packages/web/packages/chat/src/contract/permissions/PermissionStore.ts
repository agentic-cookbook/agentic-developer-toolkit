import type { Permission } from './Permission'
import type { PermissionDecision } from './PermissionDecision'

export interface PermissionStore {
  decision(permission: Permission, requesterID: string): PermissionDecision | undefined
  remember(decision: PermissionDecision, permission: Permission, requesterID: string): void
}
