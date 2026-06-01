import { useRef, useState, type RefObject } from 'react'
import { SendIcon } from './SendIcon'

interface ChatInputProps {
  onSend: (text: string) => void
  placeholder?: string
  autoFocus?: boolean
  inputRef?: RefObject<HTMLInputElement | null>
}

export function ChatInput({
  onSend,
  placeholder = 'Type a message...',
  autoFocus = false,
  inputRef: externalRef,
}: ChatInputProps) {
  const internalRef = useRef<HTMLInputElement>(null)
  const ref = externalRef || internalRef
  // Track whether the box has non-whitespace text so the send button (and
  // thus the Enter affordance) can be disabled while it's empty.
  const [hasText, setHasText] = useState(false)

  const handleSend = () => {
    const input = ref.current
    if (!input) return
    const text = input.value.trim()
    if (!text) return
    input.value = ''
    setHasText(false)
    onSend(text)
  }

  return (
    <div className="pc-input-area">
      <input
        ref={ref}
        className="pc-input"
        type="text"
        inputMode="text"
        placeholder={placeholder}
        autoComplete="off"
        autoFocus={autoFocus}
        enterKeyHint="send"
        onChange={(e) => setHasText(e.currentTarget.value.trim().length > 0)}
        onKeyDown={(e) => {
          if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault()
            handleSend()
          }
        }}
      />
      <button
        className="pc-send-btn"
        aria-label="Send"
        disabled={!hasText}
        onClick={handleSend}
      >
        <SendIcon />
      </button>
    </div>
  )
}
