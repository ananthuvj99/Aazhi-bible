---
id: L84
type: lesson
category: elements
shot: s23-sh02-v1
author: Ranjith
date: 2026-11-07
---

**L84 — A new angle with only the character attached loses the whole scene: always carry the place in** (s23-sh02 v1, failed)

Symptom: the take had no relation to the shot before. Antony sat in a small open canoe instead of standing at the uru's bow, the bow was a different vessel, the sky was dusk instead of deep night, and the burning boat looked like a Viking ship with raised curved ends.

Cause: the prompt moved to a new camera angle (c4, over the shoulder) with no plate and no start image, and attached only `@antony20`. The night bow plate was left out as "other angle (L61)". With nothing to anchor the vessel, the model invented one, and the words "bow" and "boat" pulled it to a small boat. "Small wooden fishing boat" with no shape let it draw a Viking ship.

Rule:
1. A shot that continues the previous one keeps its camera (or a push-in from it) and starts from the previous approved take's last frame. A new angle is only for when the story needs it.
2. Never send a shot whose location or vessel exists in `INDEX.md` without at least one image of it attached. L61 (other angle) is a reason to use the plate in background-only mode or with "same place, seen from another angle", never a reason to attach nothing.
3. A shot on the uru names it as the big cargo uru, standing on its deck, and attaches `@uru` or a deck plate; never write it so it could be read as a small boat.
4. Any other vessel is described by shape: a Kerala fishing vallam is long, low and narrow, flat sides, no raised carved ends, no sail, no dragon or curled prow.
5. Night is "deep night, the sky nearly black" in SCENE, LIGHTING and LOCKS.

Checklist line: item 101 in `rules/pre-delivery-checklist.md`.
