---
id: W19
type: win
category: angles
shot: s16b-sh05-v15
author: Aswanth
date: 2026-11-09
---

**W19 — A 3D grey-box blocking video plus a short "follow the video" prompt finally got a complex moving group shot right** (s16b-sh05 v15, approved) — files: `scenes/showreel/s16b-sh05/blocking-playblast.mp4`, `blocking.blend`; prompt: `scenes/showreel/s16b-sh05.md` v15; template: `templates/blocking-prompt.md`

What worked after twelve text-only versions failed (wrong direction, side stairs, clones, robotic camera): Antony coming down the deckhouse staircase, walking to the dance, two crewmen joining, and a 360° circle round his smiling face, all in one 15 s take.

Recipe:
1. Build the set to scale from the location/prop sheet in Blender (low poly is enough): structures with their real orientation (L99), open space for the action (L97).
2. One colour-coded stand-in per person (distinct shirt/lower/head colours, a prop disc for the plate). Positions and paths exactly as wanted; small human-sized moves (L96); joins take about 3 s, not 1.5 (fast blocking = fast take).
3. Camera like a person (L105): lag, changing distance, drifting framing, layered hand-held; any orbit at one constant speed, eased in, rotation kept continuous (no jerk).
4. Show the playblast to the creator and iterate before generating; only the approved final goes in the repo.
5. Prompt (short, about 5,000 characters): MOTION REFERENCE block mapping each stand-in colour to a person; SCENE CONTEXT; ACTIVE REFERENCES with "only one who…" markers; CAMERA in words per time range (hand-held / smooth constant speed); DANCE and PERFORMANCE in words (what the boxes cannot show: style, faces, smiles); LIGHTING; AUDIO; STYLE ending "nothing of the grey-box look remains"; POSITIVE LOCKS "camera path and timing exactly as the attached video".
6. Attach the playblast as the video reference plus the character/prop sheets; remove every other attachment (L88).
