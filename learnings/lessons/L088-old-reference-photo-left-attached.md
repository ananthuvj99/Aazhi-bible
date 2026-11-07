---
id: L88
type: lesson
category: platform
shot: s16a-sh01-v4
author: Aswanth
date: 2026-11-07
---

**L88 — An old reference photo left attached on the platform brought back the lantern the prompt had removed** (s16a-sh01 v4) — evidence: `scenes/showreel/evidence/s16a-sh01-v4-lantern-still-there.webp`

Symptom: the prompt said the two men are "lit only by the moon" and named no lamp, but the lantern on its rope-wound post came back at screen-left, exactly as in an earlier take.

Cause: the earlier SB023 frame (with the lantern) was still attached on the platform as a reference image from a previous generation. The model copies what a reference photo shows (L60, L61), so it overrode the text.

Rule: before every generation, clear every attachment that the delivery does not list; attach only the IDs and images named in the delivery. When a take repeats something the prompt removed, check the platform's attachments first.

Checklist line: item 105 in `rules/pre-delivery-checklist.md`.
