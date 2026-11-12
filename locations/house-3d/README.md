# Antony's house in Blender (low-poly)

Made by Ananthu with Claude, 2026-11-12. A planning and blocking model, not a platform image: no ID, never attached as-is. Renders from it can be used to make start frames and plates, which then go through image QA and get their own IDs.

## Files
- `house.blend` — open in Blender. Collections: Ground, House, Antony_room, Passage, Kitchen, Roof, Outside, Cameras.
- `build_house.py` — rebuilds the whole file and the renders:
  `/Applications/Blender.app/Contents/MacOS/Blender -b -P build_house.py -- "<this folder>"`
- `renders/` — ten views (21:9 2206×946; top views square):
  01 front wide from the sand · 02 three-quarter from the south-east · 03 cutaway top · 04 cutaway isometric · 05 Antony's room from the south-east corner (C3) · 06 Antony's room from the passage through his door (C4) · 07 Antony's room straight down (C1, west wall at the top as on `@antonyroomc1plate`) · 08 the passage from the front door · 09 the kitchen from the south entry · 10 the veranda from the steps.

## Built from
`house-exterior/card.md`, `elevations.webp` (@housefullview), `environment.webp` (@houseout), `map.png` (@housemap), `house-layout-block.txt`; `antony-room/card.md`, `antonyroom.webp`; `kitchen/card.md`, `map.png`; `hall/card.md`. Rosamma's room is a shell only (door and windows), as asked.

## Layout (metres; x = east, y = north, the house faces south)
- Main block 9 × 5 m: Antony's room west (x −4.5 … −1.0), passage 2 m wide in the middle, Rosamma's room east. Floor and plinth 0.45 m up; walls 3.0 m to the eaves.
- Veranda 2.6 m deep across the front: four turned white pillars, blue plinth, red-oxide floor, three central steps; easy chair west of the door, bench east; a wooden cross above the blue double door and a small holy picture to its right.
- Antony's room: cot along the west wall under the side window, head to the north, blue checked sheet and pillow, rose-pink cover sheet; shelf with books, tumbler and a small carved figure on the north wall; hooks with navy and white cloths in the north-west corner; grey trunk against the north wall, east side; the one clock on the front wall beside the front window, near the west corner, at 9:20.
- Kitchen 7.8 × 3.6 m across the back, under a lower hipped roof with the chimney at the north-west: aduppu on its red-oxide platform in the north-west corner with the soot stain; barred north window with white shutters; doors in the west and east walls; niche shelves, vessel shelf, switchboard and the two Sacred Heart pictures on the west wall; dried fish and a winnow on the east wall; grinder, milk can, stool with coconut halves, lantern, water pot.
- Outside: rear clothesline, stone platform with a clay pot and two cans, firewood; low laterite compound wall with the open gap on line with the steps; red-earth yard, sand in front and on the west lane; the cliff and beach to the east; six coconut palms.
- Morning sun from the east.

## Open conflicts kept as the interior sheets show them
- Kitchen doors: the rear elevation shows a centre back door; the kitchen sheet and the cutaway show doors in the west and east walls only (L10). The model follows the kitchen sheet.
- Clock time: the Scene 1 ledger says 7:45; the latest clock frames are at 9:20. The model shows 9:20; change the two `Clock_*_0920` hands if the ledger stays at 7:45.
