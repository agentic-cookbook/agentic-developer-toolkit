#!/usr/bin/env python3
"""Build entry point for `websites/landing/`.

The landing site consumes `@agentic-persona-toolkit/*` packages from source via
their `file:` references and Next.js's `transpilePackages`. No workspace build
step is required — Next compiles the symlinked TS/TSX during `next build`.

This script just runs the OpenNext Cloudflare build and populates the cache.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

LANDING_DIR = Path(__file__).resolve().parent.parent


def run(cmd: list[str], cwd: Path) -> None:
    print(f"==> {' '.join(cmd)}  (cwd={cwd})", flush=True)
    subprocess.run(cmd, cwd=cwd, check=True)


def main() -> int:
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
