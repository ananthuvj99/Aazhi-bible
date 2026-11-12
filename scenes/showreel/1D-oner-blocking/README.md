# 1D-oner blocking — Antony from his room, down the passage, to the kitchen doorway (14 s, one take, silent)

Made by Ananthu with Claude, 2026-11-12, on the Blender house (`locations/house-3d/house.blend`), following the 1D-oner v1 prompt (`scenes/showreel/1D-oner.md`). Grey-box blocking for positions, paths, timing and camera; never a look reference.

## Files
- `1d-oner-blocking-playblast.mp4` — 14 s, 1280×548 (normal quality), 24 fps.
- `1d-oner-blocking.blend`, `build_1d.py` (rebuild: `Blender -b -P build_1d.py -- "<this folder>"`).
- `plan-topview.png` — the plan: Antony's path (yellow), the camera's path (blue), Rosamma at the stove. Planning only, never attach.
- `stills-sheet.jpg` and five stills (0.5, 2, 6, 9, 13 s).

## Beats
| Time | Antony | Camera |
|---|---|---|
| 0.0–3.8 s | In the middle of his room, the cot beside him; hears her, scratches his head with both hands, tugs the mundu knot | Still, from the room's north-east corner by the trunk, 75°, looking toward the front wall: him in the middle, the barred front window and the one wall clock (front wall, near the west corner) behind him, the side window and the cot along the right |
| 3.8–6.5 s | Walks quickly to his door, steps into the passage and turns LEFT (north) | Pans LEFT with him (his door is off frame left) and follows him through the door |
| 6.5–11.5 s | Up the passage toward the open kitchen doors, a hand through his hair | Follows a beat behind, over his right shoulder |
| 11.5–14.0 s | Stops against the RIGHT side of the kitchen doorway, rubs the back of his neck, turns a little toward his mother | Eases to a stop close behind his right shoulder, looking past him to Rosamma at the stove (back to us, stirring) |

Characters: Antony in the home look (@antonyhome: white vest, checked mundu, silver chain, messy hair); Rosamma (cream saree, mid-blue blouse, grey bun, a long wooden ladle).
In this scene the kitchen double doors stand wide open, flat against the passage's end wall, so the doorway is clear.

## v2: camera only, no people (2026-11-12)
The first generation from the v1 blocking came out robotic: the model copied the grey-box figure's stiff arm and walk motion. It also showed the wrong clock time. v2 has **no people at all**, only the house and the camera, so the reference video carries the space and the camera move and nothing else. Antony's acting comes from the prompt text and @antonyhome.
- `1d-oner-camera-v2.mp4` — 14 s, 1280×548, 24 fps, motion blur. `1d-oner-camera-v2.blend`, `build_1d_camera.py`.
- The camera runs one smooth curve, using keyed positions and a keyed look-at point with eased (Bezier) curves. It has no follow-lag and no float, and keeps the same beats as v1:
  - **0–3.8 s:** a barely-there creep from the NE corner with the clock, the front window, the side window and the cot in frame.
  - **3.8–5.5 s:** turns LEFT toward his door.
  - **5.5–7.8 s:** through the door at its centre, turning left up the passage.
  - **7.8–11.5 s:** glides up the passage toward the open kitchen doors.
  - **11.5–14 s:** settles at the doorway with the aduppu at back-left.
- Stills: `v2-still-*.png` (0.5, 4.8, 6.6, 9, 13.5 s).
- The house model's kitchen was corrected against `@kitchenclean` before this render: double north window with four shutters, a soot plume, and a pan and tray on the aduppu. See `locations/house-3d/README.md`.
