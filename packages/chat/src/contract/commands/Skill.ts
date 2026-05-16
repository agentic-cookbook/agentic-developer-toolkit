import type { Command } from './Command'

export interface Skill extends Command {
  readonly skillIdentifier: string
}
