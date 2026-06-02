"use client"

import { useEffect, useRef, useState } from 'react'

// A classic terminal spinner — rotates smoothly in a monospace font.
const DEFAULT_FRAMES = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
// Settled glyph for the completed (grey) state, à la Claude's "✱ Churned for…".
const DEFAULT_DONE_GLYPH = '✱'

export interface TypingIndicatorProps {
  /** Whether a reply is currently in flight. */
  isTyping: boolean
  /**
   * "Thinking" words to cycle through while in flight (e.g. ["zeeping",
   * "zorping"]). When omitted, falls back to the classic three-dot indicator
   * and nothing persists — so existing consumers are unaffected.
   */
  labels?: string[]
  /** Frames for the rotating glyph. Defaults to a braille spinner. */
  frames?: string[]
  /** Settled glyph for the grey done line. Defaults to "✱". */
  doneGlyph?: string
  /** Flash random non-green colors while thinking (settles to grey when done). */
  colorful?: boolean
  /** Spinner frame interval (ms). */
  frameMs?: number
  /** How often to switch to a new random word (ms). */
  labelMs?: number
  /**
   * When set and nothing has been in flight yet, show this as an idle status
   * line with the animating glyph (e.g. "waiting to zeeble"). It yields to the
   * thinking state on the first reply and never returns.
   */
  idlePhrase?: string
}

export function TypingIndicator({
  isTyping,
  labels,
  frames,
  doneGlyph,
  colorful,
  frameMs,
  labelMs,
  idlePhrase,
}: TypingIndicatorProps) {
  // Classic three-dot fallback when no words are configured (no persisted state).
  if (!labels || labels.length === 0) {
    return isTyping ? (
      <div className="pc-message pc-persona pc-typing">
        <div className="pc-bubble">
          <div className="pc-dots">
            <span />
            <span />
            <span />
          </div>
        </div>
      </div>
    ) : null
  }
  return (
    <ThinkingStatus
      active={isTyping}
      idlePhrase={idlePhrase}
      labels={labels}
      frames={frames ?? DEFAULT_FRAMES}
      doneGlyph={doneGlyph ?? DEFAULT_DONE_GLYPH}
      colorful={colorful ?? false}
      frameMs={frameMs ?? 260}
      labelMs={labelMs ?? 1800}
    />
  )
}

function randomLabel(labels: string[]): string {
  return labels[Math.floor(Math.random() * labels.length)] ?? labels[0] ?? ''
}

/** zorping → zorped, zeeping → zeeped (present participle → past tense). */
function pastTense(word: string): string {
  return word.endsWith('ing') ? `${word.slice(0, -3)}ed` : `${word}ed`
}

/**
 * A vivid color that is never green — skips the ~75°–165° hue band — and stays
 * bright enough to read on a dark surface.
 */
function randomNonGreen(): string {
  const r = Math.floor(Math.random() * 270)
  const hue = r < 75 ? r : r + 90
  return `hsl(${hue}, 85%, 62%)`
}

interface ThinkingStatusProps {
  active: boolean
  idlePhrase?: string
  labels: string[]
  frames: string[]
  doneGlyph: string
  colorful: boolean
  frameMs: number
  labelMs: number
}

type Phase = 'idle' | 'thinking' | 'done'

/**
 * While `active`, shows `[rotating glyph] [silly word]…`, optionally flashing
 * random non-green colors. When it stops, freezes into a grey
 * `[done glyph] [past-tense word] for Ns` that persists until the next think,
 * mirroring Claude's completed-thinking line.
 */
function ThinkingStatus({
  active,
  idlePhrase,
  labels,
  frames,
  doneGlyph,
  colorful,
  frameMs,
  labelMs,
}: ThinkingStatusProps) {
  const [phase, setPhase] = useState<Phase>(active ? 'thinking' : 'idle')
  const [frame, setFrame] = useState(0)
  const [word, setWord] = useState(() => randomLabel(labels))
  const [color, setColor] = useState<string | undefined>(undefined)
  const [done, setDone] = useState<{ word: string; secs: number } | null>(null)

  // Always-current refs so the active→idle transition reads the latest values
  // without re-subscribing the effect on every tick.
  const wordRef = useRef(word)
  wordRef.current = word
  const startRef = useRef(0)

  // Phase transitions driven by `active` (the chat's isTyping).
  useEffect(() => {
    if (active) {
      setWord(randomLabel(labels))
      if (colorful) setColor(randomNonGreen())
      startRef.current = Date.now()
      setPhase('thinking')
    } else {
      setPhase((p) => {
        if (p !== 'thinking') return p
        const secs = Math.max(1, Math.round((Date.now() - startRef.current) / 1000))
        setDone({ word: pastTense(wordRef.current), secs })
        return 'done'
      })
    }
  }, [active, labels, colorful])

  // Spinner, word, and (optional) color cycling — only while thinking.
  useEffect(() => {
    if (phase !== 'thinking') return
    const f = setInterval(() => setFrame((i) => (i + 1) % frames.length), frameMs)
    const l = setInterval(() => setWord(randomLabel(labels)), labelMs)
    const c = colorful ? setInterval(() => setColor(randomNonGreen()), 1000) : undefined
    return () => {
      clearInterval(f)
      clearInterval(l)
      if (c) clearInterval(c)
    }
  }, [phase, frames.length, frameMs, labels, labelMs, colorful])

  // Before the first reply, an idle status rendered in the settled/completed
  // (grey) style — it's a quiet "waiting", not an active think.
  if (phase === 'idle') {
    if (!idlePhrase) return null
    return (
      <div className="pc-message pc-persona pc-typing">
        <div className="pc-bubble">
          <span className="pc-thinking pc-thinking--done">
            <span className="pc-thinking-glyph" aria-hidden="true">{doneGlyph}</span>
            <span className="pc-thinking-label">{idlePhrase}</span>
            <span className="pc-thinking-ellipsis" aria-hidden="true">…</span>
          </span>
        </div>
      </div>
    )
  }

  if (phase === 'done' && done) {
    return (
      <div className="pc-message pc-persona pc-typing">
        <div className="pc-bubble">
          <span className="pc-thinking pc-thinking--done">
            <span className="pc-thinking-glyph" aria-hidden="true">{doneGlyph}</span>
            <span className="pc-thinking-label">{done.word}</span>
            <span className="pc-thinking-for">{` for ${done.secs}s`}</span>
          </span>
        </div>
      </div>
    )
  }

  return (
    <div className="pc-message pc-persona pc-typing">
      <div className="pc-bubble">
        <span
          className="pc-thinking"
          style={colorful && color ? { color } : undefined}
          aria-live="polite"
        >
          <span className="pc-thinking-glyph" aria-hidden="true">{frames[frame]}</span>
          <span className="pc-thinking-label">{word}</span>
          <span className="pc-thinking-ellipsis" aria-hidden="true">…</span>
        </span>
      </div>
    </div>
  )
}
