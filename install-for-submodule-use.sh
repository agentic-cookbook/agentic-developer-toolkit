#!/usr/bin/env bash
# Thin entry point for the consumer-side install. See install-for-submodule-use.py
# for the full documentation. Run from a consumer repo that embeds this
# toolkit as a git submodule:
#
#   ./vendor/apt/install-for-submodule-use.sh                # consumer at cwd
#   ./vendor/apt/install-for-submodule-use.sh sites/main     # monorepo path
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
exec python3 "$SCRIPT_DIR/install-for-submodule-use.py" "$@"
