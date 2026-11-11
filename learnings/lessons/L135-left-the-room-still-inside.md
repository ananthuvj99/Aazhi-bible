---
id: L135
type: lesson
category: position
shot: 3door (SB017, Ananthu)
author: Ranjith
date: 2026-11-11
---

**L135: Antony walks back and speaks, but he is still standing inside the classroom instead of outside at the doorway** (review of the generated cut, 2026-11-11)

Symptom: After the classroom beat, Antony walks back and says his line, but the take shows him still inside the classroom. He should be outside, by the doorway.

Cause: The prompt said where he walks to, not which side of the door he stands on. With only the classroom plate attached, the model keeps him in the room it was given.

Rule:
1. When someone leaves a room and then speaks, write the side of the threshold as a fact: "outside the classroom, on the veranda, a step beyond the green door; the door frame is beside him, the classroom is behind the door".
2. Attach the plate of where he is (the veranda or the door from outside), not the classroom plate, and add the lock "he never steps back inside".
3. If the listener stays inside, place the camera so the doorway separates them, and say which side of the frame each one is on.

Checklist line: in `rules/pre-delivery-checklist.md`.
