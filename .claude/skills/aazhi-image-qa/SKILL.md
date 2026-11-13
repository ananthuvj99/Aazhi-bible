---
name: "aazhi-image-qa"
description: Continuity QA and score for every reference IMAGE in AAZHI / Techjays showreel work — plates, props, character sheets, start frames, crops and mirrored or recut images — before it is shown to the creator for approval and before it is saved to the repo. Use it unprompted whenever an image is generated (Higgsfield or any tool), cropped, mirrored, recut or handed over by a creator to be registered, and whenever the user asks "does this image match", "check the image", "score the plate", "is this the same uru / room / costume". It compares the new image element by element with every registered reference it must agree with (INDEX.md cards, the continuity ledger, the previous shots' kept frames, cameras.md), scores it out of 100 with continuity as the main weight, and says what to fix or regenerate.
---

# AAZHI Image QA — "does this image match everything it must match?"

The video model copies what a reference image shows. A plate with the wrong boat, a sheet with a different face or a frame with the door on the wrong side breaks continuity in every shot that attaches it. Your job: catch that **before** the image is approved, saved or uploaded.

Continuity is the basis of the score. A beautiful image that does not match the film's references fails.

## Step 1 — Gather what the image must match

In the repo (pull `main` first; in own-branch mode merge `origin/main`):
1. What the image is: plate (which camera position), prop, character look, start frame, crop of a creator's sheet.
2. Every registered asset that appears in it or must agree with it, from `INDEX.md` and each `card.md`: the location's other plates, the hero props (e.g. `@uru`, `@antonybag`), the characters' sheets.
3. The location's `cameras.md` (where this camera stands, what is on which side), and the screen direction of the shots around it (L68).
4. The continuity ledger (`continuity/showreel.md`): carry-forward lines, time of day, light direction, states (L67).
5. The kept/approved frames of neighbouring shots (`scenes/showreel/approved/`).
6. The creator's source image if this was made or cropped from one.

Open and look at every one of these images side by side with the new one. Never score from memory or from the card text alone.

## Step 2 — Check element by element

For each recurring element, mark ✅ match · ⚠️ close but different · ❌ different:
- **Identity of recurring things:** the same vessel (hull colour, rust, waterline, bow shape, mast count, deckhouse), the same buildings (roof, storeys, shutters, wall colour), the same room fixtures, the same face, costume item by item, prop shape and colour.
- **Geography and screen direction:** what is on the left and right, which way the vessel points, door and window sides, compared with `cameras.md` and the neighbouring shots.
- **Scale:** sizes against people, doors and each other (a 25–30 m uru stays bigger than a canoe; a bag stays about 40 cm).
- **Time and light:** time of day, sun side, colour of light, haze, compared with the ledger and the neighbouring plates.
- **Period and place:** 1998 Kerala (or 2026 where the story is there): Latin Catholic details, no modern objects, Beypore uru never a fishing boat.
- **Clean plate rules:** no lettering, signs, flags or labels (L40); no people unless the plate is meant to carry them (L60); no grid, panel titles or watermark; not a labelled map (L9).
- **Photoreal and usable:** photoreal film look (not painterly or CG), sharp enough to read the key elements, framing that matches the intended camera (L53).

## Step 2b — Logic gap finder (Ranjith, 2026-11-12; every image, every time)

Look at the image as the audience will, and ask what logically **must** be there and what logically **cannot** be there, given the story, the shots around it and the real world. Write each finding as a gap. A logic gap on a story element is a ❌, however well the image matches its references.

- **Sky and physics:** one sun or moon per scene, in the place the continuity sheet gives (L142). A view that looks away from it has no sun or moon in the sky; a view toward it shows it with its path or glare. The phase and shape are right for the story and the place (a full moon is round; near the equator a crescent lies on its back, L139). Shadows fall away from the light; reflections are on the light's side; there is a lantern flame where lantern light falls.
- **What the moment needs:** everything the dialogue or action refers to is there and readable. If Clara says "look at the board and write", the board has sums on it (L134); if a man is "at the wheel", he is visible at the wheel; if the crew are asleep on the deck, someone looking at that deck sees them (L145).
- **Reference images carry their sky too:** a prop or character image attached to a shot must not hold a sun, moon or sky that contradicts the scene (the @burningvallam image carried a crescent into the full-moon night); clean it or use a clean copy.
- **Eyelines point at their cause (Ranjith, 2026-11-12):** anyone reacting to something (the fire, a shout, a person) has his face and gaze pointed at it, in the direction the map gives. A look at the wrong side, at the camera or at the moon is a ❌ (K4 had Antony astonished while looking back over his right shoulder, away from the fire on the left).
- **What must not be there:** the moon in an aft view, a person who is below or not yet aboard, a second copy of anyone, people inside a room they are outside of, an object from a later shot.
- **Inside and outside, front and back:** who is in which room, on which side of a door, rail or window; screen sides match the previous shot.
- **New angles (L146):** if this image is a new angle, reverse or next start frame of a set already shown, a measured map exists (`*-sightlines.json`) and `tools/sightlines.py` was run for this camera; every person matches its table (hidden people absent, backs as backs, sides as mapped). No map yet: make one before scoring.
- **Cross-plate check (L147):** when several plates or keyframes show the same set in one shot or sequence, compare them with each other: mast position, sacks, lanterns, rigging, rails, each person's clothes and tell-apart detail (Raghavan's towel at his NECK, Babu's on his HEAD). Any disagreement is a ❌.
- **Head count and identity:** count the people; each one is a different, named person from his own sheet. Two people merged into one, or one missing, is a ❌ (L145).
- **Real, not illustrated:** wood grain, skin, cloth and light read as a photograph from a film; a toy-like, painted or CG look is a ❌ for any plate or start frame (L122).

Report the gaps in a `Logic gaps:` line (or "none found"). Any open gap on a story element means **Fix first**, whatever the score.

## Step 2c — No "minor" findings (Ranjith, 2026-11-12, L152)
Every mismatch found in Step 2 or 2b is fixed (edit or regenerate) before the image is shown for approval. Never label a finding "minor" and pass the image: a rail, surface, prop, costume detail or light that differs from the approved takes is a fail until fixed. Close-ups that show any part of the set are made with an approved frame of that set attached. If a fix still fails after a few tries, say so plainly and ask.

## Step 2d — Draw every eyeline (L154)
For every person in a keyframe who should be looking at something, draw a line from the eye along the gaze. It must hit the target (the far light, the speaker, the door). If it lands anywhere else, the image fails and is fixed before it is shown.

## Step 3 — Score

| Area | Points | How |
|---|---|---|
| Identity of recurring elements | 35 | proportion matching; any ❌ on a hero element (main vessel, character face, costume) = 0 for this area |
| Geography and screen direction | 20 | sides, facing, layout vs cameras.md and neighbouring shots |
| Time, light, period | 15 | time of day, sun side, palette, period details |
| Scale | 10 | sizes consistent with the references |
| Clean-plate rules | 10 | deduct 5 per lettering/flag/label, 5 per unwanted person or grid |
| Photoreal and usable | 10 | photoreal, resolution, framing |
| Logic gaps (Step 2b) | cap | any open gap on a story element caps the score at 79 (Fix first) |

Verdict: **90–100 Matches** (save) · **80–89 Matches with small drift** (save; note the drift in the card and write it away in prompts) · **65–79 Fix first** (recut, edit or regenerate before saving) · **below 65 Reject**.

## Step 4 — Report (short) before asking for approval

```
IMAGE QA — <file / proposed ID>  ·  Continuity score NN/100  ·  <verdict>
Compared with: @… , @… , <kept frame>, cameras.md <camera>
✅ … · ⚠️ … — what differs · ❌ … — what differs
Logic gaps: … (or "none found")
Eyelines: <person> → <target> ✅/❌ (line drawn from the eye; one line per person in frame, L154)
Props and surfaces vs the latest approved frame: ✅/❌ each (L151, L152)
Drift to write away in prompts: …
Fix: … (every ❌ is fixed before approval; no "minor")
```

**Every plate, keyframe, start frame and crop gets this QC, every time, for every creator (Ranjith, 2026-11-13).** No image goes to the creator or into a prompt without it, and the eyeline line is never skipped.

Show this with the image when asking the creator to approve it. A hero-element ❌ always goes to the creator, whatever the total.

## Step 5 — Record it

When the image is saved:
- Write the report to `scenes/showreel/image-qa/<file-name>.md` (one file per image) and add `continuity_score: NN` to the asset's `card.md` frontmatter.
- Commit it with the asset (`<Name>: asset: …`), so the score travels with the image.
- If a take later shows the image misled the model, log a lesson (L-number from `learnings/INDEX.md`) and add the missed check to Step 2 here.
