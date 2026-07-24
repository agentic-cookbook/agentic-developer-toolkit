import { describe, expect, it, beforeEach, vi } from 'vitest'
import { renderHook } from '@testing-library/react'
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

describe('useInputFocusReclaim', () => {
  beforeEach(() => {
    vi.spyOn(document, 'hasFocus').mockReturnValue(true)
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
})
