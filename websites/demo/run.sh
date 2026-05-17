#!/usr/bin/env bash
# Run the demo site locally on http://localhost:5175
set -euo pipefail

cd "$(dirname "$0")"

if [ ! -d node_modules ]; then
  echo "Installing demo dependencies..."
  npm install
fi

exec npm run dev
