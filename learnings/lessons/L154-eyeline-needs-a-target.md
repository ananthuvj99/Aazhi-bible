---
id: L154
type: lesson
category: angles
shot: s23-sh01 v4 (SB028 reshoot)
author: Ranjith
date: 2026-11-13
---

**L154: Antony was meant to look at the far light, but in the take his eyes went down to the water by the hull. Every prompt now says exactly where each person looks** (s23-sh01 v4)

Symptom: the light sits on the horizon at the right of the frame; in the take Antony's head points right but his eyes drop to the sea a few metres from the boat, so he never looks at the fire. The end keyframe had the same fault and QC passed it.

Cause: the prompt said "looking out to the right" and "eyes narrow", never the target, the height of the gaze or the head angle. A direction is not a target: the model chose the nearest thing to the right.

Rule (Ranjith: "mention every detail of where a character in a scene should look, in all prompts"):
1. Every prompt has an **EYELINES** block: for each person in frame, at each moment, (a) the exact target ("the tiny light on the horizon at the right"), (b) where that target is in the frame, (c) the head angle (profile, three-quarter, turned away from the camera by about 20 degrees), (d) the height of the gaze (level with the horizon, down at the deck, up at the mast), (e) when the gaze changes and to what.
2. If the target is off screen, say where it is from the camera ("behind the camera to the right", "out of the frame at the left, at chest height").
3. Image QA draws the eyeline on every keyframe: a line from the eye along the gaze must hit the target. If it does not, the keyframe fails (no minor findings).
