// Shared jsdom scaffolding for the caret-geometry hook tests (useCaretTracker,
// useBlockCursor, useCaretGaze). Two concerns live here so the harness isn't
// copy-pasted per test file:
//
//   • installCaretRectStub() — jsdom does no layout, so getBoundingClientRect
//     returns zeros; this swaps in a stub whose math is meaningful, then restores
//     the real method after each test.
//   • appendToBody() — auto-removes manually-mounted nodes after each test.
//     testing-library's cleanup only unmounts React trees, not nodes a test
//     appends to document.body itself, so without this they leak across tests.
import { afterEach, beforeEach } from 'vitest'

export function makeRect(rect: Partial<DOMRect>): DOMRect {
  return {
    x: 0, y: 0, width: 0, height: 0, top: 0, left: 0, right: 0, bottom: 0,
    toJSON: () => ({}),
    ...rect,
  } as DOMRect
}

/**
 * Replace Element.prototype.getBoundingClientRect for the current test file and
 * restore it afterwards. Elements registered via the returned `setRect` report
 * their explicit rect; unregistered <span> mirrors (created fresh inside
 * caretMetrics itself, so a test can't reach them beforehand) get a width that
 * scales with their text length, standing in for glyph width.
 */
export function installCaretRectStub(): {
  setRect: (el: Element, rect: Partial<DOMRect>) => void
} {
  const original = Element.prototype.getBoundingClientRect
  const rects = new WeakMap<Element, DOMRect>()
  beforeEach(() => {
    Element.prototype.getBoundingClientRect = function () {
      const known = rects.get(this)
      if (known) return known
      if (this.tagName === 'SPAN') {
        const width = (this.textContent?.length ?? 0) * 10
        return makeRect({ width, right: width })
      }
      return makeRect({})
    }
  })
  afterEach(() => {
    Element.prototype.getBoundingClientRect = original
  })
  return { setRect: (el, rect) => rects.set(el, makeRect(rect)) }
}

const appended: Element[] = []

/** Append `el` to document.body and auto-remove it after the current test. */
export function appendToBody<T extends Element>(el: T): T {
  document.body.appendChild(el)
  appended.push(el)
  return el
}

afterEach(() => {
  for (const el of appended) el.remove()
  appended.length = 0
})
