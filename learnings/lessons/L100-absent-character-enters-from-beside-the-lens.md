---
id: L100
type: lesson
category: position
shot: 2B-wide-v3
author: Ananthu
date: 2026-11-08
---

**L100 — A character missing from the start frame walked in from beside the lens instead of leaving his own compound** (2B wide v3) — evidence: `scenes/showreel/evidence/2B-wide-v3-enters-from-lens.jpg`

Symptom: the start frame showed the house with only Rosamma; the prompt said Antony "walks into view from the lower-left corner". He appeared large at the lower-left, as if he had come from behind the camera, and never came out of the house or the yard. Ananthu: "Antony is walking from somewhere; he should walk out of his compound and go."

Cause: a person who is not in the start image has no place to come from, so the model brings him in from the nearest frame edge.

Fix: when a character must come from a place, start him visibly there — in the start frame, or stepping out from something seen in it (from behind the pillar beside the door where the last approved shot left him), and write his route through the place (down the steps, across the yard, out through the wall gap) before any lane or edge.
