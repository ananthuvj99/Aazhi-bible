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

**L13 — Overacted shock** (1B v1) — evidence: `scenes/showreel/evidence/1B-v1-wrong-eyeline-overacted.png`
Cause: [scared] + "panic, wide eyes, stiff" read as a grimace.
Rule: write reactions understated and physical ("slight widening of the eyes, small lift of the brows, face stays relaxed, no grimace"). Prefer [worried]/[surprised] over [scared] for everyday surprises.

**L14 — No breathing room for the edit** (1B v1)
Rule: every shot holds still for 2–3 s at the start and 2–3 s after the last line or action. Write the holds as explicit timed segments.

**L15 — Prop placed outside the character's eyeline** (1B v1)
Cause: the clock was described on a side shelf he could not see from the pillow.
Rule: place any prop the character must look at where his body position lets him see it, and say so ("on the shelf directly above the head of the cot, seen by tilting his head back").

**L16 — Speaker addressed the wrong direction** (1B v1) — evidence: `scenes/showreel/evidence/1B-v1-looks-at-window.png`
Cause: camera placement left the door ambiguous, so he spoke toward the window.
Rule: put the camera at the thing the speaker addresses (stand it in the doorway he calls through). Lying-down lines go overhead so the face is upright to the lens (as in W1).

**L17 — Never add a prop the approved shots and sheets don't have** (1B v3 → v4)
Cause: an alarm clock was added for a time cue, but it is not in the room sheet and was not seen in the approved 1A.
Rule: props come only from the location card or the approved shots. If a story beat needs a cue (time of day), use what is already there — light, sound, sun through the window — or ask the user before adding a prop.
Update: Ananthu then added `@wallclock` with a sheet and a marked position — a prop becomes valid once it has a card, a sheet and a placement.

**L18 — Platform error on a long prompt** (1B v6) — SUPERSEDED by L19: v7 at 5,300 chars failed the same way, so length was not the cause. Keeping prompts compact is still good practice.
Symptom: generation failed with an error. Measured: 1A v4 (worked) 6,985 chars; 1B v1 (worked) 6,132; 1B v6 (error) 9,468.
Suspected cause: prompt length limit, likely ~8,000 characters.
Rule: keep prompts under ~6,500 characters — short HOUSE LAYOUT, minimal reference lines (the sheet carries the look), no repeated descriptions across blocks. Confirm the limit with the platform team.

