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
  it('is null and off-beat when idle', () => {
    const { result } = renderHook(() =>
      usePersonaMood<Mood>({ ...base, responding: false, composing: false }),
    )
    expect(result.current.mood).toBeNull()
    expect(result.current.beat).toBe(false)
  })

  it('reports the first typing mood while composing', () => {
    const { result } = renderHook(() =>
      usePersonaMood<Mood>({ ...base, responding: false, composing: true }),
    )
    expect(result.current.mood).toBe('curious')
    expect(result.current.beat).toBe(false)
  })

  it('prefers responding over composing', () => {
    const { result } = renderHook(() =>
      usePersonaMood<Mood>({ ...base, responding: true, composing: true }),
    )
    expect(result.current.mood).toBe('thinking')
  })

  it('advances through flight moods on the cycle', () => {
    const { result } = renderHook(() =>
      usePersonaMood<Mood>({ ...base, responding: true, composing: false }),
    )
    expect(result.current.mood).toBe('thinking')
    act(() => { vi.advanceTimersByTime(1000) })
    expect(result.current.mood).toBe('excited')
  })

  it('flags the flight rotation as off-beat even when a mood matches the beat mood', () => {
    // A rotation mood equal to answerBeat.mood must NOT read as a beat: `beat`
    // is the robust "just finished replying" signal, not a string compare.
    const { result } = renderHook(() =>
      usePersonaMood<Mood>({
        ...base,
        flightMoods: ['smug'] as const,
        responding: true,
        composing: false,
      }),
    )
    expect(result.current.mood).toBe('smug')
    expect(result.current.beat).toBe(false)
  })

  it('fires the answer beat when responding ends, then clears it', () => {
    const { result, rerender } = renderHook(
      ({ responding }: { responding: boolean }) =>
        usePersonaMood<Mood>({ ...base, responding, composing: false }),
      { initialProps: { responding: true } },
    )
    rerender({ responding: false })
    expect(result.current.mood).toBe('smug')
    expect(result.current.beat).toBe(true)
    act(() => { vi.advanceTimersByTime(2000) })
    expect(result.current.mood).toBeNull()
    expect(result.current.beat).toBe(false)
  })

  it('fires no beat when answerBeat is not configured', () => {
    // answerBeat is optional; omit it entirely. Responding ending must then be a
    // no-op — no beat mood, no beat flag — rather than throwing on the undefined.
    const { result, rerender } = renderHook(
      ({ responding }: { responding: boolean }) =>
        usePersonaMood<Mood>({
          flightMoods: base.flightMoods,
          typingMoods: base.typingMoods,
          cycleMs: base.cycleMs,
          responding,
          composing: false,
        }),
      { initialProps: { responding: true } },
    )
    rerender({ responding: false })
    expect(result.current.mood).toBeNull()
    expect(result.current.beat).toBe(false)
  })
})
