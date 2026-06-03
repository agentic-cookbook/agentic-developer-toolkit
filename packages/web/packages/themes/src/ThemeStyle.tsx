import { themes, type ThemeKey } from './manifest'

const GLOBAL_ID = 'agentic-toolkit-theme'
const SCOPED_ID = 'agentic-toolkit-theme-scoped'

const IMPORT_RE = /^@import\s+url\([^)]+\);\s*$/gm
const ROOT_DARK_RE = /(^|,\s*):root\.dark\b/gm
const ROOT_NOT_DARK_RE = /(^|,\s*):root:not\(\.dark\)/gm
const ROOT_RE = /(^|,\s*):root(?=[\s,{:])/gm
const BODY_RE = /(^|,\s*)body(?=[\s,{:.])/gm

function buildScopedCss(css: string, scope: string): string {
  const imports = (css.match(IMPORT_RE) || []).join('\n')
  const body = css
    .replace(IMPORT_RE, '')
    .replace(ROOT_DARK_RE, '$1html.dark :scope')
    .replace(ROOT_NOT_DARK_RE, '$1html:not(.dark) :scope')
    .replace(ROOT_RE, '$1:scope')
    .replace(BODY_RE, '$1:scope')
  return `${imports}\n@scope (${scope}) {\n${body}\n}`
}

export interface ThemeStyleProps {
  theme: ThemeKey
  scope?: string
}

export function ThemeStyle({ theme, scope }: ThemeStyleProps) {
  const css = scope ? buildScopedCss(themes[theme].css, scope) : themes[theme].css
  const id = scope ? SCOPED_ID : GLOBAL_ID
  // Render the <style> inline (so it's in the SSR HTML and applied on the very
  // first paint — no flash of default-sized, unstyled chat before a client
  // effect runs). The content is the resolved theme CSS, so re-rendering on a
  // theme/CSS change (incl. HMR) swaps it live. dangerouslySetInnerHTML is the
  // standard way to emit a <style> body without React escaping CSS punctuation
  // (e.g. `>`); the source is our own static theme manifest, not user input.
  return <style id={id} dangerouslySetInnerHTML={{ __html: css }} />
}
