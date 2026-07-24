// src/__tests__/usePersonaMood.test.ts
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'
import { act, renderHook } from '@testing-library/react'
import { usePersonaMood } from '../hooks/usePersonaMood'

type Mood = 'thinking' | 'curious' | 'excited' | 'smug'

const base = {
  flightMoods: ['thinking', 'excited'] as const,
  typingMoods: ['curious'] as const,
  answerBeat: { mood: 'smug' as const, ms: 2000 },
  cycleMs: 1000,
}

beforeEach(() => vi.useFakeTimers())
afterEach(() => vi.useRealTimers())

describe('usePersonaMood', () => {
  it('is null when idle', () => {
    const { result } = renderHook(() =>
      usePersonaMood<Mood>({ ...base, responding: false, composing: false }),
    )
    expect(result.current).toBeNull()
  })

  it('reports the first typing mood while composing', () => {
    const { result } = renderHook(() =>
      usePersonaMood<Mood>({ ...base, responding: false, composing: true }),
    )
    expect(result.current).toBe('curious')
  })

  it('prefers responding over composing', () => {
    const { result } = renderHook(() =>
      usePersonaMood<Mood>({ ...base, responding: true, composing: true }),
    )
    expect(result.current).toBe('thinking')
  })

  it('advances through flight moods on the cycle', () => {
    const { result } = renderHook(() =>
      usePersonaMood<Mood>({ ...base, responding: true, composing: false }),
    )
    expect(result.current).toBe('thinking')
    act(() => { vi.advanceTimersByTime(1000) })
    expect(result.current).toBe('excited')
  })

  it('fires the answer beat when responding ends, then clears it', () => {
    const { result, rerender } = renderHook(
      ({ responding }: { responding: boolean }) =>
        usePersonaMood<Mood>({ ...base, responding, composing: false }),
      { initialProps: { responding: true } },
    )
    rerender({ responding: false })
    expect(result.current).toBe('smug')
    act(() => { vi.advanceTimersByTime(2000) })
    expect(result.current).toBeNull()
  })
})
