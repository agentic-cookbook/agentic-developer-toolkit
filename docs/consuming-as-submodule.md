# Consuming the toolkit as a git submodule

For first-party consumers (e.g. `learntruefacts`), the toolkit is consumed
directly from source via a git submodule. No `pnpm build` or `dist/` step is
required — Next.js transpiles the package source on demand.

## One-time setup in the consumer

Add the submodule wherever you want it to live:

```bash
git submodule add git@github.com:agentic-cookbook/agentic-persona-toolkit.git vendor/apt
```

Then run the toolkit's install helper from the consumer's repo root, passing
the directory that contains the consumer's `package.json` (use `.` for a
single-app repo, or e.g. `sites/main` for a monorepo):

```bash
./vendor/apt/install-for-submodule-use.sh sites/main
```

The script discovers every toolkit package, adds the right `file:` refs to
the consumer's `package.json`, updates `transpilePackages` in
`next.config.{ts,mjs,js,cjs}`, and runs the consumer's package manager
(pnpm / yarn / npm — auto-detected from lockfile) to symlink them.

If you'd rather wire it up by hand, the script does this:

```json
// consumer's package.json
{
  "dependencies": {
    "@agentic-persona-toolkit/chat":     "file:./vendor/apt/packages/web/packages/chat",
    "@agentic-persona-toolkit/themes":   "file:./vendor/apt/packages/web/packages/themes",
    "@agentic-persona-toolkit/viewport": "file:./vendor/apt/packages/web/packages/viewport"
  }
}
```

```ts
// consumer's next.config.ts
const nextConfig: NextConfig = {
  transpilePackages: [
    "@agentic-persona-toolkit/chat",
    "@agentic-persona-toolkit/themes",
    "@agentic-persona-toolkit/viewport",
  ],
};
```

Either path creates one symlink per package in the consumer's
`node_modules/`, each pointing at the package directory inside the submodule.

## Day-to-day workflow

- **Edit toolkit source live.** Branch the submodule
  (`cd vendor/apt && git checkout -b feature`), edit any `.tsx` / `.ts` /
  `.css` inside `packages/web/packages/<name>/src/`, save. The consumer's
  `next dev` picks it up through HMR immediately. No reinstall, no build.
- **Commit in two places.** Commit your toolkit changes inside the submodule,
  push. Then commit the updated submodule pointer in the consumer repo.
- **Bump in other repos.** In any other consumer:
  `git submodule update --remote vendor/apt`. Source updates flow through;
  no reinstall needed unless the toolkit added a new runtime/peer dep.
- **Add a new toolkit package.** After bumping the submodule, re-run
  `./vendor/apt/install-for-submodule-use.sh <consumer-dir>` — it's
  idempotent and picks up any new packages found under the toolkit's
  `packages/web/packages/`.

## Deploying

Enable submodule checkout in your deploy platform:

- **Vercel:** Settings → Git → Include submodules.
- **Cloudflare Pages:** Settings → Builds & deployments → Include submodules.
- **GitHub Actions:** `actions/checkout@v4` with `submodules: recursive`.

The build container then runs the consumer's normal install + build (e.g.
`pnpm install && next build`) — Next handles the source-to-bundle step via
`transpilePackages`. No `pnpm build` of the toolkit is required.

## Future: npm-installed consumers

External consumers (outside this org) won't use the submodule — they'll
`npm install @agentic-persona-toolkit/chat` once the packages are published.
Each package's `publishConfig` rewrites `main`/`types`/`exports` to point at
`./dist/...` at publish time, so external consumers get a prebuilt tarball
and don't need `transpilePackages`. Until publish, `publishConfig` sits
dormant; nothing changes for the submodule flow.

To publish, from inside the toolkit repo:

```bash
cd packages/web && pnpm build         # populates dist/
pnpm --filter @agentic-persona-toolkit/chat publish
```
