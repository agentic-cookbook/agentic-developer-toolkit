"use client";

import { useEffect, type RefObject } from "react";
import gsap from "gsap";
import type { AvatarRig, Pose, Tuning } from "./types";

export interface IdleFidgetOptions {
  /** Awake + unoccupied: keep subtly alive. Off the moment there's a mood to play. */
  curious: boolean;
  /** The resting pose — supplies the brow centre the drift wanders around. */
  idlePose: Pose;
  /** Shared with gaze: while actively watching the cursor, hold the random sway at 0. */
  watchingRef: RefObject<number>;
  tuning: Tuning;
}

/**
 * Baseline aliveness while idle: a small random head sway + a slow breath (on the
 * idle layer) and a little brow drift around their resting pose — so the avatar
 * never freezes into a static logo. Generic to any avatar with an `idleLayer`
 * (and, for the brow drift, a `brows` channel). Mood-specific micro-life (an
 * asleep stir, a bored sag) is left to the avatar's per-expression effects.
 */
export function useIdleFidget(rig: AvatarRig, opts: IdleFidgetOptions): void {
  const { curious, idlePose, watchingRef, tuning } = opts;
  useEffect(() => {
    const layer = rig.idleLayer?.current;
    if (!curious || !layer) return;
    const brows = rig.brows;
    const rnd = (m: number): number => (Math.random() * 2 - 1) * m;

    // Breathing (zoom) is its OWN slow, continuous loop — much less frequent than
    // the head sway, so it swells/shrinks gently. `scale` never conflicts with the
    // sway's `rotation` on the same element.
    const breath = gsap.to(layer, {
      scale: 1.035,
      svgOrigin: rig.pivot,
      duration: 2.6,
      repeat: -1,
      yoyo: true,
      ease: "sine.inOut",
    });

    let timer: ReturnType<typeof setTimeout> | undefined;
    const fidget = (): void => {
      // Quick, varied, near-continuous — live things are never quite still. The
      // next move starts before this one settles, so it's always drifting toward
      // a fresh target rather than posing and pausing.
      const dur = 0.5 + Math.random() * 0.4;
      // While actively watching the cursor the head is purposefully aimed
      // (tilt layer), so hold the random sway at 0 — only the breath keeps going.
      const watching = Date.now() - watchingRef.current < tuning.wanderAfterMs;
      gsap.to(layer, {
        rotation: watching ? 0 : rnd(3.5),
        svgOrigin: rig.pivot,
        duration: dur,
        ease: "sine.inOut",
        overwrite: "auto",
      });
      const browL = brows?.leftRef.current;
      if (browL && idlePose.browLeft) {
        gsap.to(browL, {
          rotation: idlePose.browLeft.rotation + rnd(3),
          y: idlePose.browLeft.y + rnd(2),
          svgOrigin: brows!.leftOrigin,
          duration: dur,
          ease: "sine.inOut",
          overwrite: "auto",
        });
      }
      const browR = brows?.rightRef.current;
      if (browR && idlePose.browRight) {
        gsap.to(browR, {
          rotation: idlePose.browRight.rotation + rnd(3),
          y: idlePose.browRight.y + rnd(2),
          svgOrigin: brows!.rightOrigin,
          duration: dur,
          ease: "sine.inOut",
          overwrite: "auto",
        });
      }
      timer = setTimeout(fidget, dur * 1000 * 0.85 + Math.random() * 150);
    };
    fidget();

    return () => {
      if (timer) clearTimeout(timer);
      breath.kill();
      // settle the fidget layer back to neutral; the pose resets the brows.
      gsap.to(layer, {
        rotation: 0,
        scale: 1,
        svgOrigin: rig.pivot,
        duration: 0.5,
        ease: "power2.out",
        overwrite: "auto",
      });
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [curious]);
}
