import type { PermissionDecision } from './PermissionDecision'

export interface Permission {
  readonly id: string
  readonly displayPromptTemplate: string
  readonly defaultDecision?: PermissionDecision
}
