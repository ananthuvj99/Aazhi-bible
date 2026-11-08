# Camera, lens and rig

Decide these in planning; write only their visible result into an AI prompt.

## Contents

1. Camera body profiles
2. Lens set ↔ FOV
3. Observer or participant: lens + distance
4. Depth of field
5. Rig builds
6. Frame rate and slow motion
7. Aspect ratio and movement
8. Never write in a prompt

---

## 1. Camera body profiles

Use the camera the project names. If none, use the default.

### Default — heavy full-frame digital cinema camera
- **Sensor:** full-frame (about 36 × 24 mm), so the FOV table below maps directly onto real focal lengths.
- **Weight:** heavy once built (lens, matte box, battery, monitor). Every move has inertia: eases in, glides, settles.
- **Look in words:** "large-format look: wide latitude, the bright sky holds detail while faces in shade stay clean; gentle highlight roll-off; natural skin tones; shallow, gradual depth falloff."
- **Rigs that make sense:** tripod, dolly, slider, crane, telescopic crane, floating walk rig, large gimbal, shoulder rig with support, heavy-lift drone, vehicle mounts, water housing.
- **Rigs that don't:** FPV drones, tiny body-mounts (use a separated-sensor build or flag the exception).

### Profile — Sony VENICE 2 (8.6K sensor block)
Checked against rental-house and retailer specs.
- Full-frame CMOS about 35.9 × 24.0 mm, 8640 × 5760; 16 stops of latitude; dual base ISO 800 and 3200.
- Built-in ND: clear plus 0.3–2.4 (1–8 stops). Shallow depth of field stays possible in harsh daylight.
- PL mount with E-mount underneath; internal X-OCN raw and 4K ProRes; electronic rolling shutter.
- Body about 4.3 kg alone; a full build is several times that.
- Frame-rate ceilings (approx.): 8.6K 3:2 open gate 30 fps; 8.2K 17:9 60 fps; 8.2K 2.39:1 72 fps; Super 35 crop 5.4K 16:9 90 fps and 5.5K 2.39:1 120 fps. Super 35 crop makes lenses look about 1.5× longer; pick the next FOV step narrower.
- A separated-sensor extension (Rialto-style) lets the sensor and lens go on small gimbals, into cars, cabins and tight rooms.
- **Look in words:** "wide-latitude large-format look; deep, clean shadows with detail even in lamp light; soft highlight roll-off; natural, warm-leaning skin."

### Lighter bodies (mirrorless, compact cinema, phones, action cams)
- Easy on gimbals, drones, body mounts, cars and FPV; less inertia, so moves look lighter and quicker.
- Smaller sensors give deeper focus at the same FOV.
- **Look in words:** describe the texture honestly ("documentary immediacy", "found-footage phone look") when that is the intent.

## 2. Lens set ↔ FOV

The DOP thinks in eight focal lengths. Each lands on a step of the prompt FOV table (full-frame):

| Lens (FF) | FOV in prompt | Typical use |
|---|---|---|
| 16mm | 107° | interiors made huge, epic establishing, wide-lens-close immersion |
| 24mm | 84° | establishing, groups, immersive handheld |
| 35mm | 63° | observational, walk-and-talk, handheld coverage |
| 50mm | 47° | neutral human view, medium shots, two-shots |
| 85mm | 29° | dialogue singles, portrait |
| 135mm | 18° | close portraits, isolating a face in a crowd |
| 200mm | 12° | hands and objects from afar |
| 300mm+ | 8° | compression, surveillance, heat haze, a figure on the horizon |

Anamorphic is a choice, not a default. If chosen: "anamorphic: oval bokeh, horizontal flares, gentle edge falloff," with the same FOV steps.

## 3. Observer or participant: lens + distance

| Approach | Lens + distance | Feels like | Used in |
|---|---|---|---|
| Participant | wide (84°–63°), very close | you are there; the environment stays in frame with the emotion | The Revenant, Birdman, Children of Men |
| Locked subjectivity | one normal lens (≈47°), shallow focus, at the character's head | trapped in one person's experience | Son of Saul |
| Neutral | 47°–29°, conversational distance | classical, invisible | most dialogue |
| Observer | wide frame from a distance, held | empathy without sentiment | Roma |
| Watcher | long lens (18°–8°), far | surveillance, isolation, the world pressing in | thrillers, sport, war |

The same close-up made two ways feels different: wide and close is intimate and slightly unsettling; long and far is flattering and distant.

## 4. Depth of field

- **Shallow:** separation, intimacy, isolation; the background melts. Full-frame at wide apertures; long lenses.
- **Deep:** everything readable; relationships between people and place; Welles-style staging in depth.
- **Write it as the visible result:** "her face sharp, everything beyond 2 m dissolves into soft blur" or "deep focus: the man in the doorway 6 m behind her is as sharp as she is."
- Shallow focus is not cinematic by itself. Separation also comes from light, colour and layers.

## 5. Rig builds

| Rig | Moves it serves | Character on screen |
|---|---|---|
| Tripod (fluid / geared / Dutch head) | static, pan, tilt, whip, Dutch | still, precise |
| Slider | parallax slides, short pushes | small, elegant depth |
| Dolly + track | push, pull, truck, curved arcs, creeps | smooth, weighted, classical |
| Jib / crane | boom up / down, crane reveals | lift, scale, release |
| Telescopic crane | swoops, long reach, over crowds | authored, big-budget |
| Remote head | precise slow pans, rolls on cranes | controlled |
| Floating walk rig (Steadicam-style) | follow, lead, arcs, oners, low mode | gliding presence |
| Gimbal | pass-throughs, roll, vehicles, low over water | fluid, modern, weightless |
| Shoulder / handheld | handheld, POV, chaos | breathing, immediate |
| Body-mount | Snorricam-style | world swings, face fixed |
| Heavy-lift drone / helicopter | aerial reveals, follows, orbits | stable, sweeping |
| FPV drone (light cameras only) | dives, gaps, flips | thrilling, kinetic |
| Cable cam | gliding over spaces | floating, otherworldly |
| Camera car / crane arm | car and boat tracking | action scale |
| Water housing / splash bag | waterline, underwater, surf | immersed |
| Motion control | repeatable precise moves | polished, magical |

Ask: could a real crew do this here? Could the space physically hold the rig?

## 6. Frame rate and slow motion

| Playback feel | How it was shot (24 fps playback) | Use |
|---|---|---|
| Real time | 24–25 fps | the default |
| Subtle float | ~48 fps (2×) | memory, romance, dream |
| Clear slow motion | 72–120 fps (3–5×) | labour, sport, action beats |
| Time held | 240 fps and up (10×+) | splashes, falls, impacts (specialist cameras) |

In prompts, write "x times slower than real time," never a bare frame rate. One speed per shot.

## 7. Aspect ratio and movement

- **2.39:1 (scope):** wide frames favour lateral moves, trucks, side tracks, landscapes and two people in one frame.
- **1.85:1 / 16:9:** a balanced, general-purpose frame.
- **4:3 / 1.37:1:** narrow and enclosing; favours faces and vertical compositions (Son of Saul).
- **9:16 vertical:** favours push-ins, tilts, crane moves and orbits over wide lateral tracking.

Keep one aspect ratio for the whole project unless a change is a deliberate story device.

## 8. Never write in a prompt

Camera brand or model, sensor name, lens brand or series, rig brand, a bare frame-rate number, or a cinematographer's or film's name. Write the visible result.
