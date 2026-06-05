"use client";

import { useEffect, useMemo, useRef } from "react";
import gsap from "gsap";
import { MorphSVGPlugin } from "gsap/MorphSVGPlugin";
import {
  DEFAULT_TUNING,
  type AvatarDriverProps,
  type AvatarRig,
  type Pose,
  type Tuning,
} from "./types";
import { useBlink, useIdleLadder, useSpeech } from "./reflexes";
import { useArbitration, type MoodMap, type WakingConfig } from "./arbitration";
import { useGaze } from "./gaze";
import { useIdleFidget } from "./idleLife";
import { useSpeechBubble } from "./speechBubble";
import { applyPose } from "./pose";

if (typeof window !== "undefined") {
  gsap.registerPlugin(MorphSVGPlugin);
}

const clamp = (n: number, lo: number, hi: number): number =>
  Math.max(lo, Math.min(hi, n));

/** A choreographed mood: skips the per-pose tweens and plays a timeline instead. */
export type Choreography<E extends string> = (
  rig: AvatarRig,
  poses: Record<E, Pose>,
) => gsap.core.Timeline;

/** Incidental per-mood motion (an asleep stir, a bored sag) — returns a cleanup. */
export type ExpressionEffect = (rig: AvatarRig) => (() => void) | void;

export interface AvatarEngineConfig<E extends string> extends AvatarDriverProps<E> {
  /** The avatar's pose table — one {@link Pose} per expression. */
  poses: Record<E, Pose>;
  /** The avatar's SVG refs + geometry. */
  rig: AvatarRig;
  /** Which ladder rung is which mood (idle/bored/asleep). */
  moods: MoodMap<E>;
  /** What a click does, given the resting mood. Return null for no reaction. */
  poke?: (resting: E) => { expression: E; ms: number } | null;
  /** A natural resting transition that plays a one-shot mood (e.g. a waking yawn). */
  waking?: WakingConfig<E>;
  /** Expressions that are choreographed — the per-pose tweens are skipped and the
   *  avatar's timeline plays instead (e.g. olylo's yawn). */
  choreography?: Partial<Record<E, Choreography<E>>>;
  /** Incidental per-mood motion that runs while a mood is effective. */
  perExpressionEffects?: Partial<Record<E, ExpressionEffect>>;
  /** Expressions during which blinking is suppressed (eyes under deliberate control). */
  blinkSuppressed?: E[];
  /** Override any timings/limits; unset fields fall back to {@link DEFAULT_TUNING}. */
  tuning?: Partial<Tuning>;
}

export interface AvatarEngine<E extends string> {
  /** The mood actually shown: click reaction › waking one-shot › resting. */
  effective: E;
  /** The resting mood (driver expression, else the ladder mood) — no transient. */
  resting: E;
  /** The current utterance to render (null when silent/muted). */
  speech: { text: string; id: number } | null;
  /** Click handler the avatar wires to its root, to trigger the poke reaction. */
  poke: () => void;
}

/**
 * The avatar behavior + animation engine. Give it the avatar's poses + rig + a
 * little mood configuration; it runs every reflex (blink, idle ladder, gaze,
 * speech) and the expression-driven pose loop, and hands back what to render.
 *
 * The avatar owns its IDENTITY (the SVG it draws and the pose data); this hook
 * owns BEHAVIOR. No avatar's anatomy or mood names are baked in — the rig's
 * optional channels and the mood config carry all of that.
 */
export function useAvatarEngine<E extends string>(
  config: AvatarEngineConfig<E>,
): AvatarEngine<E> {
  const { poses, rig, moods } = config;
  const tuning = useMemo<Tuning>(() => ({ ...DEFAULT_TUNING, ...config.tuning }), [config.tuning]);

  // Shared between gaze + idle fidget: when the cursor last drove the gaze, so the
  // fidget holds its random sway while the eyes are intentionally aimed.
  const watchingRef = useRef(0);
  // Looping tweens AND any choreography timeline — killed/reset on pose change.
  const loopRef = useRef<gsap.core.Animation[]>([]);

  const ladder = useIdleLadder(config.expression != null, tuning);
  const { effective, resting, poke } = useArbitration<E>({
    expression: config.expression,
    ladder,
    moods,
    poke: config.poke,
    waking: config.waking,
  });

  // Awake + unoccupied → curious look-around + idle fidget. Asleep → eyes shut.
  const curious = effective === moods.idle;
  const eyesShut = moods.asleep != null && effective === moods.asleep;

  // Blinks pause while the eyes are under deliberate control (shut, or suppressed
  // moods like a laugh squeeze or the choreographed yawn).
  const blinkEnabled = !eyesShut && !(config.blinkSuppressed ?? []).includes(effective);
  const leftBlinking = useBlink(blinkEnabled, tuning);
  const rightBlinking = useBlink(blinkEnabled, tuning);

  // Speech: a random saying on each mood change (looping while asleep). Muted while
  // a command processes — keeps the face but says nothing.
  const rawSpeech = useSpeech(
    effective,
    (e) => poses[e]?.sayings,
    eyesShut,
    tuning.sleepMutterMs,
  );
  const speech = config.mute ? null : rawSpeech;

  // Echo each utterance out to a driver (so a chat status can mirror it).
  useEffect(() => {
    if (speech) config.onSpeak?.(speech.text);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [speech?.id]);

  // Gaze (cursor-follow / deliberate / wander), idle fidget, speech-bubble drift.
  const forcedX = config.gaze ? clamp(config.gaze.x, -1, 1) : null;
  const forcedY = config.gaze ? clamp(config.gaze.y, -1, 1) : null;
  useGaze(rig, { forcedX, forcedY, eyesShut, curious, tuning, watchingRef });
  useIdleFidget(rig, { curious, idlePose: poses[moods.idle], watchingRef, tuning });
  useSpeechBubble(rig.speech, speech);

  // Pose: tween every channel toward the target pose (or hand a choreographed mood
  // to its own timeline). Loops are killed/reset whenever the pose changes.
  useEffect(() => {
    loopRef.current.forEach((t) => t.kill());
    loopRef.current = [];
    const choreo = config.choreography?.[effective];
    if (choreo) {
      loopRef.current.push(choreo(rig, poses));
      return;
    }
    const pose = poses[effective];
    if (pose) loopRef.current = applyPose(rig, pose, eyesShut);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [effective]);
  // Kill any surviving loops on unmount (the next pose change kills them otherwise).
  useEffect(
    () => () => {
      loopRef.current.forEach((t) => t.kill());
      loopRef.current = [];
    },
    [],
  );

  // Blink: collapse the dedicated blink groups (independent of the pose eye-scale).
  useEffect(() => {
    const el = rig.eyes?.blinkLeftRef?.current;
    if (!el) return;
    gsap.to(el, { scaleY: leftBlinking ? 0.06 : 1, transformOrigin: "50% 50%", duration: 0.09, ease: "power1.inOut" });
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [leftBlinking]);
  useEffect(() => {
    const el = rig.eyes?.blinkRightRef?.current;
    if (!el) return;
    gsap.to(el, { scaleY: rightBlinking ? 0.06 : 1, transformOrigin: "50% 50%", duration: 0.09, ease: "power1.inOut" });
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [rightBlinking]);

  // Incidental per-mood motion the avatar registered (asleep stir, bored sag, …).
  useEffect(() => {
    const fx = config.perExpressionEffects?.[effective];
    if (!fx) return;
    const cleanup = fx(rig);
    return typeof cleanup === "function" ? cleanup : undefined;
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [effective]);

  return { effective, resting, speech, poke };
}
