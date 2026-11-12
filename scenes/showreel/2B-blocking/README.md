# 2B blocking — Antony leaves home, Rosamma calls from the door (15 s)

Made by Ananthu with Claude, 2026-11-12, on the Blender house (`locations/house-3d/house.blend`), following the approved 2B v8 beats. Grey-box blocking for layout and timing; use the playblast as a motion/layout reference, never as a look reference.

## Files
- `2b-blocking-playblast.mp4` — 15 s, 2206×946, 24 fps.
- `2b-blocking.blend` — the scene (house + characters + cameras + wind). Cameras: `CAM_2B_v8` (wide), `CAM_2B_close_antony`; timeline markers switch between them.
- `build_2b.py` — rebuilds everything: `Blender -b -P build_2b.py -- "<this folder>"`.
- Stills at 0 s, 3 s (her line), 9.5 s (his answer, close), 12.5 s (back to the wide), 15 s.

## Cuts
| Cut | Time | Camera | What happens |
|---|---|---|---|
| 1 | 0.0–8.0 s | wide, on the sand ~25 m from the door, eye level 1.5 m, 63°; still to 5.0 s, then turns in place left after Antony, a beat behind | Antony out from behind the pillar left of the door, down the steps beside his mother, across the yard (a little left of her so she stays in view), out through the gap, left across the sand toward the lane. Rosamma at the open door with the full plate; looks down, lifts her head, calls at 3.0 s. |
| 2 | 8.0–11.5 s | close on Antony, 47° MCU, leading him ~2.2 m ahead at face height, travelling backward | He walks toward the lens into the lane and answers, a small look back toward the house (head 25°, face readable for lip-sync); lifts his right hand once at ~10 s. |
| 3 | 11.5–15.0 s | the wide again | He walks on up the lane along the west wall, smaller; she stays at the door watching, then looks down at the plate. |

## Characters (colours chosen so they never read alike)
- Antony: lavender-grey striped shirt, grey-green checked mundu, faded beige bag on his LEFT shoulder, black hair, eyes/nose/moustache so his facing reads.
- Rosamma: cream saree with a blue border, mid-blue blouse, gold cross, grey bun, the steel plate with puttu and curry in both hands.

## Wind
Every palm leans about 2.5° away from the sea (wind from the east), sways about 1° in the trunk, and its fronds flutter, each tree on its own rhythm.

## Differences from the v8 prompt (because of the measured house)
- The yard and the walk to the lane are longer in the model than the prompt assumed, so the wide's turn ends at about 12° (the prompt says 25°) and Antony is entering the lane, not already up it, at 8 s.
- The prompt is a single continuous wide; this blocking adds the close cut on his line (Ananthu, 2026-11-12) so his face is readable while he speaks. Her line stays in the wide.
