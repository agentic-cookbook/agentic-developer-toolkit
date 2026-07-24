// src/__tests__/useRotatingPhrase.test.ts
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'
import { act, renderHook } from '@testing-library/react'
import { useRotatingPhrase, useTransientEcho } from '../hooks/useRotatingPhrase'

const POOL = ['a', 'b', 'c'] as const

beforeEach(() => vi.useFakeTimers())
afterEach(() => {
  vi.useRealTimers()
  vi.restoreAllMocks()
})

describe('useRotatingPhrase', () => {
  it('returns a member of the pool', () => {
    const { result } = renderHook(() => useRotatingPhrase(POOL, 0))
    expect(POOL).toContain(result.current)
  })

  it('stays put when the reroll key does not change', () => {
    // Deterministic, non-repeating draws: with unmocked Math.random a spurious
    // re-roll would land on the same value 1-in-3 times, so this would pass by
    // chance even if the hook incorrectly re-rolled on every render. Forcing
    // successive draws to differ makes a spurious re-roll observable.
    const draws = [0, 0.99]
    let i = 0
    vi.spyOn(Math, 'random').mockImplementation(() => draws[i++ % draws.length]!)
    const { result, rerender } = renderHook(
      ({ k }: { k: number }) => useRotatingPhrase(POOL, k),
      { initialProps: { k: 0 } },
    )
    const first = result.current
    rerender({ k: 0 })
    expect(result.current).toBe(first)
  })

  it('re-rolls when the reroll key changes', () => {
    // Complements the "stays put" case above: without this, a hook that never
    // re-rolls at all would also trivially satisfy "stays put".
    const draws = [0, 0.99]
    let i = 0
    vi.spyOn(Math, 'random').mockImplementation(() => draws[i++ % draws.length]!)
    const { result, rerender } = renderHook(
      ({ k }: { k: number }) => useRotatingPhrase(POOL, k),
      { initialProps: { k: 0 } },
    )
    expect(result.current).toBe('a')
    rerender({ k: 1 })
    expect(result.current).toBe('c')
  })

  it('returns the empty string for an empty pool', () => {
    const { result } = renderHook(() => useRotatingPhrase([], 0))
    expect(result.current).toBe('')
  })
})

describe('useTransientEcho', () => {
  it('echoes an utterance then clears it', () => {
    const { result, rerender } = renderHook(
      ({ u }: { u: { text: string; id: number } | null }) => useTransientEcho(u, 1800),
      { initialProps: { u: null as { text: string; id: number } | null } },
    )
    expect(result.current.echo).toBeNull()
    rerender({ u: { text: 'zzz', id: 1 } })
    expect(result.current.echo).toBe('zzz')
    act(() => { vi.advanceTimersByTime(1799) })
    expect(result.current.echo).toBe('zzz')
    act(() => { vi.advanceTimersByTime(1) })
    expect(result.current.echo).toBeNull()
  })

  it('bumps the idle index when the echo clears', () => {
    const { result, rerender } = renderHook(
      ({ u }: { u: { text: string; id: number } | null }) => useTransientEcho(u, 1800),
      { initialProps: { u: null as { text: string; id: number } | null } },
    )
    const before = result.current.idleIndex
    rerender({ u: { text: 'well?', id: 1 } })
    act(() => { vi.advanceTimersByTime(1800) })
    expect(result.current.idleIndex).not.toBe(before)
  })

  it('honors a custom holdMs instead of the default', () => {
    // The brief's own "echoes then clears" test passes holdMs=1800, which is
    // also the default — it can't tell a correctly-threaded holdMs apart from
    // a hardcoded 1800ms. This exercises a distinct value.
    const { result, rerender } = renderHook(
      ({ u }: { u: { text: string; id: number } | null }) => useTransientEcho(u, 500),
      { initialProps: { u: null as { text: string; id: number } | null } },
    )
    rerender({ u: { text: 'hi', id: 1 } })
    act(() => { vi.advanceTimersByTime(499) })
    expect(result.current.echo).toBe('hi')
    act(() => { vi.advanceTimersByTime(1) })
    expect(result.current.echo).toBeNull()
  })

  it('replaces the echo on a new id without letting the stale timer clear it early', () => {
    const { result, rerender } = renderHook(
      ({ u }: { u: { text: string; id: number } | null }) => useTransientEcho(u, 1800),
      { initialProps: { u: null as { text: string; id: number } | null } },
    )
    rerender({ u: { text: 'first', id: 1 } })
    act(() => { vi.advanceTimersByTime(900) })
    rerender({ u: { text: 'second', id: 2 } })
    expect(result.current.echo).toBe('second')
    // The stale id=1 timer was due to fire here (900 + 900); it must have been
    // cleared, or it would wrongly null out the id=2 echo early.
    act(() => { vi.advanceTimersByTime(900) })
    expect(result.current.echo).toBe('second')
    act(() => { vi.advanceTimersByTime(900) })
    expect(result.current.echo).toBeNull()
  })
})
