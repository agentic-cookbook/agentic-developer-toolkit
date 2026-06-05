"use client";

import { useEffect, type RefObject } from "react";
import gsap from "gsap";
import type { AvatarRig, Tuning } from "./types";

const clamp = (n: number, lo: number, hi: number): number =>
  Math.max(lo, Math.min(hi, n));

export interface GazeOptions {
  /** Deliberate gaze, already clamped to [-1,1]; null hands the eyes to reflexes. */
  forcedX: number | null;
  forcedY: number | null;
  /** Eyes are deliberately shut (asleep): hold dead still — no tracking/tilt/lean. */
  eyesShut: boolean;
  /** Awake + unoccupied: wide curious look-around (vs. small in-mood glances). */
  curious: boolean;
  tuning: Tuning;
  /**
   * Shared with the idle fidget: stamped every time the cursor drives the gaze, so
   * the fidget knows to hold its random sway while the eyes are intentionally aimed.
   */
  watchingRef: RefObject<number>;
}

/**
 * Where the irises point, spring-damped via quickTo. Priority:
 *   1. a deliberate `gaze` (e.g. eyes down at an input while you type),
 *   2. the cursor while it's moving,
 *   3. the avatar's own curious look-around when awake and the cursor's gone still.
 *
 * Head-tilt and lean ride their own layers (`tiltLayer` / `leanLayer`) so they
 * compose with the pose. Every part is optional: with no iris the eyes don't
 * steer; with no tilt/lean layer those simply don't run.
 */
export function useGaze(rig: AvatarRig, opts: GazeOptions): void {
  const { forcedX, forcedY, eyesShut, curious, tuning, watchingRef } = opts;
  useEffect(() => {
    const { gazeMax, tiltMax, leanMax, wanderAfterMs, wanderMinMs, wanderMaxMs } = tuning;

    // Irises: spring toward a target. No iris channel ⇒ a no-op look().
    const irisL = rig.iris?.leftRef.current ?? null;
    const irisR = rig.iris?.rightRef.current ?? null;
    const lookOpts = { duration: 0.5, ease: "power3" };
    const qxL = irisL ? gsap.quickTo(irisL, "x", lookOpts) : null;
    const qyL = irisL ? gsap.quickTo(irisL, "y", lookOpts) : null;
    const qxR = irisR ? gsap.quickTo(irisR, "x", lookOpts) : null;
    const qyR = irisR ? gsap.quickTo(irisR, "y", lookOpts) : null;
    const look = (gx: number, gy: number): void => {
      qxL?.(gx);
      qyL?.(gy);
      qxR?.(gx);
      qyR?.(gy);
    };

    // Head-tilt: leans toward whatever it's deliberately watching, levels off
    // when nothing's moving. Its own layer so it composes with the pose.
    const tiltEl = rig.tiltLayer?.current ?? null;
    let tiltTo: ((v: number) => void) | null = null;
    if (tiltEl) {
      gsap.set(tiltEl, { svgOrigin: rig.pivot });
      tiltTo = gsap.quickTo(tiltEl, "rotation", { duration: 0.4, ease: "power3" });
    }
    const tilt = (deg: number): void => tiltTo?.(deg);

    // Lean: the whole glyph drifts a touch toward what it watches (own translate layer).
    const leanEl = rig.leanLayer?.current ?? null;
    const leanXTo = leanEl ? gsap.quickTo(leanEl, "x", { duration: 0.5, ease: "power3" }) : null;
    const leanYTo = leanEl ? gsap.quickTo(leanEl, "y", { duration: 0.5, ease: "power3" }) : null;
    const lean = (nx: number, ny: number): void => {
      leanXTo?.(nx * leanMax);
      leanYTo?.(ny * leanMax);
    };

    // Dead still while asleep: no cursor tracking, tilt, lean, or saccade.
    if (eyesShut) {
      look(0, 0);
      tilt(0);
      lean(0, 0);
      return;
    }

    // 1. Deliberate gaze (typing): lock eyes + head toward it, ignore the rest.
    // (Tilt sign is negated so it leans INTO what it's watching, not away.)
    if (forcedX !== null && forcedY !== null) {
      look(forcedX * gazeMax, forcedY * gazeMax);
      tilt(-forcedX * tiltMax);
      lean(forcedX, forcedY);
      return;
    }
    tilt(0); // level + centred until the cursor takes over
    lean(0, 0);

    // 2. Cursor-follow.
    let lastMove = 0; // when the cursor last drove the gaze; wander waits for a lull
    let raf = 0;
    const onMove = (e: PointerEvent): void => {
      if (raf) return;
      raf = requestAnimationFrame(() => {
        raf = 0;
        const el = rig.svg.current;
        if (!el) return;
        const r = el.getBoundingClientRect();
        const dx = e.clientX - (r.left + r.width / 2);
        const dy = e.clientY - (r.top + r.height / 2);
        const len = Math.hypot(dx, dy) || 1;
        look(
          clamp((dx / len) * gazeMax, -gazeMax, gazeMax),
          clamp((dy / len) * gazeMax, -gazeMax, gazeMax),
        );
        // turn the head to watch the cursor (negated so it leans into it) and
        // drift a touch toward it; mark that it's watching so the idle sway holds.
        tilt(-clamp(dx / len, -1, 1) * tiltMax);
        lean(clamp(dx / len, -1, 1), clamp(dy / len, -1, 1));
        lastMove = Date.now();
        watchingRef.current = lastMove;
      });
    };
    const onLeave = (): void => look(0, 0);
    window.addEventListener("pointermove", onMove);
    document.addEventListener("mouseleave", onLeave);

    // 3. Restless eyes: when the cursor's still, the irises drift on their own so
    // it never stares blankly — a wide, curious look-around while idle, smaller
    // glances while in a mood. Skips its turn whenever the cursor's moving.
    let wander: ReturnType<typeof setTimeout> | undefined;
    const scheduleWander = (): void => {
      wander = setTimeout(
        () => {
          if (Date.now() - lastMove > wanderAfterMs) {
            tilt(0); // cursor's gone still — level the head; idle sway takes over
            lean(0, 0); // …and drift back to centre
            if (Math.random() < (curious ? 0.25 : 0.35)) {
              look(0, 0);
            } else {
              const angle = Math.random() * Math.PI * 2;
              const reach = curious ? 0.45 + Math.random() * 0.45 : 0.12 + Math.random() * 0.2;
              const radius = gazeMax * reach;
              look(Math.cos(angle) * radius, Math.sin(angle) * radius);
            }
          }
          scheduleWander();
        },
        wanderMinMs + Math.random() * (wanderMaxMs - wanderMinMs),
      );
    };
    scheduleWander();

    return () => {
      if (raf) cancelAnimationFrame(raf);
      if (wander) clearTimeout(wander);
      window.removeEventListener("pointermove", onMove);
      document.removeEventListener("mouseleave", onLeave);
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [forcedX, forcedY, curious, eyesShut]);
}
