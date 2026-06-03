import {
  useEffect,
  useLayoutEffect,
  useRef,
  useState,
  type CSSProperties,
  type RefObject,
} from 'react'
import type { InlineChatSizing, InactiveSizingBehavior } from '../modes/InlineChat'

const HUGGING_CLASS = 'pc-hugging'
const DEFAULT_SIZING: InlineChatSizing = { active: { mode: 'fixed' } }

export interface ChatSizing {
  ref: RefObject<HTMLDivElement | null>
  style: CSSProperties
  /** True while the user is interacting (focused or just clicked in). */
  engaged: boolean
  /** True when showing the inactive `minimal` state (input bar only). */
  collapsed: boolean
  /** State/transition class names for the chat root (`pc-anim`, `pc-collapsed`). */
  className: string
}

/**
 * Drives the inline chat's size from its active/inactive sizing behaviors.
 *
 * Reuses the bottom-anchored, content-hugging mechanism (the box hugs its
 * content so growth extends the top edge upward). When an `inactive` behavior
 * is configured, it also tracks engagement — focus expands to the active
 * size, clicking away or pressing Escape collapses to the inactive size — and
 * exposes class hooks so CSS can animate the grow-up / grow-down.
 */
export function useChatSizing(sizing: InlineChatSizing | undefined): ChatSizing {
  const { active, inactive, transition = 'animated' } = sizing ?? DEFAULT_SIZING

  const ref = useRef<HTMLDivElement | null>(null)
  const [maxHeightPx, setMaxHeightPx] = useState<number | null>(null)
  const [engaged, setEngaged] = useState(false)

  // Engagement only matters when an inactive behavior is configured; otherwise
  // the box is static and behaves exactly as it did before this option existed.
  const tracksEngagement = inactive !== undefined

  useEffect(() => {
    if (!tracksEngagement) return
    if (typeof document === 'undefined') return
    const el = ref.current
    if (!el) return

    const engage = () => setEngaged(true)
    const onPointerDown = (e: Event) => {
      setEngaged(el.contains(e.target as Node))
    }
    const onKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') setEngaged(false)
    }

    el.addEventListener('focusin', engage)
    document.addEventListener('pointerdown', onPointerDown)
    document.addEventListener('keydown', onKeyDown)
    return () => {
      el.removeEventListener('focusin', engage)
      document.removeEventListener('pointerdown', onPointerDown)
      document.removeEventListener('keydown', onKeyDown)
    }
  }, [tracksEngagement])

  // The behavior in effect for the current engagement state.
  const behavior: InactiveSizingBehavior = engaged ? active : (inactive ?? active)
  const isHugging = behavior.mode === 'content-hugging'
  const isMinimal = behavior.mode === 'minimal'
  // Both content-hugging and minimal release the wrapper's fixed height so the
  // bottom-anchored box hugs its content (minimal hugs just the input bar,
  // because the transcript is collapsed by CSS).
  const releaseHeight = isHugging || isMinimal

  useLayoutEffect(() => {
    if (!releaseHeight) return
    if (typeof window === 'undefined' || typeof ResizeObserver === 'undefined') return
    const el = ref.current
    if (!el) return

    el.classList.add(HUGGING_CLASS)
    const parent = el.parentElement
    parent?.classList.add(HUGGING_CLASS)

    const releaseOnly = () => {
      el.classList.remove(HUGGING_CLASS)
      parent?.classList.remove(HUGGING_CLASS)
    }

    // `minimal` has no cap to compute — the transcript is collapsed by CSS, so
    // the box already hugs the input bar.
    if (behavior.mode !== 'content-hugging') {
      setMaxHeightPx(null)
      return releaseOnly
    }

    const cap = behavior.maxHeight
    const recompute = () => {
      const chatBottom = el.getBoundingClientRect().bottom
      if (cap.kind === 'css') {
        setMaxHeightPx(parseCssLength(cap.value, window.innerHeight))
        return
      }
      if (cap.kind === 'viewport-offset') {
        setMaxHeightPx(Math.max(0, chatBottom - cap.topOffsetPx))
        return
      }
      const anchor = cap.ref.current
      if (!anchor) {
        setMaxHeightPx(Math.max(0, chatBottom))
        return
      }
      const anchorBottom = anchor.getBoundingClientRect().bottom
      setMaxHeightPx(Math.max(0, chatBottom - (anchorBottom + (cap.gapPx ?? 0))))
    }

    const ro = new ResizeObserver(recompute)
    ro.observe(el)

    let anchorRo: ResizeObserver | null = null
    if (cap.kind === 'element-offset' && cap.ref.current) {
      anchorRo = new ResizeObserver(recompute)
      anchorRo.observe(cap.ref.current)
    }

    window.addEventListener('resize', recompute)
    window.addEventListener('scroll', recompute, { passive: true })

    // visualViewport reflects the iOS soft-keyboard height; window.resize
    // does not. Without these listeners, content-hugging maxHeight is stale
    // while the keyboard is open.
    const vv = window.visualViewport
    vv?.addEventListener('resize', recompute)
    vv?.addEventListener('scroll', recompute)

    recompute()

    return () => {
      ro.disconnect()
      anchorRo?.disconnect()
      window.removeEventListener('resize', recompute)
      window.removeEventListener('scroll', recompute)
      vv?.removeEventListener('resize', recompute)
      vv?.removeEventListener('scroll', recompute)
      releaseOnly()
    }
  }, [releaseHeight, behavior])

  const classes: string[] = []
  if (transition === 'animated' && tracksEngagement) classes.push('pc-anim')
  if (isMinimal) classes.push('pc-collapsed')

  return {
    ref,
    style: isHugging && maxHeightPx != null ? { maxHeight: `${maxHeightPx}px` } : {},
    engaged,
    collapsed: isMinimal,
    className: classes.join(' '),
  }
}

function parseCssLength(value: string, viewportHeight: number): number {
  const trimmed = value.trim()
  const match = trimmed.match(/^(-?\d*\.?\d+)\s*(px|vh)?$/i)
  if (!match || match[1] === undefined) return 0
  const num = parseFloat(match[1])
  const unit = (match[2] ?? 'px').toLowerCase()
  if (unit === 'vh') return (num / 100) * viewportHeight
  return num
}
