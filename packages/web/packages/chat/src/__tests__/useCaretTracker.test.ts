// src/__tests__/useCaretTracker.test.ts
import { describe, expect, it, vi, beforeEach, afterEach } from 'vitest'
import { renderHook } from '@testing-library/react'
import { createRef } from 'react'
import { caretMetrics, useCaretTracker } from '../hooks/useCaretTracker'

// jsdom does no layout, so getBoundingClientRect returns zeros. Stub the
// prototype so caretMetrics' clamp math is meaningful: elements registered via
// setRect get their explicit rect; unregistered <span> mirrors (created fresh
// inside caretMetrics itself, so the test can't reach them beforehand) get a
// width that scales with their text length, standing in for glyph width.
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
})

function mountInput(value = 'hello'): { wrapper: HTMLDivElement; input: HTMLInputElement } {
  const wrapper = document.createElement('div')
  const input = document.createElement('input')
  input.className = 'pc-input'
  input.value = value
  wrapper.appendChild(input)
  document.body.appendChild(wrapper)
  return { wrapper, input }
}

describe('caretMetrics', () => {
  it('derives block width and height from the input font size', () => {
    const { input } = mountInput()
    input.style.fontSize = '20px'
    const box = caretMetrics(input)
    expect(box.height).toBe(13) // round(20 * 0.65)
    expect(box.width).toBe(8) // round(20 * 0.42)
  })

  it('clamps x inside the input box', () => {
    const { input } = mountInput('x'.repeat(500))
    setRect(input, { left: 50, right: 350, width: 300, top: 100, bottom: 140, height: 40 })
    const rect = input.getBoundingClientRect()
    const box = caretMetrics(input)
    expect(box.x).toBeGreaterThanOrEqual(rect.left)
    expect(box.x).toBeLessThanOrEqual(rect.right)
  })

  it('removes its measuring mirror from the document', () => {
    const { input } = mountInput()
    const before = document.body.childElementCount
    caretMetrics(input)
    expect(document.body.childElementCount).toBe(before)
  })
})

describe('useCaretTracker', () => {
  it('emits null immediately when disabled', () => {
    const { wrapper } = mountInput()
    const ref = createRef<HTMLDivElement>()
    Object.assign(ref, { current: wrapper })
    const onMeasure = vi.fn()
    renderHook(() => useCaretTracker(ref, false, onMeasure))
    expect(onMeasure).toHaveBeenCalledWith(null)
  })

  it('emits null on unmount when enabled', () => {
    const { wrapper } = mountInput()
    const ref = createRef<HTMLDivElement>()
    Object.assign(ref, { current: wrapper })
    const onMeasure = vi.fn()
    const { unmount } = renderHook(() => useCaretTracker(ref, true, onMeasure))
    onMeasure.mockClear()
    unmount()
    expect(onMeasure).toHaveBeenCalledWith(null)
  })
})
