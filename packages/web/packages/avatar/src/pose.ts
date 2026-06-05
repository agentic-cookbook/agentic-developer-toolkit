import gsap from "gsap";
import type { AvatarRig, Pose } from "./types";

// Settle defaults — used when a channel returns to neutral (bob/wiggle off).
const TWEEN = 0.45;
const EASE = "power3.out";

const present = <T>(...els: (T | null)[]): T[] =>
  els.filter((e): e is T => e !== null);

/**
 * Tween every wired channel toward one pose; morph the mouth/descender. Returns
 * the LOOPING tweens (antenna sway, face bob/wiggle, tail-flick) so the caller
 * can kill them on the next pose change — the one-shot tweens settle on their own.
 *
 * Every channel is guarded by its rig descriptor: an avatar that wires only
 * `eyes` + `brows` runs only those two blocks. Avatar geometry (the central
 * pivot, brow/antenna pivots, the bend curve, the descender paths) all comes
 * from the rig, so this stays pure mechanism — no avatar's anatomy is baked in.
 */
export function applyPose(rig: AvatarRig, pose: Pose, eyesShut: boolean): gsap.core.Animation[] {
  const loops: gsap.core.Animation[] = [];
  const dur = pose.dur;
  const ease = pose.ease;
  const spread = pose.spread ?? 0;
  const wiggle = pose.wiggle ?? 0;

  // ── body: whole-glyph emotional scale + rotation (+ a one-shot entry spin) ──
  // One tween so scale + rotation share a transform matrix (concurrent tweens
  // with svgOrigin fight over it). `overwrite:"auto"` is essential: React re-runs
  // this effect (incl. Strict Mode's double-invoke) and without it duplicate
  // transform tweens cancel to identity.
  const bodyEl = rig.body?.ref.current;
  if (bodyEl) {
    const spinTurns = pose.spinTurns ?? 0;
    gsap.to(bodyEl, {
      scale: pose.scale ?? 1,
      rotation: (pose.rotation ?? 0) + 360 * spinTurns, // land at `rotation` after N whirls
      svgOrigin: rig.pivot,
      duration: spinTurns ? 0.9 : dur,
      ease: spinTurns ? "power3.inOut" : ease,
      overwrite: "auto",
    });
  }

  // ── eyes: scale (openness/size), spread, vertical shift; per-eye override ──
  if (rig.eyes) {
    const origin = rig.eyes.origin ?? "50% 50%";
    const eyeY = pose.eyeY ?? 0;
    const base = pose.eye ?? { scaleX: 1, scaleY: 1 };
    const eyeL = pose.eyeLeft ?? base;
    const eyeR = pose.eyeRight ?? base;
    const leftEl = rig.eyes.leftRef.current;
    const rightEl = rig.eyes.rightRef.current;
    if (leftEl)
      gsap.to(leftEl, { scaleX: eyeL.scaleX, scaleY: eyeL.scaleY, x: -spread, y: eyeY, transformOrigin: origin, duration: dur, ease });
    if (rightEl)
      gsap.to(rightEl, { scaleX: eyeR.scaleX, scaleY: eyeR.scaleY, x: spread, y: eyeY, transformOrigin: origin, duration: dur, ease });
  }

  // ── iris: pupil dilation via the `r` attr (independent of the gaze x/y) ──
  if (rig.iris) {
    const targets = present(rig.iris.leftRef.current, rig.iris.rightRef.current);
    if (targets.length)
      gsap.to(targets, { attr: { r: rig.iris.baseR * (pose.pupil ?? 1) }, duration: dur, ease });
  }

  // ── antennae: per-pose rotation/y, then an always-on bend/wiggle on top ──
  if (rig.antennae) {
    const { bend } = rig.antennae;
    const origin = rig.antennae.origin ?? "50% 0%";
    const leftEl = rig.antennae.leftRef.current;
    const rightEl = rig.antennae.rightRef.current;
    if (pose.lLeft && leftEl)
      gsap.to(leftEl, { rotation: pose.lLeft.rotation, x: -spread, y: pose.lLeft.y, transformOrigin: origin, duration: dur, ease, delay: 0.04 });
    if (pose.lRight && rightEl)
      gsap.to(rightEl, { rotation: pose.lRight.rotation, x: spread, y: pose.lRight.y, transformOrigin: origin, duration: dur, ease, delay: 0.04 });
    if (eyesShut) {
      // held straight & still while asleep
      if (leftEl) gsap.to(leftEl, { morphSVG: bend("left", 0), duration: 0.5, ease: "sine.out" });
      if (rightEl) gsap.to(rightEl, { morphSVG: bend("right", 0), duration: 0.5, ease: "sine.out" });
    } else {
      const amp = wiggle > 0 ? 18 : 8; // big & fast when lively, small otherwise
      if (leftEl) {
        gsap.set(leftEl, { attr: { d: bend("left", -amp) } });
        loops.push(gsap.to(leftEl, { morphSVG: bend("left", amp), duration: wiggle > 0 ? 0.3 : 0.85, repeat: -1, yoyo: true, ease: "sine.inOut", delay: 0.12 }));
      }
      if (rightEl) {
        gsap.set(rightEl, { attr: { d: bend("right", amp) } });
        loops.push(gsap.to(rightEl, { morphSVG: bend("right", -amp), duration: wiggle > 0 ? 0.36 : 1.05, repeat: -1, yoyo: true, ease: "sine.inOut", delay: 0.12 })); // out of phase
      }
    }
  }

  // ── brows: rotation (swing) + y (raise/lower), each pivoting at its eye ──
  if (rig.brows) {
    const { leftOrigin, rightOrigin } = rig.brows;
    const leftEl = rig.brows.leftRef.current;
    const rightEl = rig.brows.rightRef.current;
    if (pose.browLeft && leftEl)
      gsap.to(leftEl, { rotation: pose.browLeft.rotation, y: pose.browLeft.y, svgOrigin: leftOrigin, duration: dur, ease, delay: 0.06 });
    if (pose.browRight && rightEl)
      gsap.to(rightEl, { rotation: pose.browRight.rotation, y: pose.browRight.y, svgOrigin: rightOrigin, duration: dur, ease, delay: 0.06 });
  }

  // ── chameleon: tween the face color (currentColor parts follow). Eyes use
  //    explicit fills, so they stay lit while the body recolors. ──
  const faceEl = rig.face?.ref.current;
  if (faceEl && pose.body) {
    gsap.to(faceEl, { color: pose.body, duration: dur, ease, delay: 0.08 });
  }

  // ── mouth morph ──
  const mouthEl = rig.mouth?.ref.current;
  if (mouthEl && pose.mouth) {
    gsap.to(mouthEl, { morphSVG: pose.mouth, duration: dur, ease, delay: 0.08 });
  }

  // ── descender/tail: morph between logo + plain; tail-flick wiggle when lively ──
  if (rig.descender) {
    const d = rig.descender;
    const el = d.ref.current;
    if (el) {
      gsap.to(el, { morphSVG: pose.showY ? d.logoPath : d.plainPath, duration: dur, ease, delay: 0.08 });
      if (wiggle > 0) {
        gsap.set(el, { rotation: -9, svgOrigin: d.wiggleOrigin });
        loops.push(gsap.to(el, { rotation: 9, duration: 0.22, repeat: -1, yoyo: true, ease: "sine.inOut", svgOrigin: d.wiggleOrigin }));
      } else {
        gsap.to(el, { rotation: 0, svgOrigin: d.wiggleOrigin, duration: dur, ease });
      }
    }
  }

  // ── face bob + wiggle loops (a lively bounce / giggle shimmy) ──
  if (faceEl) {
    const bob = pose.bob ?? 0;
    if (bob > 0) {
      loops.push(gsap.to(faceEl, { y: -bob, duration: 0.5, repeat: -1, yoyo: true, ease: "sine.inOut" }));
    } else {
      gsap.to(faceEl, { y: 0, duration: TWEEN, ease: EASE });
    }
    const wiggleOrigin = rig.face?.wiggleOrigin ?? "50% 60%";
    if (wiggle > 0) {
      gsap.set(faceEl, { rotation: -wiggle, transformOrigin: wiggleOrigin });
      loops.push(gsap.to(faceEl, { rotation: wiggle, duration: 0.16, repeat: -1, yoyo: true, ease: "sine.inOut" }));
    } else {
      gsap.to(faceEl, { rotation: 0, duration: TWEEN, ease: EASE });
    }
  }

  return loops;
}
