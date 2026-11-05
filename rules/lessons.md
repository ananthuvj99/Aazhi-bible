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

**L54 — Stiff, angry, to-camera delivery** (1B-3 v4) — evidence: `1B-3-v4-stiff-to-camera.png`
A speaker with nothing to do sits still and stares into the lens; [annoyed] read as anger.
Rules: give the speaker a real task during and around the line, kept below the face (re-tying a mundu, folding a sheet) and a human beat before it (hands in the hair, a long breath) — L25. Put what they talk to (a door, a person) just off frame and say "never looks into the camera at any moment". Describe the relationship tone ("the way a son grumbles to his mother") and prefer [worried] over [annoyed] for family complaints.

**L55 — Say which way the off-screen person is, and which way is wrong** (1B-3 v6) — evidence: `1B-3-v6-looks-at-window.png`
"Toward the door" was not enough: he looked toward the bright front window. And [worried] made a call across the house sound sad.
Rules: name the off-screen person's direction on screen ("the kitchen is to screen-right, out through the door") and name the tempting wrong direction ("never toward the window"). A call to another room is loud: describe it as projected and use [shouts], with "not angry, not sad".

**L56 — "Eyes on her work" made the call quiet** (1C v8)
With her eyes on the pot the model played it as quiet talk to herself. For a call to another room, she must turn and look toward where the other person is, and the camera goes where that look lands (here K1, the passage doors) so her face stays within 30° of the lens.

**L57 — [shouts] changed the emotion; the passage grew extra rooms** (1CD-single v1)
[shouts] turned a teasing mother into a shouting one. Loudness belongs in words ("loud enough to carry, with a smile in her voice"); the tag carries the emotion ([playful]). Describe each line's delivery separately.
A passage described loosely grows doors and corridors. Count them: "exactly two bedroom doors facing each other, kitchen doors at one end, front door at the other — no other doors, rooms or corridors". The house plan (@houseclean) may be attached as layout only, never shown.

**L58 — Two people, three shots, five references, 17 s: everything broke** (1CD v3.3) — evidence: `1CD-v3-wrong-rooms-no-dialogue.png`
The platform returned 15 s (its cap — 17 s was cut), put the mother in the passage, had Antony come from the wrong way, ended on two backs, and spoke no dialogue at all.
Rules: never ask for more than 15 s. One generation = one camera set-up and one speaker. Don't attach a plate of a space we only glimpse (the passage through the doors) — the model builds the scene there; use the plate that already contains it (@kitchenc2plate shows the passage). Two-person dialogue = separate generations, joined in the edit.

**L59 — "The passage doors" became a door to the outside** (1C-a v1)
The kitchen also has side doors to the yard; with the camera placed only by words, the model came in from one and she looked outside. Fix: start the move in the passage (@hallclean, whose centre shows the kitchen through the double doors) and say how many doorways the room has and which one is meant.

**L60 — A continuity frame that shows a character puts her in the shot** (1C-b v3.2) — evidence: `1C-b-v3-long-walk-twoshot.png`
With @endframe1ca (showing Rosamma) attached, she appeared in frame, still looking down the passage as at the end of 1C-a, and the scene became two profiles. The long passage walk also ate 10 s.
Rules: if a continuity frame shows someone, either keep them in the shot on purpose (over-the-shoulder, from behind, with their new action stated — "eyes on the pot, never toward the passage") or don't attach it. Skip long walks inside dialogue clips; start the speaker where the line happens (L31).
