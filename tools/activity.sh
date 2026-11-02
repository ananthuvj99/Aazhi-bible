#!/usr/bin/env bash
# Who pushed what, on every branch, newest first.
# Usage: bash tools/activity.sh [number of entries, default 30] [name to filter by]
n="${1:-30}"; who="${2:-}"
cd "$(git rev-parse --show-toplevel)" || exit 1
echo "Activity on all branches (newest first)"
echo "Date and time    | Who | Branch | What | Commit"
args=(--remotes --source --date=format:'%Y-%m-%d %H:%M' --format='%ad | %an | %S | %s | %h' -n "$n")
[ -n "$who" ] && args+=(--author="$who")
git log "${args[@]}" | sed -e 's#| origin/HEAD |#| main |#' -e 's#| origin/#| #'
echo
echo "To undo one of these, give Claude its commit code (the last column)."
