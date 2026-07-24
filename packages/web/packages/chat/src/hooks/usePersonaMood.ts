import { useEffect, useRef, useState } from 'react'

export interface PersonaMoodConfig<E extends string> {
  /** True while the persona is awaiting a reply OR streaming one out. */
  responding: boolean
  /** True while the user is composing (non-empty input). */
  composing: boolean
  /** Moods rotated while responding. */
  flightMoods: readonly E[]
  /** Moods rotated while the user composes. */
  typingMoods: readonly E[]
  /** A transient mood that outranks everything when a reply lands. */
  answerBeat?: { mood: E; ms: number }
  /** Cadence for both rotations. Default 1500ms. */
  cycleMs?: number
}

/**
 * The persona's deliberate expression hint, or `null` to hand control back to
 * its own reflexes. Priority: the answer beat > the in-flight rotation > the
 * composing rotation > none.
 *
 * "Responding" covers both awaiting the reply AND streaming it out, treated as
 * one engaged stretch so the rotation keeps going and the beat fires only when
 * the persona has actually finished talking.
 */
export function usePersonaMood<E extends string>(cfg: PersonaMoodConfig<E>): E | null {
  const { responding, composing, flightMoods, typingMoods, answerBeat, cycleMs = 1500 } = cfg
  const [step, setStep] = useState(0)
  const [beat, setBeat] = useState<E | null>(null)

  // Rotate while engaged; reset when idle.
  const engaged = responding || composing
  useEffect(() => {
    if (!engaged) {
      setStep(0)
      return
    }
    const id = setInterval(() => setStep((s) => s + 1), cycleMs)
    return () => clearInterval(id)
  }, [engaged, cycleMs])

  // When responding ends, hold the beat, then hand control back.
  const beatTimer = useRef<ReturnType<typeof setTimeout> | undefined>(undefined)
  const wasResponding = useRef(false)
  useEffect(() => {
    if (wasResponding.current && !responding && answerBeat) {
      setBeat(answerBeat.mood)
      clearTimeout(beatTimer.current)
      beatTimer.current = setTimeout(() => setBeat(null), answerBeat.ms)
    }
    wasResponding.current = responding
  }, [responding, answerBeat])
  useEffect(() => () => clearTimeout(beatTimer.current), [])

  if (beat) return beat
  if (responding) return flightMoods[step % flightMoods.length] ?? null
  if (composing) return typingMoods[step % typingMoods.length] ?? null
  return null
}
