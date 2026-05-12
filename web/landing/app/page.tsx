import type { ReactNode } from 'react'

const GITHUB_URL = 'https://github.com/agentic-cookbook/agentic-persona-toolkit'

const CAPABILITIES: { label: string; blurb: string; entities: string; comingSoon?: boolean }[] = [
  {
    label: 'Persona Authoring',
    blurb:
      'Compose agents with distinct voices, backstories, and skills — reusable across workflows.',
    entities: 'Persona · Voice · Character · Examples · Provider Service',
  },
  {
    label: 'Coordination',
    blurb: 'Orchestrate teams of personas. Hand off tasks, share context, settle on a plan.',
    entities: 'Coordinator · Handoff · SharedContext · Plan',
    comingSoon: true,
  },
  {
    label: 'Toolkit & Adapters',
    blurb: 'Drop-in adapters for popular agent runtimes. Bring your personas anywhere.',
    entities: 'ChatBackend · ProviderAdapter · StorageAdapter',
    comingSoon: true,
  },
]

const SIBLINGS: { name: string; tagline: string; href: string }[] = [
  {
    name: 'The Agentic Cookbook',
    tagline: 'The book of recipes, principles, and policies behind the whole family.',
    href: 'https://agenticcookbook.dev',
  },
  {
    name: 'Agentic Persona Registry',
    tagline: 'Public agentic personas, discoverable.',
    href: 'https://agenticpersonaregistry.com',
  },
  {
    name: 'My Agentic Storage',
    tagline: 'Private files and project data for your agents.',
    href: 'https://myagenticstorage.com',
  },
  {
    name: 'User Data Store',
    tagline: 'Identity, calendar, contacts, and the integrations that feed them.',
    href: 'https://agenticdatastore.com',
  },
  {
    name: 'Agentic Developer Team',
    tagline: 'Where the agentic ecosystem comes together for builders.',
    href: 'https://agenticdevteam.com',
  },
  {
    name: 'Learn True Facts',
    tagline: 'A dogfood site that puts the toolkit through its paces.',
    href: 'https://learntruefacts.com',
  },
]

function CtaButton({
  variant = 'primary',
  href = GITHUB_URL,
  children = 'View on GitHub',
}: {
  variant?: 'primary' | 'subtle' | 'ghost'
  href?: string
  children?: ReactNode
}) {
  const base =
    'inline-flex items-center justify-center rounded-full text-sm font-medium transition-colors'
  const styles =
    variant === 'primary'
      ? 'bg-[var(--color-apt-gold)] text-[#0c0c0f] hover:bg-[var(--color-apt-gold-bright)] px-5 py-2'
      : variant === 'subtle'
        ? 'border border-[var(--color-apt-border)] text-[var(--color-apt-text)] hover:border-[var(--color-apt-gold)] hover:text-[var(--color-apt-gold)] px-5 py-2'
        : 'text-[var(--color-apt-text-muted)] hover:text-[var(--color-apt-gold)] underline-offset-4 hover:underline'
  return (
    <a href={href} className={`${base} ${styles}`}>
      {children}
    </a>
  )
}

function SectionLabel({ children }: { children: ReactNode }) {
  return (
    <p className="font-mono text-xs uppercase tracking-[0.2em] text-[var(--color-apt-text-dim)] mb-3">
      {children}
    </p>
  )
}

function CapabilityCard({
  label,
  blurb,
  entities,
  comingSoon,
}: {
  label: string
  blurb: string
  entities: string
  comingSoon?: boolean
}) {
  return (
    <div className="rounded-2xl border border-[var(--color-apt-border)] bg-[var(--color-apt-surface)] p-6">
      <h3 className="font-serif text-2xl mb-3 text-[var(--color-apt-text)]">
        {label}
        {comingSoon && <span className="coming-soon">coming soon</span>}
      </h3>
      <p className="text-[var(--color-apt-text-muted)] leading-relaxed mb-4">{blurb}</p>
      <p className="font-mono text-xs text-[var(--color-apt-text-dim)] leading-relaxed break-words">
        {entities}
      </p>
    </div>
  )
}

