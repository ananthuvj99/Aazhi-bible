---
id: L70
type: lesson
category: timing
shot: s13-sh04-v1
author: Ranjith
date: 2026-11-06
---

**L70 — A shot never ends on the last word** (s13-sh04 v1, Aashaan's line)

Symptom: the take ended almost on Aashaan's last word. With no silence after the line, the editor had nothing to cut on and the line felt chopped off.

Cause: the prompt gave a hold after the line in ACTION, but nothing said the speaker stays silent and the clip keeps running; the model compressed the tail and stopped with the line.

Rule: in every shot whose last spoken line ends the dialogue (a single speaker, or the final line of an exchange):
1. The line ends at least 2.5 seconds before the end of the clip; write the time slot so (for a 7 s shot the line ends by 4.5 s).
2. ACTION gives that tail its own beat: the speaker is silent, mouth closed, holding a look or doing a small quiet action.
3. AUDIO says it: "after the line, only the ambient sounds; nobody speaks".
4. POSITIVE LOCKS: "after the line he stays silent for the last N seconds; the shot does not end on his last word".
Shots in the middle of a two-person exchange (the next line follows in the next shot) do not need the long tail; a short beat is enough.

Checklist line: item 83 in `rules/pre-delivery-checklist.md`.
