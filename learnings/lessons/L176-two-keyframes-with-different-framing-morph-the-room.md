---
id: L176
type: lesson
category: angles
shot: 1B-3-v9
author: Ananthu
date: 2026-11-23
---

Symptom: 1B-3 v8.2 and v9: the window view, the wall and the clock jumped and slid during the shot; the clock moved up toward the top edge; the frame seemed to change from one picture to another. He also copied the second keyframe's head-in-hands pose. Both takes were only 5 s long although the prompt was written for 15 s, so every action came out rushed.
Cause: two reference images of the same room (@1b3k12 and @1b3k22) with slightly different framing, window crop and clock place, plus a dolly push-in, so the model morphed from one image to the other; the platform duration was left at 5 s.
Rule: one camera set-up = one image of the room. For a locked shot attach only the start image; never a second keyframe of the same view unless it is pixel-identical in framing. Lock the camera in words (no push, no pan, no zoom) when the room must stay the same, and say the window view and the clock never move. Set the platform duration to the prompt's length every time (L14).
Checklist line: One room image per set-up (L176): only one image of the same view is attached; the camera is locked when the set must not change; "the window, the wall and the clock stay exactly where they are in the start image"; the platform duration equals the prompt's length.
