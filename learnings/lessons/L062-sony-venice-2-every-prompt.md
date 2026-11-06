---
id: L62
type: lesson
category: platform
shot: all shots (from s11-sh00 / s11-sh01 v2 / s11-sh02 v2 on)
author: Ranjith
date: 2026-11-05
---

**L62 — Every prompt is shot on a Sony Venice 2**

Symptom: most shot prompts in `scenes/showreel/` (1A to 3-6) never name a camera, so the look changes from generation to generation and the film does not cut together as one camera. Ranjith's direction: every AAZHI prompt is filmed on a Sony Venice 2.

Cause: the camera rule was added to `rules/prompt-rules.md` on 2026-11-04 (Ranjith) but never recorded as a learning, so prompts written from older shot files kept the old wording with no camera named.

Rule: every prompt, silent or with dialogue, new or a new version of an old shot, names the camera once in STYLE with the paste line from `rules/prompt-rules.md` ("Camera: Sony Venice 2"), adapting only the light words to the scene:
"Shot on a Sony Venice 2 full-frame digital cinema camera: very wide dynamic range that holds the brightest light and the deepest shade in one frame; clean, low-noise shadows; soft, gradual highlight roll-off; accurate, natural colour with rich, true skin tones; gentle filmic contrast; fine, organic texture; no over-sharpening, no glossy or video look."
It appears only in STYLE (never in CAMERA, OPTICS or ACTION, never as an object in the shot), and WHAT IS IN FRAME keeps "Every frame looks like the film itself, with nothing from the making of it" (L46). No other camera, lens, film-stock or rig names. When an older prompt is revised, its new version adds the line.

Checklist line: item 74 in `rules/pre-delivery-checklist.md`; QA fails a prompt whose STYLE does not name the Sony Venice 2 exactly once.
