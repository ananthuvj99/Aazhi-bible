---
id: L119
type: lesson
category: elements
shot: s23-sh06-v5
author: Ranjith
date: 2026-11-10
---

**L119 — Every shot is checked against the previous approved frames before it is sent: people, distances and props** (s23-sh06 v5, failed) — evidence: `scenes/showreel/evidence/s23-sh06-v5-strangers-boat-too-close.jpg`

Symptom: the close-up came back with two men who are not our characters (both in Antony-style striped shirts), the burning vallam close and big beside the uru, a lantern on a post that never existed, and different words. Every earlier approved frame (s23-sh01, sh02, sh05) has the fire as a small far light on the horizon and our own crew at the rail. Each wrong generation costs credits.

Cause:
1. The prompt named Raghavan and Babu many times (eyeline, performance, locks, "camera beside Raghavan's head") without attaching them; the model put two men in and built them from the only sheet attached, `@antony20`.
2. The prompt moved the fire to "about 150 metres" and attached `@burningvallam`, a close-up picture, so the boat was drawn close. No approved shot ever brought it near.
3. Nothing compared the prompt with the previous approved frames before it was sent.

Rule:
1. Before every prompt, open the previous approved frames (last frame of the shot before, plus the earlier shots of the same moment) and fill a Continuity check table in the shot file: element · previous frames · this shot. Every person, the key prop's distance and size, light sides and props in hands. The prompt's CONTINUITY block (L118) is written from that table.
2. Anyone who could appear in the frame (the people the speaker talks to, people standing near him) is attached with their own sheet and placed explicitly (seen from behind, soft, where in the frame). Never name a person in the prompt without attaching them or saying plainly they are out of frame.
3. Distances do not change between shots unless a shot shows them changing. Write the distance in metres and the size in the frame ("a tiny orange point on the horizon") and check it in a 3D blocking camera view at real distances (`tools/blocking3d.py`, camera eye at the shot's position).
4. A close-up picture of a prop that must look far away is attached only with the size lock in its reference line, the location line and POSITIVE LOCKS.
5. Lock the head count: "exactly N people in frame: ...; no one else, no copies".

Checklist line: item 138 in `rules/pre-delivery-checklist.md`.
