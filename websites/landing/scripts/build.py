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

import os
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


def pnpm_major() -> int | None:
    pnpm = shutil.which("pnpm")
    if not pnpm:
        return None
    result = subprocess.run([pnpm, "--version"], capture_output=True, text=True)
    try:
        return int(result.stdout.strip().split(".")[0])
    except (ValueError, IndexError):
        return None


def main() -> int:
    # Unset NODE_ENV so pnpm installs devDependencies (needed for @types/react etc.)
    env = {k: v for k, v in os.environ.items() if k != "NODE_ENV"}
    cmd = (
        ["pnpm", "install", "--frozen-lockfile"]
        if (pnpm_major() or 0) >= 9
        else ["npx", "--yes", "pnpm@9.15.9", "install", "--frozen-lockfile"]
    )
    print(f"==> {' '.join(cmd)}  (cwd={WEB_WORKSPACE})", flush=True)
    subprocess.run(cmd, cwd=WEB_WORKSPACE, check=True, env=env)
    run(["npm", "run", "build:next"], cwd=LANDING_DIR)
    return 0


if __name__ == "__main__":
    sys.exit(main())
