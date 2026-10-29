# Lessons log

Format: symptom seen in a generation → cause → rule now applied to every prompt.
Newest at the bottom. Never delete an entry; mark it superseded if a later lesson replaces it.

**L1 — Thrown spoon became a coconut** (showreel 1, v3)
Cause: prop described as a "coconut-shell spoon"; the model latched onto "coconut".
Rule: never put a material name in a prop description when that material is itself an object. Describe size, shape, colour, material in neutral words ("small wooden spoon, 25 cm, thin handle, shallow oval bowl"). Lock: "the object that leaves her hand and the object that lands are the same".

**L2 — Two identical Jesus pictures in the bedroom** (showreel 1, v4) — evidence: `scenes/showreel/evidence/scene1-v2-duplicate-pictures.png`
Cause: one attached picture reference, placed loosely, got duplicated; the kitchen sheet itself has two Sacred Heart pictures, which bled into another room.
Rule: list wall dressing with exact counts and positions, taken only from that room's card. Never borrow a room's dressing from another room's sheet. If an object image is attached, attach it once and state its single position.

**L3 — Wall clock showed 12:00, not 7:45** (showreel 1, v4)
Cause: time written as "a quarter to eight".
Rule: spell out each hand ("short hour hand just before the 8, long minute hand pointing at the 9").

**L4 — Camera cannot pass through barred windows**
Cause: every window in Antony's house has iron bars.
Rule: push in to the window, then HARD CUT inside. Check the location card for bars before writing a through-window move.

**L5 — Lip-sync breaks**
Cause: speaker turned away, lying sideways, hand near face, or two speakers in one shot.
Rule: lip-sync block in every dialogue prompt; one speaker per shot; gestures and head turns only in pauses; soft frontal light on the speaking face.

**L6 — Over-packed single generation**
Cause: 16 s with three performers, a throw and three lines in one prompt.
Rule: one beat per shot, ideally 4–8 s. A shot with a line must give that line its own segment.

**L7 — Dialogue crossing a cut**
Cause: line start + duration ran past the HARD CUT time.
Rule: count syllables; every line ends at least 0.2 s before the next cut.

**L8 — Romanised dialogue risk**
Cause: Manglish in brackets beside Malayalam may be spoken as a second line.
Rule: Malayalam script only inside prompts.

**L9 — House location came out wrong in 1A** (showreel 1A)
Cause: the only house reference was a top-down cutaway with the roof removed; the model had no eye-level exterior or surroundings to match.
Rule: for exterior shots attach `@houseout` (environment) and `@housefullview` (elevations); never `@houseclean`/`@housemap`. Describe the surroundings from the card (headland, compound wall gap, beach and church to the east) in the LOCATION MAP.

**L10 — Sheets can disagree with each other** — OPEN
Example: the rear elevation shows a centre back door; the kitchen interior sheet has no north door.
Rule: when two sheets conflict, flag it to the user before writing a shot that shows that part; never silently pick one.

**L11 — Sunrise direction on the Kerala coast**
Cause: the house sheets mark the sea to the north/east, but Alappad faces the Arabian Sea to the west — the sun rises over the land and sets over the sea. A sun rising out of the sea would look wrong to a Kerala audience.
Rule: dawn shots put the sun low over the inland palm-covered hills; the sea is backlit, never the source of the sunrise. Sunsets go over the sea. Avoid compass words in prompts; describe the sun relative to camera and landmarks.

**L12 — Cameras cannot pass through a tiled roof**
Rule: an aerial move ends looking straight down at the roof; the next shot opens on a matching straight-down view inside the room (match cut in the edit). Same principle as L4 for barred windows.

**W1 — What worked: aerial flight + match cut in one generation** (showreel 1A v4, approved)
A 15 s timed multishot with an 8 s aerial flight ending straight down on the roof, a MATCH CUT to a straight-down interior, and a silent performance beat (sheet reveal → smile → shock) generated cleanly. Keep using: straight-down end frame matched to straight-down open frame; silent beats for lying-down faces.
