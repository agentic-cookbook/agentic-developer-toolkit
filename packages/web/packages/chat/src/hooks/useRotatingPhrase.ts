import { useEffect, useRef, useState } from 'react'

/**
 * A phrase drawn at random from `pool`, re-rolled whenever `rerollKey` changes
 * (typically a sent-message count). The initial pick happens on mount rather
 * than during render, so server and client agree on the first frame; later key
 * changes re-roll synchronously during render so the new phrase lands in the
 * same paint as its trigger, with no one-frame lag from an effect.
 */
export function useRotatingPhrase(pool: readonly string[], rerollKey: number): string {
  const [phrase, setPhrase] = useState<string>(pool[0] ?? '')
  const [rolledKey, setRolledKey] = useState<number | null>(null)
  // An empty pool falls through to '' via `?? ''`, so no length guard is needed.
  const roll = (): string => pool[Math.floor(Math.random() * pool.length)] ?? ''

  // After the mount roll, re-roll during render on a key change (React's
  // "adjust state during render" pattern) — same paint, no effect-tick lag.
  if (rolledKey !== null && rolledKey !== rerollKey) {
    setRolledKey(rerollKey)
    setPhrase(roll())
  }

  useEffect(() => {
    setRolledKey(rerollKey)
    setPhrase(roll())
    // Roll once on mount; render-time adjustment handles later key changes.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  return phrase
}

/**
 * Echo a persona's transient utterance for `holdMs`, then clear it. `idleIndex`
 * bumps each time an echo clears, so a caller can re-roll whatever idle phrase
 * it shows between utterances.
 */
export function useTransientEcho(
  utterance: { text: string; id: number } | null | undefined,
  holdMs = 1800,
): { echo: string | null; idleIndex: number } {
  const [echo, setEcho] = useState<string | null>(null)
  const [idleIndex, setIdleIndex] = useState(0)
  const timer = useRef<ReturnType<typeof setTimeout> | undefined>(undefined)
  const id = utterance?.id
  const textRef = useRef(utterance?.text)
  textRef.current = utterance?.text
  useEffect(() => {
    if (id === undefined) return
    setEcho(textRef.current ?? null)
    clearTimeout(timer.current)
    timer.current = setTimeout(() => {
      setEcho(null)
      setIdleIndex((n) => n + 1)
    }, holdMs)
  }, [id, holdMs])
  useEffect(() => () => clearTimeout(timer.current), [])
  return { echo, idleIndex }
}
