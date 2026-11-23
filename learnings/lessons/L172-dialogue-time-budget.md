---
id: L172
type: lesson
category: dialogue
shot: s24-sh09 (Aswanth) v2
author: Aswanth
date: 2026-11-23
---

**L172: the platform refused a 30 s clip because its dialogue needs about 33 s at a natural pace** (s24-sh09 v2)

Symptom: "Didn't finish · Measuring the lines (ElevenLabs): the dialogue needs about 33s at a natural pace, but the length..." Credits spent anyway.
Cause: the platform times every line with ElevenLabs before generating; seven shots with six Malayalam lines (one very long) plus silent beats did not fit 30 s.
Fix: before delivery, budget the lines: about 2 to 2.5 Malayalam words per second, plus about 0.5 s of breath per line and the silent beats; keep the spoken time well under the clip length (aim at 70% or less). If it does not fit, split into two generations at a natural pause rather than cramming. Check this in the word check.
