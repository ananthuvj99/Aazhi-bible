#!/usr/bin/env bash
# Runs automatically when a Claude Code session opens in this repo.
# Fetches every creator's branch, updates main, and shows what changed.
cd "${CLAUDE_PROJECT_DIR:-.}" || exit 0
if ! git fetch --all --prune --quiet 2>/dev/null; then
  echo "AAZHI: could not reach GitHub, so this session works from the local copy. Run 'git fetch --all' when online."
  exit 0
fi
branch=$(git branch --show-current)
if [ "$branch" = "main" ]; then
  git pull --ff-only --quiet 2>/dev/null
else
  git fetch origin main:main --quiet 2>/dev/null
fi
echo "AAZHI session: $(git config user.name 2>/dev/null || echo 'name not set') on branch $branch"
echo
bash tools/pending.sh
echo
bash tools/activity.sh 10
exit 0
