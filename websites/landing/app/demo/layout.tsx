import type { ReactNode } from 'react'
import { Shell } from './Shell'
import './demo.css'

export default function DemoLayout({ children }: { children: ReactNode }) {
  return <Shell>{children}</Shell>
}
