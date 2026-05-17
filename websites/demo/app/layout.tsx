import type { Metadata, Viewport } from 'next'
import type { ReactNode } from 'react'
import { Shell } from './Shell'
import './demo.css'

export const metadata: Metadata = {
  title: 'Agentic Persona Toolkit — Demo',
  description:
    'Interactive demo of the agentic-persona-toolkit chat and theme packages.',
}

export const viewport: Viewport = {
  width: 'device-width',
  initialScale: 1,
}

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="" />
        <link
          rel="stylesheet"
          href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400&family=Instrument+Serif:ital@0;1&family=Manrope:wght@400;500;600&display=swap"
        />
      </head>
      <body>
        <Shell>{children}</Shell>
      </body>
    </html>
  )
}
