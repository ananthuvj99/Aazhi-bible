---
id: L148
type: lesson
category: position
shot: s21-sh04 keyframes K2–K4
author: Ranjith
date: 2026-11-12
---

**L148: Sasi slept in a different place in different keyframes. One master layout in metres, rendered as a grey-box guide for each camera, goes into every keyframe** (s21-sh04 K2–K4 vs K5–K7)

Symptom: in K5–K7 (the aft view) Sasi lies on the bow side of the sacks, with room to spare. In K2–K4 the sacks stand right against Antony at the bulwark, with no room for anyone to sleep there. Every keyframe had placed people and props at its own distances.

Cause: the measured map (L146) gave positions, but the image prompts only described them in words ("the sacks at the right", "Antony at the bulwark"). The image model chose its own distances for each frame, and nothing compared the distances between frames.

Rule:
1. For each sequence, keep one master layout in metres (`continuity/memory/<shot>-master-layout.json`): mast, props, every person, the deckhouse front, the stem.
2. For every keyframe camera, render a grey-box guide from that layout with `tools/blocking3d.py` (only what is in front of the camera), and attach it to the image generation as a layout reference: "everything stands exactly where the grey-box layout puts it; do not copy labels".
3. Cross-plate QC measures distances against the layout. A person or prop out of place by more than about a metre is a ❌.

Checklist line: in `rules/pre-delivery-checklist.md`.
