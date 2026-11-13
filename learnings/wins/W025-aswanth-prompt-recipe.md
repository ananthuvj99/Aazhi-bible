---
id: W25
type: win
category: platform
shot: s16b-sh36 v4, s16b-sh37 v1.2, s16b-sh38 v3 (Aswanth)
author: Ranjith
date: 2026-11-13
---

**W25: Aswanth's prompt recipe gets good first takes. What his prompts do that ours did not** (s16b-sh36 aerial, s16b-sh37 fishing line, s16b-sh38 Clara and the photo)

Ranjith compared three of Aswanth's prompts that came out well with ours and asked for the logic to go into every prompt.

What his prompts do:
1. **SCENE CONTEXT** is short: the time, the place, the emotional situation in one line ("the cargo is delivered; the crew are relaxed"), then the shot in one sentence.
2. **Each reference line says who does what and where**: "@antony-at-20s: the ONLY man holding the wooden fishing stick, standing at the front rail, both hands on the stick." The reference carries the role, so the model cannot swap people.
3. **One block for the key thing**, named after it ("THE STICK AND BAIT", "THE ROOM AND THE PHOTO", "THE DECKHOUSE RAIL GAP"): built as a 1998 Kerala object would be, with size in cm or m, material, wear, how it is tied or held, and what is never seen ("only its plain white back is ever seen").
4. **CAMERA AND ACTION** in one block, by time: where the camera physically is (metres up, angle, distance, "just outside the front rail at chest height"), what is in frame and what is NOT ("only the front of the boat is in frame"), then what each person does in that segment.
5. **One "(most important)" block** for the hardest thing in the shot (the fish's behaviour, Clara's held-in tears). It is written as small observable movements of the body, never as an emotion word: "pectoral fins open out like brakes", "a film of water rises along the lower lid ... nothing runs down". Acting clichés are named and ruled out ("no crying face, no trembling chin, no open mouth").
6. **REAL-WORLD PHYSICS with numbers**: weight (about 30 tonnes of wood), speed (the fan turns about once a second), sizes, and cause and effect for every moving thing, ending "Nothing moves by itself; every movement has a cause."
7. **PERFORMANCE** short: "no two men move at the same moment", "eyes ... never on the lens", "Real skin, five fingers".
8. **LIGHTING** with colour temperature (about 2800K tungsten, 5600K sun) and the quality of light, and a **colour reference image** used for the grade only ("@returntone (colour reference only): match only its colour grade ... do not copy its framing").
9. **POSITIVE LOCKS** count everything ("Exactly three men, each once"; "one line; one hook").
10. **Nothing off screen is written into the prompt.** People out of view are not listed.

What ours did differently: a long MEMORY block and NOW lines listing people who are out of view; few numbers; no single "most important" block; the key prop or surface only in passing (that is how the rail went wrong, L152).

Recipe for every later prompt: `rules/prompt-rules.md`, "Aswanth's recipe (W25)".
