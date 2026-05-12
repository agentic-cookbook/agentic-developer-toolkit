import type { ComponentType } from 'react'
import ChatExample from './_examples/chat'
import ThemeExample from './_examples/theme'

export type ExampleEntry = {
  id: string
  label: string
  Component: ComponentType
}

export const examples: ExampleEntry[] = [
  { id: 'chat', label: 'Chat', Component: ChatExample },
  { id: 'theme', label: 'Theme', Component: ThemeExample },
]
