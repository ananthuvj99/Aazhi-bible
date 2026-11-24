---
id: L182
type: lesson
category: in-frame
shot: s42-sh03 v1
author: Ranjith
date: 2026-11-24
---

Symptom: the s42-sh03 take looked unnatural, "more of a cartoon": flat waxy skin, smeared painted walls, over-clean props (Ranjith: "this looks very unnatureal and more of a cartton").
Cause: its start frame came from four edit-by-reference passes in a row (add the cap, move the cap, move the lamp and cap, turn the cap); every pass re-rendered the whole image a little more painterly and over-sharpened, and the video model copied that look from the start frame.
Rule: never chain more than two edit passes on a start frame. When a third fix is needed, make one fresh generation from the ORIGINAL references (plate or first shot of the scene, character sheets) with every fix written into that one prompt, and check the result at full size for skin texture, real wall grain and natural light before showing it.
Also (s42-sh05, 2026-11-24, Ranjith: "start frame looks too plastic"): an edit pass followed by a crop and a 1.55x upscale gave waxy, smoothed skin with a dotted pattern. Cropping and enlarging counts as a degrading pass: never enlarge a crop more than about 1.2x; generate the frame at the framing the shot needs instead.
Checklist line: start frames come from at most two edit passes; any more, regenerate fresh from the original references with all fixes in one prompt; check skin and wall texture at full size; never enlarge a crop more than about 1.2x (L182).
