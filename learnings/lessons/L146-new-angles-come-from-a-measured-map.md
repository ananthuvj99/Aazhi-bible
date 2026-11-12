---
id: L146
type: lesson
category: position
shot: s21-sh02 start frame (SB027)
author: Ranjith
date: 2026-11-12
---

**L146: Every new angle of a set already shown is worked out from a measured map of the earlier image: each person's place, distance, body direction, head direction and face, plus everything that blocks sight** (s21-sh02 start frame, 2026-11-12)

Symptom: the helm start frame for s21-sh02 was made twice by guesswork. First, all three sleepers faced the wheel. Then Sasi's head still showed above the sacks. In plate 1 (s21-sh01), Sasi lies on the bow side of the sacks, so from the wheel he cannot be seen at all, Babu shows only his back, and Raghavan is below the wheelhouse sill.

Cause: the second image was described from memory of the first, person by person, without measuring where everyone is and which way they face, and without checking what stands between them and the new camera.

Rule (Ranjith: "for any image going forward"):
1. Before making a new angle, a reverse, or the next start frame of a set an approved image already shows, measure that image into a map: every person and key prop, with position in metres, standing, sitting or lying, which way the body lies (head direction), which way the face points, and every object that can block sight (walls, sills, sacks, the mast, rails).
2. Put the map in `scenes/showreel/storyboards/<shot>-sightlines.json` and run `python tools/sightlines.py` on it for every camera. For each camera and each person it says VISIBLE or HIDDEN (and by what), which part shows, and whether the camera sees the face, the back or the side.
3. The image prompt describes exactly that table and nothing else: hidden people are not drawn, backs stay backs, and the sides of the frame follow the map.
4. The table goes into image QA (Step 2b) as the logic check. An image that shows a hidden person, or a face where the table says back, is a ❌.

Checklist line: in `rules/pre-delivery-checklist.md`.
