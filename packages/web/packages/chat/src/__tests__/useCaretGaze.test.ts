// src/__tests__/useCaretGaze.test.ts
import { describe, expect, it, vi, beforeEach, afterEach } from 'vitest'
import { renderHook, act } from '@testing-library/react'
import { createRef } from 'react'
import { useCaretGaze } from '../hooks/useCaretGaze'

// jsdom does no layout, so getBoundingClientRect returns zeros. Stub the
// prototype (same pattern as useCaretTracker.test.ts / useBlockCursor.test.ts)
// so the geometry caretMetrics computes under the hood is meaningful:
// elements registered via setRect get their explicit rect; unregistered
// <span> mirrors (created fresh inside caretMetrics itself) get a width that
// scales with their text length, standing in for glyph width.
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
  // useCaretGaze has no synchronous "already focused" shortcut of its own —
  // unlike useBlockCursor it relies entirely on useCaretTracker's
  // rAF-coalesced measurement, so every test needs fake timers to flush it.
  vi.useFakeTimers()
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

function mount(value: string): {
  wrapperRef: { current: HTMLDivElement | null }
  anchorRef: { current: HTMLDivElement | null }
  input: HTMLInputElement
  anchor: HTMLDivElement
} {
  const wrapper = document.createElement('div')
  const input = document.createElement('input')
  input.className = 'pc-input'
  input.value = value
  wrapper.appendChild(input)
  const anchor = document.createElement('div')
  document.body.append(wrapper, anchor)
  const wrapperRef = createRef<HTMLDivElement>()
  const anchorRef = createRef<HTMLDivElement>()
  Object.assign(wrapperRef, { current: wrapper })
  Object.assign(anchorRef, { current: anchor })
  return { wrapperRef, anchorRef, input, anchor }
}

// Flush useCaretTracker's rAF-coalesced measurement.
function flush(): void {
  act(() => {
    vi.advanceTimersByTime(20)
  })
}

// Fixed input geometry for the computation tests: a 300px-wide box at
// x=50..350, fontSize 20px so caretMetrics derives a caret block width of
// max(2, round(20*0.42)) = 8. With value 'hihihi' (6 chars) the mirror-span
// stub above reports textWidth = 6*10 = 60, so caretMetrics' x works out to
// clamp(rect.left + 0 + 0 + 60 - 0, rect.left, rect.right-8) = 110.
function setInputGeometry(input: HTMLInputElement): void {
  input.style.fontSize = '20px'
  setRect(input, { left: 50, right: 350, width: 300, top: 100, bottom: 140, height: 40 })
}

describe('useCaretGaze', () => {
  it('reports null when there is no anchor', () => {
    // Focused with non-empty text so the !input and empty-value guards are
    // both false — isolates the !anchor branch specifically.
    const { wrapperRef, input } = mount('hi')
    input.focus()
    const onGaze = vi.fn()
    renderHook(() => useCaretGaze(wrapperRef, undefined, onGaze))
    flush()
    expect(onGaze).toHaveBeenCalledWith(null)
  })

  it('reports null for an empty input', () => {
    // Focused, with a real anchor — isolates the empty-value branch.
    const { wrapperRef, anchorRef, input } = mount('')
    input.focus()
    const onGaze = vi.fn()
    renderHook(() => useCaretGaze(wrapperRef, anchorRef, onGaze))
    flush()
    expect(onGaze).toHaveBeenCalledWith(null)
  })

  it('reports null when the input is unfocused, even with an anchor and text', () => {
    // Deliberately left unfocused — isolates the !input branch. Without this
    // test, "no anchor" and "empty input" above would both pass vacuously:
    // an unfocused input already reports null via useCaretTracker regardless
    // of anchor or value.
    const { wrapperRef, anchorRef } = mount('hi')
    const onGaze = vi.fn()
    renderHook(() => useCaretGaze(wrapperRef, anchorRef, onGaze))
    flush()
    expect(onGaze).toHaveBeenCalledWith(null)
  })

  it('reports a gaze vector derived from the caret position relative to the anchor', () => {
    const { wrapperRef, anchorRef, input, anchor } = mount('hihihi')
    setInputGeometry(input)
    setRect(anchor, { left: 100, right: 150, width: 50, top: 0, bottom: 0, height: 0 })
    input.focus()
    const onGaze = vi.fn()
    renderHook(() => useCaretGaze(wrapperRef, anchorRef, onGaze))
    flush()
    // caretMetrics(input).x = 110; anchor center = 100 + 50/2 = 125;
    // dx = 110 - 125 = -15; denom = rect.width/2 = 150; ratio = -0.1
    expect(onGaze).toHaveBeenCalledWith({ x: -0.1, y: 0.9 })
  })

  it('clamps the gaze x to -1..1 when the caret falls outside the anchor', () => {
    const { wrapperRef, anchorRef, input, anchor } = mount('hihihi')
    setInputGeometry(input)

    // Anchor far to the right: dx = 110 - 1000 = -890, ratio ≈ -5.93.
    setRect(anchor, { left: 1000, right: 1000, width: 0, top: 0, bottom: 0, height: 0 })
    input.focus()
    const onGazeLow = vi.fn()
    renderHook(() => useCaretGaze(wrapperRef, anchorRef, onGazeLow))
    flush()
    expect(onGazeLow).toHaveBeenCalledWith({ x: -1, y: 0.9 })

    // Anchor far to the left: dx = 110 - (-800) = 910, ratio ≈ 6.07.
    setRect(anchor, { left: -800, right: -800, width: 0, top: 0, bottom: 0, height: 0 })
    const onGazeHigh = vi.fn()
    renderHook(() => useCaretGaze(wrapperRef, anchorRef, onGazeHigh))
    flush()
    expect(onGazeHigh).toHaveBeenCalledWith({ x: 1, y: 0.9 })
  })

  it('uses a custom downBias from opts instead of the 0.9 default', () => {
    const { wrapperRef, anchorRef, input, anchor } = mount('hihihi')
    setInputGeometry(input)
    setRect(anchor, { left: 100, right: 150, width: 50, top: 0, bottom: 0, height: 0 })
    input.focus()
    const onGaze = vi.fn()
    renderHook(() => useCaretGaze(wrapperRef, anchorRef, onGaze, { downBias: 0.3 }))
    flush()
    expect(onGaze).toHaveBeenCalledWith({ x: -0.1, y: 0.3 })
  })

  it('does not report anything when no element matches the default selector', () => {
    const { wrapperRef, anchorRef, input } = mount('hi')
    input.className = 'custom-input' // no longer matches CHAT_INPUT_SELECTOR
    input.focus()
    const onGaze = vi.fn()
    renderHook(() => useCaretGaze(wrapperRef, anchorRef, onGaze))
    flush()
    expect(onGaze).not.toHaveBeenCalled()
  })

  it('uses a custom selector from opts to locate the input', () => {
    const { wrapperRef, anchorRef, input, anchor } = mount('hihihi')
    input.className = 'custom-input'
    setInputGeometry(input)
    setRect(anchor, { left: 100, right: 150, width: 50, top: 0, bottom: 0, height: 0 })
    input.focus()
    const onGaze = vi.fn()
    renderHook(() => useCaretGaze(wrapperRef, anchorRef, onGaze, { selector: '.custom-input' }))
    flush()
    expect(onGaze).toHaveBeenCalledWith({ x: -0.1, y: 0.9 })
  })
})
