# Camera movement library

Every camera movement a feature cinematographer uses. Each entry covers what the move is, what it makes viewers feel, when films use it, and how to get an AI video model to execute it. The moves are organised by **axis**, because the most common AI failure is confusing a camera that *turns* with a camera that *travels*.

Search for the move's `###` heading; you rarely need the whole file.

## Contents

0. Quick index — every move under every name people use
1. How to read an entry · the axis map
2. Stillness — static / locked-off, the living frame, the creep
3. Horizontal rotation — pan, whip pan, 360° spin
4. Vertical rotation — tilt, whip tilt
5. Lens-axis rotation — Dutch angle, roll, barrel roll
6. Optical — zoom, crash zoom, rack focus, dolly zoom (both versions)
7. Depth travel — push-in, fast push, pull-out, fly-through
8. Lateral travel — truck, parallax slide, counter-move
9. Following travel — follow, lead, side track, walk-and-talk, chase
10. Orbital travel — arc, 360° orbit, spiral
11. Vertical travel — pedestal, crane / jib, telescopic crane, overhead top shot, push + rise
12. Carried and mounted — handheld, floating walk (Steadicam-style), gimbal, low mode, follow-behind-the-head, body-mount, POV
13. Aerial — drone move set, FPV, cable cam
14. Vehicle — car mounts, camera car with crane arm, towed car
15. Water — boat-riding, waterline / split-level, shoreline track, surf-line low, underwater
16. Time — slow motion, speed ramp, timelapse, hyperlapse, frozen-moment orbit, motion control
17. Compound and signature — the oner, the multi-composition oner, foreground-wipe reveal, follow-then-hold, match move
18. Speed and timing reference

---

## 0. Quick index

| Name people use | What it actually is | Entry |
|---|---|---|
| static, still, locked shot, tripod shot | camera does not move | Static |
| "camera stays but the scene moves" | held frame with motion inside it | The living frame |
| pan, pan left / right, panning shot | camera turns left / right in place | Pan |
| "panning in", "go closer", "move in" | usually a push-in (camera travels closer); a pan only turns | Push-in |
| whip pan, swish pan, flash pan | very fast blurred pan | Whip pan |
| 360 spin, 360 pan, spin around the room | camera turns a full circle on one spot | 360° spin |
| tilt up / down | camera turns up / down in place | Tilt |
| Dutch angle, canted, tilted frame | frame tilted on its axis | Dutch angle |
| roll, camera roll | frame rotates during the shot | Roll |
| barrel roll, 360 roll, upside-down spin | full turn on the lens axis | Barrel roll |
| zoom in / out, slow zoom, creep zoom | lens changes, camera stays put | Zoom |
| crash zoom, snap zoom | very fast zoom | Crash zoom |
| rack focus, focus pull, pull focus | sharpness shifts between planes | Rack focus |
| dolly zoom, Vertigo effect, zolly, contra-zoom, trombone shot | travel + opposite zoom | Dolly zoom |
| push-in, dolly in, track in | camera travels toward the subject | Push-in |
| slam dolly, crash in, snap push | push-in in about a second | Fast push |
| pull-out, pull back, dolly out | camera travels away | Pull-out |
| fly-through, push-through, through the window, keyhole shot | camera travels through an opening | Fly-through |
| truck, crab, lateral move, sideways track | camera travels sideways | Truck |
| slider shot, parallax shot | short sideways slide past a foreground | Parallax slide |
| counter-move, counter-track | camera travels against the subject's direction | Counter-move |
| tracking shot, follow shot, leading shot, side track | camera travels with a moving subject | Follow / lead / side track |
| walk-and-talk | tracking a conversation on the move | Walk-and-talk |
| chase shot | high-speed tracking | Chase |
| arc shot, half circle | camera travels part of a circle around the subject | Arc |
| 360 shot, 360 rotate, circle shot, revolving shot, orbit | camera travels a full circle around the subject | 360° orbit |
| spiral, corkscrew, helix, rising orbit | orbit + rise or descent | Spiral |
| pedestal up / down | camera rises / lowers level, no tilt | Pedestal |
| crane, jib, boom up / down, crane reveal | camera rises / descends on an arm | Crane / jib |
| Technocrane, telescopic crane | crane arm that also extends | Telescopic crane |
| top shot, overhead, god's eye, bird's-eye move | looking straight down | Overhead top shot |
| handheld, shaky cam, documentary style | operator carries the camera | Handheld |
| Steadicam, float, glide | stabilised gliding walk | Floating walk |
| gimbal shot | motorised stabiliser | Gimbal |
| low mode, ground-level tracking | travelling just above the ground | Low mode |
| over-the-head follow, Son of Saul shot | camera locked behind the character's head | Follow-behind-the-head |
| Snorricam, body cam, chest rig | camera fixed to the actor | Body-mount |
| POV, first-person, "through his eyes" | the camera is a character's eyes | POV |
| drone shot, aerial, flyover, dronie, aerial reveal, aerial orbit | flying moves | Aerial / drone move set |
| FPV, racing drone, drone dive | fast agile first-person flight | FPV |
| cable cam, wire cam, Spidercam | camera rides a cable | Cable cam |
| car mount, hood mount, car rig | camera fixed to a vehicle | Car mounts |
| Russian Arm, chase car, camera car | crane arm on a tracking vehicle | Camera car |
| process trailer, towing shot | picture car towed | Towed car |
| boat cam, on-deck shot | camera rides a boat | Boat-riding |
| over-under, split-level, half-in-water, waterline | lens at the waterline | Waterline / split-level |
| underwater shot | camera below the surface | Underwater |
| slow motion, slo-mo, high frame rate | time slowed | Slow motion |
| speed ramp | speed changes inside a shot | Speed ramp |
| timelapse, hyperlapse | time sped up | Timelapse / hyperlapse |
| bullet time, frozen moment, time-slice | time frozen while the camera moves | Frozen-moment orbit |
| motion control, robot arm | programmed repeatable move | Motion control |
| oner, long take, single take, continuous shot | scene with no cut | The oner |
| Spielberg oner | one take passing through several compositions | Multi-composition oner |
| wipe reveal, foreground reveal | passing something close reveals the subject | Foreground-wipe reveal |
| match cut move, transition move | move continues across a cut | Match move |
| wide shot, close-up, OTS, two-shot | framing, not movement | `shot-sizes-and-angles.md` |
| low angle, high angle, bird's-eye view | camera angle, not movement | `shot-sizes-and-angles.md` |

---

## 1. How to read an entry · the axis map

