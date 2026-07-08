"use client"
import type { ReactElement, ReactNode } from 'react'
import { useKeyboardInset } from './useKeyboardInset'

interface ViewportShellProps {
  children: ReactNode
  className?: string
  /**
   * Whether the shell clips its own overflow (default true). Pass false when
   * content deliberately overhangs the shell's box — e.g. a corner badge like
   * the chat package's RegistryMark. The page itself stays locked either way:
   * html/body keep overflow:hidden, so opening the shell cannot introduce
   * page scroll.
   */
  clip?: boolean
}

/**
 * Top-level page shell. Locks the page to the visible viewport, mounts
 * the keyboard-inset hook, and exposes a vertical flex container that
 * `<ViewportSpacer>` and `<ViewportComposer>` slot into.
 */
export function ViewportShell({ children, className, clip = true }: ViewportShellProps): ReactElement {
  useKeyboardInset()
  const cls = ['viewport-shell', clip ? '' : 'vp-shell--open', className]
    .filter(Boolean)
    .join(' ')
  return <div className={cls}>{children}</div>
}
