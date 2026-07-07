import { useState } from 'react'
import type { ContentItem } from '../types'

interface RichContentProps {
  items: ContentItem[]
}

/**
 * Link protocols safe to render as an `href`. Content items come from the persona/LLM response, so a
 * prompt-injected link could carry a `javascript:`/`data:`/`vbscript:` URL that runs in this page's
 * origin — and can read the localStorage access token — when clicked. Allow only navigational
 * schemes; anything else yields no href, so the label renders as inert text (SEC-L4).
 */
const SAFE_LINK_PROTOCOLS = new Set(['http:', 'https:', 'mailto:', 'tel:'])
function safeHref(url: string): string | undefined {
  try {
    // Resolve against a dummy base so a bare/relative path (no scheme) counts as https.
    const protocol = new URL(url, 'https://x.invalid').protocol
    return SAFE_LINK_PROTOCOLS.has(protocol) ? url : undefined
  } catch {
    return undefined
  }
}

function GatedImage({ src, alt }: { src: string; alt?: string }) {
  const [ready, setReady] = useState(false)
  const reveal = () => setReady(true)
  return (
    <img
      className="pc-content-image"
      src={src}
      alt={alt || ''}
      style={ready ? undefined : { display: 'none' }}
      onLoad={reveal}
      onError={reveal}
    />
  )
}

export function RichContent({ items }: RichContentProps) {
  return (
    <div className="pc-content">
      {items.map((item, i) => {
        if (item.type === 'link') {
          return (
            <a
              key={i}
              className="pc-content-link"
              href={safeHref(item.url)}
              target="_blank"
              rel="noopener noreferrer"
            >
              {item.label || item.url}
            </a>
          )
        }
        if (item.type === 'image') {
          return <GatedImage key={i} src={item.src} alt={item.alt} />
        }
        return null
      })}
    </div>
  )
}
