---
id: L64
type: lesson
category: elements
shot: s11-sh01-v3
author: Ranjith
date: 2026-11-05
---

**L64 — A prop that is not on the character sheet gets dropped** (s11-sh01 v3) — reference: `scenes/showreel/evidence/s11-antony-bag-reference.png`

Symptom: Antony came through the tuition door with no bag, although the prompt gave him "a small faded khaki cloth bag on his left shoulder".

Cause: the `@antony20` sheet has no bag. The prompt says "100% matches the reference", so the sheet wins over one short line of text (L41). "Small" also made the bag easy to lose in a wide shot.

Rule: a prop the character carries but the sheet does not show is written in full every time it is on screen:
1. In the character's reference line, with size, colour, material, strap, the shoulder and where it hangs, and "he carries it the whole shot".
2. Again in every ACTION beat he is in, and in POSITIVE LOCKS.
3. Its size matches the reference the creator approved, not a guess.
4. To make it hold for good, it gets its own prop card and image (L17: a prop is valid once it has a card, a sheet and a placement). Ask the creator before making that image.

Checklist line: item 76 in `rules/pre-delivery-checklist.md`.
