import { useCallback, type RefObject } from 'react'
import { CHAT_INPUT_SELECTOR, caretMetrics, useCaretTracker } from './useCaretTracker'

/** A unit-square gaze direction: -1..1 on each axis. */
export interface GazeVector {
  x: number
  y: number
}

export interface CaretGazeOptions {
  /** How far down to point while composing. Default 0.9 (peering at the box). */
  downBias?: number
  selector?: string
}

const clampUnit = (n: number): number => Math.max(-1, Math.min(1, n))

/**
 * Caret-follow: while the user composes, map the caret's screen-x to a gaze
 * direction relative to `anchorRef`'s frame (half the input width → ±1), biased
 * downward so an avatar peers at the box. An empty or blurred input reports
 * `null`, handing the avatar's gaze back to its own reflexes.
 */
export function useCaretGaze<T extends HTMLElement>(
  wrapperRef: RefObject<T | null>,
  anchorRef: RefObject<HTMLElement | null> | undefined,
  onGaze: (gaze: GazeVector | null) => void,
  opts: CaretGazeOptions = {},
): void {
  const { downBias = 0.9, selector = CHAT_INPUT_SELECTOR } = opts
  const onMeasure = useCallback(
    (input: HTMLInputElement | null): void => {
      const anchor = anchorRef?.current
      if (!input || !anchor || input.value.length === 0) {
        onGaze(null)
        return
      }
      const a = anchor.getBoundingClientRect()
      const rect = input.getBoundingClientRect()
      const dx = caretMetrics(input).x - (a.left + a.width / 2)
      onGaze({ x: clampUnit(dx / (rect.width / 2 || 1)), y: downBias })
    },
    [anchorRef, onGaze, downBias],
  )
  useCaretTracker(wrapperRef, true, onMeasure, selector)
}
