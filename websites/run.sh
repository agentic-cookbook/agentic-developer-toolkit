#!/usr/bin/env bash
# Run the demo site locally on http://localhost:6006/chat
set -euo pipefail

root="$(cd "$(dirname "$0")/demo" && pwd)"

if [ ! -d "$root/node_modules" ]; then
  echo "Installing demo dependencies..."
  npm install --prefix "$root"
fi

exec npm run dev --prefix "$root"
