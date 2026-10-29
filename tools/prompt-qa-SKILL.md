---
name: aazhi-prompt-qa
description: Request-vs-prompt QA gate for AAZHI / Techjays film-platform video prompts. Use after EVERY scene prompt is drafted for AAZHI or the Techjays showreel — before it is handed to the user — and whenever the user asks "does this prompt have everything I asked", "check the prompt", "score this prompt", "will this generate well", or pastes a prompt and a request together. It extracts every requirement from the user's messages, proves each one is in the prompt, finds contradictions and risky additions, runs the generation-risk checklist, gives a score out of 100 with a short summary, and asks the user to approve corrections before rewriting. Trigger even if the user does not ask, whenever a new or revised AAZHI prompt is about to be delivered.
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
- **[STANDING]** project rules (repo `rules/prompt-rules.md`, `rules/pre-delivery-checklist.md`, saved preferences): Malayalam-only dialogue, 32-tag emotion list one per bracket, lip-sync block verbatim, sound effects only, holds, IDs exactly as registered, scoped prompts, etc.
- **[APPROVED]** exact dialogue the user confirmed — the Malayalam must match character for character.

Split compound asks: "mother in the passage, Antony comes out of his room, veranda behind him" is three requirements. Include negative asks ("no clock", "don't throw the spoon"). Dictated messages are messy — resolve the intended meaning, and if a requirement is genuinely ambiguous, list it as **[UNCLEAR]** and ask.

## Step 2 — Trace each requirement into the prompt (OUTPUT)

For each requirement, find the exact place in the prompt that satisfies it and mark:
- ✅ **Met** — quote the block name (e.g. "FIRST FRAME", "Shot 2 LOCATION").
- ⚠️ **Partial / weak** — present but easy for the model to ignore (said once, buried, contradicted elsewhere, no timing).
- ❌ **Missing** — not in the prompt.
- 🔁 **Contradicted** — the prompt says something that conflicts with it.

## Step 3 — Find what the user did NOT ask for

Flag anything the prompt adds that could change the result: new props, new dialogue or changed wording, new rooms, moods, camera moves, timing changes, removed beats. Additions are allowed only if they serve a stated requirement or a standing rule — otherwise list them as **Unrequested**.

## Step 4 — Generation-risk scan

Run the repo checklist (`rules/pre-delivery-checklist.md`, lessons L1 onward). At minimum check: start positions (characters begin where the dialogue happens), single location per dialogue shot, references tied to shots and only for things on screen or framing the shot, reverse-angle backgrounds named, nothing off-screen named (word scan, including hidden words like "o'clock"), no English paraphrase of any line, Malayalam lock in five places, one speaker per cut in MCU with face to lens, emotion tags valid, lines fit their time slots and never cross a cut, holds at start and end, full duration stated, footwear and wardrobe locked, light direction per cut.

## Step 5 — Score

Score out of 100:

| Area | Points | How |
|---|---|---|
| User requirements [NOW] + [EARLIER] | 40 | proportion Met; Partial = half; any Contradicted = 0 for that item |
| Approved dialogue exact | 15 | all lines character-for-character, tags valid, in the right cut |
| Generation-risk checklist | 25 | deduct 5 per Must-fix risk, 2 per Should-fix |
| Standing rules | 10 | lip-sync block, Malayalam lock, no music, IDs exact |
| No unrequested changes | 10 | deduct 3 per risky unrequested addition |

Verdict bands: **90–100 Ready** · **75–89 Ready with small risks** · **60–74 Fix before generating** · **below 60 Do not generate**.

## Step 6 — Report and approval gate

Output exactly this, short:

```
PROMPT QA — <shot>  ·  Score NN/100  ·  <verdict>

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
- Otherwise **stop and wait for the user's approval** before rewriting. Do not silently fix and redeliver.
- After approval, apply only the approved corrections, re-run this QA, and show the new score with the revised prompt.

## Step 7 — Learn

When the user reports a bad generation, compare the output to the prompt, find which requirement or risk was missed, add a lesson to the repo (`rules/lessons.md`), and add a matching line to the checklist so this QA catches it next time.
