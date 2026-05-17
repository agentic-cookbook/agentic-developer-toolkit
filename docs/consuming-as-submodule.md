# Consuming the toolkit as a git submodule

For first-party consumers (e.g. `learntruefacts`), the toolkit is consumed
directly from source via a git submodule. No `pnpm build` or `dist/` step is
required — Next.js transpiles the package source on demand.

## One-time setup in the consumer

Add the submodule wherever you want it to live:

```bash
git submodule add git@github.com:agentic-cookbook/agentic-persona-toolkit.git vendor/apt
```

In the consumer's `package.json` (e.g. `sites/main/package.json`), add a
`file:` ref per package you want to use:

```json
{
  "dependencies": {
    "@agentic-persona-toolkit/chat":     "file:./vendor/apt/packages/web/packages/chat",
    "@agentic-persona-toolkit/themes":   "file:./vendor/apt/packages/web/packages/themes",
    "@agentic-persona-toolkit/viewport": "file:./vendor/apt/packages/web/packages/viewport"
  }
}
```

In the consumer's `next.config.ts`, list the same package names under
`transpilePackages` so Next compiles their TS/TSX:

```ts
const nextConfig: NextConfig = {
  transpilePackages: [
    "@agentic-persona-toolkit/chat",
    "@agentic-persona-toolkit/themes",
    "@agentic-persona-toolkit/viewport",
  ],
};
```

Then install. The submodule ships an `install-for-submodule-use.sh`
helper that just runs `npm install` — a memorable shortcut so you don't
have to remember the command. From the directory containing your
consumer's `package.json`:

```bash
./vendor/apt/install-for-submodule-use.sh   # equivalent to: npm install
```

This creates one symlink per package in the consumer's `node_modules/`,
each pointing at the package directory inside the submodule.

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
- **Add a new toolkit package.** Add a `file:` line in `package.json`,
  add the name to `transpilePackages`, then re-run
  `./vendor/apt/install-for-submodule-use.sh` to symlink it.

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
