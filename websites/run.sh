#!/usr/bin/env bash
# Run the landing site locally on http://localhost:5174/demo/chat
set -euo pipefail

root="$(cd "$(dirname "$0")/landing" && pwd)"

if [ ! -d "$root/node_modules" ]; then
  echo "Installing landing dependencies..."
  npm install --prefix "$root"
fi

exec npm run dev --prefix "$root"
