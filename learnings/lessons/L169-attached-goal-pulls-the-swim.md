---
id: L169
type: lesson
category: angles
shot: s24-sh05 (Aswanth) v2.2
author: Aswanth
date: 2026-11-23
---

**L169: with the burning boat attached, the swim back went toward the fire, not the uru** (s24-sh05 v2.2)

Symptom: in the back shot of Antony towing Selvan "toward the uru ahead", the burning vallam appeared ahead of them, so they swam back toward the fire.
Cause: `@burningvallam` was attached for SHOT 1 with no limit, and the firelight was written "on the swimmers"; the model put the strongest, attached object where the swimmers were heading.
Fix: limit each attached place or object to the shots it belongs in ("SHOT 1 only"); in the shot that leaves it, say where it is ("behind the camera, NOT in this shot, its glow only on their backs, no fire ahead") and name the goal as "the only boat in the frame". Pairs with L167 (keep the goal in frame).
