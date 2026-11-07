---
id: L85
type: lesson
category: position
shot: s23-sh02-v1
author: Ranjith
date: 2026-11-07
---

**L85 — A shot that continues the previous one always starts from that shot's last frame** (s23-sh02 v1, failed)

Symptom: SB029 follows straight on from SB028 (same moment, same bow, same Antony), but the take had no relation to it: a different vessel, a different sky, Antony sitting instead of standing.

Cause: the previous approved take's last frame was not attached. Each generation remembers nothing, so without it the model rebuilt the scene from scratch.

Rule (obvious, so never skip it):
1. If a shot carries on from the previous shot (same place, same moment, same people), its start image is the last frame of the previous approved take. It is required, not optional.
2. Keep the previous shot's camera, or move from it within the shot (push-in, pan). Cut to a new angle only when the story needs it, and then still attach the previous last frame as a reference plus the place's plate (L84).
3. Before writing the prompt, ask the creator for that last frame and save it in `scenes/<scene>/<shot>/approved/` (or `scenes/showreel/approved/`). If they don't have it, say the shot is at risk before delivering it.
4. The prompt's FIRST FRAME and the "Start image (0.0s)" reference line both say "the exact first frame: same place, same pose".

Checklist line: item 102 in `rules/pre-delivery-checklist.md`.
