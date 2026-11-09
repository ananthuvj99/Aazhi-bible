---
id: L107
type: lesson
category: platform
shot: 3tease-v2
author: Ananthu
date: 2026-11-09
---

**L107 — A classroom prompt that described the children closely was blocked by the content filter** (3tease v2)

Symptom: Higgsfield's content filter blocked the generation before rendering ("a reference image or a phrase was flagged"); nothing was rendered.

Likely cause: with eight children in frame (start image and @tuitionboardclass), the prompt described them closely — girls and boys, pinafores, shorts, plaits, ages, "eye level of a seated child", "framed between the children's heads", "nudge each other", "shoulders shaking" — and also used L72 words ("barefoot", "grin") and an adult walking "close to him, half a metre". Children plus body, clothing or touch words trips the filter (see L93).

Rule:
1. When children are in frame, call them "the class" or "the pupils", "in school uniform", seated at their desks; no ages, no girl/boy breakdown, no clothing pieces, hair or body words, no touch or body movement words; let the reference image carry their look.
2. No camera height or framing tied to a child; name the adults as adults ("two young adults").
3. Re-run the L72/L89 word list on every prompt with children in it.
