---
id: L143
type: lesson
category: elements
shot: s21-sh03 v3, SB027–SB032 bow shots (Ranjith); @urubowplate (Aswanth)
author: Ranjith
date: 2026-11-11
---

**L143: Aswanth's bow plate (@urubowplate), used in all his uru shots, never reached our night shots; we kept drawing a different bow** (full-moon redo, 2026-11-11)

Symptom: Aswanth has used `@urubowplate` throughout his uru scenes: the closed blue triangular bow deck, low blue bulwarks, four red-brown bitts, big rope coils, the lantern at the foot of the mast. Our bow shots (s21-sh03, SB028–SB032) still used our own `@urudeckc2platenight`, with a tall stem post and turned-post rails. That is a different bow, and it matches neither his plate nor the uru four-view sheet. We even remade it today as `@urudeckc2platefullmoon`.

Cause:
1. `@urubowplate` was never added to INDEX.md: no folder, no card, no image in the repo (his shot file says "image still to be added to the repo"). The "check INDEX first" step could not find it.
2. Aswanth's L116 (2026-11-10) said in plain words that `@urudeckc2platenight` "shows yet another bow". Nobody went back to fix our plate, because we never searched other creators' new lessons for our own IDs.
3. His L131 reached our branch at the start of today's session, but the lessons were not re-read before the full-moon redo.
4. When our c2 plate was approved on 2026-11-07, its QA compared it only with our own day plate, not with the uru four-view sheet.

Rule:
1. Any ID used in a shot file must have a row in INDEX.md. Run `python tools/unregistered-ids.py` at the start of a session and before a prompt; register whatever it lists (the creator's image, card and row) or ask for the image.
2. After every pull, read the lessons and wins added since your last session, from every creator, and search them for your own IDs and shot names. If another creator's lesson says one of your assets is wrong, fix or retire it the same day.
3. One set, one plate: when two plates show the same part of the uru, the one in more approved takes wins, and the other is retired (here `@urubowplate` wins).
4. Image QA for any uru plate compares it with the four-view sheet (`props/uru/fourview.png`) as well as the other plates.

Checklist line: in `rules/pre-delivery-checklist.md`.
