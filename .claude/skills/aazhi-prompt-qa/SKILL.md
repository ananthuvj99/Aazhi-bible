---
name: "aazhi-prompt-qa"
description: Request-vs-prompt and reference-ID QA gate for AAZHI / Techjays film-platform video prompts. Use after EVERY scene prompt is drafted for AAZHI or the Techjays showreel — before it is handed to the user — and whenever the user asks "does this prompt have everything I asked", "check the prompt", "score this prompt", "will this generate well", or pastes a prompt and a request together. It extracts every requirement from the user's messages, proves each one is in the prompt, checks every needed reference ID against the repo registry (including backgrounds seen behind characters and through doors) and adds missing ones, finds contradictions and risky additions, runs the generation-risk checklist, gives a score out of 100 with a short summary, and asks the user to approve corrections before rewriting. Trigger even if the user does not ask, whenever a new or revised AAZHI prompt is about to be delivered.
---

# AAZHI Prompt QA — "did the prompt get everything I asked?"

The user generates on a paid platform. A wasted generation costs time and money. Your job is to stop a bad prompt **before** it reaches the platform.

You audit two things against each other:
- **INPUT** — what the user asked for: their latest message, plus every still-valid instruction from earlier in the conversation (dialogue they approved, corrections they made, standing rules).
- **OUTPUT** — the prompt that was drafted.

Run this after every prompt draft, unprompted. Never deliver a prompt without the QA block.

## Step 1 — Extract requirements (INPUT)

Read the user's latest message and the conversation since the shot was first discussed. List every requirement as a short, checkable line, tagged by source:

- **[NOW]** asked in the latest message
- **[EARLIER]** asked earlier for this shot and not withdrawn
- **[STANDING]** project rules (repo `rules/prompt-rules.md`, `rules/pre-delivery-checklist.md`, saved preferences): Malayalam-only dialogue, one emotion tag per scene from the platform's fixed list, lip-sync block verbatim, sound effects only, holds, IDs exactly as registered, scoped prompts, etc.
- **[APPROVED]** exact dialogue the user confirmed — the Malayalam must match character for character.

Split compound asks: "mother in the passage, Antony comes out of his room, veranda behind him" is three requirements. Include negative asks ("no clock", "don't throw the spoon"). Dictated messages are messy — resolve the intended meaning, and if a requirement is genuinely ambiguous, list it as **[UNCLEAR]** and ask.

## Step 2 — Trace each requirement into the prompt (OUTPUT)

For each requirement, find the exact place in the prompt that satisfies it and mark:
- ✅ **Met** — quote the block name (e.g. "FIRST FRAME", "Shot 2 LOCATION").
- ⚠️ **Partial / weak** — present but easy for the model to ignore (said once, buried, contradicted elsewhere, no timing).
- ❌ **Missing** — not in the prompt.
- 🔁 **Contradicted** — the prompt says something that conflicts with it.

## Step 2b — Reference-ID audit (always)

Use the AAZHI bible repo (in Claude Code it is the current folder; pull main first. In claude.ai, clone github.com/ananthuvj99/Aazhi-bible with the token the user supplies). Run `git fetch --all --prune` and `bash tools/pending.sh` first. Read `INDEX.md`, the list of every registered ID from every creator, with its folder; then each needed asset's `card.md` (what it shows, when to attach it, its mode, never-pair rules) and the location's `cameras.md`, which holds the **sight-lines** of what is visible behind or through each camera position. If an asset the shot needs is not in `INDEX.md`, check the other creators' open branches or pull requests before calling it missing. Look at the character and location sheet images in the repo when a choice depends on what a sheet actually shows.

Then, shot by shot:
1. List every person, place, prop and **background** the prompt puts in frame — including what is behind each person in reverse angles and what is seen through doors and windows (use the sight-lines table; this is how a missing veranda behind Antony gets caught).
2. From `INDEX.md` and the cards, derive the IDs each shot needs, with mode (full / background-only) and shot scope.
3. Compare with ACTIVE REFERENCES and mark: ✅ present · ❌ missing (add it) · ⛔ wrong (off-screen, wrong costume variant such as @antonyhome after he dressed, a room a character must leave — L31) · ✏️ misspelled (must match the registry exactly).
4. Write the corrected ACTIVE REFERENCES lines, each with scope and mode, ready to paste — and note the matching LOCATION / background text each one needs so the prompt and the references agree.
5. Mapped (labelled) sheets: suggest only as an option the user chooses, with the label-print warning.

