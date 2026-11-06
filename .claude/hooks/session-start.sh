#!/usr/bin/env bash
# Runs automatically when a Claude Code session opens in this repo.
# Updates main (everyone works on main) and shows what changed.
cd "${CLAUDE_PROJECT_DIR:-.}" || exit 0
if ! git fetch --all --prune --quiet 2>/dev/null; then
  echo "AAZHI: could not reach GitHub, so this session works from the local copy. Run 'git fetch --all' when online."
  exit 0
fi
branch=$(git branch --show-current)
if [ "$(git config --get aazhi.ownbranch)" = "true" ] && [ -n "$branch" ] && [ "$branch" != "main" ]; then
  # Own-branch mode: this creator works on their own branch; their personal sync hook
  # merges main into it and pushes it into main. Leave the branch as it is.
  echo "AAZHI: own-branch mode on '$branch' (synced with main both ways by the personal hook)."
else
  if [ "$branch" != "main" ]; then
    echo "AAZHI: switching to main (everyone works on main now)."
    git switch main --quiet 2>/dev/null
    branch=main
  fi
  git pull --rebase --quiet 2>/dev/null
fi
echo "AAZHI session: $(git config user.name 2>/dev/null || echo 'name not set') on branch $branch"
echo
bash tools/pending.sh
echo
bash tools/activity.sh 10
exit 0
