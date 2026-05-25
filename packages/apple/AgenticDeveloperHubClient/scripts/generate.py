#!/usr/bin/env python3
"""Regenerate the typed OpenAPI client into Sources/Generated/.

Manual-generate-and-commit workflow (the generated output is committed, NOT
produced by a per-build SwiftPM plugin — those are unreliable inside an
XcodeGen .xcodeproj). This script:

  1. Ensures a pinned checkout of apple/swift-openapi-generator under .tooling/
     (cloned on demand; .tooling/ is gitignored).
  2. Patches a working copy of the spec to work around two invalid constructs
     emitted by the backend's runtime OpenAPI generator (smiley4 ktor-openapi);
     see patch_spec(). The committed openapi.json stays the pristine upstream
     snapshot — patches are applied only to a temp copy at generate time.
  3. Runs the generator against the patched copy using
     openapi-generator-config.yaml, emitting Client.swift + Types.swift into
     Sources/Generated/.

Refresh the spec snapshot first when the backend changes:
    python3 scripts/generate.py --refresh-spec

Usage:
    python3 scripts/generate.py [--refresh-spec]
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

GENERATOR_REPO = "https://github.com/apple/swift-openapi-generator"
GENERATOR_VERSION = "1.12.2"
SPEC_URL = "https://api.agenticdeveloperhub.com/openapi.json"

ROOT = Path(__file__).resolve().parent.parent
TOOLING = ROOT / ".tooling" / "swift-openapi-generator"
SPEC = ROOT / "openapi.json"
PATCHED_SPEC = ROOT / ".tooling" / "openapi.patched.json"
CONFIG = ROOT / "openapi-generator-config.yaml"
OUTPUT = ROOT / "Sources" / "Generated"

HTTP_METHODS = {"get", "post", "put", "patch", "delete", "head", "options", "trace"}
PATH_PLACEHOLDER = re.compile(r"\{([^}]+)\}")


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


def patch_spec(doc: dict) -> dict:
    """Work around invalid constructs the backend's OpenAPI generator emits.

    The backend uses smiley4 ktor-openapi, which produces two things that
    OpenAPIKit (and therefore swift-openapi-generator) rejects outright:

    1. ``{"$ref": "*"}`` — a placeholder for "any JSON value" used inside the
       recursive kotlinx JsonElement/JsonObject/JsonArray schemas. ``*`` is not
       a resolvable JSON Reference, so we replace each occurrence with ``{}``,
       the OpenAPI spelling for a free-form value (maps to a free-form container
       in the generated Swift).
    2. Operations with an empty ``responses`` object (a handful of MCP and
       websocket routes). OpenAPIKit requires at least one response, so we inject
       a synthetic ``default`` response describing it as undocumented upstream.
    3. Path templates with ``{placeholders}`` that are never declared as path
       parameters (the generator omits them across ~80 operations). We inject a
       string-typed path parameter at the path-item level for each missing one.
    """
    refs = [0]

    def walk(node):
        if isinstance(node, dict):
            if node.get("$ref") == "*":
                refs[0] += 1
                return {}  # free-form JSON value
            return {k: walk(v) for k, v in node.items()}
        if isinstance(node, list):
            return [walk(x) for x in node]
        return node

    doc = walk(doc)

    patched_responses = 0
    for path_item in doc.get("paths", {}).values():
        if not isinstance(path_item, dict):
            continue
        for method, operation in path_item.items():
            if method not in HTTP_METHODS or not isinstance(operation, dict):
                continue
            if not operation.get("responses"):
                operation["responses"] = {
                    "default": {
                        "description": "Undocumented response "
                        "(synthesized by generate.py — upstream spec omitted responses).",
                    }
                }
                patched_responses += 1

    comp_params = doc.get("components", {}).get("parameters", {})

    def declared_path_params(params) -> set:
        names = set()
        for p in params or []:
            if not isinstance(p, dict):
                continue
            if "$ref" in p:
                target = comp_params.get(p["$ref"].split("/")[-1], {})
                if target.get("in") == "path":
                    names.add(target.get("name"))
            elif p.get("in") == "path":
                names.add(p.get("name"))
        return names

    added_path_params = 0
    for path, item in doc.get("paths", {}).items():
        if not isinstance(item, dict):
            continue
        placeholders = set(PATH_PLACEHOLDER.findall(path))
        if not placeholders:
            continue
        declared = declared_path_params(item.get("parameters"))
        for method, operation in item.items():
            if method in HTTP_METHODS and isinstance(operation, dict):
                declared |= declared_path_params(operation.get("parameters"))
        for name in sorted(placeholders - declared):
            item.setdefault("parameters", []).append({
                "name": name, "in": "path", "required": True,
                "schema": {"type": "string"},
            })
            added_path_params += 1

    print(f"  patched {refs[0]} invalid '$ref: *' nodes -> free-form value")
    print(f"  patched {patched_responses} operations missing responses")
    print(f"  added {added_path_params} undeclared path parameters")
    return doc


def generate() -> None:
    if not SPEC.exists():
        sys.exit(f"Missing spec snapshot {SPEC}. Run with --refresh-spec first.")
    print(f"Patching working copy of {SPEC.name}:")
    doc = json.loads(SPEC.read_text())
    PATCHED_SPEC.parent.mkdir(parents=True, exist_ok=True)
    PATCHED_SPEC.write_text(json.dumps(patch_spec(doc)))
    OUTPUT.mkdir(parents=True, exist_ok=True)
    run([
        "swift", "run",
        "--package-path", str(TOOLING),
        "swift-openapi-generator", "generate",
        str(PATCHED_SPEC),
        "--config", str(CONFIG),
        "--output-directory", str(OUTPUT),
    ])
    print(f"\nGenerated sources in {OUTPUT}:")
    for f in sorted(OUTPUT.glob("*.swift")):
        print(f"  {f.name}  ({f.stat().st_size:,} bytes)")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--refresh-spec", action="store_true",
        help="re-download openapi.json from the live backend before generating",
    )
    args = parser.parse_args()

    if args.refresh_spec:
        refresh_spec()
    ensure_generator()
    generate()


if __name__ == "__main__":
    main()
