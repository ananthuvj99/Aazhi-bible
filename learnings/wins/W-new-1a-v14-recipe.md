---
id: W-new
type: win
category: platform
shot: "showreel 1A v14 (approved)"
author: Ranjith
date: 2026-11-04
---

**W-new — 1A v14 recipe: what to copy from an approved prompt** (showreel 1A v14, approved by Ananthu: "came out great")

Expands W5 (one line in `rules/lessons.md`) into a recipe any shot can reuse. Full prompt: `scenes/showreel/1A.md`, section v14.

Symptom (what came out well): a 15-second aerial flight over the coast, a match cut into the bedroom, and a slow smiling wake. The house, roof, the single church and the room all matched their sheets. The cover sheet showed the body under it, the sunlight was strong, and there was no music or added sound effect.

Cause (why it worked):
1. **SCENE tells the whole shot in one plain paragraph** before any detail: where, when, light, what moves, what ends the shot, "Nobody speaks".
2. **Every reference carries its time range** ("@houseout (0.0s–8.0s)", "@antonyroomc1plate (8.0s–15.0s)") and the details the model tends to drop, written into the tag line.
3. **WHAT IS IN FRAME lists everything allowed, per part** (exterior, interior) and ends "Every frame looks like the film itself, with nothing from the making of it."
4. **One block per place, named and timed** (THE FLIGHT 0.0–8.0s, THE ROOM 8.0–15.0s), written in layers (foreground, middle, distance) for the exterior and **in the plate's own frame orientation** for the room ("along the TOP of the frame", "RIGHT wall", "lower right", "top-left corner").
5. **Landmarks counted and placed once**, with what fills the other places ("exactly one white church… Along the near beach on the left there are only palms, boats and a few small huts").
6. **Props that must read get their own sheet and a contrasting colour** ("clearly a different cloth from the blue checked bedding"). Bedding is slept-in. A body under cloth is named part by part (chest, hips, both thighs, hollow between the legs, a raised knee that tents it, feet as bumps, one foot sticking out), with "never flat on the cot".
7. **Numbers instead of adjectives**: altitude in metres (40 → 20), speed in km/h (30 → 15), FOV per segment (84° → 63° → 47°), sun height (about 45°) and direction (south-east), 5600K, haze 5%, clock hands spelled out.
8. **CAMERA timed in phases with physical behaviour**: "smooth, weighted float… perfectly level, the faintest gentle drift, no shake"; "eases to a stop… soft, natural deceleration and holds". Exactly one cut, named (MATCH CUT at 8.0s), with "nothing else cuts".
9. **ACTION timed in 1.5–3 s beats**, with a still hold at the start and room to breathe at the end.
10. **PERFORMANCE as muscle and timing**: "a relaxed jaw, heavy eyelids, the smile arriving gradually and reaching his eyes before they open". **PHYSICS** gives weight and contact: the cot sags, the sheet catches on nose and chin, dust motes in the beams.
11. **Light written for strength**: "strong direct sunlight", "bold, sharp-edged stripes of sun and bar shadow", "the whole room glows with bounced sunlight"; highlights stay clean and the shade keeps detail.
12. **AUDIO bans music AND sound design** ("no riser, no whoosh, no swell, no rumble, no transition sound at the match cut… a steady level that does not build"), then gives a timed list of real sounds covering every second.
13. **STYLE describes the cinema-camera look by its qualities**: very wide dynamic range, clean low-noise shadows, soft highlight roll-off, accurate colour and skin, gentle filmic contrast, fine organic texture, "no over-sharpening, no glossy or video look". From 2026-11-04 it also names the camera, Sony Venice 2 (see `rules/prompt-rules.md`, "Camera").
14. **POSITIVE LOCKS restate only the few facts that must not drift**: references matched, the landmark count, the view direction, the end state of the key prop, "Nobody speaks", "Runs the full N seconds".
15. **Test at 480p, then re-render the same prompt and references at 1080p.**

Rule (the recipe to repeat): build every prompt in this order and to this level of precision (SCENE paragraph → timed references → WHAT IS IN FRAME → one block per place in the plate's own orientation → FIRST FRAME → FORMAT MODE → OPTICS → CAMERA → ACTION → PERFORMANCE → PHYSICS → LIGHTING → AUDIO → STYLE → POSITIVE LOCKS), using numbers for every distance, speed, angle, light and time. For dialogue shots, add the dialogue block and the Malayalam lock from `rules/prompt-rules.md`. Keep one camera set-up per generation (L37, L50) unless the shot is a single flowing move with one named cut, as here.
