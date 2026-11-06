# AAZHI — team memory (read me first, every session)

This repo is the shared memory of the AAZHI / Techjays Originals film team (Ananthu, Ranjith, Aswanth). Claude Code loads this file automatically; follow it exactly.

## Every session
1. `git pull --rebase` on `main` before anything else.
2. Follow `rules/workflow.md` (how we pull, write prompts, push after feedback, avoid clashes).
3. Before writing any Seedance prompt, read: `learnings/INDEX.md` (+ relevant lesson files), `rules/pre-delivery-checklist.md`, `rules/prompt-rules.md`, `rules/style-cinema-camera.md`, `continuity/showreel.md`, the shot's file in `scenes/showreel/`, and `INDEX.md` for every reference ID.

## Prompts
- Dialogue in Malayalam script only; no English paraphrase; no music; one camera set-up and one speaker per generation; 15 s max.
- Run the continuity check and the QA check (score /100, IDs, request-vs-prompt) before handing a prompt over.

## After the person comments on a generation
Update the shot file, frames (`evidence/` or `approved/`), `learnings/` (one file per lesson + a row in `learnings/INDEX.md`), checklist, continuity ledger and `INDEX.md`; commit with the person's name first; `git pull --rebase` then `git push` to `main`; confirm GitHub matches. Never force-push; never delete someone else's line.
