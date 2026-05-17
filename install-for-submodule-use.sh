#!/usr/bin/env bash
# Consumer-side convenience. Run this from the directory that contains
# your consumer app's package.json (e.g. websites/myapp/), NOT its
# parent — npm needs to find package.json in the cwd.
#
# When package.json is present, this is equivalent to `npm install`; it
# re-links the file: refs that point into this submodule
# (e.g. file:./vendor/agentic-persona-toolkit/packages/web/packages/<name>).

set -euo pipefail

if [ ! -f "$PWD/package.json" ]; then
  echo "error: no package.json in $PWD" >&2
  echo "       Run this from the directory that contains your consumer app's" >&2
  echo "       package.json (e.g. websites/myapp/), not its parent." >&2
  exit 1
fi

echo "==> Running 'npm install' in $PWD"
npm install
