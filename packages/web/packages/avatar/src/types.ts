import type { RefObject } from "react";

/**
 * The persona-agnostic types an avatar speaks to the engine in.
 *
 * An avatar owns its IDENTITY — the SVG glyph it renders and the pose data that
 * gives each mood its look. The engine owns BEHAVIOR — reflexes (blink, idle
 * ladder, gaze, speech) and the expression-driven pose loop. The two meet here:
 *
 *   • {@link AvatarDriverProps} — the public puppet contract a driver sets.
 *   • {@link Pose} — one mood's look, every channel optional.
 *   • {@link AvatarRig} — the avatar's SVG refs + geometry, injected into the
 *     engine. Each animated CHANNEL (eyes, brows, antennae, mouth, …) is
 *     optional: omit a channel's descriptor and the engine skips it. An
 *     eyes-and-brows avatar wires only `eyes` + `brows`; olylo wires them all.
 *
 * The engine reads `.current` at effect time, so the rig holds REF OBJECTS, not
 * elements — the same way olylo's effects always read `someRef.current`.
 */

/** A nullable React ref, as `useRef<T>(null)` produces. */
export type Ref<T> = RefObject<T | null>;

/**
 * The deliberate inputs a driver (a chat, a persona) sets on an avatar. Generic
 * over the avatar's own expression vocabulary `E`. Persona-agnostic: a driver
 * can puppet any avatar through this contract without knowing its anatomy.
 */
export interface AvatarDriverProps<E extends string = string> {
  /** Deliberate mood. Omit and the avatar runs on reflexes alone (blink/gaze/sleep). */
  expression?: E;
  /**
   * A deliberate gaze direction, normalized: x ∈ [-1,1] (right is +), y ∈ [-1,1]
   * (down is +). While set, it overrides cursor-follow and idle look-around.
   * Omit or pass null to hand the eyes back to those reflexes.
   */
  gaze?: { x: number; y: number } | null;
  /** Fires with each short utterance the avatar blurts, so a driver can echo it. */
  onSpeak?: (text: string) => void;
  /** When true, the avatar keeps its expressions but stays silent (no speech bubbles). */
  mute?: boolean;
}

/**
 * One expression's look. Every field is optional except timing — an avatar fills
 * in only the channels it has. Globals (`scale`/`rotation`/`spread`/`body`/…)
 * apply across channels; the rest target a single channel and are ignored when
 * the avatar doesn't wire that channel into its {@link AvatarRig}.
 */
export interface Pose {
  // ── timing (always required) ──
  /** Transition duration (s) — fast for surprise/anger, slow for sad/sleepy. */
  dur: number;
  /** Transition ease (gsap string) — e.g. `back.out(1.7)` for an overshoot/pop. */
  ease: string;

  // ── globals (channel-independent) ──
  /** Utterances; one picked at random on entering this mood. Omit/[] = silent. */
  sayings?: string[];
  /** Whole-glyph size multiplier (body channel). >1 swells, <1 withdraws. Omit = 1. */
  scale?: number;
  /** Whole-glyph settled rotation in degrees (body channel). Omit = 0. */
  rotation?: number;
  /** Extra full entry turns whirled, landing at `rotation` (body channel). Omit = 0. */
  spinTurns?: number;
  /** Parts spread apart (+) / together (−) in viewBox units — eyes + antennae. Omit = 0. */
  spread?: number;
  /** Chameleon color: the face group + any `currentColor` parts take it. */
  body?: string;
  /** Face bob amplitude in viewBox units (face channel); loops while held. Omit = 0. */
  bob?: number;
  /** Face wiggle rotation in degrees (face channel); loops while held. Omit = 0. */
  wiggle?: number;

  // ── eyes / iris channels ──
  /** Eye scale about its own centre — openness + size. Drives both eyes. */
  eye?: { scaleX: number; scaleY: number };
  /** Per-eye scale override for asymmetric looks (a one-eye squint). Falls back to `eye`. */
  eyeLeft?: { scaleX: number; scaleY: number };
  eyeRight?: { scaleX: number; scaleY: number };
  /** Vertical shift of BOTH eyes (viewBox units, negative = up). Omit = 0. */
  eyeY?: number;
  /** Pupil dilation — multiplier on the iris base radius. <1 constricts, >1 dilates. Omit = 1. */
  pupil?: number;

  // ── antennae channel ──
  /** Antenna stroke pose (pivots at its base): rotation + vertical offset. */
  lLeft?: { rotation: number; y: number };
  lRight?: { rotation: number; y: number };

  // ── brows channel ──
  /** Eyebrow pose: y raises(−)/lowers(+); rotation swings out(−)/in(+). */
  browLeft?: { y: number; rotation: number };
  browRight?: { y: number; rotation: number };

  // ── mouth / descender channels ──
  /** Mouth path `d` — MorphSVG morphs between poses. Keep point counts matched. */
  mouth?: string;
  /** Descender "logo mode" toggle: true ⇒ the avatar's `logoPath`, else `plainPath`. */
  showY?: boolean;
}

// ─────────────────────────────────────────────────────────────────────────────
// The rig — an avatar's SVG refs + geometry, injected into the engine. Every
// channel is optional; absent channels are skipped by every effect.
// ─────────────────────────────────────────────────────────────────────────────

/** Eyes — scale (openness/size), spread, vertical shift, per-eye override. */
export interface EyesChannel {
  leftRef: Ref<SVGGElement>;
  rightRef: Ref<SVGGElement>;
  /** Inner blink groups — collapsed on blink, independent of the pose eye-scale. */
  blinkLeftRef?: Ref<SVGGElement>;
  blinkRightRef?: Ref<SVGGElement>;
  /** transformOrigin for each eye's scale. Default "50% 50%". */
  origin?: string;
}

