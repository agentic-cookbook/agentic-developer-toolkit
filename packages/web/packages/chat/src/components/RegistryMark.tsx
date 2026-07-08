import { memo } from 'react'
import type { CSSProperties, ReactElement, ReactNode } from 'react'

/**
 * The Agentic Persona Registry mark — the registry credential a persona chat
 * wears on its frame corner. Optional: render it as a sibling of the chat
 * view inside the host's `position: relative` wrapper (it cannot live inside
 * `.persona-chat`, whose overflow:hidden would clip the overhang) and import
 * css/components/registry-mark.css. If the page shell clips overflow (e.g.
 * ViewportShell), open it — see ViewportShell's `clip` prop.
 *
 * Inks: the @ ring and the eye shells ride currentColor — tint them by setting
 * `color` on the mark or an ancestor (the registry house color, or the
 * persona's own hue) — with the eyes set apart from the ring by their shape, a
 * finer stroke, and constant blue irises. The irises (AI-blue) and the sparkle
 * cluster (ADH gold) are the hub's constant accents: hex literals ON PURPOSE,
 * not theme tokens like --accent, so they don't dissolve into the host skin.
 */

const ADH_GOLD = '#c4a35a'
/** Iris blue — the generic AI-eye iris, not any one persona's. */
const IRIS_BLUE = '#33ccff'

/* Artwork geometry — the single source for BOTH the SVG viewBox and the CSS
 * corner anchoring (exported below as --pc-rm-anchor-*, so the two cannot
 * drift). The anchor point is the @ ring's CENTER (its bbox center), not the
 * box center — the sparkle cluster makes the box asymmetric, so box-centering
 * would shove the @ off the corner. */
const VIEW = { minX: 0, minY: -2, width: 32, height: 26 }
const AT_CENTER = { x: 12, y: 12 }
const pct = (fraction: number): string => `${+(fraction * 100).toFixed(3)}%`
/** Translate that moves AT_CENTER onto the box's pinned top-right corner. */
const ANCHOR_X = pct(1 - (AT_CENTER.x - VIEW.minX) / VIEW.width) // 62.5%
const ANCHOR_Y = pct(-((AT_CENTER.y - VIEW.minY) / VIEW.height)) // -53.846%
const MARK_STYLE = {
  '--pc-rm-anchor-x': ANCHOR_X,
  '--pc-rm-anchor-y': ANCHOR_Y,
  // Single-source the ADH gold: the SVG sparkles use the constant directly, the
  // popover-bloom CSS reads this custom prop — one source, no TS↔CSS drift.
  '--pc-rm-adh-gold': ADH_GOLD,
} as CSSProperties

/** Four-pointed AI sparkle at (cx, cy), radius r — N/E/S/W points, concave sides. */
function star(cx: number, cy: number, r: number): string {
  const k = r * 0.28
  const q = (n: number): string => n.toFixed(2)
  return (
    `M${q(cx)},${q(cy - r)} Q${q(cx + k)},${q(cy - k)} ${q(cx + r)},${q(cy)}` +
    ` Q${q(cx + k)},${q(cy + k)} ${q(cx)},${q(cy + r)}` +
    ` Q${q(cx - k)},${q(cy + k)} ${q(cx - r)},${q(cy)}` +
    ` Q${q(cx - k)},${q(cy - k)} ${q(cx)},${q(cy - r)} Z`
  )
}

/* The gold cluster, top-right outside the ring — computed once at module
 * load (the host chat re-renders per streamed token; these never change). */
const SPARKLE_MAIN = star(25.4, 4.4, 3.8)
const SPARKLE_TOP = star(22.4, 0, 1.6)
const SPARKLE_LOW = star(28.9, 9, 2.3)

export interface RegistryMarkProps {
  /** The persona's profile URL on the registry — the mark links here. */
  profileUrl: string
  /** Accessible name for the link (e.g. "Visit X's profile on the registry"). */
  label: string
  /**
   * Popover content shown above the mark on hover/focus. May contain links —
   * the popover stays open while the pointer is over it, and links inside it
   * are keyboard-reachable (the popover shows while focus is within the
   * mark). Omit for no popover.
   */
  tip?: ReactNode
  className?: string
}

function RegistryMarkImpl({
  profileUrl,
  label,
  tip,
  className,
}: RegistryMarkProps): ReactElement {
  return (
    <span
      className={className ? `pc-registry-mark ${className}` : 'pc-registry-mark'}
      style={MARK_STYLE}
    >
      <a
        className="pc-rm-link"
        href={profileUrl}
        target="_blank"
        rel="noopener noreferrer"
        aria-label={label}
      >
        <svg
          viewBox={`${VIEW.minX} ${VIEW.minY} ${VIEW.width} ${VIEW.height}`}
          fill="none"
          stroke="currentColor"
          strokeLinecap="round"
          strokeLinejoin="round"
          aria-hidden="true"
        >
          {/* The @ ring: the recognizable at-sign — a near-closed oval ring
              with the little "a" stem hooking in on the right and the tail at
              the lower right — drawn heavier (2.2). The two eyes below are its
              inner "a", so the whole thing reads as an @ with eyes. */}
          <g className="pc-rm-glyph">
            <path d="M15.5,8 v5 a2.25,2.25 0 0 0 4.5,0 v-1 a8,10.5 0 1 0 -4,9" strokeWidth="2.2" />
          </g>
          {/* The two eyes are the @'s inner "a" — a larger left eye and a
              smaller one beside it. They ride currentColor like the ring but
              read as eyes via their shape, a finer stroke, and the blue irises. */}
          <g className="pc-rm-eyes">
            <ellipse cx="9.4" cy="12" rx="1.8" ry="3" stroke="currentColor" strokeWidth="1.2" />
            <ellipse cx="13.1" cy="12.2" rx="1.55" ry="2.55" stroke="currentColor" strokeWidth="1.2" />
            <circle cx="9.4" cy="12" r="1.2" fill={IRIS_BLUE} stroke="none" />
            <circle cx="13.1" cy="12.2" r="1" fill={IRIS_BLUE} stroke="none" />
          </g>
          <g className="pc-rm-gold" fill={ADH_GOLD} stroke="none">
            <path d={SPARKLE_MAIN} />
            <path d={SPARKLE_TOP} opacity="0.85" />
            <path d={SPARKLE_LOW} opacity="0.92" />
          </g>
        </svg>
      </a>
      {tip ? <span className="pc-rm-tip">{tip}</span> : null}
    </span>
  )
}

/* Memoized: the host chat re-renders on every streamed token, but the mark's
 * props are static after mount, so it re-renders once and then stays put — as
 * long as callers pass a stable `tip` (a module constant, not inline JSX). */
export const RegistryMark = memo(RegistryMarkImpl)
