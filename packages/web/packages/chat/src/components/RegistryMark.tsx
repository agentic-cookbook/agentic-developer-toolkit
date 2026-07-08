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
 * drift). The mark is "@o": the at-sign is a vertical-OVAL ring (a typographic
 * @, taller than wide), a round eye sits in it as the inner "a", a second round
 * eye "o" tucks against the ring's right edge, and the sparkles trail off the
 * top-right. The anchor point is the @ RING's center (12,12), NOT the box
 * center, so the @ itself perches on the host corner and the eye + sparkles
 * overhang up and to the right. The viewBox is the measured content bounds. */
const VIEW = { minX: 2, minY: -2, width: 38, height: 26 }
const AT_CENTER = { x: 12, y: 12 }
const pct = (fraction: number): string => `${+(fraction * 100).toFixed(3)}%`
/** Translate that moves AT_CENTER onto the box's pinned top-right corner. */
const ANCHOR_X = pct(1 - (AT_CENTER.x - VIEW.minX) / VIEW.width) // 73.684%
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

/* The gold cluster, off the top-right past the standalone eye — computed once
 * at module load (the host chat re-renders per streamed token; these never
 * change). */
const SPARKLE_MAIN = star(33, 4, 3.6)
const SPARKLE_TOP = star(30, -0.4, 1.5)
const SPARKLE_LOW = star(36.4, 8.6, 2.2)

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
          {/* The @ ring: Lucide's at-sign (outer ring + "a" stem + tail),
              squished horizontally about its center (12,12) into a vertical
              OVAL — a typographic @, taller than wide, its sides a hair finer
              than its top/bottom from the non-uniform scale. Drawn heavier (2.2). */}
          <g
            className="pc-rm-glyph"
            transform="translate(12,12) scale(0.78,1) translate(-12,-12)"
          >
            <path d="M16,8 v5 a3,3 0 0 0 6,0 v-1 a10,10 0 1 0 -4,8" strokeWidth="2.2" />
          </g>
          {/* "@o": two ROUND eyes. The first is the @'s inner "a", centered in
              the oval ring; the second is a standalone eye "o" tucked against
              (touching) the ring's right edge. Both shells ride currentColor
              like the ring; the blue irises mark them as eyes. */}
          <g className="pc-rm-eyes">
            <circle cx="12" cy="12" r="4" stroke="currentColor" strokeWidth="1.3" />
            <circle cx="12" cy="12" r="1.7" fill={IRIS_BLUE} stroke="none" />
            <circle cx="25.5" cy="12" r="4" stroke="currentColor" strokeWidth="1.3" />
            <circle cx="25.5" cy="12" r="1.7" fill={IRIS_BLUE} stroke="none" />
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
