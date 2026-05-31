"use client"

import { useEffect, useRef, useState } from 'react'

// A classic terminal spinner — rotates smoothly in a monospace font.
const DEFAULT_FRAMES = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
// Settled glyph for the completed (grey) state, à la Claude's "✱ Churned for…".
const DONE_GLYPH = '✱'

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
  /** Spinner frame interval (ms). */
  frameMs?: number
  /** How often to switch to a new random word (ms). */
  labelMs?: number
}

export function TypingIndicator({ isTyping, labels, frames, frameMs, labelMs }: TypingIndicatorProps) {
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
      labels={labels}
      frames={frames ?? DEFAULT_FRAMES}
      frameMs={frameMs ?? 90}
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

interface ThinkingStatusProps {
  active: boolean
  labels: string[]
  frames: string[]
  frameMs: number
  labelMs: number
}

type Phase = 'idle' | 'thinking' | 'done'

/**
 * While `active`, shows `[rotating glyph] [silly word]…`. When it stops, freezes
 * into a grey `✱ [past-tense word] for Ns` that persists until the next think,
 * mirroring Claude's completed-thinking line.
 */
function ThinkingStatus({ active, labels, frames, frameMs, labelMs }: ThinkingStatusProps) {
  const [phase, setPhase] = useState<Phase>(active ? 'thinking' : 'idle')
  const [frame, setFrame] = useState(0)
  const [word, setWord] = useState(() => randomLabel(labels))
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
  }, [active, labels])

  // Spinner + word cycling — only while thinking.
  useEffect(() => {
    if (phase !== 'thinking') return
    const f = setInterval(() => setFrame((i) => (i + 1) % frames.length), frameMs)
    const l = setInterval(() => setWord(randomLabel(labels)), labelMs)
    return () => {
      clearInterval(f)
      clearInterval(l)
    }
  }, [phase, frames.length, frameMs, labels, labelMs])

  if (phase === 'idle') return null

  if (phase === 'done' && done) {
    return (
      <div className="pc-message pc-persona pc-typing">
        <div className="pc-bubble">
          <span className="pc-thinking pc-thinking--done">
            <span className="pc-thinking-glyph" aria-hidden="true">{DONE_GLYPH}</span>
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
        <span className="pc-thinking" aria-live="polite">
          <span className="pc-thinking-glyph" aria-hidden="true">{frames[frame]}</span>
          <span className="pc-thinking-label">{word}</span>
          <span className="pc-thinking-ellipsis" aria-hidden="true">…</span>
        </span>
      </div>
    </div>
  )
}
