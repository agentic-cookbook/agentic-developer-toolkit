// src/__tests__/useCaretTracker.test.ts
import { describe, expect, it, vi } from 'vitest'
import { renderHook } from '@testing-library/react'
import { createRef } from 'react'
import { caretMetrics, useCaretTracker } from '../hooks/useCaretTracker'
import { appendToBody, installCaretRectStub } from './helpers/caretDom'

// jsdom does no layout, so getBoundingClientRect returns zeros; installCaretRectStub
// swaps in one whose math is meaningful. setRect registers an explicit rect for an
// element; unregistered <span> mirrors get a width that scales with their text length.
const { setRect } = installCaretRectStub()

function mountInput(value = 'hello'): { wrapper: HTMLDivElement; input: HTMLInputElement } {
  const wrapper = document.createElement('div')
  const input = document.createElement('input')
  input.className = 'pc-input'
  input.value = value
  wrapper.appendChild(input)
  appendToBody(wrapper)
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

  it('locates the input via a custom selector', () => {
    // A field the default '.pc-input' selector would miss. Passing a matching
    // custom selector makes the hook find it and wire up, so unmount tears down
    // with the usual emit(null) — proof the selector arg routed the query.
    const wrapper = document.createElement('div')
    const input = document.createElement('input')
    input.className = 'custom-field'
    wrapper.appendChild(input)
    appendToBody(wrapper)
    const ref = createRef<HTMLDivElement>()
    Object.assign(ref, { current: wrapper })
    const onMeasure = vi.fn()
    const { unmount } = renderHook(() => useCaretTracker(ref, true, onMeasure, '.custom-field'))
    onMeasure.mockClear()
    unmount()
    expect(onMeasure).toHaveBeenCalledWith(null)
  })

  it('never wires up when the selector matches no element', () => {
    // The wrapper has a '.pc-input', but a selector that matches nothing makes
    // the hook bail before registering any teardown — so unmount emits nothing.
    const { wrapper } = mountInput()
    const ref = createRef<HTMLDivElement>()
    Object.assign(ref, { current: wrapper })
    const onMeasure = vi.fn()
    const { unmount } = renderHook(() => useCaretTracker(ref, true, onMeasure, '.no-such-input'))
    onMeasure.mockClear()
    unmount()
    expect(onMeasure).not.toHaveBeenCalled()
  })
})
