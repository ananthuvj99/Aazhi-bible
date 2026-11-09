---
id: L102
type: lesson
category: characters
shot: 2B-v5
author: Ananthu
date: 2026-11-09
---

**L102 — Two Antonys: one already walking on the lane from the first frame, another coming out of the front door** (2B v5) — evidence: `scenes/showreel/evidence/2B-v5-two-antonys.jpg`

Symptom: from frame one a man in Antony's shirt and mundu walked up the sandy lane at frame-left, while Antony also came out of the front door and down the steps.

Cause: Antony was not in the start image, and the prompt placed him in two places (coming out of the door, and on the lane later, in SCENE, ACTION and CUT 2). The model filled the empty lane at once with a second Antony.

Fix: when a character enters later, write where he is NOT at the start ("the lane is empty; Antony is inside the house until 1.0s") and lock "only one Antony in the whole video" in POSITIVE LOCKS; best, start him in the start frame (L100).
