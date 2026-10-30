# AAZHI production bible

Single source of truth for generating AAZHI / ആഴി shots on the Techjays AI film platform.
Images are the reference sheets; every image has a `card.md` beside it describing exactly what it contains.

## Session start (Claude does this every time)
1. Clone this repo.
2. Read `rules/prompt-rules.md` and `rules/lessons.md` in full.
3. Read `continuity-ledger.md`.
4. For the shot being written, open the card **and view the image** of every character and location it touches.
5. Write the prompt, run the continuity-director review against cards + ledger + previous shot files.

## QA gate (every prompt)
Before any prompt is handed over, run `tools/prompt-qa-SKILL.md`: extract every requirement from the user's messages, trace each into the prompt, flag missing/contradicted/unrequested items, run the checklist, score /100, and ask for approval before applying corrections.

## The learning loop
1. Prompt written → saved as `scenes/<sequence>/<shot>.md` with status `ready`.
2. User generates on the platform and reports back (screenshot of the problem frame + one line).
3. Claude diagnoses the cause, then:
   - adds a numbered entry to `rules/lessons.md` (symptom → cause → rule),
   - fixes the affected card / ledger,
   - revises the prompt, bumps its version, records the result in the shot file,
   - saves the screenshot under `scenes/<sequence>/evidence/`,
   - commits with a message naming the lesson.
4. When a shot is approved, status → `approved`, and its end state is written into `continuity-ledger.md`.

## Template for dialogue generations
`scenes/showreel/2-PART-A.md` (approved, W2): one location, ≤3 shots per 15 s, clean singles + EYELINE, one emotion tag per speaker.

## Layout
```
rules/                 prompt rules, lessons log, platform emotion tag screenshots
characters/<id>/       sheet.png + card.md   (folder name = platform ID without @)
locations/<name>/      clean.png (attach this) + map.png (labelled, never attach) + card.md
scenes/showreel/       plan.md, one file per shot, evidence/
continuity-ledger.md   current state of the story world
```
