# Writing camera movement for AI video models

How text-to-video and image-to-video models (Seedance, Kling, Veo, Runway, Sora, Wan and others) read camera language, why they fail, and how to write moves they execute. If the project has its own prompt-writer skill, its house rules win where they differ.

## Contents

1. How models understand camera movement
2. The ten writing rules
3. Measurements and vocabulary
4. Lens and FOV in prompts
5. Image-to-video specifics
6. Dialogue and identity protection
7. Common failures → causes → fixes
8. Templates
9. Reliable phrasing per move
10. Testing without burning credits

---

## 1. How models understand camera movement

- Models learned camera language from huge amounts of real footage, so standard terms (push in, dolly, pan, tilt, crane, tracking, orbit, handheld, aerial) are recognised. But a camera prompt is not a camera API: the words steer a probability, they don't drive a rig. Anything left ambiguous, the model fills in with the most common version it has seen.
- The most common version is often wrong for you. A "pan" becomes a sideways glide; a "dolly zoom" becomes a plain push; "static" gets a slow drift; "handheld" becomes phone jitter.
- Models are good at what they've seen a lot: slow pushes, tracking walks, aerial reveals, static frames with natural motion. They're weak at rare or compound moves: dolly zooms, full orbits around faces, rolls, precise timed sequences.
- The visible result is what the model learns from. Describe what the audience sees ("his face stays the same size while the street behind him rushes closer"), not just the technique's name.

## 2. The ten writing rules

1. **One dominant move per shot.** Two axes at most (push + rise, follow + slight tilt). Prompting guides across models agree on this. Split anything more complex into timed phases or separate shots.
2. **Say rotate or travel.** "The camera stays in place and turns…" versus "the camera travels sideways, staying parallel…". This single distinction prevents most failures.
3. **Write it like a grip would rig it:** start frame, path, direction, speed, stop frame, duration, height, distance, lens.
4. **Lock stillness in words.** "Locked-off, the frame stays perfectly still for the whole shot." Repeat it once in the prompt's locks.
5. **Give the move something to reveal.** Name foreground, midground and background separately; that's where parallax comes from. Flat backgrounds produce flat video.
6. **Describe the visible result of optical tricks.** Zooms, dolly zooms and rack focus are defined by what changes on screen.
7. **Give it weight.** "Eases in over one second, glides, settles; smooth, weighted, no micro-jitter." For handheld, give the sway in cm and call it slow and heavy.
8. **Left and right are from the camera's point of view.**
9. **Positive phrasing only.** State what happens ("stays level", "keeps her centred"), not what must not happen.
10. **Write the look, not the gear.** Camera, lens, rig brand and film titles get ignored or derail the move. Generic move words are fine.

## 3. Measurements and vocabulary

| Quantity | How to write it | Example |
|---|---|---|
| Travel speed | km/h | "travels forward at 0.5 km/h" |
| Rotation | degrees over seconds | "pans 60° to the right over 5 seconds" |
| Height | metres from the ground | "eye level 1.5 m", "rises from 1.5 m to 6 m" |
| Distance | metres to the subject | "2 m from her face" |
| Duration | seconds, or timecodes | "over 6 seconds", "0–3 s: …" |
| Shake | cm of sway, and its tempo | "slow 2–3 cm sway", "jolts 5–8 cm with each impact" |
| Lens | FOV in degrees from the anchor table | "29° FOV" |
| Focus | distances of both planes and the time | "from 0.5 m to 4 m over 1.5 seconds" |
| Time speed | multiples of real time | "five times slower than real time" |
| Atmosphere | percent and metres | "fog density 30%, visible from 10 m" |

Useful vocabulary: *eases in, glides, settles, creeps, drifts, rises level, travels straight, stays parallel, keeps her centred, holds, locked-off, breathes, jolts, rolls, arcs, circles, sweeps, passes through.*

## 4. Lens and FOV in prompts

Use only these steps (full-frame equivalents), never in-between values:

| FOV | ≈ Lens (FF) | Feel |
|---|---|---|
| 180° | fisheye | distorted POV, dream |
| 107° | 14–16mm | huge interiors, epic establishing |
| 84° | 20–24mm | wide, immersive, groups |
| 63° | 28–35mm | observational, walk-and-talk, handheld |
| 47° | 40–50mm | neutral human view |
| 29° | 75–85mm | dialogue singles, portrait |
| 18° | 100–135mm | close portrait, isolation |
| 12° | 180–200mm | details from afar |
| 8° | 300–400mm | extreme compression, surveillance, heat haze |

For multi-shot prompts, give the FOV per segment and add "no drift mid-segment."

## 5. Image-to-video specifics

- The first frame decides where the move starts. Make sure the move is possible from that frame: a push-in needs space to travel; a reveal needs something off-frame to reveal, which you must describe.
- Keep motion text short and specific. Image-to-video adheres better to a concise movement line than to a long description of the image (which it already has).
- Don't redescribe what the image shows in conflicting words; describe only what changes.
- For a reveal or pull-out, describe in order what enters the frame, or the model invents it.

## 6. Dialogue and identity protection

- The speaker's face stays readable to the lens through every line: three-quarter or frontal, never turning away mid-line, never covered by a passing object.
- During lines, hold or push slowly. Make the bigger moves between lines.
- Arcs around a face: ≤ 90° per phase. Full orbits: four timed quarters, constant distance and height, naming what's behind the subject at each quarter.
- Fast moves past faces (whips, crash zooms) blur identity. Land and settle before the face matters.
- Wide lenses very close to faces distort features. Use 63° or narrower for close faces unless the distortion is the point.

