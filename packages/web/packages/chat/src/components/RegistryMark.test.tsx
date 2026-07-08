import { describe, it, expect } from 'vitest'
import { render, screen } from '@testing-library/react'
import { RegistryMark } from './RegistryMark'

const PROFILE = 'https://registry.example/olylo'

describe('RegistryMark', () => {
  it('links to the profile with the accessible label', () => {
    render(<RegistryMark profileUrl={PROFILE} label="Visit olylo's profile" />)
    const link = screen.getByRole('link', { name: "Visit olylo's profile" })
    expect(link).toHaveAttribute('href', PROFILE)
    expect(link).toHaveAttribute('target', '_blank')
    expect(link).toHaveAttribute('rel', 'noopener noreferrer')
  })

  it('renders popover content inside the .pc-rm-tip element, links included', () => {
    const { container } = render(
      <RegistryMark
        profileUrl={PROFILE}
        label="profile"
        tip={
          <>
            Visit the <a href={PROFILE}>Registry</a>
          </>
        }
      />,
    )
    const tip = container.querySelector('.pc-rm-tip')
    expect(tip).not.toBeNull()
    const link = screen.getByRole('link', { name: 'Registry' })
    expect(tip).toContainElement(link) // the show/hide gate keys off .pc-rm-tip
    expect(link).toHaveAttribute('href', PROFILE)
  })

  it('renders no popover without a tip', () => {
    const { container } = render(<RegistryMark profileUrl={PROFILE} label="profile" />)
    expect(container.querySelector('.pc-rm-tip')).toBeNull()
  })

  it('merges a custom className and injects the anchor + ink custom properties', () => {
    const { container } = render(
      <RegistryMark profileUrl={PROFILE} label="profile" className="extra" />,
    )
    const root = container.querySelector('.pc-registry-mark') as HTMLElement
    expect(root).toHaveClass('extra')
    // Corner anchoring rides these inline vars; the CSS only carries fallbacks.
    expect(root.style.getPropertyValue('--pc-rm-anchor-x')).toBe('66.25%')
    expect(root.style.getPropertyValue('--pc-rm-adh-gold')).toBe('#c4a35a')
  })
})
