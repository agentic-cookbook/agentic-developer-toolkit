import { memo } from 'react'
import type { CSSProperties, NamedExoticComponent, ReactElement, ReactNode } from 'react'

/**
 * The Agentic Persona Registry mark — the registry credential a persona chat
 * wears on its frame corner. Optional: render it as a sibling of the chat
 * view inside the host's `position: relative` wrapper (it cannot live inside
 * `.persona-chat`, whose overflow:hidden would clip the overhang) and import
 * css/components/registry-mark.css. If the page shell clips overflow (e.g.
 * ViewportShell), open it — see ViewportShell's `clip` prop.
 *
 * The mark is a single "@" — the exact JetBrains Mono glyph (embedded as a
 * path, so it needs no font loaded) with the four-pointed AI star set into its
 * counter, where the "o" of the "@" sits. Two inks: the "@" rides currentColor
 * — tint it by setting `color` on the mark or an ancestor (the registry house
 * color, or the persona's own hue) — and the star is ADH gold, a hex literal ON
 * PURPOSE (not a theme token like --accent) so the registry accent never
 * dissolves into the host skin.
 */

const ADH_GOLD = '#c4a35a'

/* Artwork geometry — the single source for BOTH the SVG viewBox and the CSS
 * corner anchoring (exported below as --pc-rm-anchor-*, so the two cannot
 * drift). The artwork is just the "@" glyph; the star sits inside its counter.
 * The anchor point is the glyph's own center (12,12), so the "@" perches
 * astride the host's top-right corner — half above the frame, half over the
 * chat. The viewBox is a center-symmetric box (a hair of padding around the
 * glyph's ~6.4..17.6 × 2..22 bounds, whose own center is (12,12)), which lands
 * the anchors on a clean 50% (AT_CENTER sits exactly at the box's midpoint). */
const VIEW = { minX: 5, minY: 1, width: 14, height: 22 }
const AT_CENTER = { x: 12, y: 12 }
const pct = (fraction: number): string => `${+(fraction * 100).toFixed(3)}%`
/** Translate that moves AT_CENTER onto the box's pinned top-right corner. */
const ANCHOR_X = pct(1 - (AT_CENTER.x - VIEW.minX) / VIEW.width) // 50%
const ANCHOR_Y = pct(-((AT_CENTER.y - VIEW.minY) / VIEW.height)) // -50%
const MARK_STYLE = {
  '--pc-rm-anchor-x': ANCHOR_X,
  '--pc-rm-anchor-y': ANCHOR_Y,
  // Single-source the ADH gold: the SVG star uses the constant directly, the
  // popover-bloom CSS reads this custom prop — one source, no TS↔CSS drift.
  '--pc-rm-adh-gold': ADH_GOLD,
} as CSSProperties

/* The exact JetBrains Mono (weight 400) "@" outline, lifted from the font and
 * normalized into a 24-unit box (coords at 2dp — sub-pixel at any mark size).
 * Embedded rather than rendered as live <text> so the mark carries its own
 * shape and never depends on the host having the font loaded. Filled, tinted by
 * currentColor. */
const AT_GLYPH =
  'M12.49 22Q10.64 22 9.27 21.23Q7.9 20.46 7.15 19.03Q6.4 17.61 6.4 15.7V8.3Q6.4 6.35 7.11 4.93Q7.82 3.52 9.13 2.76Q10.45 2 12.27 2Q13.92 2 15.12 2.64Q16.32 3.28 16.96 4.48Q17.6 5.67 17.6 7.33V16.67H16.05V15.48H15.45L15.86 15.04Q15.86 15.87 15.23 16.38Q14.6 16.89 13.55 16.89Q12.14 16.89 11.39 16.03Q10.64 15.17 10.64 13.52V10.91Q10.64 9.26 11.39 8.4Q12.14 7.54 13.55 7.54Q14.6 7.54 15.23 8.05Q15.86 8.57 15.86 9.41L15.55 8.96H16.08L15.86 7.43V7.33Q15.86 6.09 15.45 5.24Q15.03 4.39 14.24 3.96Q13.45 3.52 12.27 3.52Q10.32 3.52 9.23 4.78Q8.14 6.04 8.14 8.3V15.7Q8.14 17.87 9.3 19.12Q10.47 20.37 12.49 20.37H14.01V22ZM14.12 15.52Q15.01 15.52 15.43 14.98Q15.86 14.43 15.86 13.3V10.89Q15.86 9.87 15.43 9.39Q15.01 8.91 14.12 8.91Q13.25 8.91 12.82 9.4Q12.38 9.89 12.38 10.91V13.52Q12.38 14.54 12.82 15.03Q13.25 15.52 14.12 15.52Z'

/** Four-pointed AI star at (cx, cy) with independent x/y radii — N/E/S/W points,
 * concave sides. Separate rx/ry let the star fill a non-round opening (here the
 * "@"'s tall-narrow counter) instead of spilling past it into the ring. */
function star(cx: number, cy: number, rx: number, ry: number): string {
  const kx = rx * 0.28
  const ky = ry * 0.28
  const q = (n: number): string => n.toFixed(2)
  return (
    `M${q(cx)},${q(cy - ry)} Q${q(cx + kx)},${q(cy - ky)} ${q(cx + rx)},${q(cy)}` +
    ` Q${q(cx + kx)},${q(cy + ky)} ${q(cx)},${q(cy + ry)}` +
    ` Q${q(cx - kx)},${q(cy + ky)} ${q(cx - rx)},${q(cy)}` +
    ` Q${q(cx - kx)},${q(cy - ky)} ${q(cx)},${q(cy - ry)} Z`
  )
}

/* The AI star, centered on the "@" counter (the "o", center ~(14.1, 12.2)) but
 * scaled 2× past the counter-fit radii (2.0×3.3 → 4.0×6.6) so it reads as a bold
 * star overrunning the "@" ring while its points still stay inside the glyph
 * viewBox (east point x≈18.1 < 19, so nothing clips). Computed once at module
 * load (the host chat re-renders per streamed token; this never changes). */
const STAR = star(14.1, 12.2, 4.0, 6.6)

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
      className={['pc-registry-mark', className].filter(Boolean).join(' ')}
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
          aria-hidden="true"
        >
          {/* The "@": the exact JetBrains Mono glyph, filled with the tint. */}
          <path className="pc-rm-glyph" d={AT_GLYPH} fill="currentColor" />
          {/* The AI star set into the "@" counter — the registry's gold accent. */}
          <path className="pc-rm-gold" d={STAR} fill={ADH_GOLD} />
        </svg>
      </a>
      {tip ? <span className="pc-rm-tip">{tip}</span> : null}
    </span>
  )
}

/* Memoized: the host chat re-renders on every streamed token, but the mark's
 * props are static after mount, so it re-renders once and then stays put — as
 * long as callers pass a stable `tip` (a module constant, not inline JSX). */
export const RegistryMark: NamedExoticComponent<RegistryMarkProps> = memo(RegistryMarkImpl)