/** Steerable pupils — dilation (the `r` attr) + gaze translate (x/y). */
export interface IrisChannel {
  leftRef: Ref<SVGCircleElement>;
  rightRef: Ref<SVGCircleElement>;
  /** Base iris radius in viewBox units; `pose.pupil` scales it. */
  baseR: number;
}

/** Bendy feelers — rotation/y per pose + an always-on side-to-side bend/wiggle. */
export interface AntennaeChannel {
  leftRef: Ref<SVGPathElement>;
  rightRef: Ref<SVGPathElement>;
  /** transformOrigin for the per-pose rotate/translate. Default "50% 0%". */
  origin?: string;
  /** Builds the bend path `d` for one side at a given sway amplitude (avatar geometry). */
  bend: (side: "left" | "right", amp: number) => string;
}

/** Eyebrows — rotation (swing out/in) + y (raise/lower), each pivoting at its eye. */
export interface BrowsChannel {
  leftRef: Ref<SVGGElement>;
  rightRef: Ref<SVGGElement>;
  /** svgOrigin the LEFT brow pivots about (its eye centre), e.g. "50 50". */
  leftOrigin: string;
  /** svgOrigin the RIGHT brow pivots about, e.g. "270 50". */
  rightOrigin: string;
}

/** A morphing mouth path. Morph targets come from `pose.mouth`. */
export interface MouthChannel {
  ref: Ref<SVGPathElement>;
}

/** The tail/descender under the mouth — morphs between a "logo" and "plain" path. */
export interface DescenderChannel {
  ref: Ref<SVGPathElement>;
  /** Path when `pose.showY` is true (logo mode). */
  logoPath: string;
  /** Path otherwise (a plain tail). */
  plainPath: string;
  /** svgOrigin for the lively tail-flick wiggle, e.g. "160 85". */
  wiggleOrigin: string;
}

/** The face group — carries the chameleon color tween + the bob/wiggle loops. */
export interface FaceChannel {
  ref: Ref<SVGGElement>;
  /** transformOrigin for the wiggle. Default "50% 60%". */
  wiggleOrigin?: string;
}

/**
 * The avatar's SVG, injected into the engine. `pivot` and the transform layers
 * are how the engine stays DOM-agnostic; the channels are how it stays
 * anatomy-agnostic — it animates only the channels an avatar actually wires.
 */
export interface AvatarRig {
  /** The root <svg>; gaze reads its bounding rect for cursor math. */
  svg: Ref<SVGSVGElement>;
  /**
   * The central pivot — typically between the eyes — that whole-glyph
   * scale/rotation, the head-tilt, and the idle sway/breath all turn about.
   * e.g. "160 50" (viewBox units).
   */
  pivot: string;
  /** Idle fidget (sway + breath) and asleep micro-stirs ride this layer. */
  idleLayer?: Ref<SVGGElement>;
  /** Head-tilt toward a deliberate gaze rides this layer. */
  tiltLayer?: Ref<SVGGElement>;
  /** Lean/drift toward what's watched (a pure-translate layer). */
  leanLayer?: Ref<SVGGElement>;
  /** Whole-glyph emotional scale + rotation (+ entry spin). */
  body?: { ref: Ref<SVGGElement> };
  eyes?: EyesChannel;
  iris?: IrisChannel;
  antennae?: AntennaeChannel;
  brows?: BrowsChannel;
  mouth?: MouthChannel;
  descender?: DescenderChannel;
  face?: FaceChannel;
  /** The <text> node a spoken utterance pops above and drifts off from. */
  speech?: Ref<SVGTextElement>;
}

/**
 * Timings + travel limits, all overridable. Defaults match olylo; an avatar
 * passes a partial override to retune without touching the engine.
 */
export interface Tuning {
  /** Max iris travel in viewBox units. */
  gazeMax: number;
  /** Max head-tilt toward a deliberate gaze (degrees). */
  tiltMax: number;
  /** Max whole-glyph drift toward what's watched (viewBox units). */
  leanMax: number;
  /** Cursor must be still this long before the idle look-around starts (ms). */
  wanderAfterMs: number;
  /** A new idle glance every wanderMin..Max ms. */
  wanderMinMs: number;
  wanderMaxMs: number;
  /** Blink: how long the lid stays shut, and the random gap between blinks (ms). */
  blinkDurationMs: number;
  minBlinkMs: number;
  maxBlinkMs: number;
  /** Idle ladder: inactivity before bored, then asleep (ms). */
  boredAfterMs: number;
  asleepAfterMs: number;
  /** Typing pins the avatar awake + curious this long before it can drift off (ms). */
  alertAfterTypingMs: number;
  /** While asleep, mutter on this loop (ms) — sparser than waking chatter. */
  sleepMutterMs: number;
}

export const DEFAULT_TUNING: Tuning = {
  gazeMax: 7,
  tiltMax: 9,
  leanMax: 6,
  wanderAfterMs: 1200,
  wanderMinMs: 1400,
  wanderMaxMs: 3200,
  blinkDurationMs: 130,
  minBlinkMs: 2800,
  maxBlinkMs: 7000,
  boredAfterMs: 6000,
  asleepAfterMs: 14000,
  alertAfterTypingMs: 30000,
  sleepMutterMs: 11000,
};

/** The inactivity ladder rung. */
export type Ladder = "active" | "bored" | "asleep";
