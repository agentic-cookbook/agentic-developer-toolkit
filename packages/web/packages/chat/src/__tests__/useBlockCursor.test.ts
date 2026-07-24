// src/__tests__/useBlockCursor.test.ts
import { describe, expect, it, vi, beforeEach, afterEach } from 'vitest'
import { renderHook, act } from '@testing-library/react'
import { createRef } from 'react'
import { useBlockCursor } from '../hooks/useBlockCursor'

// jsdom does no layout, so getBoundingClientRect returns zeros. Stub the
// prototype (same pattern as useCaretTracker.test.ts) so the geometry
// caretMetrics computes under the hood is meaningful: elements registered via
// setRect get their explicit rect; unregistered <span> mirrors (created fresh
// inside caretMetrics itself) get a width that scales with their text length.
const ORIGINAL_GBCR = Element.prototype.getBoundingClientRect
const rectsByElement = new WeakMap<Element, DOMRect>()

function makeRect(rect: Partial<DOMRect>): DOMRect {
  return {
    x: 0, y: 0, width: 0, height: 0, top: 0, left: 0, right: 0, bottom: 0,
    toJSON: () => ({}),
    ...rect,
  } as DOMRect
}

function setRect(el: Element, rect: Partial<DOMRect>) {
  rectsByElement.set(el, makeRect(rect))
}

beforeEach(() => {
  Element.prototype.getBoundingClientRect = function () {
    const known = rectsByElement.get(this)
    if (known) return known
    if (this.tagName === 'SPAN') {
      const width = (this.textContent?.length ?? 0) * 10
      return makeRect({ width, right: width })
    }
    return makeRect({})
  }
})

afterEach(() => {
  Element.prototype.getBoundingClientRect = ORIGINAL_GBCR
  vi.useRealTimers()
  vi.restoreAllMocks()
})

function mount(): { ref: { current: HTMLDivElement | null }; input: HTMLInputElement } {
  const wrapper = document.createElement('div')
  const input = document.createElement('input')
  input.className = 'pc-input'
  wrapper.appendChild(input)
  document.body.appendChild(wrapper)
  const ref = createRef<HTMLDivElement>()
  Object.assign(ref, { current: wrapper })
  return { ref, input }
}

// A fixed geometry used by the measurement tests below: 200px-wide input,
// 40px tall, positioned at (10, 5). With fontSize 20px caretMetrics derives
// height = round(20 * 0.65) = 13 and width = max(2, round(20 * 0.42)) = 8, and
// an empty input parks the caret at the box's left edge (x = rect.left = 10,
// top = rect.top + (rect.height - height) / 2 = 5 + 13.5 = 18.5).
function setInputGeometry(input: HTMLInputElement, left: number): void {
  input.style.fontSize = '20px'
  setRect(input, { left, right: left + 200, width: 200, top: 5, bottom: 45, height: 40 })
}

describe('useBlockCursor', () => {
  it('returns null while disabled', () => {
    const { ref } = mount()
    const { result } = renderHook(() => useBlockCursor(ref, false, 0))
    expect(result.current).toBeNull()
  })

  it('hides the native caret while enabled and restores it on disable', () => {
    const { ref, input } = mount()
    const { rerender } = renderHook(
      ({ on }: { on: boolean }) => useBlockCursor(ref, on, 0),
      { initialProps: { on: true } },
    )
    expect(input.style.caretColor).toBe('transparent')
    rerender({ on: false })
    expect(input.style.caretColor).toBe('')
  })

  it('leaves the native caret alone when no element matches the selector', () => {
    const { ref, input } = mount()
    renderHook(() => useBlockCursor(ref, true, 0, '.does-not-exist'))
    expect(input.style.caretColor).toBe('')
  })

  it('does not measure a caret while the input is unfocused', () => {
    const { ref, input } = mount()
    setInputGeometry(input, 10)
    const { result } = renderHook(() => useBlockCursor(ref, true, 0))
    expect(document.activeElement).not.toBe(input)
    expect(result.current).toBeNull()
  })

  it('measures the caret geometry on mount when the input is already focused', () => {
    const { ref, input } = mount()
    setInputGeometry(input, 10)
    input.focus()
    const { result } = renderHook(() => useBlockCursor(ref, true, 0))
    expect(result.current).toEqual({ x: 10, top: 18.5, height: 13, width: 8 })
  })

  it('re-measures when resetKey changes while the input stays focused', () => {
    const { ref, input } = mount()
    setInputGeometry(input, 10)
    input.focus()
    const { result, rerender } = renderHook(
      ({ key }: { key: number }) => useBlockCursor(ref, true, key),
      { initialProps: { key: 0 } },
    )
    expect(result.current).toEqual({ x: 10, top: 18.5, height: 13, width: 8 })

    setInputGeometry(input, 60) // caret "moved" — e.g. the field grew text
    rerender({ key: 1 })
    expect(result.current).toEqual({ x: 60, top: 18.5, height: 13, width: 8 })
  })

  it('keeps the same object reference when a re-measure yields identical geometry', () => {
    const { ref, input } = mount()
    setInputGeometry(input, 10)
    input.focus()
    const { result, rerender } = renderHook(
      ({ key }: { key: number }) => useBlockCursor(ref, true, key),
      { initialProps: { key: 0 } },
    )
    const first = result.current
    expect(first).not.toBeNull()

    // Same geometry, bumped resetKey: the equality guard should keep `prev`.
    rerender({ key: 1 })
    expect(result.current).toBe(first)
  })

  it('follows the caret via the tracker and clears the box on blur', () => {
    vi.useFakeTimers()
    const { ref, input } = mount()
    setInputGeometry(input, 10)
    const { result } = renderHook(() => useBlockCursor(ref, true, 0))
    expect(result.current).toBeNull() // not focused yet

    act(() => {
      input.focus()
      vi.advanceTimersByTime(20) // flush useCaretTracker's rAF-coalesced measure
    })
    expect(result.current).toEqual({ x: 10, top: 18.5, height: 13, width: 8 })

    act(() => {
      input.blur()
      vi.advanceTimersByTime(20)
    })
    expect(result.current).toBeNull()
  })
})
