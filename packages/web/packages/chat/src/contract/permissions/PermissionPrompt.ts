import type { Permission } from './Permission'

export interface PermissionPrompt {
  readonly id: string
  readonly permission: Permission
  readonly requesterID: string
  readonly displayPrompt: string
  readonly requestedAt: Date
}
