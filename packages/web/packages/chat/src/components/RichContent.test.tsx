import { describe, it, expect } from 'vitest'
import { render, fireEvent, screen } from '@testing-library/react'
import { RichContent } from './RichContent'

describe('RichContent image gating', () => {
  it('hides images until they have loaded', () => {
    render(
      <RichContent
        items={[
          { type: 'image', src: '/a.png', alt: 'a' },
        ]}
      />,
    )
    const img = screen.getByAltText('a') as HTMLImageElement
    expect(img.style.display).toBe('none')
    fireEvent.load(img)
    expect(img.style.display).toBe('')
  })

  it('reveals image after error too (fail-open)', () => {
    render(
      <RichContent
        items={[
          { type: 'image', src: '/missing.png', alt: 'x' },
        ]}
      />,
    )
    const img = screen.getByAltText('x') as HTMLImageElement
    expect(img.style.display).toBe('none')
    fireEvent.error(img)
    expect(img.style.display).toBe('')
  })
})

// SEC-L4: link URLs come from the persona/LLM response; a `javascript:` (or data:/vbscript:) href
// would execute in this page's origin and could read the localStorage access token when clicked.
describe('RichContent link protocol allowlist (SEC-L4)', () => {
  it('drops the href for a javascript: URL (no execution sink)', () => {
    render(
      <RichContent items={[{ type: 'link', url: 'javascript:alert(document.cookie)', label: 'click' }]} />,
    )
    expect((screen.getByText('click') as HTMLAnchorElement).getAttribute('href')).toBeNull()
  })

  it('keeps http/https/mailto links', () => {
    render(
      <RichContent
        items={[
          { type: 'link', url: 'https://example.com/x', label: 'web' },
          { type: 'link', url: 'mailto:a@b.com', label: 'mail' },
        ]}
      />,
    )
    expect((screen.getByText('web') as HTMLAnchorElement).getAttribute('href')).toBe('https://example.com/x')
    expect((screen.getByText('mail') as HTMLAnchorElement).getAttribute('href')).toBe('mailto:a@b.com')
  })
})
