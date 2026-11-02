---
id: L27
type: lesson
category: elements
shot: "1C v5, 1D v3"
author: Ananthu
date: 2026-10-29
---

**L27 — Everything written in a prompt is a candidate to be drawn** (1C v5, 1D v3) — evidence: `1C-v5-clock-leaked-into-kitchen.png`, `1D-v3-meet-in-kitchen-doorway.png`, `1D-v3-conversation-jumps-to-bedroom.png`
Symptoms: the wall clock (described only in the HOUSE LAYOUT and CONTINUITY blocks as being in Antony's room) appeared in the kitchen. In 1D, Antony emerged near the kitchen and the conversation cut jumped into his bedroom because @antonyroomclean was attached for a later cut.
Cause: the model cannot tell "background knowledge about the house" from "things to show". Every object, room and reference in the prompt bleeds into every cut.
Rules:
1. Two layers. Continuity lives in the bible (ledger, cards). The prompt carries only what is VISIBLE in this shot. No global HOUSE LAYOUT block; no mention of rooms, props or people the camera does not see.
2. Every cut starts with a location line: "CUT 2 — LOCATION: the central passage, same spot as cut 1 (not a bedroom, not the kitchen)".
3. Each reference is assigned to its cut: "@antonyroomclean — cut 3 only".
4. List exactly what is in each room on screen ("this kitchen contains only: ...").
5. Split generations at location changes whenever a line of dialogue is involved. One location per generation is the reliable default; multi-location only for silent transitions. The edit stitches the generations.
