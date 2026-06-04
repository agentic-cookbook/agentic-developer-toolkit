#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/packages/web"

command -v node >/dev/null || { echo "error: node is required"; exit 1; }
command -v pnpm >/dev/null || { echo "error: pnpm is required"; exit 1; }

echo "==> Installing workspace deps in packages/web/"
pnpm install

cat <<'EOF'

Workspace ready.

Consumers (the demo, submodule users) read packages from
source — no build step needed. See docs/consuming-as-submodule.md
for the one-time consumer wiring; after that, run your project's
usual install command (`npm install`, `pnpm install`, `yarn`)
from the consumer's package.json dir.

Run tests with:
    cd packages/web && pnpm test

Build dist/ artifacts (only needed for npm publish) with:
    cd packages/web && pnpm build
EOF
