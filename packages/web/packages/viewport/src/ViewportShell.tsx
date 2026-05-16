"use client"
import type { ReactNode } from 'react'
import { useKeyboardInset } from './useKeyboardInset'

interface ViewportShellProps {
  children: ReactNode
  className?: string
}

/**
 * Top-level page shell. Locks the page to the visible viewport, mounts
 * the keyboard-inset hook, and exposes a vertical flex container that
 * `<ViewportSpacer>` and `<ViewportComposer>` slot into.
 */
export function ViewportShell({ children, className }: ViewportShellProps) {
  useKeyboardInset()
  const cls = className ? `viewport-shell ${className}` : 'viewport-shell'
  return <div className={cls}>{children}</div>
}
