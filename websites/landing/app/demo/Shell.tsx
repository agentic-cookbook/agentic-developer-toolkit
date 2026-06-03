'use client'

import { type ReactNode } from 'react'
import { useRouter, useSelectedLayoutSegment } from 'next/navigation'
import {
  ColorModeProvider,
  ThemeStyle,
  type ThemeKey,
} from '@agentic-developer-toolkit/themes'
import { examples } from './manifest'
import { useDemoTheme } from './theme-store'

const RAIL_WIDTH = 200
const SHELL_THEME: ThemeKey = 'myprojects'
const EXAMPLE_SCOPE = '.apt-example-content'

const sectionHeaderStyle: React.CSSProperties = {
  fontSize: '0.7rem',
  fontWeight: 600,
  textTransform: 'uppercase',
  letterSpacing: '0.08em',
  margin: '0 0 0.5rem',
  padding: '0 0.5rem',
  color: 'var(--color-text-secondary, rgba(0,0,0,0.55))',
}

export function Shell({ children }: { children: ReactNode }) {
  const router = useRouter()
  const segment = useSelectedLayoutSegment()
  const activeId = segment ?? examples[0]?.id ?? ''

  // Theme selection now lives in each example's options (a popup); the Shell
  // only reads the active theme to apply it to the example content.
  const [theme] = useDemoTheme()

  const active = examples.find((e) => e.id === activeId) ?? examples[0]

  return (
    <ColorModeProvider>
      <div
        style={{
          minHeight: '100vh',
          display: 'flex',
          fontFamily: 'var(--font-sans, Inter, sans-serif)',
          color: 'var(--color-text-primary, #1a1a24)',
          background: 'var(--color-surface, #f4f4f8)',
        }}
      >
        <ThemeStyle theme={SHELL_THEME} />
        <ThemeStyle theme={theme} scope={EXAMPLE_SCOPE} />

        <nav
          style={{
            width: RAIL_WIDTH,
            flex: `0 0 ${RAIL_WIDTH}px`,
            height: '100vh',
            position: 'sticky',
            top: 0,
            borderRight: '1px solid var(--color-border, rgba(0,0,0,0.1))',
            background: 'var(--color-surface-raised, #fff)',
            display: 'flex',
            flexDirection: 'column',
          }}
        >
          <section
            style={{
              flex: '1 1 0',
              minHeight: 0,
              overflowY: 'auto',
              padding: '1.25rem 0.75rem',
              display: 'flex',
              flexDirection: 'column',
              gap: '0.75rem',
            }}
          >
            <div style={{ display: 'flex', flexDirection: 'column', gap: '0.25rem' }}>
              <h2 style={sectionHeaderStyle}>Examples</h2>
              {examples.map((e) => {
                const selected = e.id === active?.id
                return (
                  <button
                    key={e.id}
                    onClick={() => router.push(`/demo/${e.id}/`)}
                    style={{
                      textAlign: 'left',
                      padding: '0.45rem 0.6rem',
                      borderRadius: 4,
                      border: '1px solid transparent',
                      background: selected ? 'var(--color-accent-dim, rgba(0,0,0,0.06))' : 'transparent',
                      fontFamily: 'inherit',
                      fontSize: '0.85rem',
                      color: 'inherit',
                      cursor: 'pointer',
                    }}
                  >
                    {e.label}
                  </button>
                )
              })}
            </div>
          </section>
        </nav>

        <main
          style={{
            flex: 1,
            minWidth: 0,
            display: 'flex',
            flexDirection: 'column',
            overflow: 'hidden',
            background: 'var(--color-surface, #f4f4f8)',
          }}
        >
          {active ? (
            <header
              style={{
                flex: '0 0 auto',
                padding: '1rem 1.5rem',
                borderBottom: '1px solid var(--color-border, rgba(0,0,0,0.1))',
                background: 'var(--color-surface-raised, #fff)',
              }}
            >
              <h1
                style={{
                  margin: 0,
                  fontFamily: 'inherit',
                  fontSize: '1.25rem',
                  fontWeight: 600,
                  textAlign: 'left',
                  color: 'var(--color-text-primary, #1a1a24)',
                }}
              >
                {active.label}
              </h1>
            </header>
          ) : null}
          <div
            className="apt-example-content"
            style={{
              flex: '1 1 0',
              minHeight: 0,
              overflow: 'auto',
              textAlign: 'left',
              background: 'var(--color-surface, #f4f4f8)',
              color: 'var(--color-text-primary, #1a1a24)',
            }}
          >
            {children}
          </div>
        </main>
      </div>
    </ColorModeProvider>
  )
}