**L19 — "Invented location_id not in allow-list"** (1B v6, v7) — evidence: `scenes/showreel/evidence/1B-v7-error-invented-location-id.png`
Symptom: platform error at "Understanding the prompt (OpenAI)": the planner returned a location_id that is not in the project's allow-list.
What changed vs. working prompts (1A v4, 1B v1): the HOUSE LAYOUT block naming other rooms (veranda, passage, kitchen, mother's bedroom), a second location tag @hallclean, and the new tag @wallclock.
Suspected cause: the planner maps every location it reads to a location ID; rooms that are named but not attached (or a tag not registered as a location) get an invented ID and are rejected.
Rule (until the dev team confirms): one location tag per generation; describe only the room on screen; never name other rooms; register every tag before use. HOUSE LAYOUT block suspended.
Questions for the dev team: (1) Does the planner create a location for every room named in the text? (2) Is @hallclean registered as a location? (3) What type is @wallclock (character/prop/location)? (4) Can one generation use more than one location?
Update (L19): the hall tag is registered as `@hallclean`, not `@hall_clean` — an unregistered location tag is the most likely trigger for the invented location_id. Rule: copy tags exactly as registered on the platform (IDs = sheet names with no spaces and no underscores).

**L20 — Bedding continuity** (1B v9) — evidence: `scenes/showreel/evidence/1B-v9-overhead-no-bedsheet-cover-sheet.png`
Approved 1A shows the cot made up with a faded blue checked bedsheet and pillow, and Antony on top of it. v9 showed a bare rope cot and a sheet over him.
Rule: the cot is always made up with the blue checked bedsheet and pillow; Antony lies on top, nothing covering him. Continuity is what the approved generation shows, not what an earlier prompt said.

**L21 — Wide framing kills lip-sync** (1B v9) — evidence: `1B-v9-doorway-bed-wrong-clock-wrong-marked.png`
His shout was delivered in a wide doorway shot; the face was too small for the lip-sync tool.
Rule: wide shots are for blocking only. Every line goes to an MCU with the face at least a third of the frame height. Also write "moderate mouth movement, no gaping or yawning".

**L22 — Furniture orientation must be stated relative to the frame** (1B v9)
The cot came out pointing at the camera (head against the far wall). Ananthu marked it sideways across the frame.
Rule: for every camera position, state how the furniture runs in frame ("runs sideways across the frame, long side facing the camera, head end at screen-right").

**L23 — Clock on the wrong wall** (1B v9)
The clock appeared on the far wall facing the door. It belongs on the front wall beyond the foot of the cot.
Rule: name the wall that holds the prop AND name the walls that don't ("the far wall seen from the door carries no clock").

**L24 — Off-screen dialogue confuses lip-sync**
Rule: every spoken word on camera with the mouth visible; split a line around an insert rather than voicing it over the insert.

**L25 — Talking to camera while walking feels fake** (1C v4)
Rule: for natural dialogue, keep the speaker busy with a task and their eyes on the task; satisfy lip-sync by placing the camera where their face already points (e.g. beside the stove facing a cook), not by having them look into the lens. Face toward the lens ≠ eyes on the lens.

**L26 — Entrances from the wrong room** (1D v2) — evidence: `scenes/showreel/evidence/1D-v2-mother-wrong-entrance-sandals.png`
Rosamma appeared from a bedroom instead of the kitchen, and wore sandals indoors (the sheet shows sandals).
Rule: when a character enters, show them IN their origin room in the first frame (visible through the doorway) and walk them out; name the doors that stay empty. Lock footwear explicitly whenever the sheet differs from the scene (Rosamma barefoot indoors).

**L27 — Everything written in a prompt is a candidate to be drawn** (1C v5, 1D v3) — evidence: `1C-v5-clock-leaked-into-kitchen.png`, `1D-v3-meet-in-kitchen-doorway.png`, `1D-v3-conversation-jumps-to-bedroom.png`
Symptoms: the wall clock (described only in the HOUSE LAYOUT and CONTINUITY blocks as being in Antony's room) appeared in the kitchen. In 1D, Antony emerged near the kitchen and the conversation cut jumped into his bedroom because @antonyroomclean was attached for a later cut.
Cause: the model cannot tell "background knowledge about the house" from "things to show". Every object, room and reference in the prompt bleeds into every cut.
Rules:
1. Two layers. Continuity lives in the bible (ledger, cards). The prompt carries only what is VISIBLE in this shot. No global HOUSE LAYOUT block; no mention of rooms, props or people the camera does not see.
2. Every cut starts with a location line: "CUT 2 — LOCATION: the central passage, same spot as cut 1 (not a bedroom, not the kitchen)".
3. Each reference is assigned to its cut: "@antonyroomclean — cut 3 only".
4. List exactly what is in each room on screen ("this kitchen contains only: ...").
5. Split generations at location changes whenever a line of dialogue is involved. One location per generation is the reliable default; multi-location only for silent transitions. The edit stitches the generations.

**L28 — Dialogue generated in English** (1D-a v2)
Cause: the prompt is written in English and the compact AUDIO line stated the language only once, in passing; the model voiced the lines in English.
Rule: state the spoken language four times — a SPOKEN LANGUAGE line under SCENE, "speaks only Malayalam" in the speaker's reference line, "says his line in Malayalam" in each ACTION line, and "Malayalam only … the exact Malayalam words in quotes … no English, no translation" in AUDIO — plus a lock in POSITIVE LOCKS.

**L29 — English paraphrase of the dialogue gets voiced** (1D-a)
Suspected cause: the SCENE paragraph summarised the lines in English ("he tells her he is going to sea today and must quickly go and bathe"). The platform's dub planner reads the whole prompt and can take that English summary as the line to speak.
Rule: never paraphrase or translate dialogue anywhere in a prompt. Describe speech only as "says one Malayalam line" / "answers with one Malayalam line"; the only words that can be spoken are the Malayalam text in quotes in AUDIO. English meanings live in the repo plan, not in prompts.

**L30 — Rushed, short, unnatural** (1D-a v4)
Symptoms: output ended at 7 s, action felt fast, cuts felt rough.
Rules: (1) set the platform duration and say "the video runs the full N seconds; quiet moments fill the gaps"; (2) at most two or three shots per 15 s generation; (3) slow, everyday pacing written in — "unhurried", "a slow breath", holds between beats; (4) prefer a slow camera push between lines over extra cuts; (5) let the listener keep working (mother keeps cooking) instead of turning to face the speaker.

**L31 — Characters don't travel between zones on cue** (1D-a v6) — evidence: `1D-a-v6-mother-stayed-in-kitchen.png`
Prompt had Rosamma start in the kitchen doorway and walk to the middle of the passage in 2.5 s; with @kitchenclean tagged and the first frame built around the kitchen door, the model kept her in the kitchen.
Rule: start every character in the frame already where the dialogue needs them. Only add a walk-in when the walk is the point of the shot, give it its own shot and time, and don't tag the room they leave.

**L32 — Reverse-angle backgrounds must be named** (1D-a v6) — evidence: `1D-a-v6-wrong-background-behind-antony.png`
The over-the-shoulder shot showed a blank wall behind Antony. In the passage, the reverse angle toward the front of the house sees the open front door and the veranda.
Rule: for every reverse angle, state what is directly behind the person in frame using the house map, and tag that place as "(shot N only, background only)".
