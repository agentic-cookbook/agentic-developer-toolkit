"use client";

import { useEffect } from "react";
import gsap from "gsap";
import type { Ref } from "./types";

/**
 * Pop a spoken utterance above the head, then let it drift off at a random angle
 * (biased upward) while fading — like a thought floating away. Pure: it just
 * animates whatever <text> node the avatar hands it. A missing ref is a no-op,
 * so an avatar without a speech node can still call the engine.
 */
export function useSpeechBubble(
  speechRef: Ref<SVGTextElement> | undefined,
  speech: { text: string; id: number } | null,
): void {
  useEffect(() => {
    const el = speechRef?.current;
    if (!speech || !el) return;
    gsap.killTweensOf(el);
    // Random drift vector: angle within ±55° of straight up, ~40–90px of travel.
    const angle = (-90 + (Math.random() * 110 - 55)) * (Math.PI / 180);
    const dist = 40 + Math.random() * 50;
    const driftX = Math.cos(angle) * dist;
    const driftY = Math.sin(angle) * dist;
    const spin = Math.random() * 24 - 12; // gentle tumble, ±12°
    gsap.set(el, { x: 0, y: 0, rotation: 0 });
    const tl = gsap.timeline();
    tl.fromTo(
      el,
      { opacity: 0, scale: 0.7, y: 6, transformOrigin: "50% 100%" },
      { opacity: 0.7, scale: 1, y: -4, duration: 0.22, ease: "back.out(2)" },
    ).to(el, {
      x: driftX,
      y: -4 + driftY,
      rotation: spin,
      opacity: 0,
      scale: 0.95,
      duration: 1.3,
      delay: 0.5,
      ease: "power1.in",
    });
    return () => {
      tl.kill();
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [speech?.id]);
}
