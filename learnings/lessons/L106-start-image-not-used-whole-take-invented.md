---
id: L106
type: lesson
category: platform
shot: 2B-v8
author: Ananthu
date: 2026-11-09
---

**L106 — The start image was not used: every frame was a different house and place** (2B v8) — evidence: `scenes/showreel/evidence/2B-v8-first-frame-not-the-start-image.jpg`

Symptom: the take opened on a close angle of a different blue house with a chapel at the left and the beach behind, not on @2bwidestartclear; the whole 10 s was invented. It also came out 10 s long and 2.4:1 at 992×432, not 15 s 16:9.

Cause: the first frame did not match the start image at all, which means the platform did not receive it as the start frame — the new ID had not been uploaded yet, or it was attached as a plain reference instead of in the start-image slot. With no start image and no location sheet attached, the model built the place from words.

Fix: before generating, upload every new image under its exact ID and put the start image in the platform's start-image slot; check the platform's preview shows that image as frame one; set Duration 15 s and 16:9. When a prompt depends on a start image, also attach a location reference (@houseout or the plate) so a missed start image cannot invent a new place.
