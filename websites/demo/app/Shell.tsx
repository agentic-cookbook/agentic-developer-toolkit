'use client'

import { useCallback, useSyncExternalStore, type ReactNode } from 'react'
import { useRouter, useSelectedLayoutSegment } from 'next/navigation'
import {
  ColorModeProvider,
  ThemeStyle,
  themeIds,
  type ThemeKey,
} from '@agentic-persona-toolkit/themes'
import { ThemePicker } from './ThemePicker'
import { examples } from './manifest'

const STORAGE_THEME = 'apt-demo:theme'

function safeRead(key: string): string | null {
  if (typeof window === 'undefined') return null
  try {
    return window.localStorage.getItem(key)
  } catch {
    return null
  }
}

function safeWrite(key: string, value: string): void {
  if (typeof window === 'undefined') return
  try {
    window.localStorage.setItem(key, value)
  } catch {
    // best-effort
  }
}

const RAIL_WIDTH = 200
const SHELL_THEME: ThemeKey = 'myprojects'
const EXAMPLE_SCOPE = '.apt-example-content'
const DEFAULT_THEME: ThemeKey = 'agenticcookbookweb'

function readStoredTheme(): ThemeKey {
  const stored = safeRead(STORAGE_THEME)
  if (stored && (themeIds as readonly string[]).includes(stored)) {
    return stored as ThemeKey
  }
  return DEFAULT_THEME
}

function subscribeTheme(callback: () => void): () => void {
  if (typeof window === 'undefined') return () => {}
  window.addEventListener('apt-demo:theme', callback)
  window.addEventListener('storage', callback)
  return () => {
    window.removeEventListener('apt-demo:theme', callback)
    window.removeEventListener('storage', callback)
  }
}

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

  const theme = useSyncExternalStore(
    subscribeTheme,
    readStoredTheme,
    () => DEFAULT_THEME,
  )

  const setTheme = useCallback((next: ThemeKey) => {
    safeWrite(STORAGE_THEME, next)
    if (typeof window !== 'undefined') {
      window.dispatchEvent(new CustomEvent('apt-demo:theme', { detail: next }))
    }
  }, [])

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
                    onClick={() => router.push(`/${e.id}/`)}
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

          <section
            style={{
              flex: '0 0 auto',
              display: 'flex',
              flexDirection: 'column',
              padding: '0.75rem',
              borderTop: '1px solid var(--color-border, rgba(0,0,0,0.1))',
              background: 'var(--color-surface-raised, #fff)',
            }}
          >
            <div
              style={{
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'space-between',
                padding: '0 0.5rem',
                margin: '0 0 0.5rem',
              }}
            >
              <h2 style={{ ...sectionHeaderStyle, padding: 0, margin: 0 }}>Themes</h2>
            </div>
            <ThemePicker value={theme} onChange={setTheme} />
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
