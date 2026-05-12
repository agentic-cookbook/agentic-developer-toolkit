#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/packaging"

command -v node >/dev/null || { echo "error: node is required"; exit 1; }
command -v pnpm >/dev/null || { echo "error: pnpm is required"; exit 1; }

echo "==> Installing workspace deps from packaging/"
pnpm install

echo "==> Generating themes/theme-data.ts"
pnpm --filter @agentic-persona-toolkit/themes run build:data

cat <<'EOF'

Workspace ready. Build with:
    cd packaging && pnpm build

Run tests with:
    cd packaging && pnpm test
EOF
