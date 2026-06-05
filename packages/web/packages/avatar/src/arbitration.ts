"use client";

import { useEffect, useRef, useState } from "react";
import type { Ladder } from "./types";

/** Maps the inactivity ladder rungs to this avatar's expressions. */
export interface MoodMap<E extends string> {
  /** The plain resting mood (active rung). */
  idle: E;
  /** The bored rung. Falls back to `idle` when an avatar has no bored mood. */
  bored?: E;
  /** The asleep rung. Falls back to `idle` when an avatar has no sleep. */
  asleep?: E;
}

/** A natural transition between two resting moods that plays a one-shot mood. */
export interface WakingConfig<E extends string> {
  /** Resting mood the avatar is leaving (e.g. asleep). */
  from: E;
  /** Resting mood it's arriving at (e.g. idle). */
  to: E;
  /** The one-shot mood to play across the transition (e.g. a waking yawn). */
  play: E;
  /** How long the one-shot holds (ms). */
  ms: number;
}

export interface ArbitrationConfig<E extends string> {
  /** A driver-set deliberate mood; overrides the ladder when present. */
  expression?: E;
  /** The current inactivity-ladder rung. */
  ladder: Ladder;
  moods: MoodMap<E>;
  /** What a click does, given the current resting mood. Return null for no reaction. */
  poke?: (resting: E) => { expression: E; ms: number } | null;
  /** A natural resting transition that plays a one-shot mood (e.g. waking yawn). */
  waking?: WakingConfig<E>;
}

export interface Arbitration<E extends string> {
  /** The mood actually shown: click reaction › waking one-shot › resting. */
  effective: E;
  /** The resting mood (driver expression, else the ladder mood) — no transient. */
  resting: E;
  /** Click handler: triggers the configured poke reaction. */
  poke: () => void;
}

/**
 * Arbitrates which mood is shown. A transient click reaction outranks a natural
 * waking one-shot, which outranks the resting mood. The mood VOCABULARY is the
 * avatar's — this hook is configured with the mapping (which ladder rung is which
 * mood, what a poke does, what plays on waking), so no avatar's mood names are
 * baked into the engine.
 */
export function useArbitration<E extends string>(config: ArbitrationConfig<E>): Arbitration<E> {
  const { expression, ladder, moods, waking } = config;

  // The resting mood: a driver-set expression, else the idle ladder's mood.
  const resting: E =
    expression ??
    (ladder === "asleep"
      ? (moods.asleep ?? moods.idle)
      : ladder === "bored"
        ? (moods.bored ?? moods.idle)
        : moods.idle);

  // Click reaction: a transient mood that briefly outranks everything.
  const [reaction, setReaction] = useState<E | null>(null);
  const reactionTimer = useRef<ReturnType<typeof setTimeout> | undefined>(undefined);
  const poke = (): void => {
    const r = config.poke?.(resting);
    if (!r) return;
    setReaction(r.expression);
    if (reactionTimer.current) clearTimeout(reactionTimer.current);
    reactionTimer.current = setTimeout(() => setReaction(null), r.ms);
  };
  useEffect(() => () => {
    if (reactionTimer.current) clearTimeout(reactionTimer.current);
  }, []);

  // Waking one-shot: when the avatar rouses on its own (the configured resting
  // transition) and wasn't jolted by a click, play the waking mood for a beat.
  const [wakingMood, setWakingMood] = useState<E | null>(null);
  const wakeTimer = useRef<ReturnType<typeof setTimeout> | undefined>(undefined);
  const prevResting = useRef(resting);
  useEffect(() => {
    if (
      waking &&
      prevResting.current === waking.from &&
      resting === waking.to &&
      reaction == null // not jolted awake by a click
    ) {
      setWakingMood(waking.play);
      if (wakeTimer.current) clearTimeout(wakeTimer.current);
      wakeTimer.current = setTimeout(() => setWakingMood(null), waking.ms);
    }
    prevResting.current = resting;
  }, [resting, reaction, waking]);
  useEffect(() => () => clearTimeout(wakeTimer.current), []);

  const effective: E = reaction ?? wakingMood ?? resting;
  return { effective, resting, poke };
}
