---
id: L138
type: lesson
category: elements
shot: s13-sh02 / s13-sh03 (SB020)
author: Ranjith
date: 2026-11-11
---

**L138: The water moved, but the moored uru stood dead still, like a building** (review of the generated cut, 2026-11-11)

Symptom: As they come to board, the water moves but the boat looks fixed in place. A real moored wooden boat rocks.

Cause: The prompts locked the uru ("stays moored, matches the reference exactly") and gave the water motion but never the hull. "Exactly as the reference" reads as frozen.

Rule:
1. Every moored-boat shot has a PHYSICS line: "the uru rocks slowly on the harbour swell, a few degrees side to side, rising and falling about 15 cm, once every four or five seconds; the mast sways a little against the sky; the mooring ropes slacken and tighten; the gangplank shifts and creaks on the quay edge".
2. Keep "stays moored in place" (it does not drift), but never "still", "fixed" or "motionless".
3. At sea the motion is bigger and the camera rides it; in the harbour it is gentle and the camera on the quay stays still while the boat moves.

Checklist line: in `rules/pre-delivery-checklist.md`.
