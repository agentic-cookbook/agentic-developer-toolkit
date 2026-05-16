import type { Command } from './Command'

export interface Tool extends Command {
  readonly builtInIdentifier: string
}
