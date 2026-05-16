import type { GatingPoint } from './GatingPoint'
import type { HookContext } from './HookContext'
import type { HookDecision } from './HookDecision'

export interface GatingHook {
  readonly points: ReadonlySet<GatingPoint>
  gate(point: GatingPoint, context: HookContext): Promise<HookDecision>
}
