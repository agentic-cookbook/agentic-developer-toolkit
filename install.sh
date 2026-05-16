#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/packages/web"

command -v node >/dev/null || { echo "error: node is required"; exit 1; }
command -v pnpm >/dev/null || { echo "error: pnpm is required"; exit 1; }

echo "==> Installing workspace deps in packages/web/"
pnpm install

echo "==> Generating themes/theme-data.ts"
pnpm --filter @agentic-persona-toolkit/themes run build:data

cat <<'EOF'

Workspace ready. Build with:
    cd packages/web && pnpm build

Run tests with:
    cd packages/web && pnpm test
EOF
