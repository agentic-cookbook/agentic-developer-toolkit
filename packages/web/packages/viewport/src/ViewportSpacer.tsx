import type { ReactNode } from 'react'

interface ViewportSpacerProps {
  children?: ReactNode
  className?: string
}

/**
 * Flex spacer that absorbs leftover vertical space inside a `<ViewportShell>`,
 * pushing siblings (typically a `<ViewportComposer>`) to the bottom.
 */
export function ViewportSpacer({ children, className }: ViewportSpacerProps) {
  const cls = className ? `vp-spacer ${className}` : 'vp-spacer'
  return <div className={cls}>{children}</div>
}
