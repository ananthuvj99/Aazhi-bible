# s21-sh04 v2 take: what went wrong (30 s, "Crew Awakened by Burning Vallam")

Ranjith, 2026-11-12. Checked second by second with `tools/takeqc.py` (sheets in `scenes/showreel/evidence/s21-sh04-v2/`) against the prompt, the keyframe images, MEMORY and the measured map (`storyboards/s21-sh01-sh02-sightlines.json`).

## What came out, second by second
| Time | Planned | What the take shows |
|---|---|---|
| 0–9 s | Cut 1: glide from far behind to the high view | The glide works: from far behind, in over the deckhouse to the high view. |
| 9–15 s | Cut 2: behind Antony at the bow, the fire flares at 10.5 s, his astonished face | **Cut 2 never happens.** The high view simply holds until 15 s; the fire appears at about 14 s, small on the left horizon, seen from the high view. Antony's astonishment is never shown. |
| 15–23 s | Cut 3: aft view, Antony runs in from the bow, wakes Babu; each wakes in turn | Antony appears **by the deckhouse door** (from the wrong end) and wakes Babu; the men wake and get up. |
| 23–30 s | Cut 4: Aashaan runs out; five men along the rail, not in a row, staring at the fire | Aashaan walks out and **shades his eyes at the camera**; all five end **in a straight line facing the camera**, faces blank. |

## Continuity and logic problems found
| # | Problem | Where | Why it happened (our side) |
|---|---|---|---|
| 1 | **Dialogue the prompt never asked for** | cuts 3–4 | AUDIO said only "No spoken words." When the prompt was trimmed to fit, the standard "and no voices" and the mouths-closed lock were cut. Five men waking in alarm, with no "mouths closed, no voices" lock, invites shouting. |
| 2 | **Raghavan's towel on his head** | 15–30 s | The approved s21-sh01 start frame already shows Raghavan's red-and-white towel **on his head and eyes**. The prompt said "towel over his eyes", and when he gets up it stays on his head. That makes two men in head towels, and Raghavan reads as a second Babu. My QC of that frame missed it. |
| 3 | **The sacks change place** | 9 s vs 16 s | In the high view (`@s21sh04platehigh`) the sacks sit **aft** of the mast, toward the deckhouse. In the aft view (`@s21sh01startfullmoon`) they are **forward** of the mast, near the camera. The measured map puts them 1.4 m forward of the mast. The high frame broke the map, and my QC passed it. |
| 4 | **Lantern at the mast foot** | 9 s vs 16 s | Burning in the high view, missing in the aft view. Different plates, never checked against each other. |
| 5 | **Something long falls off the uru** | about 5–6 s | A long diagonal line from the mast (a stay or spar) is there at 3–5 s and gone by 6 s, so it reads as a stick falling. The far start frame has rigging lines that the high frame doesn't, and the model drops them between the two. |
| 6 | **The bow moves in the hold** | 9–15 s | The prompt said the uru "rolls gently" while the camera held, so the whole boat sways in the frame. In a hold, the camera should ride with the boat. |
| 7 | **Cut 2 missing, fire shown in the wrong view** | 9–15 s | Four cuts in one generation: the model kept the first camera longer and dropped the bow cut. The fire was described in cut 2 only, so it appeared wherever the model happened to be. |
| 8 | **Antony enters from the wrong end** | 16 s | The aft view looks toward the deckhouse, and the bow is behind the camera. The model brought him in by the door because no frame showed where he comes from. |
| 9 | **Men in a straight row, facing the camera, faces blank** | 25–30 s | The fire lies beyond the right-hand rail and forward, so they should face the right rail, turned away from the camera. No end frame showed this, and EXPRESSIONS alone didn't hold across 30 s and five people (L92, L123). |
| 10 | **Aashaan shading his eyes at the camera** | 24–30 s | The same cause: no frame told the model where the fire is in this view. |

## What to change: keyframe plates for every beat (Ranjith, 2026-11-12)
Each beat of the 30 s gets its own plate, made from the measured map and passed through QC and the logic check, **before** any video:

| Key | Time | Plate | Status |
|---|---|---|---|
| K1 | 0 s | far behind the stern (`@s21sh04start`) | approved; keep, check the rigging lines against K2 |
| K2 | 9 s | high view (`@s21sh04platehigh`) | **remake**: sacks forward of the mast (map), Raghavan's towel at his neck, rigging as in K1 |
| K3 | 9–10 s | at the bow behind Antony, calm, no fire yet | new |
| K4 | 13–15 s | Antony's astonished profile, the fire small on the left horizon | new |
| K5 | 16 s | aft view: sleepers in their mapped places, Raghavan's towel at his neck, the lantern at the mast foot, Antony arriving from the camera side | new (replaces `@s21sh01startfullmoon` here) |
| K6 | 21 s | the men up, hurrying to the right-hand rail, mouths closed | new |
| K7 | 24 s | Aashaan coming out of the door, turning toward the rail | new |
| K8 | 30 s | five men along the right-hand rail, at different distances, facing the rail and the far glow, faint orange on their faces | new |

Then generate **four clips, one per cut, each with its start and end keyframe** (K1→K2, K3→K4, K5→K6, K7→K8), instead of one 30 s video with four cuts, and join them in the edit. Every clip is checked with `tools/takeqc.py` before the next one.

## Fixes for the prompts, whatever the method
- AUDIO always ends with "No spoken words and no voices; every mouth stays closed." That line is never trimmed (a new checklist line).
- Hold beats: "the camera rides with the boat; the boat is still in the frame."
- Every person in the MEMORY People line keeps his tell-apart detail in the image too (Raghavan: the towel at his NECK). A keyframe that breaks it fails QC.
