import { describe, expect, it, beforeEach, afterEach, vi } from 'vitest'
import { renderHook, act } from '@testing-library/react'
import { createRef } from 'react'
import { useInputFocusReclaim } from '../hooks/useInputFocusReclaim'

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

// Stubs window.getSelection() to report `text` as the current selection, so
// the pointerup handler's drag-to-select guard sees a non-empty selection.
function stubSelection(text: string): void {
  vi.spyOn(window, 'getSelection').mockReturnValue({
    toString: () => text,
  } as Selection)
}

describe('useInputFocusReclaim', () => {
  beforeEach(() => {
    vi.spyOn(document, 'hasFocus').mockReturnValue(true)
  })

  afterEach(() => {
    vi.useRealTimers()
    vi.restoreAllMocks()
  })

  it('claims focus when enabled', () => {
    const { ref, input } = mount()
    renderHook(() => useInputFocusReclaim(ref, true))
    expect(document.activeElement).toBe(input)
  })

  it('does not claim focus while disabled', () => {
    const { ref, input } = mount()
    renderHook(() => useInputFocusReclaim(ref, false))
    expect(document.activeElement).not.toBe(input)
  })

  it('does not claim focus on a disabled input', () => {
    const { ref, input } = mount()
    input.disabled = true
    renderHook(() => useInputFocusReclaim(ref, true))
    expect(document.activeElement).not.toBe(input)
  })

  it('does not reclaim focus synchronously at pointerup — only after the timer fires', () => {
    vi.useFakeTimers()
    const { ref, input } = mount()
    renderHook(() => useInputFocusReclaim(ref, true))
    input.blur()

    act(() => {
      document.dispatchEvent(new Event('pointerup'))
    })
    // setTimeout(refocus, 0) defers past the pointerup tick — not reclaimed yet
    expect(document.activeElement).not.toBe(input)

    act(() => {
      vi.advanceTimersByTime(0)
    })
    expect(document.activeElement).toBe(input)
  })

  it('does not reclaim focus on pointerup while text is selected', () => {
    vi.useFakeTimers()
    const { ref, input } = mount()
    renderHook(() => useInputFocusReclaim(ref, true))
    input.blur()
    stubSelection('selected text')

    act(() => {
      document.dispatchEvent(new Event('pointerup'))
    })
    act(() => {
      vi.advanceTimersByTime(0)
    })
    expect(document.activeElement).not.toBe(input)
  })

  it('does not call focus() when document.hasFocus() is false', () => {
    vi.useFakeTimers()
    vi.spyOn(document, 'hasFocus').mockReturnValue(false)
    const { ref, input } = mount()
    const focusSpy = vi.spyOn(input, 'focus')
    renderHook(() => useInputFocusReclaim(ref, true))

    act(() => {
      document.dispatchEvent(new Event('pointerup'))
    })
    act(() => {
      vi.advanceTimersByTime(0)
    })
    expect(focusSpy).not.toHaveBeenCalled()
  })
})
