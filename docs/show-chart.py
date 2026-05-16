#!/usr/bin/env python3
"""Render a mermaid `.mmd` file to SVG and open it in Brave."""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} NAME", file=sys.stderr)
        return 1

    name = sys.argv[1]
    src = Path(f"{name}.mmd")
    out = Path(f"{name}.svg")
    puppeteer_config = Path(os.path.expanduser("~/.puppeteer-config.json"))

    subprocess.run(
        ["mmdc", "-i", str(src), "-o", str(out), "-p", str(puppeteer_config)],
        check=True,
    )
    subprocess.run(["open", str(out), "-a", "Brave Browser"], check=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
