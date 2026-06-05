"use client";

import { useEffect, useRef, useState } from "react";
import type { Ladder, Tuning } from "./types";

/**
 * The avatar's involuntary reflexes — no driver needed. These are pure: they
 * know nothing of any particular avatar's anatomy, only timings (from
 * {@link Tuning}). Blink and the idle ladder lifted unchanged from olylo;
 * `useSpeech` is the same mechanism with its sayings injected instead of read
 * from a hard-wired pose table.
 */

/** Random eye-blink that pauses when the eyes are meant to stay shut. */
export function useBlink(enabled: boolean, tuning: Tuning): boolean {
  const [blinking, setBlinking] = useState(false);
  useEffect(() => {
    if (!enabled) {
      setBlinking(false);
      return;
    }
    let timer: ReturnType<typeof setTimeout>;
    const schedule = () => {
      const delay =
        tuning.minBlinkMs + Math.random() * (tuning.maxBlinkMs - tuning.minBlinkMs);
      timer = setTimeout(() => {
        setBlinking(true);
        timer = setTimeout(() => {
          setBlinking(false);
          schedule();
        }, tuning.blinkDurationMs);
      }, delay);
    };
    schedule();
    return () => clearTimeout(timer);
  }, [enabled, tuning]);
  return blinking;
}

/**
 * Inactivity ladder: active → bored → asleep, reset by any pointer/key activity
 * (or a deliberate expression). No driver needed — the avatar's own reflex.
 */
export function useIdleLadder(expressionActive: boolean, tuning: Tuning): Ladder {
  const [ladder, setLadder] = useState<Ladder>("active");
  const ladderRef = useRef<Ladder>("active");
  ladderRef.current = ladder; // current state for the move handler to read
  const lastActivity = useRef(0);
  const alertUntil = useRef(0); // typing pins him awake until this time
  useEffect(() => {
    lastActivity.current = Date.now();
    // Mouse movement wakes/keeps him active — but only when the window is
    // actually focused, so a stray move over a background window won't rouse him.
    const move = () => {
      if (!document.hasFocus()) return;
      lastActivity.current = Date.now();
      if (ladderRef.current !== "active") setLadder("active");
    };
    const wake = () => {
      lastActivity.current = Date.now();
    };
    // Typing also opens a grace window so he doesn't get bored/sleepy right after.
    const typed = () => {
      lastActivity.current = Date.now();
      alertUntil.current = Date.now() + tuning.alertAfterTypingMs;
    };
    window.addEventListener("pointermove", move);
    window.addEventListener("keydown", typed);
    window.addEventListener("pointerdown", wake);
    const poll = setInterval(() => {
      const now = Date.now();
      // During the post-typing grace, hold him alert and keep resetting the idle
      // clock, so when it lapses he resumes looking-around (not straight to sleep).
      if (now < alertUntil.current) lastActivity.current = now;
      const idle = now - lastActivity.current;
      const next: Ladder =
        idle > tuning.asleepAfterMs
          ? "asleep"
          : idle > tuning.boredAfterMs
            ? "bored"
            : "active";
      setLadder((prev) => (prev === next ? prev : next));
    }, 400);
    return () => {
      clearInterval(poll);
      window.removeEventListener("pointermove", move);
      window.removeEventListener("keydown", typed);
      window.removeEventListener("pointerdown", wake);
    };
  }, [tuning]);
  useEffect(() => {
    if (expressionActive) lastActivity.current = Date.now();
  }, [expressionActive]);
  return ladder;
}

/**
 * A short utterance emitted when the mood changes (and on a loop while `looping`,
 * e.g. asleep muttering). `sayingsFor` supplies the lines for a mood, so the hook
 * stays decoupled from any particular avatar's pose table.
 */
export function useSpeech<E extends string>(
  effective: E,
  sayingsFor: (e: E) => string[] | undefined,
  looping: boolean,
  mutterMs: number,
): { text: string; id: number } | null {
  const [speech, setSpeech] = useState<{ text: string; id: number } | null>(null);
  const nextId = useRef(0);
  useEffect(() => {
    const lines = sayingsFor(effective) ?? [];
    if (lines.length === 0) {
      setSpeech(null);
      return;
    }
    const emit = () => {
      const text = lines[Math.floor(Math.random() * lines.length)] ?? lines[0]!;
      nextId.current += 1;
      setSpeech({ text, id: nextId.current });
    };
    emit();
    if (looping) {
      const loop = setInterval(emit, mutterMs);
      return () => clearInterval(loop);
    }
    return undefined;
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [effective]);
  return speech;
}