## 7. Common failures → causes → fixes

| What you see | Cause | Fix |
|---|---|---|
| Static shot drifts or pushes | stillness not stated | "locked-off, the frame stays perfectly still"; repeat in locks |
| Pan became a sideways glide | rotate/travel ambiguity | "the camera stays in place and turns" |
| Truck became a pan | same | "travels sideways, staying parallel, does not turn" |
| Pedestal became a tilt | same | "rises level from 1.0 m to 1.6 m" |
| Zoom became a dolly | optical move not described | "camera position stays fixed; the background flattens" |
| Dolly zoom became a push | rare move, named only | describe the subject staying the same size and the background changing; give start and end FOV |
| Whip pan became a hard cut | blur too short | give 0.5–0.8 s of horizontal blur |
| Face changes during orbit | arc too large | ≤ 90° per phase; frame wider; name the background per quarter |
| Subject shrinks or collides in a follow | speeds not matched | one shared speed and a fixed distance |
| Handheld looks like a phone | no amplitude | "slow, heavy 2–3 cm sway" |
| Move feels weightless or "CG" | no easing | "eases in over one second, settles" |
| Reveal shows the wrong place | reveal not described | list in order what enters the frame |
| Model adds cuts | cuts not controlled | "one continuous shot, the camera does not cut on its own" |
| Both planes sharp in a rack focus | distances missing | give both distances and which goes soft |
| Horizon perfectly level at sea | roll not stated | give roll angle and period |
| Slow motion speeds up mid-shot | mixed speeds in one shot | one speed per shot; cut between speeds |
| Background sharp despite "shallow focus" | falloff not described | "everything beyond 2 m dissolves into soft blur" |

## 8. Templates

**Single shot camera block**
```
OPTICS — [shot size], [FOV]° FOV, [depth-of-field look]; [layers: foreground / midground / background].
CAMERA — [height] m, [distance] m from [subject]. The camera [stays in place and turns | travels] [direction from the camera's view]
at [speed] over [duration], [easing]. Starts on [start frame]; ends on [end frame]. Focus [behaviour].
[Weight / shake]. [What moves inside the frame].
```

**Timed multi-phase move**
```
One continuous shot, the camera does not cut on its own.
0–3 s: [phase 1 — one move, start and end frame].
3–7 s: [phase 2].
7–10 s: [phase 3 — settle and hold].
```

**Sequence of cuts**
```
CUT 1 — [size, FOV, camera behaviour]. No drift mid-segment.
CUT 2 — …
Cuts only at the specified points; the camera does not cut on its own.
```

## 9. Reliable phrasing per move

| Move | Phrasing that executes reliably |
|---|---|
| Static | "locked-off, the frame stays perfectly still for the whole shot" |
| Living frame | "the frame stays still while rain / smoke / curtains / crowd move [direction, speed]" |
| Creep | "creeps forward at 0.2 km/h, barely perceptible, from MS to MCU over 10 seconds" |
| Pan | "stays in place and pans 60° to the right over 5 seconds, from A to B" |
| Whip pan | "a horizontal whip to the right blurs the frame for 0.6 seconds and settles on B" |
| Tilt | "fixed position, tilts up 50° over 4 seconds from his boots to his face" |
| Roll | "rolls 180° clockwise over 6 seconds; he ends upright, the room upside down" |
| Zoom | "position fixed, view narrows from 47° to 29° over 8 seconds, the background flattening" |
| Rack focus | "focus shifts over 1.5 seconds from the cup at 0.5 m to the man at 4 m; the cup melts into blur" |
| Dolly zoom | "travels toward him while the view widens from 29° to 63°; his face stays the same size while the corridor stretches away" |
| Push-in | "travels straight toward her at 0.5 km/h for 6 seconds, MS to CU, easing in and out" |
| Pull-out | "travels straight back at 1 km/h; as it does, [A], then [B] enter the frame" |
| Truck | "travels sideways to the right at 2 km/h, staying parallel 3 m away; it does not turn" |
| Follow / lead | "leads him, travelling backward at 4 km/h, 2 m ahead at chest height, matching his pace" |
| Arc | "arcs 70° to the left around her at 3 m, eye level, over 5 seconds" |
| 360° orbit | four timed quarters (see library) |
| Pedestal | "rises level from 1.0 m to 1.6 m over 2 seconds" |
| Crane | "rises from 1.5 m to 6 m over 6 seconds, tilting down to keep her centred; the town is revealed below" |
| Handheld | "handheld at chest height, slow heavy 2–3 cm sway, reframing half a beat late" |
| Floating walk | "glides behind her at 4 km/h, 2 m back, gentle 1 cm float with each step" |
| Aerial | "stable aerial, 40 m above the coast, flying forward at 25 km/h, slowly tilting down" |
| Slow motion | "slow motion, five times slower than real time" |
| Oner | "one continuous shot, the camera does not cut on its own" + timed phases |

## 10. Testing without burning credits

- Test the move at the shortest duration the model allows before generating the full shot.
- Change one variable at a time (speed, then FOV, then distance).
- If the same defect shows up in every batch, the problem is the prompt or the reference, not luck. Rewrite rather than regenerate.
- When a compound move keeps failing, split it into two generations joined by a cut or a hidden stitch.
- Keep a note of phrasings that worked on your model; models differ, and your notes beat any general guide.
