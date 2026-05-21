# Toolkit Repo Pattern

How this repo (`agentic-persona-toolkit`) is laid out and consumed. Capture
this pattern when starting a sibling toolkit repo — server packages, alternate
domain SDKs, anything that ships reusable libraries to a mix of first-party
and external consumers.

## What the pattern solves

Shipping reusable packages from a single repo to two audiences:

- **First-party consumers** — apps inside your org that want live edits.
  They embed the repo as a git submodule, edit library source directly, and
  pick up changes through HMR with no build step.
- **External consumers** — future third-party users who `npm install @org/pkg`
  once the packages are published. Same code; a dormant publish config flips
  on at publish time.

No build step is needed for the first-party path. No code changes are needed
to flip on the external path.

## Repo layout

The repo root holds no language-specific manifests. Each platform owns a
top-level dir under `packages/<platform>/` which is the ROOT of that
platform's native build system (its conventional manifest lives there).

```
<repo>/
├── README.md
├── AGENTS.md
├── install.sh                       # bootstrap the workspace (for toolkit devs)
├── docs/
├── packages/
│   ├── web/                         # pnpm workspace root (package.json, lockfile)
│   │   ├── pnpm-workspace.yaml
│   │   └── packages/
│   │       ├── chat/
│   │       ├── themes/
│   │       └── viewport/
│   ├── apple/                       # Package.swift + project.yml
│   ├── terminal/                    # pyproject.toml
│   ├── android/                     # (TBD)
│   └── windows/                     # (TBD)
└── websites/
    └── landing/                     # public marketing + /demo route (QA + deployed)
```

Libraries may only depend on other `packages/<platform>/packages/*` — never on
ad-hoc paths outside their workspace.

## The source-by-default manifest (the key trick)

Each library's `package.json` points its `main` / `types` / `exports` at
`./src/...`, with `publishConfig` mirroring the same shape against
`./dist/...`. pnpm and npm honor `publishConfig` only at publish time:

```json
{
  "main": "./src/index.ts",
  "types": "./src/index.ts",
  "exports": {
    ".": { "types": "./src/index.ts", "import": "./src/index.ts" }
  },
  "publishConfig": {
    "main": "./dist/index.js",
    "types": "./dist/index.d.ts",
    "exports": {
      ".": { "types": "./dist/index.d.ts", "import": "./dist/index.js" }
    }
  }
}
```

In-repo and submodule consumers resolve `./src/index.ts` directly. The
consuming app's bundler (Next.js's `transpilePackages`, Vite's
`optimizeDeps`, etc.) compiles the TypeScript on demand — no toolkit build
step needed.

At publish time, `publishConfig` flips the manifest to point at `./dist/...`.
Published consumers get a prebuilt tarball with no source-or-bundler coupling.

## Consumer wiring — first-party submodule path

See [`consuming-as-submodule.md`](consuming-as-submodule.md) for the full
walkthrough. In short:

1. `git submodule add <toolkit-url> vendor/<name>`
2. Add `file:` refs to the consumer's `package.json`:
   `"@org/pkg": "file:./vendor/<name>/packages/<platform>/packages/pkg"`
3. List the same names under the consuming app's transpile list
   (e.g., Next.js `transpilePackages`).
4. From the consumer app dir, run your project's install command
   (`npm install` / `pnpm install` / `yarn`).

Live edits in `vendor/<name>/packages/<platform>/packages/<pkg>/src/` flow
through to the consumer's dev server via HMR.

## Consumer wiring — future npm path

Once the packages are published, external consumers just
`npm install @org/pkg`. `publishConfig` makes their tarball point at `dist/`,
so they don't need `transpilePackages` or any submodule setup. The first-party
submodule flow continues to work in parallel — same source, different shipping.

## The install script at the repo root

`install.sh` bootstraps the workspace for toolkit developers
(`cd packages/web && pnpm install`) and prints pointers to test / build
commands. Consumers don't run it — they run their own project's install
command (`npm install` / `pnpm install` / `yarn`) from the consumer app dir
after pulling a new submodule SHA. Their package manager picks up the `file:`
refs and re-links them.

## Deployment

Enable submodule checkout in your deploy platform:

- **Vercel:** Settings → Git → Include submodules.
- **Cloudflare Pages:** Settings → Builds & deployments → Include submodules.
- **GitHub Actions:** `actions/checkout@v4` with `submodules: recursive`.

The build container runs the consumer's normal install + build. The consuming
framework (Next.js, etc.) handles source-to-bundle for the toolkit packages.
No toolkit build step required in CI.

## Adapting for other ecosystems

The pattern translates to any ecosystem with file-based local deps plus a
publish-time manifest override:

| Ecosystem | Source-by-default mechanism | Publish-time mechanism |
|---|---|---|
| TypeScript / npm | `main`/`types`/`exports` → `src/`, plus `transpilePackages` in the consumer | `publishConfig` flips to `dist/` |
| Python | `pyproject.toml` with editable installs (`pip install -e ./packages/foo`) | Standard `pip install` from a published wheel |
| Go | `replace github.com/org/pkg => ./packages/pkg` in the consumer's `go.mod` | Tagged release; consumer drops the `replace` |
| Rust | `path = "../../packages/pkg"` in the consumer's `Cargo.toml` | Tagged crate publish; consumer switches to `version = "..."` |
| Swift | Local `Package.swift` package ref | Tagged release with `from:` |

**The principle is the same in every ecosystem:** package metadata points at
source by default; a publish-time mechanism flips it to a prebuilt artifact
with no code changes. Demos and first-party apps live in the same repo and
consume the packages exactly the way external consumers will.

## Starting a new toolkit repo (checklist)

- [ ] Repo root has only `README.md`, `AGENTS.md`, `install.sh`,
      `.gitignore`, `docs/`, `packages/`, and optionally `websites/`.
      No language manifest at the root.
- [ ] `packages/<platform>/` for each platform you ship; each is a workspace
      root in its native package manager.
- [ ] Library manifests point at source by default with a publish-time override.
- [ ] In-repo demo / QA app under `websites/landing/` (the `/demo` route)
      consumes the libraries via the same submodule pattern external consumers
      will use. Run locally with `python3 websites/landing/run.py`.
- [ ] `install.sh` bootstraps the workspace for developers. Consumers run
      their own package manager's install command; no consumer-side wrapper
      script is needed.
- [ ] `docs/consuming-as-submodule.md` documents the consumer flow.
- [ ] `docs/repo-pattern.md` (this file) documents the design so the next
      sibling repo can copy it.
- [ ] `AGENTS.md` orients agents and humans landing in the repo.
- [ ] `.claude/CLAUDE.md` captures layout and conventions for AI agents.