Each entry gives:
- **What** — the physical move.
- **Axis** — rotate (the camera turns, its position is fixed) or travel (the camera's position moves), and in which direction.
- **Viewers feel** — the emotional effect.
- **Used for** — the story situations that earn it.
- **Films** — examples from award-winning and landmark cinema.
- **Rig** — what a real crew puts the camera on.
- **Prompt** — observable phrasing for an AI video model (adapt the numbers).
- **AI risk → fix** — how models usually break it, and the line that prevents it.

**The axis map:**

| Axis | Rotate in place | Travel through space |
|---|---|---|
| Horizontal (left–right) | pan, whip pan, 360° spin | truck, parallax slide, side track, counter-move |
| Vertical (up–down) | tilt, whip tilt | pedestal, crane / jib, boom |
| Depth (toward–away) | — | push-in, pull-out, fly-through, follow, lead |
| Around the subject | — | arc, 360° orbit, spiral |
| Lens axis | Dutch angle, roll, barrel roll | — |
| Optical (no camera motion) | zoom, crash zoom, rack focus | (dolly zoom combines travel with zoom) |
| Unstructured | handheld, body-mount, boat-riding | — |

---

## 2. Stillness

### Static / locked-off
- **What:** the camera does not move at all.
- **Axis:** none.
- **Viewers feel:** observation, objectivity, tension; attention goes to performance and composition. Depending on context, it can feel trapped, cold or unflinching.
- **Used for:** dialogue and shot-reverse-shot where performance carries the scene; improvised performances (several locked cameras let actors play freely, as in The Wolf of Wall Street); painterly compositions; trapping a character; refusing to comfort the audience during cruelty; comic deadpan; a held final image. A long stretch of stillness also makes the next small move feel enormous.
- **Films:** the coin-toss dialogue in No Country for Old Men; soldiers pinned on the beach in Dunkirk; the long hold on Solomon hanging in 12 Years a Slave; Ozu's low, still frames in Tokyo Story; Wes Anderson's symmetrical tableaux.
- **Rig:** tripod, or a dolly with the head locked.
- **Prompt:** "locked-off, eye level 1.5 m, 3 m from them; the frame stays perfectly still for the whole shot."
- **AI risk → fix:** models add a slow drift or gentle push. State the stillness explicitly and once more in the prompt's locks. Give the frame life inside it (see next entry), or the clip can look frozen.

### The living frame
- **What:** a static frame in which something moves: weather, water, smoke, curtains, crowds, traffic, flickering light, an actor crossing.
- **Axis:** none for the camera; movement lives inside the frame.
- **Viewers feel:** a breathing, cinematic stillness; the world is alive around the characters, and nature can carry their emotion.
- **Used for:** almost any held shot; mood; grief; waiting; establishing a place; dialogue on location.
- **Films:** Kurosawa's rain, wind and snow behind still characters (Rashomon, Seven Samurai); the rain, fog and wind in Ee.Ma.Yau; the passing landscape in a Ghibli film.
- **Rig:** tripod.
- **Prompt:** "locked-off frame; heavy rain falls through the backlight at 4 m, the palm fronds behind them thrash in the wind, smoke drifts left across the midground; the frame itself stays perfectly still."
- **AI risk → fix:** the model moves the camera instead of the elements. Say what moves, in which direction and how fast, and that the camera stays still. This is often the most reliable cinematic shot an AI model can produce.

### The creep
- **What:** a move so slow (0.1–0.3 km/h) that the audience feels it more than sees it.
- **Axis:** usually depth travel, sometimes lateral.
- **Viewers feel:** unease, inevitability, attention tightening without being announced.
- **Used for:** a scene where something is quietly going wrong; the long build before a revelation; slow infiltration.
- **Films:** the near-invisible forward drift through the first half of Parasite; Deakins' slow pushes.
- **Rig:** dolly on track, remote head, or slider.
- **Prompt:** "the camera creeps forward at 0.2 km/h over 10 seconds, barely perceptible, the framing tightening from a medium shot to a medium close-up."
- **AI risk → fix:** models make it too fast or skip it. Give the speed, the duration, and both framings.

---

## 3. Horizontal rotation

### Pan
- **What:** the camera turns left or right on a fixed point.
- **Axis:** horizontal rotate.
- **Viewers feel:** a slow pan builds anticipation and lets space unfold; a follow pan keeps us with a moving subject; a reveal pan delivers new information at its end.
- **Used for:** following action across the frame; connecting a speaker to a listener; revealing a landscape or a threat; storybook "information pans" that sweep across a detailed world.
- **Films:** Roma's slow lateral pans as calm transitions; Wes Anderson's fast, precise informational pans; countless Western landscape pans.
- **Rig:** fluid head on tripod or dolly; geared or remote head for very smooth slow pans.
- **Prompt:** "the camera stays in place and pans 60° to the right over 5 seconds, easing in and out, from the open door to the man waiting by the window."
- **AI risk → fix:** pans that overshoot their subject, or become sideways travel. Name the first and last subject, give degrees and seconds, and say the camera position stays fixed.

### Whip pan
- **What:** a pan so fast the image smears into motion blur.
- **Axis:** horizontal rotate, very fast.
- **Viewers feel:** energy, surprise, comic timing, a jolt in time or place; between two people, a sense of combat or chemistry.
- **Used for:** arguments, musical rhythm, transitions between locations, reacting to a sudden sound.
- **Films:** La La Land, where whip pans build energy between Mia and Sebastian; Whiplash, where they're timed to the drumming during the confrontations.
- **Rig:** fluid head with the drag loosened, or handheld.
- **Prompt:** "subject A settled until 0.3 s; a horizontal whip pan to the right blurs the frame from 0.3 s to 0.8 s or longer; subject B settled by 1.4 s."
- **AI risk → fix:** a whip with less than about 0.5–0.8 s of blur renders as a plain hard cut. Give the blur its time, and settle on both ends.

### 360° spin
- **What:** the camera stays on one spot and turns a full circle, showing everything around it. Different from a 360° orbit, where the camera travels around a subject.
- **Axis:** horizontal rotate, 360°.
- **Viewers feel:** being surrounded, searching, the walls closing in; or wonder at a whole place.
- **Used for:** searching a crowd for one face; waking in an unknown room; standing in the middle of a festival or a battlefield.
- **Rig:** geared or remote head with unlimited pan; or a floating-walk operator turning on the spot.
- **Prompt:** "the camera stays on one spot at 1.5 m and pans a full 360° to the right over 10 seconds: the doorway, then the stove at 90°, the window at 180°, the bookshelf at 270°, and back to the doorway."
- **AI risk → fix:** models stop at 180°, or the room changes as it comes round. Name what appears at each quarter turn and say the turn ends on the starting view.

---

## 4. Vertical rotation

### Tilt
- **What:** the camera turns up or down on a fixed point.
- **Axis:** vertical rotate.
- **Viewers feel:** tilting up gives awe, scale, power, dominance; tilting down lands on detail, weight, consequence, vulnerability.
- **Used for:** revealing height (a tower, a cliff, a giant); introducing an imposing character from boots to face; moving from a face to the hands that give the person away.
- **Films:** Jurassic Park, where tilting up to the first dinosaur carries the characters' awe straight to the audience; Inception, where the camera tilts up as the Paris street folds overhead; Men in Black, where tilting up builds the agents' imposing presence.
- **Rig:** fluid or geared head.
- **Prompt:** "fixed position; the camera tilts up 50° over 4 seconds from his boots to his face against the sky."
- **AI risk → fix:** the model reframes or travels upward instead. Name the first thing in frame and the last, and say the camera position stays fixed.

### Whip tilt
- **What:** a very fast blurred tilt.
- **Axis:** vertical rotate, very fast.
- **Viewers feel:** shock, a sudden look up or down.
- **Used for:** a sound from above; a sudden discovery on the floor.
- **Rig:** fluid head or handheld.
- **Prompt:** "a vertical whip upward blurs the frame for 0.6 s and settles on the figure on the balcony."
- **AI risk → fix:** same as the whip pan: give the blur its time.

---

## 5. Lens-axis rotation

### Dutch angle
- **What:** a static frame tilted on its axis.
- **Axis:** lens-axis, held.
- **Viewers feel:** unease, a world off balance, moral disorder.
- **Used for:** sparingly — intoxication, a mind coming apart, a corrupted place.
- **Films:** The Third Man's canted post-war Vienna.
- **Rig:** Dutch head on the tripod.
- **Prompt:** "the frame is tilted 15° clockwise and holds for the whole shot."
- **AI risk → fix:** models straighten the horizon. State the angle and that it holds.

### Roll
- **What:** the frame rotates during the shot.
- **Axis:** lens-axis rotate.
- **Viewers feel:** losing balance; or, deliberately, a power reversal — the world turns while one person stays upright.
- **Used for:** panic, falling, intoxication; the moment the power in a scene flips.
- **Films:** The Dark Knight, where the camera slowly rolls 180° until the upside-down Joker appears upright while the city behind him stays inverted; Black Panther, where a slow roll as Killmonger takes the throne passes the kingdom's instability to the audience.
- **Note:** rolls feel dizzying and unnatural, so use one only when you want the audience uncomfortable.
- **Rig:** 3-axis remote head or gimbal with roll unlocked.
- **Prompt:** "the camera slowly rolls 180° clockwise over 6 seconds; his face ends upright in frame while the room behind him ends upside down."
- **AI risk → fix:** models stop early or roll the subject with the room. State the final orientation of both subject and background.

### Barrel roll
- **What:** a full 360° turn on the lens axis.
- **Axis:** lens-axis rotate, 360°.
- **Viewers feel:** total disorientation, falling, capsizing.
- **Used for:** a fall, a capsize, a dream, a crash.
- **Rig:** gimbal or remote head with unlimited roll.
- **Prompt:** "the frame rolls a full 360° clockwise over 4 seconds while the camera drifts forward; the horizon turns upside down and comes back level."
- **AI risk → fix:** models stop at 90°. State 360° and that the horizon passes upside down.

---

## 6. Optical

### Zoom
- **What:** the focal length changes while the camera stays put. Because the camera doesn't move, there's no parallax: the perspective just flattens (zoom in) or widens (zoom out). Human eyes can't do this, so a zoom always feels a little unnatural.
- **Axis:** optical; no camera movement.
- **Viewers feel:** a slow zoom in feels hypnotic, voyeuristic, like attention narrowing into dread. A zoom out reveals context, often ironically. Handheld zooms feel like documentary, satire or surveillance.
- **Used for:** dread; surveillance; 1970s period texture; ironic reveals; documentary and satire.
- **Films:** the slow zoom on Jack in The Shining; Kubrick's zooms onto characters sliding into madness in Full Metal Jacket; The Graduate opening on a slow zoom out; Barry Lyndon's painterly slow zoom-outs; the handheld snap-zooms of The Big Short and Succession.
- **Rig:** cine zoom lens on tripod, often with a zoom motor for an even creep.
- **Prompt:** "the camera position stays fixed while the view slowly zooms in from 47° to 29° over 8 seconds; the background flattens and seems to press toward him."
- **AI risk → fix:** models render it as a dolly. Say "camera position stays fixed" and describe the flattening.

### Crash zoom
- **What:** a very fast zoom onto a detail.
- **Axis:** optical, fast.
- **Viewers feel:** shock, comic punctuation, exploitation-film energy.
- **Used for:** a sudden reveal, a comic beat, a stylised genre moment.
- **Films:** Tarantino's crash zooms in Django Unchained and Kill Bill; Shaolin and spaghetti-Western homages.
- **Rig:** cine zoom, punched by hand.
- **Prompt:** "camera fixed; in 0.4 seconds the view snaps from 63° to 12°, landing on the pistol on the table."
- **AI risk → fix:** reads as a cut if it's too fast. Give it about half a second.

### Rack focus
- **What:** sharpness moves from one plane to another during the shot.
- **Axis:** optical.
- **Viewers feel:** attention redirected without a cut; a connection between foreground and background; a realisation.
- **Used for:** a character noticing something behind them; an object becoming the subject; someone approaching from the background.
- **Rig:** any; wireless follow focus. Full-frame cameras at wide apertures make the shift dramatic.
- **Prompt:** "focus starts on the coffee cup 0.5 m from the camera, then shifts over 1.5 seconds to the man in the doorway 4 m away; the cup melts into soft blur."
- **AI risk → fix:** both planes stay sharp. Give both distances and say which one goes soft.

### Dolly zoom
- **What:** the camera travels toward or away from the subject while the zoom moves the opposite way, so the subject stays the same size and the background warps. There are **two opposite versions**, and they feel different.
- **Version A — dolly in + zoom out:** the camera moves closer while the view widens; the background stretches away and seems to recede. Feels like epiphany, shock, the floor dropping away, realising something terrible.
- **Version B — dolly out + zoom in:** the camera moves back while the view narrows; the background compresses and rushes toward the subject. Feels like tunnel vision, the world closing in, claustrophobia, or (gently) intimacy.
- **Used for:** once in a film, at a true turning point; a character's internal conflict; the presence of a supernatural force (the road scene in The Fellowship of the Ring). It can also be used warmly: keeping one person the same size while the other person in the background grows can pull two characters together. Overused, it becomes a gimmick.
- **Films:** Vertigo, which introduced it; Brody on the beach in Jaws; the diner in Goodfellas; Raging Bull (dolly out + zoom in, pushing the crowd into LaMotta's tunnel vision); Freddie Mercury at Live Aid in Bohemian Rhapsody, pulling the stadium crowd closer to him.
- **Rig:** dolly on track, cine zoom with a motor synced to the move.
- **Prompt (A):** "the camera travels toward him at 1 km/h while the view widens from 29° to 63° over 4 seconds; his face stays exactly the same size in frame while the corridor behind him stretches away and recedes into the distance."
- **Prompt (B):** "the camera travels back from him at 1 km/h while the view narrows from 63° to 29° over 4 seconds; his face stays exactly the same size in frame while the street behind him compresses and rushes toward him, the buildings looming large and close."
- **AI risk → fix:** the move models get wrong most often; they do a plain push or pull. Describe the visible result (subject stays the same size; background stretches away, or rushes in), give start and end FOV, keep it under 5 seconds, and lock the subject's size.

---

## 7. Depth travel

### Push-in
- **What:** the camera travels toward the subject.
- **Axis:** depth travel, forward.
- **Viewers feel:** closer to a character's mind; rising intensity; realisation; importance ("look at this").
- **Used for:** a decision, a confession, a point of no return; toward an object, to mark it as evidence.
- **Films:** in The Godfather, the camera barely moves while Sonny and Tom argue after the attempt on the Don, so the slight push when Michael steps up feels grand; the slow push on Michael before he shoots in the restaurant; the push-ins of The Assassination of Jesse James by the Coward Robert Ford; pushes onto the documents in The Post; Deakins' slow, single pushes.
- **Rig:** dolly on track; slider for short pushes; gimbal or floating walk for free ones.
- **Prompt:** "starting 2 m from her face, the camera travels straight toward her at 0.5 km/h for 6 seconds, easing in and out, ending in a tight close-up; smooth, weighted glide."
- **AI risk → fix:** overshoots into the face or drifts sideways. Give start and end distance or size, and the word "straight".

### Fast push
- **What:** a push-in in about one second (slam dolly).
- **Axis:** depth travel, fast.
- **Viewers feel:** alarm, a jolt, sudden focus.
- **Used for:** a sudden sound, a betrayal discovered, a name shouted.
- **Rig:** dolly pushed hard, or a gimbal operator running in.
- **Prompt:** "in 1 second the camera rushes straight toward his face at 8 km/h, from a medium shot to a close-up, and stops sharply with a small settle."
- **AI risk → fix:** under a second it renders as a cut. Keep about a second and describe the settle.

### Pull-out
- **What:** the camera travels away from the subject.
- **Axis:** depth travel, backward.
- **Viewers feel:** detachment, isolation, consequence, an ending; context arriving; a character being abandoned by the camera itself.
- **Used for:** after a loss; to show someone is alone; to reveal who else is there or how big the situation is; final shots.
- **Films:** The Shining, pulling back from Jack at his typewriter so we distance ourselves from him as Wendy does; the final pull-out in Catch Me If You Can; the camera retreating from Arthur on the stairwell in Joker; the crane pull-back over the wounded in Gone with the Wind.
- **Rig:** dolly on track; crane for pull-outs that also rise.
- **Prompt:** "the camera travels straight back from him at 1 km/h over 8 seconds, from a close-up of his face to a wide shot that reveals the empty platform around him."
- **AI risk → fix:** the reveal content is invented. Describe what enters the frame as the camera travels back, in order.

### Fly-through
- **What:** the camera travels through an opening: a window, a doorway, a gap in a crowd, a fence, a keyhole.
- **Axis:** depth travel through a boundary.
- **Viewers feel:** entering another world; a seamless, almost magical transition; sometimes voyeurism.
- **Used for:** outside-to-inside transitions; entering a party; discovering a hidden room.
- **Rig:** gimbal or separated-sensor build for small openings; drone for big ones.
- **Prompt:** "the camera travels forward at 3 km/h through the open window, about 1 m wide, passes the wooden frame, and settles inside on the family at the dinner table."
- **AI risk → fix:** the opening morphs as the camera crosses it. Give the opening's size and material, and describe what's on the other side before the camera arrives.

---

## 8. Lateral travel

### Truck
- **What:** the camera travels sideways, parallel to the subject or scene.
- **Axis:** horizontal travel.
- **Viewers feel:** surveying; a calm journey; a storybook unrolling.
- **Used for:** passing along a line of people, an inspection, a street, a production line.
- **Films:** Moonrise Kingdom, trucking right with the Scoutmaster's morning inspection; Roma's lateral moves.
- **Rig:** dolly on straight track.
- **Prompt:** "the camera travels sideways to the right at 2 km/h, staying parallel to the line of soldiers 3 m away, passing each face in turn; it does not turn."
- **AI risk → fix:** models turn it into a pan. Say "travels sideways, staying parallel, does not turn".

### Parallax slide
- **What:** a short sideways move past something close in the foreground, so the layers slide past each other at different speeds.
- **Axis:** horizontal travel, short.
- **Viewers feel:** depth and polish; a quiet reveal.
- **Used for:** inserts; revealing a face from behind a pillar, plant or doorframe; product and food shots.
- **Rig:** slider.
- **Prompt:** "the camera slides 40 cm to the left over 4 seconds; the potted plant in the foreground passes across the frame faster than the room behind it, revealing her at the desk."
- **AI risk → fix:** the foreground warps. Keep it simple and give its distance from the lens.

### Counter-move
- **What:** the camera travels opposite to the subject's direction while panning to keep them, so the background slides fast behind them.
- **Axis:** horizontal travel + rotate.
- **Viewers feel:** energy and tension in an ordinary walk; a charged entrance.
- **Used for:** entrances, crossing a crowded space, walking toward a decision.
- **Rig:** dolly with a fluid head.
- **Prompt:** "as she walks left across the frame at 4 km/h, the camera travels right at 2 km/h while turning to keep her centred; the shop fronts behind her slide quickly across the frame."
- **AI risk → fix:** models move the camera the same way as the subject. State both directions from the camera's point of view.

---

## 9. Following travel

### Follow / lead / side track
- **What:** the camera travels with a moving subject: behind them (follow), in front walking backward (lead), or alongside (side track).
- **Axis:** depth or horizontal travel, matched to the subject.
- **Viewers feel:** **follow** — curiosity, going where they go, sometimes threat ("someone is behind them"). **Lead** — we watch their face and state on the move. **Side** — a journey, momentum, accompaniment. Every tracking shot asks where the character is going and what will happen when they get there.
- **Used for:** walks, entrances, inspections, journeys, pursuits, long takes.
- **Films:** 1917, designed to look like one continuous tracking shot; the trench inspection in Paths of Glory; the handheld follow out of the police station in Three Billboards Outside Ebbing, Missouri; the endless school corridors in Elephant; the walk to the Copacabana in Goodfellas; Jallikattu, where the camera walks and runs in sync with the characters.
- **Rig:** floating walk rig, dolly on long track, gimbal, vehicle for fast ones.
- **Prompt:** "the camera leads him, travelling backward at 4 km/h, staying 2 m ahead at chest height, holding his face in a medium shot as he walks toward it."
- **AI risk → fix:** distance drifts and the subject shrinks or collides with the lens. Give one shared speed for camera and subject and a fixed distance.

### Walk-and-talk
- **What:** a lead or side track on two or more characters talking as they walk.
- **Axis:** depth or horizontal travel.
- **Viewers feel:** urgency, momentum, a world busy around the conversation.
- **Used for:** exposition that would be dull standing still; workplace drama; reunions on the move.
- **Rig:** floating walk rig or gimbal.
- **Prompt:** "the camera leads the two women, travelling backward at 4 km/h, 2.5 m ahead, holding a two-shot as they talk; colleagues and carts pass between the camera and them every few seconds."
- **AI risk → fix:** the speakers' faces turn away and lip-sync breaks. Keep both faces three-quarter to the lens and give passing foreground traffic for depth.

### Chase
- **What:** high-speed tracking after, beside or ahead of a fleeing subject.
- **Axis:** depth or horizontal travel, fast.
- **Viewers feel:** adrenaline, pursuit, danger.
- **Used for:** foot chases, vehicle chases, animal pursuits.
- **Films:** the buffalo pursuits in Jallikattu (influenced, its cinematographer said, by Jaws, Apocalypto and Mad Max: Fury Road).
- **Rig:** running gimbal or handheld operator, quad bike, camera car.
- **Prompt:** "the camera chases him from behind at 18 km/h through the narrow lane, 3 m back at shoulder height, jolting with each stride."
- **AI risk → fix:** speeds and distances drift. Give them, plus what the camera passes.

---

## 10. Orbital travel

### Arc
- **What:** the camera travels part of a circle around the subject, keeping them in frame.
- **Axis:** orbital travel, partial.
- **Viewers feel:** a moment deepening; the other side of a person revealed; growing tension when it circles people in a confined space.
- **Used for:** reunions, decisions, confrontations, revealing what a character sees behind them.
- **Films:** The Dark Knight twice: circling the Joker as he menaces Rachel at the party, so we feel the unease she feels; and circling two men debating in a cramped office, tension building until it's interrupted. Imagine either shot locked on a tripod: the performance survives, but the unease doesn't.
- **Rig:** curved dolly track; floating walk rig.
- **Prompt:** "the camera arcs 70° to the left around her at 3 m distance over 5 seconds, at eye level; the harbour behind her slides from frame-left to behind her head."
- **AI risk → fix:** past roughly 90° the face drifts from its reference and the background reshuffles. Keep arcs around faces within 90° per phase.

### 360° orbit
- **What:** the camera travels a full circle around the subject.
- **Axis:** orbital travel, 360°.
- **Viewers feel:** the world spinning around one person. It can mean euphoria and reunion, heroic unity (around a group), being trapped or interrogated, or a mind losing its grip. Speeding up the orbit makes it dizzy.
- **Used for:** once or twice in a film, for a big emotional moment, and tied to one character's experience. Start it when their moment starts; stop it when it ends.
- **Films:** Moonlight's opening, where the orbit begins when the addict starts asking for drugs and settles into a two-shot when he leaves; the 360° around the assembled team in The Avengers; the accelerating spin around Rocket in the standoff in City of God.
- **Rig:** circular track, floating walk operator walking the circle, large gimbal, aerial for buildings and boats.
- **Prompt:** split into four timed quarters so the face is re-anchored each time: "0–3 s: the camera circles left around him at 3 m, eye level, from his face to his right profile, the café behind him. 3–6 s: on to his back, the street behind him. 6–9 s: on to his left profile, the river behind him. 9–12 s: back to his face, the café behind him again. He stays centred, same size, same height through the whole circle."
- **AI risk → fix:** the riskiest move for identity. Use the quarters, keep distance and height constant, name what's behind him at each quarter, keep it slow (12 seconds or more for a full circle). If the face needn't hold, frame wider so the subject is small, or do 180° and cut.

### Spiral
- **What:** an orbit combined with a rise or a descent.
- **Axis:** orbital + vertical travel.
- **Viewers feel:** rising — release, transcendence, an ending; descending — a world closing in on someone.
- **Used for:** endings, prayers, dreams, a figure alone in a vast place.
- **Rig:** crane on a circular track, or a drone (most common).
- **Prompt:** "the camera circles 180° to the left around her while rising from 2 m to 12 m over 10 seconds, tilting down to keep her centred as she grows small on the empty beach."
- **AI risk → fix:** already two axes, so add nothing else. Keep rotation within 180° per generation and let the subject become small.

---

## 11. Vertical travel

### Pedestal
- **What:** the camera rises or lowers vertically while staying level.
- **Axis:** vertical travel, no tilt.
- **Viewers feel:** a gentle shift in perspective or status; staying with a person as they stand or sit.
- **Used for:** following someone standing up at their eye line; revealing what's on a counter from above it.
- **Rig:** dolly column, small jib.
- **Prompt:** "as he stands, the camera rises level from 1.0 m to 1.6 m over 2 seconds, staying at his eye line."
- **AI risk → fix:** models tilt instead. Say "rises level" and give both heights.

### Crane / jib
- **What:** the camera rises or descends through space on an arm, often with a tilt.
- **Axis:** vertical travel (often + tilt).
- **Viewers feel:** crane up — release, an ending, a person left small in a big world, the story's scope. Crane down — arriving into a world. Up and down within one take can trace a character's fortunes rising and falling.
- **Used for:** establishing shots that introduce a location; openings and endings; revealing a place over a wall; following action vertically. Big crane moves add instant production value, which is why historical epics and action films rely on them; small boom moves quietly reveal a character or a detail.
- **Films:** Full Metal Jacket, booming up with Private Pyle's hopeful climb and down with his failure; the opening crane of Touch of Evil; the pull-back over the wounded in Gone with the Wind.
- **Rig:** jib or crane with a remote head.
- **Prompt:** "the camera starts 1.5 m high behind the garden wall and rises to 6 m over 6 seconds, tilting down to keep her centred, revealing the whole town below the hill."
- **AI risk → fix:** the reveal is invented or the subject lost. Give start and end heights, what stays centred, and what appears.

### Telescopic crane
- **What:** a crane arm that also extends and retracts, so the camera can travel in from far away, swoop over crowds and snake through spaces.
- **Axis:** vertical + depth travel.
- **Viewers feel:** sweeping, authored, big-budget scale.
- **Used for:** going from a wide over a crowd into a close-up; a long move along a battlefield.
- **Films:** a staple of large-scale long takes; The Revenant tracks its actors in one of three modes: handheld, Steadicam or telescopic crane.
- **Rig:** telescopic crane with remote head, often on a camera car.
- **Prompt:** split into phases: "0–4 s: the camera descends from 8 m to 4 m over the festival crowd. 4–8 s: it travels forward 6 m and settles in a medium shot of her at the stall."
- **AI risk → fix:** long compound moves break mid-way. Use timed phases.

### Overhead top shot
- **What:** the camera looks straight down, static or moving.
- **Axis:** vertical view; any travel.
- **Viewers feel:** fate, pattern, detachment; vulnerability and insignificance; omniscient surveillance; people as pieces on a board. A moving overhead can also show power shifting between characters.
- **Used for:** a body, a table, a crowd pattern, a map-like view of a chase.
- **Films:** the torch-lit crowd chasing the buffalo, seen from above, in Jallikattu; the overhead patterns of Busby Berkeley musicals.
- **Rig:** crane with head tilted 90°, overhead rig, drone.
- **Prompt:** "the camera looks straight down from 5 m, centred on the dinner table, and slowly rotates 30° clockwise over 6 seconds."
- **AI risk → fix:** the angle slides toward a high three-quarter view. Say "straight down, 90°".

### Push + rise
- **What:** the camera travels forward and rises at once.
- **Axis:** depth + vertical travel.
- **Viewers feel:** elevation; a moment growing larger than the characters.
- **Used for:** the end of a sequence, a promise, a triumph.
- **Rig:** crane or jib on a dolly.
- **Prompt:** "the camera travels forward at 1 km/h while rising from 1.5 m to 3 m over 6 seconds, tilting down to keep them centred."
- **AI risk → fix:** fine as two axes; add no pan or arc.

---

## 12. Carried and mounted

### Handheld
- **What:** the operator carries the camera, usually on the shoulder.
- **Axis:** unstructured.
- **Viewers feel:** immediacy, documentary truth, urgency, panic, intimacy. With a heavy camera it breathes rather than shakes. Compared with smooth Steadicam, it is more visceral and less distant.
- **Used for:** fights, arrests, chaos, crowded rooms, raw emotion; a character losing control; subtle subjectivity in films based on true events. It's also used against a static style in the same scene to contrast two minds.
- **Restraint:** random movement is easy to overuse. Too much and it stops meaning anything; too little and nobody notices. Decide its amplitude for the story, not by habit.
- **Films:** the desert climax of Seven (panicked Mills handheld, calm John Doe locked-off); the long documentary-style car take in Children of Men; Son of Saul; the buffalo sequences in Jallikattu; the handheld zooms of The Big Short and Succession.
- **Rig:** shoulder rig, often with a support vest and arm.
- **Prompt:** "handheld at chest height; the camera breathes with a slow 2–3 cm sway, reacts half a beat late to his turns, and reframes on the fly."
- **AI risk → fix:** phone-like jitter or unreadable shake. Give the amplitude in cm and describe the sway as slow and heavy. For chaos, raise it: "jolts 5–8 cm with each impact".

### Floating walk (Steadicam-style)
- **What:** the camera glides with a walking operator on a stabilising arm and vest.
- **Axis:** any travel, smooth.
- **Viewers feel:** a presence moving with the characters; seduction into a world; dreamlike drift; dread when it glides through empty corridors.
- **Used for:** following through spaces, walk-and-talks, long takes, ominous approaches.
- **Films:** the Copacabana walk in Goodfellas; the hotel corridors in The Shining; Elephant's corridors; Moonlight's opening orbit.
- **Rig:** full-size floating walk rig.
- **Prompt:** "the camera glides behind her at walking pace, 4 km/h, 2 m back at shoulder height, with a gentle 1 cm float in each step; smooth, weighted, no shake."
- **AI risk → fix:** it turns into handheld or dolly. Say "glides" and give the float amplitude.

### Gimbal
- **What:** a motorised 3-axis stabiliser, carried, cable-hung or vehicle-mounted.
- **Axis:** any; very smooth; can roll.
- **Viewers feel:** fluid, modern, weightless; can pass where a floating rig can't.
- **Used for:** passing through windows and car doors, hand-offs between operators, roll moves, low moves over water.
- **Rig:** large cinema gimbal; separated-sensor build on smaller gimbals.
- **Prompt:** "the camera passes smoothly through the open car window, travelling forward at 2 km/h, and settles on the driver."
- **AI risk → fix:** pass-throughs morph the opening. Describe its size and the crossing in one clear phrase.

### Low mode
- **What:** a floating rig or gimbal flipped so the camera travels just above the ground.
- **Axis:** travel at ground level.
- **Viewers feel:** a child's or animal's eye; an ominous approach; intimacy with the ground.
- **Used for:** following feet, children, animals, water creeping in; horror approaches.
- **Films:** the tricycle through the hotel corridors in The Shining.
- **Rig:** floating rig in low mode; underslung gimbal.
- **Prompt:** "the camera glides 30 cm above the floor, following the boy's tricycle at 8 km/h around the corner of the long corridor."
- **AI risk → fix:** height creeps up. Give height in cm and lock it.

### Follow-behind-the-head
- **What:** the camera locked close behind or beside a character's head, moving with them, background in heavy blur.
- **Axis:** travel locked to the character.
- **Viewers feel:** total subjectivity; trapped in one person's experience; horror kept at the edge of sight.
- **Used for:** trauma, ordeal, war, a character in a world they can't escape.
- **Films:** Son of Saul — one 40mm lens, shallow focus, the camera always at the protagonist's eye level and always with him.
- **Rig:** handheld or floating rig.
- **Prompt:** "the camera stays 50 cm behind his right shoulder at his head height, moving with every step; his face and shoulder are sharp, everything beyond 2 m dissolves into soft blur."
- **AI risk → fix:** the model sharpens the background. Say how far the focus falls off.

### Body-mount
- **What:** the camera is rigged to the actor's body facing them, so they stay fixed in frame while the world swings around them.
- **Axis:** locked to the actor.
- **Viewers feel:** intoxication, panic, dissociation.
- **Used for:** drunkenness, drug sequences, a breakdown, a walk after shock.
- **Films:** the drunk scene in Mean Streets; the drug sequences in Requiem for a Dream.
- **Rig:** body-mount with a lightweight or separated-sensor camera.
- **Prompt:** "the camera is fixed to his chest facing his face; his face stays locked in the centre of the frame while the street behind him lurches and swings with each step."
- **AI risk → fix:** models move the face instead of the world. Say the face stays fixed in frame.

### POV
- **What:** the camera becomes a character's eyes.
- **Axis:** any, as the character moves.
- **Viewers feel:** identification; seeing exactly what they see; in horror, becoming the threat.
- **Used for:** discovery, a child looking up at adults, a killer's approach, a drunk's stagger.
- **Films:** the opening POV of the killer in Halloween.
- **Rig:** handheld or gimbal at the character's eye height.
- **Prompt:** "point of view at 1.2 m eye height, a slow handheld glance from left to right across the empty classroom; his own hand enters the bottom of frame and pushes the door."
- **AI risk → fix:** the model shows the character in frame. Say whose eyes, and that only their hands may enter frame.

---

## 13. Aerial

### Drone move set
Stable, heavy-lift aerial moves, each with its own feeling:
- **Rising reveal** — starts low behind something and rises to reveal what's beyond. *Feels like* discovery, scale. "Rises from 3 m to 30 m over 8 seconds; as it clears the treetops, the whole valley opens up."
- **Pull-back rise ("dronie")** — flies backward and upward away from a person. *Feels like* isolation, an ending, smallness. "Flies backward and up from 5 m to 50 m over 10 seconds, keeping her centred as the landscape grows around her."
- **Flyover** — flies straight over the subject, tilting down as it passes. *Feels like* passage, inspection. "Flies forward over the convoy at 30 m and tilts down to look straight at the lead truck as it passes over."
- **Aerial orbit** — circles a building, boat or person; the subject is small, so this holds better than a face orbit. *Feels like* importance, isolation, siege. "Circles the farmhouse at 40 m, 180° over 12 seconds."
- **Top-down spin** — straight down, rotating. *Feels like* fate, pattern. "Looks straight down from 60 m and rotates 45° clockwise over 8 seconds."
- **Aerial follow** — tracks a vehicle, boat or runner. *Feels like* journey, pursuit. "Follows the car from behind at 60 km/h, 20 m up, 30 m back."
- **Low skim** — fast, just above water or ground. *Feels like* speed, exhilaration. "Skims 1.5 m over the lake at 40 km/h toward the shore."
- **Films:** the helicopter shots following the car through the mountains at the start of The Shining.
- **AI risk → fix:** small-drone jitter or FPV swoops. Say "stable, heavy, slow", and give altitude and speed.

### FPV
- **What:** a small, agile first-person racing drone that dives, banks, flips and threads through gaps at speed.
- **Viewers feel:** thrill, speed, video-game energy.
- **Used for:** action, sports, music videos, a stylised dream or chase.
- **Rig:** a tiny camera. A heavy cinema camera can't fly FPV, so with a heavy cinema camera profile, flag it as a style exception.
- **Prompt:** "fast first-person flight: dives down the building face at 60 km/h, levels out 2 m above the street, banks hard around the bus and through the open archway."
- **AI risk → fix:** chaotic paths. Give the route in order, with heights and speeds.

### Cable cam
- **What:** the camera rides a cable strung between two points.
- **Viewers feel:** gliding, otherworldly travel above a space.
- **Used for:** stadiums, festival crowds, long beaches, canyons.
- **Rig:** cable cam with a stabilised head.
- **Prompt:** "the camera glides along the stadium 15 m above the crowd at 20 km/h, looking down at the waving flags."
- **AI risk → fix:** reads as a drone; usually fine.

---

## 14. Vehicle

### Car mounts
- **What:** the camera is rigged to the vehicle: bonnet looking in, side, or interior.
- **Viewers feel:** grounded travel; we ride with them; claustrophobic intimacy inside.
- **Used for:** driving dialogue, journeys, escapes.
- **Rig:** hard mounts; separated-sensor or compact camera inside the cabin.
- **Prompt:** "camera fixed to the bonnet facing in through the windscreen, 1 m from the driver; the car drives at 40 km/h; the camera moves rigidly with it, with fine road vibration."
- **AI risk → fix:** the camera floats independently of the car. Say "moves rigidly with the vehicle".

### Camera car with crane arm
- **What:** a tracking vehicle carrying a gyro-stabilised crane arm, so the camera can swing around a moving car.
- **Viewers feel:** action-film scale; sweeping around speed.
- **Used for:** chases, hero cars, speedboats.
- **Rig:** remote head on the arm of a camera car or chase boat.
- **Prompt:** "the camera travels alongside the car at 70 km/h, 1 m above the road and 3 m from the door, then swings forward to frame the driver through the windscreen; perfectly stable."
- **AI risk → fix:** speed mismatch between camera and car. Give one shared speed.

### Towed car
- **What:** the picture car is towed on a low trailer so actors can perform while the camera is mounted around them.
- **Viewers feel:** steady intimacy in a moving car.
- **Used for:** dialogue in a moving car.
- **Prompt:** "two-shot through the windscreen; the camera holds steady at the car's speed; the road and trees flow past the side windows."
- **AI risk → fix:** low; state the background flow speed.

### Long take inside a vehicle
- **Films:** the continuous take inside the car during the ambush in Children of Men, using a specially built car rig.
- **Prompt:** "one continuous shot inside the moving car: the camera sits at the centre of the cabin and turns smoothly between the passengers as they talk; through the windows the road flows past at 40 km/h."
- **AI risk → fix:** passengers drift seats. Fix each person's seat and lock it.

---

## 15. Water

### Boat-riding
- **What:** the camera rides the boat, moving with the hull.
- **Viewers feel:** life at sea; the swell felt in the stomach; vulnerability.
- **Used for:** any on-deck scene.
- **Films:** Amaram, where Madhu Ambat shot close to the actors from a small boat with a one-man crew to keep it realistic and sober; the sea in its many moods in Chemmeen.
- **Rig:** handheld or gimbal with roll free, so the horizon breathes; a gyro-stabilised head when the horizon must stay level.
- **Prompt:** "the camera rides the deck at chest height; the horizon rolls 4° to each side every 7 seconds with the swell; fine spray drifts past the lens."
- **AI risk → fix:** a perfectly level horizon makes the boat feel like a set. Give roll angle and period. For a stable horizon: "the horizon stays level while the deck tilts under them."

### Waterline / split-level
- **What:** the lens sits at the waterline, dipping under and coming back up, or holding half above and half below.
- **Viewers feel:** two worlds at once; immersion; the hidden depth of water; trust (learning to swim) or threat.
- **Used for:** swimming, drowning, nets, hulls, baptism.
- **Films:** the swimming lesson in Moonlight, shot at water level, the camera dipping under the surface and back up.
- **Rig:** water housing with a split dome port.
- **Prompt:** "the lens sits exactly at the waterline; the upper half shows the man's face and the sky, the lower half his legs treading in green water; small waves wash over the lens every few seconds, dipping the view under and back up."
- **AI risk → fix:** the model picks one world. Say "upper half … lower half …".

### Shoreline track
- **What:** a lateral or lead track along the beach or riverbank, with the water in the frame layers.
- **Viewers feel:** time passing; companionship; the coast as home.
- **Used for:** walks, children running, conversations by the water.
- **Films:** Roma's beach sequence, held wide in one long take so the audience feels the danger from a distance.
- **Rig:** floating rig or a dolly on a sand platform.
- **Prompt:** "the camera travels left along the wet sand at 4 km/h, 3 m from them, keeping pace; waves wash in across the foreground every 6 seconds."
- **AI risk → fix:** the sea stops moving. Give the wave rhythm.

### Surf-line low
- **What:** a very low camera at the water's edge as waves run toward and around the lens.
- **Viewers feel:** the sea reaching for someone; threat or tenderness.
- **Used for:** someone walking into the water; boats launched; arrivals by sea.
- **Rig:** low mount with a splash bag or housing.
- **Prompt:** "the camera sits 15 cm above the sand at the water's edge; foam runs toward the lens and around it every 5 seconds while the boat is pushed into the surf behind."
- **AI risk → fix:** droplets fill the frame. Say whether drops stay on the lens or the lens stays clean.

### Underwater
- **What:** the camera fully below the surface.
- **Viewers feel:** silence, weightlessness, danger, dream, rebirth.
- **Used for:** drowning, diving, dreams, birth and rebirth imagery.
- **Rig:** underwater housing.
- **Prompt:** "underwater, 2 m below the surface, the camera drifts slowly upward toward the bright rippling surface as she sinks past it, bubbles rising from her mouth."
- **AI risk → fix:** light behaves like air. Describe shafts of light, particles, colour shift with depth.

---

## 16. Time

### Slow motion
- **What:** recording faster than playback, so time slows.
- **Viewers feel:** a gentle 2× is a dreamlike float; 3–5× is clear slow motion; 10× or more holds a splash or a falling glass in the air.
- **Used for:** memory, beauty in labour or sport, violence held in time, a fall, a decisive moment.
- **Films:** the death of the thief in Seven Samurai, slowed at the moment he falls.
- **Prompt:** "slow motion, five times slower than real time: the net opens into a full circle against the low sun." Never give a bare frame-rate number.
- **AI risk → fix:** speed changes mid-shot. One speed per shot; cut between speeds.

### Speed ramp
- **What:** speed changes inside one shot, e.g. real time → slow motion at the key moment → real time.
- **Viewers feel:** emphasis, rhythm, music-video energy.
- **Used for:** action beats, sport, music.
- **Prompt:** plan it as two shots joined by a match cut (real time, then slow motion of the same action) and ramp in the edit.
- **AI risk → fix:** in-shot speed changes look broken. Always split.

### Timelapse / hyperlapse
- **What:** a timelapse keeps the camera still while time runs fast; a hyperlapse moves the camera steadily while time runs fast around it.
- **Viewers feel:** time passing — hours, days, seasons, years; the scale of a city or nature.
- **Used for:** waiting, transitions in time, the tide, cities, montages.
- **Films:** the time-lapse cityscapes of Koyaanisqatsi.
- **Prompt:** "timelapse: the camera holds perfectly still while the tide rises over the beach and clouds race across the sky, from afternoon to dusk in 8 seconds."
- **AI risk → fix:** people move at normal speed. Say that everything except the camera moves fast.

### Frozen-moment orbit (bullet time)
- **What:** time stops, or nearly stops, while the camera travels around the frozen moment.
- **Viewers feel:** a moment lifted out of time; heavily stylised.
- **Used for:** stylised action, dreams, a moment of transcendence.
- **Films:** The Matrix.
- **Rig:** a ring of many cameras or a high-speed robot; not a single-camera move. For a realist film, plan an extreme slow-motion arc instead.
- **Prompt:** "time nearly stops: shattered glass hangs in the air while the camera arcs 90° around her over 4 seconds; only the camera moves."
- **AI risk → fix:** the action keeps moving. Say exactly what stays frozen and that only the camera moves.

### Motion control
- **What:** a programmable robotic arm that repeats a move exactly, or moves very fast and precisely.
- **Viewers feel:** precise, polished, magical repetition; past and present (or twins) in one frame on the same move.
- **Used for:** food and product inserts, twins, ghosts, then-and-now transitions.
- **Rig:** motion-control rig.
- **Prompt:** "a precise, perfectly smooth robotic move: the camera swings 90° over the plate in 1.5 seconds and stops dead."
- **AI risk → fix:** for repeated passes, use identical camera numbers.

---

## 17. Compound and signature moves

### The oner
- **What:** a whole scene in one unbroken shot.
- **Viewers feel:** immersion, real time, mounting tension, bravura; the cut is never there to release us.
- **Used for:** seduction into a world (the Copacabana in Goodfellas), war and survival (1917, The Revenant), chaos (Children of Men), a climax that must not let go (the 11-minute end of Angamaly Diaries), a whole film as one breath (Birdman).
- **Prompt:** "one continuous shot, the camera does not cut on its own," then the path in timed phases.
- **AI risk → fix:** generation lengths are limited (around 30 seconds on current models). For longer, plan hidden stitches (passing a dark doorway, a pillar, a body crossing the lens) with a short empty-frame beat at each.

### Multi-composition oner
- **What:** one take that passes through several distinct compositions — wide, medium, close, over-the-shoulder — through blocking and camera movement together.
- **Viewers feel:** the scene flows without the audience noticing the coverage; energy without cutting.
- **Used for:** dialogue scenes with movement, exposition, ensemble scenes.
- **Films:** Spielberg's oners in Raiders of the Lost Ark, Jaws, Jurassic Park; Kurosawa's moves from close-up to full shot to over-the-shoulder in one take; Lubezki walking into the close-up from the wide.
- **Prompt:** "0–4 s: wide two-shot as he enters. 4–8 s: the camera travels with him to the table and settles in a medium shot as he sits. 8–12 s: it eases in to his close-up as she answers off-screen."
- **AI risk → fix:** each composition needs a stated time window and framing.

### Foreground-wipe reveal
- **What:** the camera moves past something close (pillar, tree, passer-by), which wipes the frame and reveals the subject.
- **Viewers feel:** discovery, stealth, an elegant hidden cut point.
- **Used for:** entrances, reveals, hiding a stitch in a long take.
- **Prompt:** "the camera travels right past the stone pillar 0.5 m from the lens; as it clears the pillar, the old man is revealed sitting on the bench."
- **AI risk → fix:** the subject is visible before the wipe. Say what's visible before and after.

### Follow-then-hold
- **What:** the camera follows a character, then stops while they carry on (or the reverse).
- **Viewers feel:** the camera chooses to stay behind; separation, farewell.
- **Used for:** departures, a character leaving something forever.
- **Prompt:** "the camera follows him to the gate at 4 km/h, then stops at the gate while he walks on down the road and grows smaller."
- **AI risk → fix:** the camera keeps following. Give the stop point.

### Match move
- **What:** a move at the end of one shot continues in the next shot in another time or place.
- **Viewers feel:** time folding; memory; connection.
- **Used for:** then-and-now, memory transitions, cross-cutting.
- **Prompt:** describe both halves with the same direction, speed and framing, joined by a MATCH CUT.
- **AI risk → fix:** generate both halves with identical camera numbers.

---

## 18. Speed and timing reference

| Move | Typical speed / rate | Typical duration |
|---|---|---|
| creep | 0.1–0.3 km/h | 8–20 s |
| slow push / pull | 0.5–1 km/h | 4–8 s |
| fast push | 6–10 km/h | ~1 s |
| walking follow / lead / side | 4–5 km/h | 5–30 s |
| jog follow | 8–10 km/h | 3–8 s |
| running chase | 12–18 km/h | 2–6 s |
| vehicle tracking | 20–80 km/h | 3–10 s |
| slow pan | 5–15° per second | 3–8 s |
| reveal pan | 15–30° per second | 2–4 s |
| whip pan | blur 0.5–0.8 s | under 1.5 s total |
| 360° spin | ~36° per second | ~10 s |
| arc around a face | ≤ 90° per phase | 4–8 s |
| 360° orbit | 90° per 3 s or slower | 12 s + |
| crane rise | 0.5–1 m per second | 4–8 s |
| aerial forward | 15–40 km/h | 5–15 s |
| handheld sway (calm / tense / chaos) | 1–2 cm / 2–4 cm / 5–8 cm | — |

Ease every move in and out over about one second. A real camera with mass never starts or stops instantly.
