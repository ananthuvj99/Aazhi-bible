# Lessons log — moved

Every lesson and win is now its own file in `learnings/lessons/` and `learnings/wins/`, listed in `learnings/INDEX.md`. Lessons from every creator go there.

**Note 2026-11-04 — Antony room re-issued as a sheet + camera plates**
`@antonyroomclean` and `@antonyroommapped` are retired. Use `@antonyroom` (four views) plus the plate for the camera position (`@antonyroomc1plate`, `c3`, `c4`; see `locations/antony-room/cameras.md`). Describe the room in the plate's own frame orientation, and set the clock hands whenever C1 or C2 shows the clock.

**W4 — 1A v10 worked at 480p** (Ananthu: "pretty good")
Recipe: approved W1 structure + room described in the C1 plate's own orientation + no equipment words + "No music at all…" with timed sound effects + camera look described (not named). Test at 480p, then re-render the same prompt and references at 1080p.
Note: when the light feels weak, give the sun's height and direction, say "strong direct sunlight", "sharp-edged stripes", and that the room "glows with bounced sunlight".

**L47 — A cover sheet in the bedding's pattern disappears; made beds look fake** (1A v11) — evidence: `1A-v11-neat-sheet-merged.png`
The blue checked cover sheet merged with the blue checked bedsheet into one flat, neat bed with no body shape.
Rule: no cover sheet (L20 stands). Write bedding as slept-in: "crumpled and creased in every direction, twisted into folds around him, pulled loose at one corner and hanging over the edge; the pillow dented and askew". If a cover sheet is ever needed, give it a different colour and say it shows the body's shape.

**L48 — Landmarks get duplicated** (1A v11) — evidence: `1A-v11-two-churches.png`
The model drew the church twice.
Rule: give a count and a single position for every landmark ("exactly one white church, small in the distance beyond the headland, to the right of the house") and say what stands in the other places instead.

**L49 — "No music" still gets a riser; sheets lie flat** (1A v13) — evidence: `1A-v13-sheet-flat-no-body.png`
The model added a cinematic riser under the aerial move, and the cover sheet lay flat on the cot with no body under it.
Rules: in AUDIO also ban sound design — "no riser, no whoosh, no swell, no rumble, no transition sound; steady level that does not build". For a body under cloth, name each part the cloth rises over (chest, hips, thighs, the hollow between the legs, a raised bent knee that tents it, the feet as bumps) and say "never flat on the cot".

**W5 — 1A v14 approved** ("came out great")
What made it work: approved W1 structure; room written in the C1 plate's orientation; a dedicated prop sheet (@coversheet) in a colour that contrasts with the bedding; slept-in bedding; body under the cloth named part by part with a raised knee; one landmark with count + position; strong late-morning sun with direction and height; camera look described, not named; no music AND no sound design; tested at 480p first.

**L50 — A four-shot generation collapsed to 3 seconds** (1B v15) — evidence: `1B-v15-3s-collapsed.png`
The platform returned one 3-second wide shot from an 18-second, four-shot prompt — and the first shot copied the C1 plate's wide framing instead of the close-up.
Rule: four set-ups never go in one generation. Keep one camera set-up per generation; put beats that share a set-up into one continuous shot (eyes to the clock and the line, both overhead), and generate inserts (the clock) separately to cut in during the edit. Don't attach a wide room plate to a close-up.

**L51 — A clock prop sheet creates a second clock** (1B-1 v4) — evidence: `1B-1-v4-clock-on-back-wall-looks-at-camera.png`
With @wallclock attached as well as the room sheet (which already shows the clock), the model hung a clock on the back wall above the window — wrong wall, and he looked into the camera.
Rules: if the room sheet already shows a prop, don't attach the prop sheet too — point to where it hangs in the room sheet. State which walls have no clock (L23). For "looking at something while talking", put the object out of frame at a named corner and the face about 30° off the camera toward it.
**L52 — Continuity from a start frame** (1B-1 v4) — evidence: `1B-1-v4-sheet-changed.png`
Text alone could not hold the sheet's position from 1A. Attach the previous shot's last frames as a start image (@endframe1a) and say "the first frame matches it exactly".

**L53 — The plate decides where the camera stands** (1B-3 v3) — evidence: `1B-3-v3-cot-in-passage.png`
With @antonyroomc4plate (shot from the passage, looking through the door), the model used that view as the set and put Antony's cot in the passage, with a second cot seen in the room through the door.
Rule: attach only the plate whose camera position is where the shot is filmed from. For action inside a room, use an inside plate (C1/C3) and say "the camera stands inside the room; the doorway and passage are behind it and never seen; exactly one cot". Use C4 only for shots that look in from the passage.