## Step 3 — Find what the user did NOT ask for

Flag anything the prompt adds that could change the result: new props, new dialogue or changed wording, new rooms, moods, camera moves, timing changes, removed beats. Additions are allowed only if they serve a stated requirement or a standing rule — otherwise list them as **Unrequested**.

## Step 4 — Generation-risk scan

Run the repo checklist (`rules/pre-delivery-checklist.md`) and the lessons and wins in `learnings/INDEX.md`, from every creator. At minimum check: start positions (characters begin where the dialogue happens), single location per dialogue shot, references tied to shots and only for things on screen or framing the shot, reverse-angle backgrounds named, nothing off-screen named (word scan, including hidden words like "o'clock"), no English paraphrase of any line, Malayalam lock in five places, one speaker per cut in MCU with face to lens, exactly one valid scene emotion, lines fit their time slots and never cross a cut, holds at start and end, full duration stated, footwear and wardrobe locked, light direction per cut, STYLE names the Sony Venice 2 once with its look line and no other equipment name appears (checklist 62).

## Step 5 — Score

Score out of 100:

| Area | Points | How |
|---|---|---|
| User requirements [NOW] + [EARLIER] | 35 | proportion Met; Partial = half; any Contradicted = 0 for that item |
| Approved dialogue exact | 15 | all lines character-for-character, tags valid, in the right cut |
| Reference IDs | 10 | deduct 5 per missing needed ID, 5 per wrong ID, 2 per misspelling or missing scope/mode |
| Generation-risk checklist | 20 | deduct 5 per Must-fix risk, 2 per Should-fix |
| Standing rules | 10 | lip-sync block, Malayalam lock, no music, IDs exact |
| No unrequested changes | 10 | deduct 3 per risky unrequested addition |

Verdict bands: **90–100 Ready** · **75–89 Ready with small risks** · **60–74 Fix before generating** · **below 60 Do not generate**.

## Step 6 — Report and approval gate

Output exactly this, short:

```
PROMPT QA — <shot>  ·  Score NN/100  ·  <verdict>

Reference IDs:
✅ @… (shot, mode)   ❌ @… missing — needed for …   ⛔ @… remove — …
Paste-ready ACTIVE REFERENCES: (only if changed)

Your asks:
✅ … (block)
⚠️ … — why it's weak
❌ … — not in the prompt
🔁 … — conflicts with …

Risks found: (only if any)
• Must fix: …
• Should fix: …

Unrequested changes: (only if any)
• …

Proposed corrections:
1. …
2. …

Approve these corrections? (yes / pick numbers / no)
```

- If the score is **90+ and there is nothing Must-fix**, say "Ready to generate" and skip the approval question.
- **Small corrections you may apply yourself**, then re-run QA and list what changed: rewording so the prompt follows an existing rule; adding a reference ID that already exists in `INDEX.md`; removing a word that names something off screen; adding holds, the dialogue block or the duration line. At most two automatic rounds.
- **Everything else needs the user's approval first:** any change to approved dialogue; changing the action, cast, camera position or scene emotion; a new or replaced image, plate or ID; changing or removing a rule; anything still flagged after two automatic rounds. Stop and ask with the format above.
- After approval, apply only the approved corrections, re-run this QA, and show the new score with the revised prompt.

## Step 7 — Learn

When the user reports a bad generation, compare the output to the prompt, find which requirement or risk was missed, add a lesson file to `learnings/lessons/` from `templates/learning.md` (author = the creator in this session, from `git config user.name`; shot, category, date; numbered `L-new` until Ananthu merges it), add its row to `learnings/INDEX.md`, and add a matching line to `rules/pre-delivery-checklist.md` so this QA catches it next time. Commit the lesson on its own (`lesson: ...`) and push it to the creator's branch straight away, so the other creators' sessions pick it up. When the user says a take came out well, record what worked as a win in `learnings/wins/` the same way.
