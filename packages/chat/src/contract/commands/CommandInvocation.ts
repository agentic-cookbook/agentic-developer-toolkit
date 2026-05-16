import type { CommandInvoker } from './CommandInvoker'

export interface CommandInvocation {
  readonly id: string
  readonly commandName: string
  readonly invokerID: string
  readonly invokerKind: CommandInvoker
  readonly argumentsJSON: string
  readonly requestedAt: Date
}
