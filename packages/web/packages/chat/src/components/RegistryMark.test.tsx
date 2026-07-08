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

  it('renders popover content, links included', () => {
    render(
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
    expect(screen.getByRole('link', { name: 'Registry' })).toHaveAttribute('href', PROFILE)
  })

  it('renders no popover without a tip', () => {
    const { container } = render(<RegistryMark profileUrl={PROFILE} label="profile" />)
    expect(container.querySelector('.pc-rm-tip')).toBeNull()
  })
})
