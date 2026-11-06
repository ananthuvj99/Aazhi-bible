# Working rule — one shared memory for the whole team

This repo is the team's common memory. Ananthu, Ranjith and Aswanth (and anyone else with write access) work the same way, and every Claude session follows this file. No approval step: everyone pushes straight to `main`.

## 1. Start of every session
- Clone `main` fresh (or `git pull --rebase` if already cloned).
- Read before writing anything: `learnings/INDEX.md` (+ the lesson files that touch this shot), `rules/pre-delivery-checklist.md`, `rules/style-cinema-camera.md`, `continuity/showreel.md`, the shot's file in `scenes/showreel/`, and `INDEX.md` for every ID.

## 2. Writing a prompt
- Build it only from what is on `main` right now. Run the continuity and QA checks before handing it over.
- Save the prompt as a new version in the shot's file and push it.

## 3. After every generation the person comments on — push in the same turn
- Shot file: what came out, status (approved / partial / failed), next version.
- Frames: failures → `scenes/showreel/evidence/`, start/end frames → `scenes/showreel/approved/`.
- Each new lesson or win → its own file in `learnings/lessons/` or `learnings/wins/` + one row in `learnings/INDEX.md` (never `rules/lessons.md`).
- New checklist items, continuity-ledger lines, new IDs in `INDEX.md`.
- Commit message starts with the person's name: `Ranjith: 2-B v3 approved; L62`.

## 4. Pushing safely when three people work at once
- Always `git pull --rebase` immediately before `git push`. Never force-push. Never rewrite history.
- If the rebase conflicts: keep BOTH sides (merge the lines), re-run, push. Never delete someone else's line.
- Lesson/win numbers: after pulling, take the next free number in `learnings/INDEX.md` and push right away. If someone took it first, renumber yours to the next free one.
- Working on the same shot at the same time: add a line under `## Generation results` rather than rewriting the prompt block; the newest pushed version wins.
- After pushing, check that GitHub `main` equals the local commit, and say so.

## 5. Credentials
- Each person uses their OWN fine-grained GitHub token (this repo only, Contents: read and write, with an expiry). Never commit a token or paste someone else's.
