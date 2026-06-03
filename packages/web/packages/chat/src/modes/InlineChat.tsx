import type { RefObject } from 'react'
import type { ChatBackend } from '../backends/types'
import type { ChatParticipant } from '../types'
import { useChatSession, type ChatSession } from '../hooks/useChatSession'
import { useContentHuggingSize } from '../hooks/useContentHuggingSize'
import { Transcript } from '../components/Transcript'
import { ChatInput } from '../components/ChatInput'
import { InlinePopover } from '../components/InlinePopover'
import { TypingIndicator } from '../components/TypingIndicator'

/**
 * How the inline chat box determines its outer height.
 *
 * - `fixed`: respect whatever height the surrounding CSS gives the wrapper
 *   (today's behavior — `.pc-inline` is 50vh capped at 600px).
 * - `content-hugging`: the box height equals its content. Because the wrapper
 *   is bottom-anchored, growth extends the top edge upward and the input bar
 *   stays put. `maxHeight` caps growth; past the cap the transcript scrolls.
 */
export type InlineChatSizing =
  | { mode: 'fixed' }
  | {
      mode: 'content-hugging'
      maxHeight:
        | { kind: 'css'; value: string }
        | { kind: 'viewport-offset'; topOffsetPx: number }
        | {
            kind: 'element-offset'
            ref: RefObject<HTMLElement | null>
            gapPx?: number
          }
    }

export interface InlineChatViewProps {
  session: ChatSession
  className?: string
  sizing?: InlineChatSizing
  placeholder?: string
  /** "Thinking" words for the in-flight indicator (falls back to dots). */
  thinkingLabels?: string[]
  /** Frames for the in-flight rotating glyph. */
  thinkingFrames?: string[]
  /** Settled glyph for the grey done line. */
  thinkingDoneGlyph?: string
  /** Flash random non-green colors while thinking. */
  thinkingColorful?: boolean
  /**
   * Keep the status indicator animating while a reply is streaming in (the words
   * "coming out"), not only while awaiting the first token.
   */
  statusWhileStreaming?: boolean
  /** Idle status line shown before the first reply (e.g. "waiting to zeeble"). */
  idlePhrase?: string
  /** A transient utterance to flash in the status (overrides any phase). */
  statusUtterance?: string | null
  /** Show the input but disable typing/sending (e.g. during an intro sequence). */
  inputDisabled?: boolean
  /** Fade older messages — each line dimmer than the one below it. */
  fadeOlder?: boolean
}

export function InlineChatView({
  session,
  className,
  sizing,
  placeholder,
  thinkingLabels,
  thinkingFrames,
  thinkingDoneGlyph,
  thinkingColorful,
  statusWhileStreaming,
  idlePhrase,
  statusUtterance,
  inputDisabled,
  fadeOlder,
}: InlineChatViewProps) {
  const { messages, isTyping, sendMessage } = session
  // While he's "talking" (a reply streaming in), keep the status alive too.
  const streaming = !!statusWhileStreaming && messages.some((m) => m.isStreaming)
  const { ref, style } = useContentHuggingSize(sizing)
  return (
    <div ref={ref} className={`persona-chat ${className || ''}`} style={style}>
      <Transcript
        messages={messages}
        isTyping={isTyping}
        suppressTypingIndicator
        fadeOlder={fadeOlder}
        renderPopover={(msg) =>
          msg.popover ? <InlinePopover data={msg.popover} /> : null
        }
      />
      {/* Status sits right above the input (not in the scrolling transcript). */}
      <TypingIndicator
        isTyping={isTyping || streaming}
        idlePhrase={idlePhrase}
        utterance={statusUtterance}
        labels={thinkingLabels}
        frames={thinkingFrames}
        doneGlyph={thinkingDoneGlyph}
        colorful={thinkingColorful}
      />
      <ChatInput onSend={sendMessage} placeholder={placeholder} disabled={inputDisabled} />
    </div>
  )
}

export interface InlineChatProps {
  backend: ChatBackend
  persona: ChatParticipant
  user?: ChatParticipant
  welcomeMessage?: string
  className?: string
  sizing?: InlineChatSizing
  placeholder?: string
  thinkingLabels?: string[]
  thinkingFrames?: string[]
  thinkingDoneGlyph?: string
  thinkingColorful?: boolean
  statusWhileStreaming?: boolean
  idlePhrase?: string
  statusUtterance?: string | null
  inputDisabled?: boolean
  fadeOlder?: boolean
}

export function InlineChat(props: InlineChatProps) {
  const session = useChatSession(props)
  return (
    <InlineChatView
      session={session}
      className={props.className}
      sizing={props.sizing}
      placeholder={props.placeholder}
      thinkingLabels={props.thinkingLabels}
      thinkingFrames={props.thinkingFrames}
      thinkingDoneGlyph={props.thinkingDoneGlyph}
      thinkingColorful={props.thinkingColorful}
      statusWhileStreaming={props.statusWhileStreaming}
      idlePhrase={props.idlePhrase}
      statusUtterance={props.statusUtterance}
      inputDisabled={props.inputDisabled}
      fadeOlder={props.fadeOlder}
    />
  )
}
