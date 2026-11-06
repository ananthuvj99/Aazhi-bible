# AAZHI production bible — how every session works

This repo is the shared memory for AAZHI (ആഴി), a Techjays Originals AI-made Malayalam film set on the Alappad coast in a Latin Catholic fishing community (1998–2026). Three creators work from it, all directly on `main`: there is no approval step — every creator's Claude pulls the latest `main` before writing and pushes to `main` after every piece of feedback (see `rules/workflow.md`). The video model remembers nothing between generations, so everything that must stay the same lives here.

## Start of every session

A hook in `.claude/settings.json` runs automatically when the session opens: it fetches and updates `main` and prints the latest activity. If that output isn't in the session, run `git fetch --all --prune`, `bash tools/pending.sh` and `bash tools/activity.sh` yourself.

1. Find out who you are working with: their name is `git config user.name`. If it isn't set, ask for their name and set it with `git config user.name "<Name>"`. Every asset and learning from this session is credited to that person.
2. Stay on `main` and run `git pull --rebase`. No personal branches.
3. Read `INDEX.md`: every character look, location, plate, prop and scale sheet, with ID, folder, creator and status.
4. Read `learnings/INDEX.md`, `rules/prompt-rules.md` and `rules/pre-delivery-checklist.md`.
5. For the scene being worked on, read its panels in `storyboard/aazhi-storyboard.md`, its ledger in `continuity/` and the approved frames of the previous shot in `scenes/<scene>/<shot>/approved/`.
6. Tell the creator what changed since their last session, from the hook's output.

## The loop for every shot

**Before every breakdown and every prompt**, run `git pull --rebase` on `main` so you have everyone's latest assets and lessons, and apply them.

1. **Brief.** The creator describes the scene and attaches references.
2. **Breakdown.** Run the `aazhi-scene-breakdown` skill: shot by shot, every reference to call, what is missing, the lessons that apply, and questions. Reuse any asset in `INDEX.md`, whoever made it.
3. **Assets.** Make missing plates or start frames through the Higgsfield MCP, named by the rules below. Show them; save them only after the creator approves (folder, card, `INDEX.md` row). Tell the creator to upload each new image to the platform under exactly its ID.
4. **Base prompt.** Write it from the breakdown, the cards and the rules, following the `seedance-2-5-prompt-writer` skill.
5. **Checks.** Run `aazhi-continuity-director`, then `aazhi-prompt-qa`. Fix small issues yourself for at most two rounds; ask about anything bigger (see Approval).
6. **Deliver.** One copyable code block with the final prompt, then: the IDs to attach (each with shot and mode), the settings (duration, aspect ratio, dialogue language Malayalam) and the QA score.
7. **Feedback.** Bad take: log a lesson. Good take: log a win. Save the approved first and last frames in `scenes/<scene>/<shot>/approved/`.
8. **Next shot.** Ask for the last frame of the approved take. Without one, propose positions from the room's `topview.png` and `cameras.md`, and offer a start frame.

## Adding a character, location, prop or plate

Whenever a creator gives you a new character sheet, or you make any new asset:

1. Check `INDEX.md` first. If it already exists, use it and say who made it. Never make a second version; a new costume or state is a new look with its own ID.
2. Make its folder: `characters/<id>/` (one folder per look), `locations/<name>/`, `props/<id>/`, or `locations/<name>/plates/` for plates.
3. Save the image: `sheet.png` for a character, `clean.png` for a location, `<camera>-plate.png` for a plate, `prop.png` for a prop.
4. Write `card.md` from `templates/` with `created_by` set to the creator in this session (never to whoever made the template), `created` (date) and `status: approved` once the creator approves the image.
5. Add its row to `INDEX.md` in the same commit. A folder without an index row, or a row without a folder, is incomplete.
6. Commit and push to `main` straight away (pull --rebase first).

## Learnings from every creator

- **Bad take** → a file in `learnings/lessons/` from `templates/learning.md` (type `lesson`), a row in `learnings/INDEX.md`, and a line in `rules/pre-delivery-checklist.md`.
- **Good take** → a file in `learnings/wins/` (type `win`) that records the recipe, and a row in `learnings/INDEX.md`.
- Always fill author with the creator who reported the take in this session (from `git config user.name`), plus shot, category and date. The same name goes in the `learnings/INDEX.md` row. After a fresh pull, name new files with the next free number (e.g. `L062-<slug>.md`) and push straight away; if someone took that number first, renumber to the next free one.
- Apply every new lesson to all later prompts with the same situation, not only the shot that failed.
- Categories: position, elements, characters, sizes, angles, in-frame, dialogue, timing, light, platform.

