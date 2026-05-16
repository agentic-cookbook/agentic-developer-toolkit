import type { Backend } from '../backend/Backend'
import type { Command } from '../commands/Command'
import type { GatingHook } from '../hooks/GatingHook'
import type { ObservingHook } from '../hooks/ObservingHook'
import type { Participant } from '../participants/Participant'
import type { PermissionStore } from '../permissions/PermissionStore'
import type { DisplayConfig } from './DisplayConfig'

export interface ChatConfig {
  readonly conversationID: string
  readonly localParticipantID: string
  readonly initialParticipants: ReadonlyArray<Participant>
  readonly commands: ReadonlyArray<Command>
  readonly observingHooks: ReadonlyArray<ObservingHook>
  readonly gatingHooks: ReadonlyArray<GatingHook>
  readonly permissionStore: PermissionStore
  readonly backend: Backend
  readonly display: DisplayConfig
}
