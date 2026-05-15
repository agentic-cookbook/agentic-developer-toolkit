"use client"
import { useEffect } from 'react'

/**
 * Writes `--kb-inset` on `:root` from `window.visualViewport` — the only
 * browser API that reflects the iOS soft-keyboard height. Consumers can
 * then read `var(--kb-inset)` (in px) anywhere in their CSS.
 *
 * Mounted automatically by `<ViewportShell>`; export is for advanced cases
 * (e.g. consumers that want the variable without the shell layout).
 */
export function useKeyboardInset(): void {
  useEffect(() => {
    if (typeof window === 'undefined') return
    const vv = window.visualViewport
    if (!vv) return

    const update = () => {
      const inset = Math.max(0, window.innerHeight - vv.height - vv.offsetTop)
      document.documentElement.style.setProperty('--kb-inset', `${inset}px`)
    }
    vv.addEventListener('resize', update)
    vv.addEventListener('scroll', update)
    update()
    return () => {
      vv.removeEventListener('resize', update)
      vv.removeEventListener('scroll', update)
    }
  }, [])
}
