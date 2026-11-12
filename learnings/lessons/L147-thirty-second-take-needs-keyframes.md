---
id: L147
type: lesson
category: timing
shot: s21-sh04 v2 (30 s, four cuts)
author: Ranjith
date: 2026-11-12
---

**L147: A 30-second, four-cut generation dropped a cut, invented dialogue and drifted on props; every beat needs its own QC'd keyframe plate** (s21-sh04 v2)

Symptom (full report: `reports/s21-sh04-v2-take-analysis.md`):
- The bow cut never happened, so Antony's astonishment was never shown.
- Speech appeared although the prompt had no dialogue.
- Raghavan wore his towel on his head.
- The sacks swapped sides of the mast between views, and the lantern at the mast foot came and went.
- A spar seemed to fall off.
- The boat swayed in the hold.
- Antony came in from the wrong end.
- The five men ended in a straight row facing the camera, faces blank.

Cause:
1. One generation carried four cuts. The model holds the first camera, merges cuts, and drops whatever is described only in a missing cut.
2. The images given covered only the start and one middle view, so nothing showed the model the end states.
3. Two of our own plates disagreed: the sacks were on different sides of the mast, and the lantern appeared in only one. The start frame also put Raghavan's towel on his head, and my QC did not compare plates with each other or with the map.
4. "No voices" and the mouths-closed lock were trimmed away to fit the length.

Rule:
1. For a long shot, every beat gets a keyframe plate (every 2–8 s, at each change of camera or action), made from the measured map (L146) and passed through image QA and the logic gap finder.
2. **Cross-plate check:** every keyframe is compared with every other keyframe of the shot for the same set: mast, sacks, lanterns, rigging, rails, each person's clothes and tell-apart detail. Any difference is a ❌.
3. Generate one clip per camera, from its start keyframe to its end keyframe, and join them in the edit. Don't put several cuts in one generation unless the creator asks for it, knowing the risk.
4. Check every take frame by frame with `python tools/takeqc.py <video> <prefix> 1` before writing the next prompt.
5. "No spoken words and no voices; every mouth stays closed" is never trimmed from a silent shot.
6. In a hold, the camera rides with the boat, so the boat stays still in the frame.
7. Every keyframe's eyelines point at their cause: who looks at what, in the direction the map gives. K4 first showed Antony astonished while looking back over his right shoulder, away from the fire on the left; Ranjith caught it.

Checklist line: in `rules/pre-delivery-checklist.md`.
