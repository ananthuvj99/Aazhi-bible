#!/usr/bin/env bash
# Assets and learnings on other creators' branches that are not in main yet.
cd "$(git rev-parse --show-toplevel)" || exit 1
paths=(INDEX.md characters locations props references/scale learnings rules)
found=0
for ref in $(git for-each-ref --format='%(refname:short)' refs/remotes/origin | grep -v -E '^origin(/HEAD|/main)?$'); do
  changes=$(git diff --name-status origin/main..."$ref" -- "${paths[@]}" 2>/dev/null)
  [ -z "$changes" ] && continue
  found=1
  who=$(git log -1 --format='%an' "$ref")
  echo "Waiting for approval on ${ref#origin/} (last push by $who):"
  echo "$changes" | sed -e 's/^A\t/  added    /' -e 's/^M\t/  changed  /' -e 's/^D\t/  deleted  /' -e 's/^R[0-9]*\t/  moved    /'
done
[ "$found" = 0 ] && echo "Nothing waiting for approval: every branch's assets and learnings are already in main."
exit 0
