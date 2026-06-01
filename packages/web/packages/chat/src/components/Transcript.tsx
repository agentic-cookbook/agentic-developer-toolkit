import { useRef, type ReactNode } from 'react'
import type { ChatMessage } from '../types'
import { MessageBubble } from './MessageBubble'
import { TypingIndicator } from './TypingIndicator'
import { useScrollToBottom } from '../hooks/useScrollToBottom'

interface TranscriptProps {
  messages: ChatMessage[]
  isTyping: boolean
  selectedIndex?: number
  onMessageClick?: (index: number) => void
  renderPopover?: (message: ChatMessage) => ReactNode
  showDetailArrows?: boolean
  onDetailArrowClick?: (index: number) => void
  className?: string
  /** "Thinking" words for the in-flight indicator (falls back to dots). */
  thinkingLabels?: string[]
  /** Frames for the in-flight rotating glyph. */
  thinkingFrames?: string[]
  /** Settled glyph for the grey done line. */
  thinkingDoneGlyph?: string
  /** Flash random non-green colors while thinking. */
  thinkingColorful?: boolean
  /** Don't render the in-transcript indicator (a host renders it elsewhere). */
  suppressTypingIndicator?: boolean
  /** Fade older messages: each line dimmer than the one below it, the newest at
   * full opacity. Off by default. */
  fadeOlder?: boolean
}

// Opacity for a message `distance` lines above the newest (0 = newest).
const FADE_STEP = 0.13
const FADE_MIN = 0.18
function fadeOpacity(distance: number): number {
  return Math.max(FADE_MIN, 1 - distance * FADE_STEP)
}

export function Transcript({
  messages,
  isTyping,
  selectedIndex = -1,
  onMessageClick,
  renderPopover,
  showDetailArrows = false,
  onDetailArrowClick,
  className,
  thinkingLabels,
  thinkingFrames,
  thinkingDoneGlyph,
  thinkingColorful,
  suppressTypingIndicator,
  fadeOlder = false,
}: TranscriptProps) {
  const ref = useRef<HTMLDivElement>(null)
  useScrollToBottom(ref, [messages.length, isTyping])

  const lastIndex = messages.length - 1

  return (
    <div ref={ref} className={`pc-transcript ${className || ''}`}>
      {messages.map((msg, i) => (
        <div
          key={msg.id}
          style={fadeOlder ? { opacity: fadeOpacity(lastIndex - i) } : undefined}
        >
          <MessageBubble
            message={msg}
            index={i}
            isSelected={i === selectedIndex}
            onClick={onMessageClick ? () => onMessageClick(i) : undefined}
            showDetailArrow={showDetailArrows && !!msg.popover}
            onDetailArrowClick={
              onDetailArrowClick ? () => onDetailArrowClick(i) : undefined
            }
          />
          {renderPopover && msg.popover && renderPopover(msg)}
        </div>
      ))}
      {!suppressTypingIndicator && (
        <TypingIndicator
          isTyping={isTyping}
          labels={thinkingLabels}
          frames={thinkingFrames}
          doneGlyph={thinkingDoneGlyph}
          colorful={thinkingColorful}
        />
      )}
    </div>
  )
}
