import type { ReactNode } from 'react'

interface ViewportComposerProps {
  children: ReactNode
  className?: string
}

/**
 * Bottom-anchored slot inside a `<ViewportShell>`. Its bottom padding is
 * `calc(var(--kb-inset) + env(safe-area-inset-bottom))`, so the composer
 * lifts above the iOS keyboard automatically and respects the home-indicator
 * safe area.
 */
export function ViewportComposer({ children, className }: ViewportComposerProps) {
  const cls = className ? `vp-composer ${className}` : 'vp-composer'
  return <div className={cls}>{children}</div>
}
