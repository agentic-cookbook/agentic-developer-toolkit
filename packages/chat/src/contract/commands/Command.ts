import type { Permission } from '../permissions/Permission'
import type { CommandInvoker } from './CommandInvoker'

export interface Command {
  readonly name: string
  readonly description: string
  readonly allowedInvokers: ReadonlySet<CommandInvoker>
  readonly permission?: Permission
  readonly argumentSchema: string
}
