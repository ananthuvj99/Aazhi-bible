---
id: L63
type: lesson
category: elements
shot: s11-sh01-v2
author: Ranjith
date: 2026-11-05
---

**L-new — Furniture in the plate's action path comes back in the take** (s11-sh01 v2) — evidence: `scenes/showreel/evidence/s11-sh01-v2-bench-across-aisle.png`

Symptom: in the take, a long desk ran across the centre aisle in front of the teacher's table, and Clara stood behind the table reading a book instead of bending over the front-right bench. The prompt never mentioned that desk.

Cause: the desk, and Clara behind the table with an open book, are both in the attached plate @tuitionboardclass. The reference line said "100% matches the reference", and the prompt only said what the room contains without saying the aisle and the floor in front of the table were open. So the model kept the plate's furniture and staging (L41: sheet props override wishes).

Rule: before attaching a plate, look at the image itself and list every piece of furniture on the path or the spot where the action happens. If the plate has furniture there the shot does not want:
1. Say in the reference line which parts of the plate to match, and that the path is open ("the centre aisle is open floor all the way to the teacher's table").
2. Name the open floor in the room block, with a size, and name the only furniture there ("the teacher's table, the only furniture at the front").
3. Put the open path and the character's place in POSITIVE LOCKS.
4. If the furniture still comes back, ask the creator for a corrected plate (a new or replaced image needs approval).
Also check whether the plate shows a person in a different position from the shot's first frame, and place them in words.

Checklist line: item 75 in `rules/pre-delivery-checklist.md`.
