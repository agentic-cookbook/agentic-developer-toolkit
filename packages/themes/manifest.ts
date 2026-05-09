import agenticcookbookwebCss from './styles/agenticcookbookweb.css?inline'
import devTeamCss from './styles/dev-team.css?inline'
import mikefullertonCss from './styles/mikefullerton.css?inline'
import myprojectsCss from './styles/myprojects.css?inline'
import myprojectsoverviewCss from './styles/myprojectsoverview.css?inline'
import professionalCss from './styles/professional.css?inline'
import techyCss from './styles/techy.css?inline'
import terminalCss from './styles/terminal.css?inline'
import terminalSplitCss from './styles/terminal-split.css?inline'
import whimsicalCss from './styles/whimsical.css?inline'

export type ThemeKey =
  | 'agenticcookbookweb'
  | 'dev-team'
  | 'mikefullerton'
  | 'myprojects'
  | 'myprojectsoverview'
  | 'professional'
  | 'techy'
  | 'terminal'
  | 'terminal-split'
  | 'whimsical'

export interface ThemeEntry {
  id: ThemeKey
  label: string
  css: string
}

export const themes: Record<ThemeKey, ThemeEntry> = {
  agenticcookbookweb: { id: 'agenticcookbookweb', label: 'Agentic Cookbook', css: agenticcookbookwebCss },
  'dev-team': { id: 'dev-team', label: 'Dev Team', css: devTeamCss },
  mikefullerton: { id: 'mikefullerton', label: 'Mike Fullerton', css: mikefullertonCss },
  myprojects: { id: 'myprojects', label: 'My Projects', css: myprojectsCss },
  myprojectsoverview: { id: 'myprojectsoverview', label: 'Projects Overview', css: myprojectsoverviewCss },
  professional: { id: 'professional', label: 'Professional', css: professionalCss },
  techy: { id: 'techy', label: 'Techy', css: techyCss },
  terminal: { id: 'terminal', label: 'Terminal', css: terminalCss },
  'terminal-split': { id: 'terminal-split', label: 'Terminal Split', css: terminalSplitCss },
  whimsical: { id: 'whimsical', label: 'Whimsical', css: whimsicalCss },
}

export const themeIds: ThemeKey[] = Object.keys(themes) as ThemeKey[]
