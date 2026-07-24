import { useEffect, useRef, type RefObject } from 'react'

/** Viewport geometry of the text caret in a single-line input. */
export interface CaretMetrics {
  x: number
  top: number
  height: number
  width: number
}

/** Default selector for the chat's text field, as rendered by ChatInput. */
export const CHAT_INPUT_SELECTOR = '.pc-input'

/**
 * Measure the text caret of a single-line `<input>` in viewport coordinates.
 * An `<input>` exposes no caret-pixel API, so we mirror the text up to the caret
 * in a hidden span and read its width. The block cursor's width and height both
 * derive from the input's own computed font-size here — one basis, no em-vs-px
 * drift — and x is clamped so the block never spills past the box edges.
 */
export function caretMetrics(input: HTMLInputElement): CaretMetrics {
  const style = window.getComputedStyle(input)
  const mirror = document.createElement('span')
  mirror.style.position = 'absolute'
  mirror.style.visibility = 'hidden'
  mirror.style.whiteSpace = 'pre'
  mirror.style.fontFamily = style.fontFamily
  mirror.style.fontSize = style.fontSize
  mirror.style.fontWeight = style.fontWeight
  mirror.style.fontStyle = style.fontStyle
  mirror.style.letterSpacing = style.letterSpacing
  // The caret renders at the focus end of a selection (selectionEnd for a
  // forward/collapsed selection, selectionStart for a backward one) — not always
  // selectionStart, or a range selection parks the block at the wrong end while
  // edits land at the invisible one.
  const caret =
    input.selectionDirection === 'backward'
      ? input.selectionStart ?? input.value.length
      : input.selectionEnd ?? input.value.length
  mirror.textContent = input.value.slice(0, caret)
  document.body.appendChild(mirror)
  const textWidth = mirror.getBoundingClientRect().width
  mirror.remove()
  const rect = input.getBoundingClientRect()
  const padLeft = parseFloat(style.paddingLeft) || 0
  const borderLeft = parseFloat(style.borderLeftWidth) || 0
  const fontSize = parseFloat(style.fontSize) || 16
  const height = Math.round(fontSize * 0.65) // ~two-thirds-height block
  const width = Math.max(2, Math.round(fontSize * 0.42)) // ~half a monospace cell
  const rawX = rect.left + borderLeft + padLeft + textWidth - input.scrollLeft
  // Pin inside the text box, leaving room for the block's own width so it never
  // overflows the right edge into the send button.
  const x = Math.max(rect.left, Math.min(rect.right - width, rawX))
  // A single-line input vertically centers its line, so centering the block in
  // the box aligns it with the glyphs.
  const top = rect.top + (rect.height - height) / 2
  return { x, top, height, width }
}

/**
 * Track the chat input's caret and call `onMeasure(input)` — rAF-coalesced —
 * whenever it may have moved, or `onMeasure(null)` when the input shouldn't show
 * a caret (blurred, window backgrounded, or `enabled` is false). Shared by every
 * caret-pinned feature (avatar gaze, block cursor) so the event wiring lives in
 * exactly one place.
 */
export function useCaretTracker<T extends HTMLElement>(
  wrapperRef: RefObject<T | null>,
  enabled: boolean,
  onMeasure: (input: HTMLInputElement | null) => void,
  selector: string = CHAT_INPUT_SELECTOR,
): void {
  const onMeasureRef = useRef(onMeasure)
  onMeasureRef.current = onMeasure
  useEffect(() => {
    const emit = (input: HTMLInputElement | null): void => onMeasureRef.current(input)
    if (!enabled) {
      emit(null)
      return
    }
    const input = wrapperRef.current?.querySelector<HTMLInputElement>(selector)
    if (!input) return
    let raf = 0
    const report = (): void => {
      raf = 0
      // A native caret shows only while the input holds selection AND the window
      // is foregrounded — mirror that so caret-pinned UI doesn't linger on a
      // backgrounded tab.
      emit(document.activeElement === input && document.hasFocus() ? input : null)
    }
    const schedule = (): void => {
      if (!raf) raf = requestAnimationFrame(report)
    }
    // selectionchange covers every caret move (typing, navigation, clicks);
    // focus/blur toggle visibility; scroll/resize + visualViewport keep a
    // fixed-positioned overlay pinned when the layout shifts (the iOS soft
    // keyboard only fires visualViewport events). Routing blur through the same
    // rAF as focus lets a blur→refocus in one frame coalesce to a single
    // measure — no flicker.
    const onSel = (): void => {
      if (document.activeElement === input) schedule()
    }
    input.addEventListener('focus', schedule)
    input.addEventListener('blur', schedule)
    document.addEventListener('selectionchange', onSel)
    window.addEventListener('scroll', schedule, true)
    window.addEventListener('resize', schedule)
    const vv = window.visualViewport
    vv?.addEventListener('resize', schedule)
    vv?.addEventListener('scroll', schedule)
    schedule()
    return () => {
      if (raf) cancelAnimationFrame(raf)
      input.removeEventListener('focus', schedule)
      input.removeEventListener('blur', schedule)
      document.removeEventListener('selectionchange', onSel)
      window.removeEventListener('scroll', schedule, true)
      window.removeEventListener('resize', schedule)
      vv?.removeEventListener('resize', schedule)
      vv?.removeEventListener('scroll', schedule)
      emit(null)
    }
  }, [wrapperRef, enabled, selector])
}
