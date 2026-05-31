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
}: TranscriptProps) {
  const ref = useRef<HTMLDivElement>(null)
  useScrollToBottom(ref, [messages.length, isTyping])

  return (
    <div ref={ref} className={`pc-transcript ${className || ''}`}>
      {messages.map((msg, i) => (
        <div key={msg.id}>
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
      <TypingIndicator
        isTyping={isTyping}
        labels={thinkingLabels}
        frames={thinkingFrames}
        doneGlyph={thinkingDoneGlyph}
        colorful={thinkingColorful}
      />
    </div>
  )
}
