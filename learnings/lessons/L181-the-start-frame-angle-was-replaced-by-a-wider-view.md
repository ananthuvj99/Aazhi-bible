---
id: L181
type: lesson
category: angles
shot: 1D-exit-v3
author: Ananthu
date: 2026-11-24
---

Symptom: 1D-exit v3 did not keep the close over-the-shoulder angle of its start image (@1calast). From the first frame the model showed a wider view with the stove and fire, a big window with no bars and a level beach, then Antony walked off toward the window; the clip ran 5 s.
Cause: the prompt described things outside the start frame's edges (the stove, the curry, the whole window and the sea "far below"), and the platform duration was left at 5 s, so the model recomposed the room to fit what was written.
Rule: when the start image is a close angle, describe only what is inside its frame and say what the frame does NOT show ("the stove and the window are out of frame; only the thin edge of the white shutter shows at the right"); lock the framing with sizes ("her head and shoulder fill the left third, his head and chest the right third"); if the window could come into view, give it its iron bars; and check the platform duration matches the prompt before generating.
