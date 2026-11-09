---
id: L111
type: lesson
category: angles
shot: s16b-sh10-v1
author: Aswanth
date: 2026-11-09
---

**L111 — A fast camera turn came out crisp and mechanical because the blocking video has no motion blur** (s16b-sh10 v1, partial)

Symptom: the 360 turn read as a sharp, linear, computer move.

Cause: the Eevee playblast renders every frame sharp and the prompt did not ask for blur, so the model kept the crisp look.

Rule: any fast pan, orbit or turn gets a CAMERA sentence asking for natural filmic motion blur: the edges and background streak sideways along the direction of the turn, the subject at the middle stays readable. Positive wording, no equipment words.

Checklist line: item 130 in `rules/pre-delivery-checklist.md`.