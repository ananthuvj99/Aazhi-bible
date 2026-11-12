# s21-sh04 v2 take — continuity review (Ananthu with Claude, 2026-11-12)

Take reviewed: Ranjith's 30 s generation (`content (7) (1).mp4`, 2206×946, 24 fps). Reported by Ananthu; the shot is Ranjith's, so these are notes for him, not changes to his shot file.

## What came out
- **Two shots, not four.** One cut only, at 15.75 s. The prompt asks for cuts at 9 s and 16 s: CUT 2 (the bow, behind Antony's right shoulder, his face turning to the fire) never appears. The fire flares inside the drone shot at 13.5 s, and CUTs 3 and 4 run together as one shot.
- Shot 1 (0–15.75 s): the drone glide from behind the stern to just above the deckhouse roof railing. Good: the moon ahead-right with its path, one lantern at the mast foot, the bow, Antony at the starboard bow, the fire small ahead-left.
- Shot 2 (15.75–30 s): the main deck looking aft; Antony wakes the men; Aashaan comes out of the door; they line up at the rail.

## Continuity breaks
1. **The sacks move from one side of the mast to the other.** Shot 1: the lashed sacks sit beside the mast on the right and reach aft of it, with the lantern between them and the mast. Shot 2: the sacks are in the foreground, between the camera and the mast, so forward of it. Ranjith's map (`storyboards/s21-sh01-sh02-sightlines.json`) puts them forward of the mast at (1.7, 3.4).
   - Root cause: the two attached frames disagree. `@s21sh04platehigh` (02) shows the sacks beside and aft of the mast; `@s21sh01startfullmoon` (03) shows them forward of it. Each cut copied its own frame.
2. **The mast changes size and place.** Shot 1: a slim pole on the centreline, forward of the sleepers. Shot 2: a thick column with iron bands and rope coils, at the left edge right beside the deckhouse — behind the sleepers instead of in front of them. Frame 03 already shows this thick mast at the left edge.
3. **The long pole (boom) falls and vanishes.** 4.5–6.0 s: a long spar lies diagonally from the mast across to the starboard rail by the sacks; from 7.0 s it is gone. The `@uru` sheet has a fixed boom from the mast aft along the centreline; the start image (01) shows it lying diagonally, frame 02 does not show it, and no prompt says where it is — so the model moves and drops it.
4. **The towels move.** Babu (by the port rail): at 15.9 s the checked towel covers his forehead and eyes; by 18.8 s it is a band round his forehead. Raghavan (mid-deck): at 15.9 s a towel lies over his eyes; at 18.8 s a band on his head plus a second folded red cloth beside his pillow. MEMORY says Raghavan's towel goes round his NECK — but frame 03 shows it on his head over his eyes, and CUT 3 of the prompt says he "pulls the towel off his eyes". The prompt and the frame contradict MEMORY.
5. **Sleepers change count and lie differently.** Shot 1 shows two sleepers lying across the deck aft of the mast (Sasi hidden by the sacks, as the map says). Shot 2 shows three: Sasi asleep against the sacks, Babu lying along the port rail (not across), Raghavan across the deck right in front of the deckhouse — with only a metre or two of deck to the door, where shot 1 shows several metres.
6. **The moon height.** The distances sheet says about 35° up; frames 01, 02 and the take show it about 12° up. Not a break inside the take, but the sheet and the frames disagree.

## Fix
A grey-box Blender scene (`build_blocking.py`, `blocking.blend`, `blocking-playblast.mp4`) holds every position from Ranjith's map: one slim mast at y = 2 with its lantern; the boom fixed on the centreline; the sacks at (1.7, 3.4), forward of the mast on the starboard side; Sasi on their bow side; Babu by the port rail; Raghavan mid-deck in front of the deckhouse with his towel round his neck; Antony at the starboard bow; Aashaan at the wheel; the deckhouse 5 × 4 m at y = −9 with its door on the port side; the moon ahead-right about 12° up; the fire ahead-left at about 500 m from 13.5 s. Both camera moves are animated in it, timed as in the take (cut at 15.75 s).

Use it in one of two ways:
1. Remake frames 02 and 03 from the Blender stills (same camera, same layout) so the two references agree, then regenerate.
2. Attach the playblast as the motion/layout reference video, with the frames.

Either way, add to MEMORY: "the boom lies fixed along the centreline from the mast back toward the deckhouse, about 3 m up; it never moves", and settle Raghavan's towel (neck, as MEMORY says, or over his eyes, as frame 03 and CUT 3 say).
