import type { HookContext } from './HookContext'
import type { ObservingPoint } from './ObservingPoint'

export interface ObservingHook {
  readonly points: ReadonlySet<ObservingPoint>
  observe(point: ObservingPoint, context: HookContext): Promise<void>
}
