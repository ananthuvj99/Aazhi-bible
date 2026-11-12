---
id: L145
type: lesson
category: in-frame
shot: s21-sh01 v3, s21-sh02 v6 (SB027 full-moon redo)
author: Ranjith
date: 2026-11-12
---

**L145: The full-moon redo brought back logic gaps: a moon in the aft view, Babu and Raghavan merged into one sleeper, nobody at the wheel, and from the helm the sleeping crew were not on the deck at all** (s21-sh01 v3 failed; s21-sh02 start frame)

Symptom:
1. s21-sh01 v3: a full moon sat on the horizon at the right of a view looking AFT, where the moon must be behind the camera (L142).
2. Only two sleepers: one man wore Babu's checked lungi with Raghavan's grey hair and neck towel, so the two had merged into one.
3. The wheel was visible through the deckhouse windows, but nobody stood at it.
4. s21-sh02: from Aashaan's place at the wheel, the deck outside the windows was empty, although the three men sleep on that deck. Aashaan and the wheel also looked like an illustration.

Cause:
1. The word "moon" appeared about eight times in the s21-sh01 prompt. The MEMORY block described the forward view ("top right with its silver path"), and the locks said "no moon". Every mention, even a negative one, invites the model to draw it.
2. MEMORY shortened each reference line to "Raghavan, as in MEMORY". That removed each man's distinct look from beside his ID, and MEMORY listed seven people when only four were in frame.
3. The plate shows the wheel empty, and Aashaan was only "seen small through the windows", so the model kept the plate's empty wheel.
4. The helm plate and start frame were made as empty sets. Nobody checked who should be seen from that spot at that moment, and GPT's wheelhouse came out painted.

Rule:
1. A view that faces away from the moon names it once only, as "the light comes from behind the camera", and describes the sky in positive words ("an even navy sky"). MEMORY's Light line gives only the moon's direction, not how it looks in frame.
2. Each person in frame keeps a full reference line: his own look, clothes and the detail that tells him apart from the others. MEMORY's People line lists only the people in this shot; anyone else goes in the NOW line as "below, out of view".
3. When a set's plate is empty but people must be in it (someone at the wheel, sleepers on the deck), make a start frame with every person placed, from their own sheets, and count heads in it before any video.
4. Every plate and start frame passes the logic gap finder (image QA Step 2b, prompt QA Step 4b): what the moment needs (people seen from this spot, the board with sums), what cannot be there (the moon in an aft view, merged or extra people), inside or outside, and a real photographic look.
5. A reverse view of the same people shows them from the other side (Ranjith, 2026-11-12). The second helm start frame showed all three sleepers facing the wheel, but they had been lying facing the bow. From the wheel, Sasi (behind the sacks) shows only the top of his head, Babu shows his back, and Raghavan, lying against the wheelhouse wall, is hidden below the sill. Before making a reverse view, write down for each person which way he faces and what stands between him and the new camera; faces seen in one view become backs in the reverse.

Checklist line: in `rules/pre-delivery-checklist.md`.