export default function Page() {
  return (
    <div className="min-h-screen bg-[var(--color-apt-bg)] text-[var(--color-apt-text)]">
      <nav className="fixed top-0 z-50 w-full border-b border-[var(--color-apt-border)] bg-[var(--color-apt-bg)]/80 backdrop-blur-md">
        <div className="mx-auto flex h-16 max-w-6xl items-center justify-between px-6">
          <div className="flex items-baseline gap-3">
            <span className="font-serif text-xl text-[var(--color-apt-text)]">
              Agentic <span className="italic text-[var(--color-apt-gold)]">Persona Toolkit</span>
            </span>
            <span className="font-mono text-[10px] uppercase tracking-[0.2em] text-[var(--color-apt-text-dim)] hidden sm:inline">
              agenticpersonatoolkit.dev
            </span>
          </div>
          <CtaButton />
        </div>
      </nav>

      <section className="px-6 pt-32 pb-20 md:pt-44 md:pb-28">
        <div className="mx-auto max-w-3xl text-center">
          <SectionLabel>Persona authoring + coordination</SectionLabel>
          <h1 className="font-serif text-5xl leading-tight mb-8 md:text-7xl">
            Build agents with personality.
            <br />
            <span className="italic text-[var(--color-apt-gold)]">Coordinate them with intent.</span>
          </h1>
          <p className="mx-auto mb-10 max-w-2xl text-lg leading-relaxed text-[var(--color-apt-text-muted)] md:text-xl">
            A toolkit for creating, coordinating, and managing AI agent personas in agentic
            workflows — from a single character to a coordinated team.
          </p>
          <div className="flex flex-col gap-4 sm:flex-row sm:justify-center">
            <CtaButton variant="primary" />
            <CtaButton variant="subtle" href="#whats-in-here">
              See what&rsquo;s inside
            </CtaButton>
          </div>
        </div>
      </section>

      <section
        id="whats-in-here"
        className="border-t border-[var(--color-apt-border)] bg-[var(--color-apt-bg)] px-6 py-20 md:py-28"
      >
        <div className="mx-auto max-w-6xl">
          <div className="mb-12 max-w-2xl">
            <SectionLabel>What&rsquo;s in the toolkit</SectionLabel>
            <h2 className="mb-4 font-serif text-4xl text-[var(--color-apt-text)] md:text-5xl">
              Three pieces for{' '}
              <span className="italic text-[var(--color-apt-gold)]">shipping agents</span>.
            </h2>
            <p className="text-lg leading-relaxed text-[var(--color-apt-text-muted)]">
              Author one persona or a whole team, coordinate their work, and plug into the runtime
              you already use.
            </p>
          </div>
          <div className="grid gap-5 md:grid-cols-2 lg:grid-cols-3">
            {CAPABILITIES.map((c) => (
              <CapabilityCard key={c.label} {...c} />
            ))}
          </div>
        </div>
      </section>

      <section className="border-t border-[var(--color-apt-border)] bg-[var(--color-apt-surface)]/40 px-6 py-20 md:py-28">
        <div className="mx-auto max-w-6xl">
          <div className="mb-12 max-w-2xl">
            <SectionLabel>The family</SectionLabel>
            <h2 className="mb-4 font-serif text-4xl text-[var(--color-apt-text)] md:text-5xl">
              Part of the{' '}
              <span className="italic text-[var(--color-apt-gold)]">Agentic Cookbook family</span>.
            </h2>
            <p className="text-lg leading-relaxed text-[var(--color-apt-text-muted)]">
              The toolkit sits alongside its siblings — the registry that defines personas, the
              stores that hold their data, and the sites that put them to work.
            </p>
          </div>
          <div className="grid gap-5 md:grid-cols-2 lg:grid-cols-3">
            {SIBLINGS.map((s) => (
              <a
                key={s.name}
                href={s.href}
                className="group block rounded-2xl border border-[var(--color-apt-border)] bg-[var(--color-apt-surface)] p-6 transition-colors hover:border-[var(--color-apt-gold)]"
              >
                <h3 className="mb-2 font-serif text-2xl text-[var(--color-apt-text)] group-hover:text-[var(--color-apt-gold)]">
                  {s.name}
                </h3>
                <p className="mb-4 text-sm leading-relaxed text-[var(--color-apt-text-muted)]">
                  {s.tagline}
                </p>
                <p className="font-mono text-[10px] uppercase tracking-[0.15em] text-[var(--color-apt-text-dim)]">
                  {s.href.replace('https://', '')} →
                </p>
              </a>
            ))}
          </div>
        </div>
      </section>

      <section className="border-t border-[var(--color-apt-border)] bg-[var(--color-apt-bg)] px-6 py-20 md:py-28">
        <div className="mx-auto max-w-2xl text-center">
          <h2 className="mb-6 font-serif text-4xl text-[var(--color-apt-text)] md:text-5xl">
            Give your agents <span className="italic text-[var(--color-apt-gold)]">a soul</span>.
            <br />
            Then give them a team.
          </h2>
          <p className="mb-10 text-lg leading-relaxed text-[var(--color-apt-text-muted)]">
            The toolkit is open source and under active development. Star it, file an issue, or pull
            it into your next agent project.
          </p>
          <CtaButton variant="primary" />
        </div>
      </section>

      <footer className="border-t border-[var(--color-apt-border)] px-6 py-10">
        <div className="mx-auto flex max-w-6xl flex-col items-center justify-between gap-4 md:flex-row">
          <p className="font-mono text-xs uppercase tracking-[0.2em] text-[var(--color-apt-text-dim)]">
            agenticpersonatoolkit.dev · part of the agentic cookbook family
          </p>
          <CtaButton variant="ghost" />
        </div>
      </footer>
    </div>
  )
}
