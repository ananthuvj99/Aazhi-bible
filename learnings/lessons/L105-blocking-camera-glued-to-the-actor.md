---
id: L105
type: lesson
category: angles
shot: s16b-sh05-v14
author: Aswanth
date: 2026-11-09
---

**L105 — A blocking camera locked at a fixed offset behind the actor made the generated move feel robotic** (s16b-sh05 v14) — evidence: `scenes/showreel/evidence/s16b-sh05-v14-contact.png`

Symptom: the take followed the 3D playblast faithfully, but Antony stayed glued to the same spot in the frame the whole time, the world sliding past him like a game camera; it read as robotic, not as an operator walking behind someone.

Cause: in the Blender blocking the camera was computed as "Antony's position + a fixed offset" every frame, with a tiny sine wobble. The model copied that mechanical lock exactly.

Rule: animate blocking cameras like a person: the camera lags the actor (smoothed follow, a beat late on starts and stops), the distance changes (he pulls ahead on the walk, the camera catches up), the framing drifts (he does not stay centred), the look leads toward what matters (the dance), and handheld motion mixes several slow and fast frequencies. Check the playblast for "glued" framing before sending it.

Checklist line: item 123 in `rules/pre-delivery-checklist.md`.
