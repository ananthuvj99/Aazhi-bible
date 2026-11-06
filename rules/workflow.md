# Working rule (Ananthu, 2026-11-06)

## Before writing any prompt
1. Pull the latest `main` (clone it fresh in a new session).
2. Read: `learnings/INDEX.md` (+ the relevant lesson files), `rules/pre-delivery-checklist.md`, `rules/style-cinema-camera.md`, `continuity/showreel.md`, the shot's file in `scenes/showreel/`, and `INDEX.md` for every ID.
3. Write the prompt from what is on `main`, then run the continuity and QA checks before handing it over.

## After every generation Ananthu comments on
Commit and push to `main` in the same turn:
- the shot file: result notes, status (approved / partial / failed) and the new version;
- evidence frames (`scenes/showreel/evidence/`) for failures, approved frames (`scenes/showreel/approved/`) for start/end frames;
- each new lesson or win as its own file in `learnings/lessons/` or `learnings/wins/`, plus a row in `learnings/INDEX.md` (never `rules/lessons.md`);
- new checklist items, continuity-ledger lines and new IDs in `INDEX.md`.
Then confirm that GitHub `main` matches.
