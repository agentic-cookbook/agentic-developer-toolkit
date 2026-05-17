#!/usr/bin/env python3
"""Build entry point for `websites/landing/`.

The landing site consumes `@agentic-persona-toolkit/*` packages from source via
their `file:` references and Next.js's `transpilePackages`. Next compiles the
symlinked TS/TSX during `next build`, so no toolkit dist step is needed.

We still have to install the toolkit workspace under `packages/web/` so the
toolkit packages' peer/dev deps (`react`, `@types/react`, etc.) are resolvable
from inside each package's directory — TypeScript walks up from each source
file's physical location, not from the consumer's `node_modules`.
"""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

LANDING_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = LANDING_DIR.parent.parent
WEB_WORKSPACE = REPO_ROOT / "packages" / "web"


def run(cmd: list[str], cwd: Path) -> None:
    print(f"==> {' '.join(cmd)}  (cwd={cwd})", flush=True)
    subprocess.run(cmd, cwd=cwd, check=True)


def ensure_pnpm() -> str:
    """Return a pnpm command runner, enabling corepack if pnpm is missing."""
    if shutil.which("pnpm"):
        return "pnpm"
    if shutil.which("corepack"):
        run(["corepack", "enable"], cwd=REPO_ROOT)
        if shutil.which("pnpm"):
            return "pnpm"
    print("error: pnpm not found and corepack could not provide it", file=sys.stderr)
    sys.exit(1)


def main() -> int:
    pnpm = ensure_pnpm()
    # Install the toolkit workspace so peer/dev deps resolve from inside each
    # symlinked package during Next's typecheck.
    run([pnpm, "install", "--frozen-lockfile"], cwd=WEB_WORKSPACE)
    run(["npx", "opennextjs-cloudflare", "build"], cwd=LANDING_DIR)
    # Copies prerendered SSG cache entries into the static-assets directory so
    # the worker can serve them via the staticAssetsIncrementalCache adapter.
    # Cloudflare's CI only runs the build, not deploy, so this step has to be
    # part of the build pipeline rather than relying on `opennextjs-cloudflare
    # deploy` to do it.
    run(["npx", "opennextjs-cloudflare", "populateCache", "local"], cwd=LANDING_DIR)
    return 0


if __name__ == "__main__":
    sys.exit(main())
