#!/usr/bin/env python3
"""Build entry point for `websites/landing/`.

The landing site depends on workspace packages (`@agentic-persona-toolkit/chat`,
`@agentic-persona-toolkit/themes`) via `file:../../packages/web/packages/*`
references. Those packages publish from their `dist/` outputs, so the workspace
must be installed and built before Next can resolve them. CI runs
`npm clean-install` in this directory only, so we bootstrap the web workspace
here, then hand off to OpenNext.

Locally the same script works: if `pnpm` is on PATH it's used directly; otherwise
we activate it via corepack (bundled with Node 22+).
"""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

LANDING_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = LANDING_DIR.parent.parent
WEB_WORKSPACE_DIR = REPO_ROOT / "packages" / "web"
PNPM_VERSION = "9.15.9"


def run(cmd: list[str], cwd: Path) -> None:
    print(f"==> {' '.join(cmd)}  (cwd={cwd})", flush=True)
    subprocess.run(cmd, cwd=cwd, check=True)


def ensure_pnpm() -> None:
    if shutil.which("pnpm"):
        return
    run(["corepack", "enable"], cwd=REPO_ROOT)
    run(["corepack", "prepare", f"pnpm@{PNPM_VERSION}", "--activate"], cwd=REPO_ROOT)


def main() -> int:
    ensure_pnpm()
    run(["pnpm", "install", "--frozen-lockfile"], cwd=WEB_WORKSPACE_DIR)
    run(["pnpm", "-r", "--workspace-concurrency=1", "run", "build"], cwd=WEB_WORKSPACE_DIR)
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
