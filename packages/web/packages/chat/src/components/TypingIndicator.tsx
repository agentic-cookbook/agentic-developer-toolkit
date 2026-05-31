"use client"

import { useEffect, useState } from 'react'

// A classic terminal spinner — rotates smoothly in a monospace font.
const DEFAULT_FRAMES = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']

export interface TypingIndicatorProps {
  /**
   * "Thinking" words to cycle through while a reply is in flight
   * (e.g. ["zeeping", "zorping"]). When omitted, falls back to the classic
   * three-dot indicator — so existing consumers are unaffected.
   */
  labels?: string[]
  /** Frames for the rotating glyph. Defaults to a braille spinner. */
  frames?: string[]
  /** Spinner frame interval (ms). */
  frameMs?: number
  /** How often to switch to a new random word (ms). */
  labelMs?: number
}

export function TypingIndicator({ labels, frames, frameMs, labelMs }: TypingIndicatorProps = {}) {
  if (!labels || labels.length === 0) {
    return (
      <div className="pc-message pc-persona pc-typing">
        <div className="pc-bubble">
          <div className="pc-dots">
            <span />
            <span />
            <span />
          </div>
        </div>
      </div>
    )
  }
  return (
    <ThinkingIndicator
      labels={labels}
      frames={frames ?? DEFAULT_FRAMES}
      frameMs={frameMs ?? 90}
      labelMs={labelMs ?? 1800}
    />
  )
}

interface ThinkingProps {
  labels: string[]
  frames: string[]
  frameMs: number
  labelMs: number
}

function randomLabel(labels: string[]): string {
  return labels[Math.floor(Math.random() * labels.length)] ?? labels[0] ?? ''
}

/**
 * `[rotating glyph] [silly word]…` — a Claude-style thinking indicator. Only
 * mounts while a reply is in flight, so its timers live just for that window.
 */
function ThinkingIndicator({ labels, frames, frameMs, labelMs }: ThinkingProps) {
  const [frame, setFrame] = useState(0)
  const [label, setLabel] = useState(() => randomLabel(labels))

  useEffect(() => {
    const id = setInterval(() => setFrame((i) => (i + 1) % frames.length), frameMs)
    return () => clearInterval(id)
  }, [frames.length, frameMs])

  useEffect(() => {
    const id = setInterval(() => setLabel(randomLabel(labels)), labelMs)
    return () => clearInterval(id)
  }, [labels, labelMs])

  return (
    <div className="pc-message pc-persona pc-typing">
      <div className="pc-bubble">
        <span className="pc-thinking" aria-live="polite">
          <span className="pc-thinking-glyph" aria-hidden="true">
            {frames[frame]}
          </span>
          <span className="pc-thinking-label">{label}</span>
          <span className="pc-thinking-ellipsis" aria-hidden="true">…</span>
        </span>
      </div>
    </div>
  )
}
