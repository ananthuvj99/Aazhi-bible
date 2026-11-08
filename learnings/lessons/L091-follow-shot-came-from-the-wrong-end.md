---
id: L91
type: lesson
category: angles
shot: s16b-sh05-v5
author: Aswanth
date: 2026-11-08
---

**L91 — The follow shot ran the wrong way: Antony walked toward the deckhouse instead of coming down from it** (s16b-sh05 v5) — evidence: `scenes/showreel/evidence/s16b-sh05-v5-wrong-direction-watchers-in-a-line.webp`; path wanted: `scenes/showreel/approved/s16b-sh05-path-sketch.webp`

Symptom: Antony was meant to come down the staircase from the deckhouse roof and walk forward to the dance. The take looked aft instead: the carved deckhouse filled the background ahead of him, and he walked toward it.

Cause: the prompt described the deckhouse and its staircase in detail (in `@uru`'s line and the first frame) but never said which way the camera looks or what is behind it. The model put the most described structure ahead of the camera.

Rule:
1. In every follow or walking shot, state the camera's direction in boat or room terms ("the camera looks FORWARD toward the bow"), what is ahead (the goal) and what is behind the camera (where he came from), in the location block, the camera block and POSITIVE LOCKS (L68).
2. Name the starting structure only as "behind the camera" once he has left it; keep its detailed description out of the reference lines.
3. For a start on a staircase or other tricky spot, make a start still of the first frame first (L61).

Checklist line: item 108 in `rules/pre-delivery-checklist.md`.
