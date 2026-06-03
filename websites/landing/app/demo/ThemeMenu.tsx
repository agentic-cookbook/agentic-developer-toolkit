'use client'

import { useEffect, useRef, useState, type CSSProperties } from 'react'
import { themeIds, themes } from '@agentic-developer-toolkit/themes'
import { useDemoTheme } from './theme-store'

/**
 * A compact dropdown for picking the demo theme. Self-contained — it reads and
 * writes the shared theme store, so it works wherever it's dropped (the chat
 * options, the theme showcase, …). Closes on outside click or Escape.
 */
export function ThemeMenu({ className }: { className?: string }) {
  const [theme, setTheme] = useDemoTheme()
  const [open, setOpen] = useState(false)
  const ref = useRef<HTMLDivElement>(null)

  useEffect(() => {
    if (!open) return
    const onPointerDown = (e: Event) => {
      if (ref.current && !ref.current.contains(e.target as Node)) setOpen(false)
    }
    const onKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') setOpen(false)
    }
    document.addEventListener('pointerdown', onPointerDown)
    document.addEventListener('keydown', onKeyDown)
    return () => {
      document.removeEventListener('pointerdown', onPointerDown)
      document.removeEventListener('keydown', onKeyDown)
    }
  }, [open])

  return (
    <div ref={ref} className={className} style={{ position: 'relative' }}>
      <button
        type="button"
        onClick={() => setOpen((v) => !v)}
        aria-haspopup="listbox"
        aria-expanded={open}
        style={triggerStyle}
      >
        <span style={ellipsisStyle}>{themes[theme].label}</span>
        <span
          aria-hidden
          style={{ opacity: 0.6, transition: 'transform 0.15s', transform: open ? 'rotate(180deg)' : 'none' }}
        >
          ▾
        </span>
      </button>

      {open && (
        <ul role="listbox" aria-label="Theme" style={menuStyle}>
          {themeIds.map((id) => {
            const selected = id === theme
            return (
              <li key={id} role="option" aria-selected={selected}>
                <button
                  type="button"
                  onClick={() => {
                    setTheme(id)
                    setOpen(false)
                  }}
                  style={{
                    ...itemStyle,
                    fontWeight: selected ? 600 : 400,
                    background: selected ? 'var(--color-accent-dim, rgba(0,0,0,0.08))' : 'transparent',
                  }}
                >
                  {themes[id].label}
                </button>
              </li>
            )
          })}
        </ul>
      )}
    </div>
  )
}

const ellipsisStyle: CSSProperties = {
  overflow: 'hidden',
  textOverflow: 'ellipsis',
  whiteSpace: 'nowrap',
}

const triggerStyle: CSSProperties = {
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'space-between',
  gap: '0.5rem',
  width: '100%',
  padding: '0.45rem 0.6rem',
  borderRadius: 4,
  border: '1px solid var(--color-border, rgba(0,0,0,0.2))',
  background: 'var(--color-surface-raised, #fff)',
  color: 'inherit',
  fontFamily: 'inherit',
  fontSize: '0.85rem',
  cursor: 'pointer',
  textAlign: 'left',
}

const menuStyle: CSSProperties = {
  position: 'absolute',
  top: 'calc(100% + 4px)',
  left: 0,
  right: 0,
  zIndex: 50,
  margin: 0,
  padding: 4,
  listStyle: 'none',
  border: '1px solid var(--color-border, rgba(0,0,0,0.2))',
  borderRadius: 6,
  background: 'var(--color-surface-raised, #fff)',
  boxShadow: '0 8px 24px color-mix(in srgb, var(--color-text-primary, #000) 18%, transparent)',
  maxHeight: '50vh',
  overflowY: 'auto',
}

const itemStyle: CSSProperties = {
  display: 'block',
  width: '100%',
  padding: '0.4rem 0.55rem',
  borderRadius: 4,
  border: 'none',
  color: 'inherit',
  fontFamily: 'inherit',
  fontSize: '0.85rem',
  cursor: 'pointer',
  textAlign: 'left',
}
