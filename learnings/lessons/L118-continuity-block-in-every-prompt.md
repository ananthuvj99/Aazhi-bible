---
id: L118
type: lesson
category: position
shot: s23-sh06-v4
author: Ranjith
date: 2026-11-10
---

**L118 — Every prompt carries a CONTINUITY block: what this shot inherits from the shot before** (s23-sh06 v4, Ranjith's rule)

Why: the video model remembers nothing, and the takes that broke in SB029–SB031 (a different boat, Antony from the wrong door, the crew in unison) all lost something the previous approved shot had already settled. Writing it down in one place in the prompt tells the model what must not change, and shows the creator how continuity is being kept before they spend a generation.

Rule:
1. Right after ACTIVE REFERENCES, every prompt has a block `CONTINUITY (carried over from the previous shot, the reference image)` with, in one short paragraph: the time (same night, seconds later); each person's clothes, hair, props and what is in their hands; where everyone stands relative to each other (who is aft, who is forward, which rail); where the key element is (the fire, the boat, the door); where the light comes from; anything that changed on purpose.
2. Every fact in it comes from the previous approved take's last frame (named as the reference or start image) or the continuity ledger, never from memory of an earlier prompt.
3. The delivery shows the creator the same list in plain words ("How continuity is kept").

Checklist line: item 137 in `rules/pre-delivery-checklist.md`.