## Approval

**Claude fixes alone, then says what it changed:** rewording to follow an existing rule; adding an ID that already exists in `INDEX.md`; removing a word that names something off screen; adding holds, the dialogue block or the duration line; saving a lesson that only adds a check.

**Claude asks the creator first:** any change to approved dialogue; changing the action, cast, camera position or scene emotion; a new or replaced image, plate or ID; changing or removing an existing rule; anything still flagged after two automatic rounds.

**No merge approval.** After the creator's feedback, push to `main` in the same turn: `git pull --rebase`, then `git push`; never force-push; when a rebase conflicts keep both sides and never delete someone else's line. Changing or removing an existing rule, or editing someone else's approved shot, still needs that creator (or Ananthu) to agree in the conversation first. Commit messages start with the creator's name.

## Naming

A camera position belongs to its location, not to a scene. `antonyroom-c1-top` is the same spot in every scene; a new location starts at C1. Never renumber; a new spot takes the next number. The view word is only a reminder.

| What | File name | Platform ID |
|---|---|---|
| Camera position | `antonyroom-c1-top` | not uploaded |
| Plate | `antonyroom-c1-plate` | `@antonyroomc1plate` |
| Plate, other time of day | `antonyroom-c1-plate-night` | `@antonyroomc1platenight` |
| Top view | `locations/antony-room/topview.png` | never attached |
| Shot | `s01-sh02-v3` | not uploaded |
| Start frame | `s01-sh02-start` | `@s01sh02start` |
| Approved frames | `s01-sh02-first`, `s01-sh02-last` | `@s01sh02last` |
| Character look | `characters/antonyhome/` | `@antonyhome` |
| Scale sheet | `scale-antony-door` | `@scaleantonydoor` |

Platform IDs have no hyphens or underscores. Never print a name inside an image.

## Prompt rules (always)

- Dialogue in Malayalam script only, with no English paraphrase or romanised copy anywhere in the prompt; dubbing language Malayalam.
- One emotion per scene, from the platform's fixed list, written once. If the mood changes, split the scene.
- While someone speaks, only their face is in frame; the listener gets a separate silent shot and is never behind the speaker. Every prompt with dialogue carries the dialogue block from `rules/prompt-rules.md` word for word.
- Write only what the camera sees: no other rooms, no back-story, no equipment words.
- IDs exactly as in `INDEX.md`, attached only when in frame. Reverse angles name what is behind the person.
- Positions come from the last approved frame; characters start where the dialogue happens; eyes slightly off the lens.
- One camera set-up per generation, 5–8 s, with 2–3 s holds at the start and end.
- Top views and labelled maps are for planning; never attach them.

## Saving: push straight away, one item per commit

- The moment a new asset, lesson, win or shot version is saved, commit it and push it to your own branch, so the other creators see it within seconds.
- One item per commit, so any one of them can be undone alone. The message starts with its type: `asset: Clara's mother (@claramother)`, `lesson: door side flips between angles (L-new-door-side)`, `win: yard staging held (W-new-yard-staging)`, `shot: s03-sh02 v3`, `rule: ...`, `undo: ...`.
- Work only on your own branch and your own shots. Open a pull request to `main` when work is ready for Ananthu.
- Never commit access tokens or API keys. Never force-push or rewrite history.

## Who did what, and undoing it

- **See who pushed what:** `bash tools/activity.sh` lists every change on every branch, newest first, with who, branch, what and a commit code. `bash tools/activity.sh 50 Ranjith` shows one person's last 50. On GitHub, each branch's Commits page shows the same.
- **Undo something not yet merged:** run `git revert <commit code>` on that branch and push. Ananthu can also simply not merge it.
- **Undo something already in `main`:** run `git revert <commit code>` on your own branch, push, and open a pull request for Ananthu. GitHub also has a Revert button on every merged pull request.
- **Delete an asset:** if any shot used its ID, never delete it. Set `status: retired` in its card and its `INDEX.md` row, so old shots still make sense. Remove the folder and row only for an asset no shot ever used, and only with Ananthu's approval.
- **Who may undo what:** anyone can undo their own unmerged work. Undoing someone else's work, or anything in `main`, goes to Ananthu.
- `revert` never erases history: the undo is a new commit, so it can itself be undone.
