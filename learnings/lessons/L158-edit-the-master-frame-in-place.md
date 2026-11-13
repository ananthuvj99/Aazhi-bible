---
id: L158
type: lesson
category: position
shot: s23-sh02c (SB029 wake keyframes)
author: Ranjith
date: 2026-11-13
---

**L158: Build a new angle of a locked set by editing the locked frame itself; let the action place the actor**

What happened: for the crew-wake shot, generated keyframes of the uru drifted from Aswanth's frames: a red-brown varnished deckhouse, baluster rails along the forward deck, an invented overhang. And the image model kept putting Antony in the wrong place: on a raised platform at camera height, near the bow, on the bulwark. Ranjith: "he's standing above, right? That's not correct", "does it change uru from ashwanth's frames?", "we can change camera angles but continuity should be there".

Rule:
1. When a locked frame of the set exists (here Aswanth's rc-066), make the keyframe by editing that frame (inpaint with a mask), not by generating the set again. Check the result against the locked frame item by item: hull, rails, deckhouse, mast, lamps.
2. Nano Banana 2.1 with `resolution: 2k`, `thinking_level: high` and `is_inpaint` with a mask holds the rest of the frame best. A mask edit can still return a different aspect ratio (crop back to 21:9) or redraw the whole frame: QC every result.
3. If the model will not put a person in the right spot after two tries, leave him out of the still and bring him in during the shot ("runs in from the deckhouse corner at 0.3s"). Never keep a still with the person in the wrong place.
4. A new shot after an approved take starts on that take's last frame; a new angle comes after a cut on action that keeps the direction of movement (he leaves frame right, he enters from that side).
