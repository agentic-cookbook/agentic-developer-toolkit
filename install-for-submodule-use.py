#!/usr/bin/env python3
"""Wire @agentic-persona-toolkit/* packages into a consumer site that embeds
this toolkit as a git submodule.

Run from the consumer repo, after `git submodule add ... vendor/apt`:

    ./vendor/apt/install-for-submodule-use.sh                 # consumer at cwd
    ./vendor/apt/install-for-submodule-use.sh sites/main      # monorepo path

Idempotent. Re-run any time the toolkit adds a new package (after
`git submodule update --remote vendor/apt`); the script discovers new
packages and re-wires them.

Steps:
  1. Discover packages in <toolkit>/packages/web/packages/* whose
     package.json declares an @agentic-persona-toolkit/* name.
  2. Update the consumer's package.json dependencies with `file:` refs
     pointing at the correct relative path.
  3. Update the consumer's next.config.{ts,mjs,js,cjs} so each toolkit
     package name appears in `transpilePackages`. If the config has no
     `transpilePackages` field, prints the lines to add manually.
  4. Run the consumer's package manager (pnpm / yarn / npm, auto-detected)
     to refresh the file: symlinks.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

TOOLKIT_ROOT = Path(__file__).resolve().parent
WEB_PACKAGES_DIR = TOOLKIT_ROOT / "packages" / "web" / "packages"
NEXT_CONFIG_CANDIDATES = ("next.config.ts", "next.config.mjs", "next.config.js", "next.config.cjs")


def discover_packages() -> list[tuple[str, Path]]:
    if not WEB_PACKAGES_DIR.is_dir():
        sys.exit(f"error: toolkit packages dir not found: {WEB_PACKAGES_DIR}")
    found: list[tuple[str, Path]] = []
    for pkg_dir in sorted(WEB_PACKAGES_DIR.iterdir()):
        pkg_json = pkg_dir / "package.json"
        if not pkg_json.is_file():
            continue
        data = json.loads(pkg_json.read_text())
        name = data.get("name", "")
        if name.startswith("@agentic-persona-toolkit/"):
            found.append((name, pkg_dir))
    return found


def update_package_json(consumer_dir: Path, packages: list[tuple[str, Path]]) -> bool:
    pkg_json_path = consumer_dir / "package.json"
    if not pkg_json_path.is_file():
        sys.exit(f"error: {pkg_json_path} not found")

    raw = pkg_json_path.read_text()
    data = json.loads(raw)
    deps = data.setdefault("dependencies", {})

    changed = False
    for name, pkg_dir in packages:
        rel = Path(os.path.relpath(pkg_dir, consumer_dir)).as_posix()
        wanted = f"file:{rel}"
        current = deps.get(name)
        if current != wanted:
            arrow = "(new)" if current is None else current
            print(f"  {name}: {arrow} -> {wanted}")
            deps[name] = wanted
            changed = True

    if changed:
        pkg_json_path.write_text(json.dumps(data, indent=2) + "\n")
    return changed


def find_next_config(consumer_dir: Path) -> Path | None:
    for name in NEXT_CONFIG_CANDIDATES:
        path = consumer_dir / name
        if path.is_file():
            return path
    return None


def update_next_config(consumer_dir: Path, package_names: list[str]) -> None:
    config_path = find_next_config(consumer_dir)
    if config_path is None:
        print("  no next.config.* found — skipping (not a Next.js consumer?)")
        return

    text = config_path.read_text()
    array_re = re.compile(r"transpilePackages\s*:\s*\[([^\]]*)\]", re.DOTALL)
    match = array_re.search(text)

    if match is None:
        print(f"  WARNING: no `transpilePackages` field in {config_path.name}.")
        print("  Add this to your Next config:")
        print()
        print("    transpilePackages: [")
        for n in package_names:
            print(f'      "{n}",')
        print("    ],")
        print()
        return

    existing = re.findall(r"""['"]([^'"]+)['"]""", match.group(1))
    merged = list(dict.fromkeys(existing + package_names))
    if merged == existing:
        return

    new_inner = "\n    " + ",\n    ".join(f'"{n}"' for n in merged) + ",\n  "
    new_text = text[: match.start()] + f"transpilePackages: [{new_inner}]" + text[match.end() :]
    config_path.write_text(new_text)
    added = [n for n in merged if n not in existing]
    print(f"  added to transpilePackages in {config_path.name}: {', '.join(added)}")


def detect_package_manager(consumer_dir: Path) -> str:
    if (consumer_dir / "pnpm-lock.yaml").is_file():
        return "pnpm"
    if (consumer_dir / "yarn.lock").is_file():
        return "yarn"
    return "npm"


def run_install(consumer_dir: Path) -> None:
    pm = detect_package_manager(consumer_dir)
    if shutil.which(pm) is None:
        sys.exit(f"error: detected '{pm}' as the consumer's package manager but it's not on PATH")
    print(f"==> {pm} install  (cwd={consumer_dir})")
    subprocess.run([pm, "install"], cwd=consumer_dir, check=True)


def main(argv: list[str]) -> int:
    if len(argv) > 2 or (len(argv) == 2 and argv[1] in {"-h", "--help"}):
        print(__doc__)
        return 0 if len(argv) == 2 and argv[1] in {"-h", "--help"} else 2

    consumer_dir = Path(argv[1] if len(argv) == 2 else ".").resolve()
    if not consumer_dir.is_dir():
        sys.exit(f"error: {consumer_dir} is not a directory")

    packages = discover_packages()
    if not packages:
        sys.exit(f"error: no @agentic-persona-toolkit/* packages found under {WEB_PACKAGES_DIR}")

    print(f"Toolkit:  {TOOLKIT_ROOT}")
    print(f"Consumer: {consumer_dir}")
    print(f"Packages: {', '.join(name for name, _ in packages)}")
    print()

    print("==> package.json")
    if not update_package_json(consumer_dir, packages):
        print("  (already up to date)")
    print()

    print("==> next.config.*")
    update_next_config(consumer_dir, [n for n, _ in packages])
    print()

    run_install(consumer_dir)
    print()
    print("Done. Toolkit packages are symlinked from source — edit them in")
    print(f"  {TOOLKIT_ROOT}/packages/web/packages/<name>/src/")
    print("and your consumer's `next dev` will pick up changes via HMR.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
