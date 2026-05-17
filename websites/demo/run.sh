#!/usr/bin/env bash
# Run the demo site locally on http://localhost:5175
set -euo pipefail

cd "$(dirname "$0")"

REPO_ROOT="$(cd ../.. && pwd)"
CHAT_DIST="$REPO_ROOT/packages/web/packages/chat/dist"
THEMES_DIST="$REPO_ROOT/packages/web/packages/themes/dist"

if [ ! -d "$CHAT_DIST" ] || [ ! -d "$THEMES_DIST" ]; then
  echo "error: chat/themes packages are not built." >&2
  echo "" >&2
  echo "Bootstrap the workspace first:" >&2
  echo "  cd $REPO_ROOT && ./install.sh" >&2
  echo "  cd $REPO_ROOT/packages/web && pnpm build" >&2
  exit 1
fi

if [ ! -d node_modules ]; then
  echo "Installing demo dependencies..."
  npm install
fi

exec npm run dev
