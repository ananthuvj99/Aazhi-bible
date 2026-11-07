---
id: L82
type: lesson
category: position
shot: s21-sh02-v3
author: Ranjith
date: 2026-11-07
---

**L82 — "Behind the wheel" is read from the camera: put the camera behind the person, not the person behind the object** (s21-sh02 v3) — evidence: `scenes/showreel/evidence/s21-sh02-v3-aashaan-faces-camera.png`

Symptom: the prompt wanted Aashaan seen from behind, steering toward the bow. In the take he stood on the far side of the wheel, between the wheel and the windows, facing the camera, smiling into the lens. A helmsman faces forward, toward where the boat is going, so from behind we should see his back with the wheel in front of him.

Cause:
1. "Aashaan stands squarely behind the wheel" means "on the far side of the wheel" when read from the camera. The model put him exactly there.
2. The plate (@urudeckc3platenight) shows the wheel in the foreground with open space between it and the windows, and no room in front of the lens for a person; the model filled the empty space it could see.
3. A character sheet's front view pulls the face toward the lens unless the back is locked.

Rule:
1. Place people relative to the CAMERA, not to an object: "the camera is directly behind Aashaan's back; he stands between the camera and the wheel, close to the lens; the wheel is in front of HIM, on the far side from the camera; beyond the wheel, the windows."
2. Say what is NOT seen and lock it: "his face is never seen; only the back of his head, his shoulders and his back; he never turns round".
3. When the plate has no room for the person in the foreground (the plate was made empty from that exact spot), make a start frame first with the person in place, seen from behind, and attach it as the start image (L52, L61).
4. Check it in the 3D blocking: the camera pyramid, then the person, then the object he faces, in that order along the line of view.

Checklist line: item 99 in `rules/pre-delivery-checklist.md`.
