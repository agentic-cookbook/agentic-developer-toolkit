#!/usr/bin/env python3
"""Regenerate the typed OpenAPI client into Sources/Generated/.

Manual-generate-and-commit workflow (the generated output is committed, NOT
produced by a per-build SwiftPM plugin — those are unreliable inside an
XcodeGen .xcodeproj). This script:

  1. Ensures a pinned checkout of apple/swift-openapi-generator under .tooling/
     (cloned on demand; .tooling/ is gitignored).
  2. Runs the generator against the spec using openapi-generator-config.yaml,
     emitting Client.swift + Types.swift into Sources/Generated/.

Pass --spec <path> to generate from a freshly-dumped local spec (the parent
orchestrator uses this). The spec is copied into ROOT/openapi.json first,
refreshing the committed snapshot.

Refresh the spec snapshot from the live backend:
    python3 scripts/generate.py --refresh-spec

Usage:
    python3 scripts/generate.py [--spec <path>] [--refresh-spec]
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

GENERATOR_REPO = "https://github.com/apple/swift-openapi-generator"
GENERATOR_VERSION = "1.12.2"
# The machine-readable spec is served by the Scalar docs site, not the API host
# (the API host returns 404 for /openapi.json). The runtime API itself lives at
# https://api.agenticdeveloperstorage.com — see DaemonContract.backendURL.
SPEC_URL = "https://apidocs.agenticdeveloperstorage.com/openapi.json"

ROOT = Path(__file__).resolve().parent.parent
TOOLING = ROOT / ".tooling" / "swift-openapi-generator"
SPEC = ROOT / "openapi.json"
CONFIG = ROOT / "openapi-generator-config.yaml"
OUTPUT = ROOT / "Sources" / "Generated"


def run(cmd: list[str], cwd: Path | None = None) -> None:
    print(f"$ {' '.join(cmd)}")
    subprocess.run(cmd, cwd=cwd, check=True)


def refresh_spec() -> None:
    print(f"Fetching {SPEC_URL} -> {SPEC}")
    with urllib.request.urlopen(SPEC_URL, timeout=30) as resp:
        SPEC.write_bytes(resp.read())
    print(f"  wrote {SPEC.stat().st_size} bytes")


def ensure_generator() -> None:
    """Clone the pinned generator if absent; otherwise pin it to the tag."""
    if not TOOLING.exists():
        TOOLING.parent.mkdir(parents=True, exist_ok=True)
        run([
            "git", "clone", "--depth", "1",
            "--branch", GENERATOR_VERSION,
            GENERATOR_REPO, str(TOOLING),
        ])
        return
    # Already cloned — make sure it's at the pinned tag.
    describe = subprocess.run(
        ["git", "describe", "--tags", "--exact-match"],
        cwd=TOOLING, capture_output=True, text=True,
    )
    if describe.stdout.strip() != GENERATOR_VERSION:
        run(["git", "fetch", "--depth", "1", "origin", "tag", GENERATOR_VERSION], cwd=TOOLING)
        run(["git", "checkout", GENERATOR_VERSION], cwd=TOOLING)


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--spec",
        help="path to an OpenAPI spec to generate from; refreshes the committed "
             "openapi.json snapshot. Omit to use the existing snapshot.",
    )
    parser.add_argument(
        "--refresh-spec", action="store_true",
        help="re-download openapi.json from the live backend before generating",
    )
    return parser.parse_args(argv)


def resolve_spec(args) -> Path:
    """Decide which spec to generate from and ensure SPEC holds it."""
    if args.spec:
        shutil.copyfile(args.spec, SPEC)
    elif args.refresh_spec:
        refresh_spec()
    if not SPEC.exists():
        sys.exit(f"Missing spec snapshot {SPEC}. Pass --spec or --refresh-spec.")
    return SPEC


def generate() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    run([
        "swift", "run",
        "--package-path", str(TOOLING),
        "swift-openapi-generator", "generate",
        str(SPEC),
        "--config", str(CONFIG),
        "--output-directory", str(OUTPUT),
    ])
    print(f"\nGenerated sources in {OUTPUT}:")
    for f in sorted(OUTPUT.glob("*.swift")):
        print(f"  {f.name}  ({f.stat().st_size:,} bytes)")


def main() -> None:
    args = parse_args()
    resolve_spec(args)
    ensure_generator()
    generate()


if __name__ == "__main__":
    main()
