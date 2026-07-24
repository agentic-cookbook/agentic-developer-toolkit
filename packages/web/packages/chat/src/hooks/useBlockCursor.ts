import { useCallback, useEffect, useState, type RefObject } from 'react'
import {
  CHAT_INPUT_SELECTOR,
  caretMetrics,
  useCaretTracker,
  type CaretMetrics,
} from './useCaretTracker'

/**
 * Old-school block cursor: while `enabled`, returns the geometry of a blinking
 * rectangle to draw over the input's caret, and hides the native I-beam. Themes
 * that draw their own block cursor turn this on; everyone else leaves it off and
 * keeps the native caret.
 *
 * Unlike gaze this shows even on an empty input, the way a real terminal parks
 * its cursor at an empty prompt. The equality guard limits re-renders to the
 * frames where the block actually moves — scroll events during streaming
 * re-measure but rarely shift it.
 *
 * `resetKey` should change on each send: sending clears the field
 * programmatically (`input.value = ""`), which fires no input/selectionchange
 * event, so the tracker never hears about it and the block would stay parked at
 * the just-sent text's end. Bumping `resetKey` re-measures so the cursor snaps
 * back to the empty prompt.
 */
export function useBlockCursor<T extends HTMLElement>(
  wrapperRef: RefObject<T | null>,
  enabled: boolean,
  resetKey: number,
  selector: string = CHAT_INPUT_SELECTOR,
): CaretMetrics | null {
  const [caretBox, setCaretBox] = useState<CaretMetrics | null>(null)

  const onCaretMeasure = useCallback((input: HTMLInputElement | null): void => {
    if (!input) {
      setCaretBox(null)
      return
    }
    const box = caretMetrics(input)
    setCaretBox((prev) =>
      prev &&
      prev.x === box.x &&
      prev.top === box.top &&
      prev.height === box.height &&
      prev.width === box.width
        ? prev
        : box,
    )
  }, [])

  useCaretTracker(wrapperRef, enabled, onCaretMeasure, selector)

  // Re-measure on each send so the block snaps back to the empty prompt.
  useEffect(() => {
    if (!enabled) return
    const input = wrapperRef.current?.querySelector<HTMLInputElement>(selector)
    if (input && document.activeElement === input) onCaretMeasure(input)
  }, [resetKey, enabled, onCaretMeasure, wrapperRef, selector])

  // Hide the native I-beam in JS, only while the block cursor is active — so a
  // failed hydration degrades to the native caret instead of no caret at all.
  // Inline style beats the theme's cascade; cleared when disabling so other
  // themes keep their native caret.
  useEffect(() => {
    if (!enabled) return
    const input = wrapperRef.current?.querySelector<HTMLInputElement>(selector)
    if (!input) return
    input.style.caretColor = 'transparent'
    return () => {
      input.style.caretColor = ''
    }
  }, [enabled, wrapperRef, selector])

  return enabled ? caretBox : null
}
