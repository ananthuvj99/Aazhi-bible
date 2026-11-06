# AAZHI production bible

Single source of truth for generating AAZHI / ആഴി shots on the Techjays AI film platform, shared by every creator.

- **How every session works:** `CLAUDE.md` (Claude Code reads it automatically).
- **Every asset, with its ID, creator and status:** `INDEX.md`.
- **Lessons and wins from every creator:** `learnings/INDEX.md`.
- **Prompt rules and the checklist:** `rules/`.
- **Shared agents:** `.claude/skills/`.
- **New creators start here:** `ONBOARDING.md`.
- **Who pushed what, and what's waiting for approval:** `bash tools/activity.sh`, `bash tools/pending.sh`.

## Template for dialogue generations
`scenes/showreel/2-PART-A.md` (approved, W2): one location, at most 3 shots per 15 s, clean singles plus EYELINE, one emotion tag per scene.

## Layout
```
CLAUDE.md                    how every session works
INDEX.md                     every character, location, plate, prop, scale sheet
characters/<id>/             card.md + sheet image, one folder per look
locations/<name>/            card.md, clean image, labelled map (never attach), cameras.md
props/<id>/                  card.md + image
references/scale/            scale sheets
storyboard/                  aazhi-storyboard.md: the full storyboard, 126 panels, approved dialogue
scenes/showreel/             plan.md, one file per shot, retired/, evidence/
continuity/                  one ledger per scene sequence (showreel.md)
learnings/                   INDEX.md, lessons/, wins/
rules/                       prompt rules, checklist, platform emotion tags
asset-requests/              image-generation prompts for assets still to be made
templates/                   cards and learning files to copy
.claude/skills/              the shared agents
```

**Working rule:** every prompt is written from `main`; every result Ananthu comments on is pushed to `main`. See `rules/workflow.md`.
