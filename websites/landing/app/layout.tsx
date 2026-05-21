import type { Metadata } from 'next'
import './globals.css'

const SITE_URL = 'https://agenticdevelopertoolkit.com'
const TITLE = 'The Agentic Developer Toolkit — build agents with personality, coordinate them with intent'
const DESCRIPTION =
  'A toolkit for creating, coordinating, and managing AI agent personas in agentic workflows — from a single character to a coordinated team.'

export const metadata: Metadata = {
  metadataBase: new URL(SITE_URL),
  title: TITLE,
  description: DESCRIPTION,
  alternates: { canonical: '/' },
  openGraph: {
    type: 'website',
    url: SITE_URL,
    siteName: 'The Agentic Developer Toolkit',
    title: TITLE,
    description: DESCRIPTION,
  },
  twitter: {
    card: 'summary',
    title: TITLE,
    description: DESCRIPTION,
  },
  icons: { icon: '/favicon.svg' },
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
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
      <body>{children}</body>
    </html>
  )
}
