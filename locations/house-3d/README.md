# Antony's house in Blender (low-poly)

Made by Ananthu with Claude, 2026-11-12. A planning and blocking model, not a platform image: no ID, never attached as-is. Renders from it can be used to make start frames and plates, which then go through image QA and get their own IDs.

## Files
- `house.blend` — open in Blender. Collections: Ground, House, Antony_room, Passage, Kitchen, Roof, Outside, Cameras.
- `build_house.py` — rebuilds the whole file and the renders:
  `/Applications/Blender.app/Contents/MacOS/Blender -b -P build_house.py -- "<this folder>"`
- `renders/` — fourteen views (21:9 2206×946; top views square):
  01 front wide from the sand · 02 three-quarter from the south-east · 03 cutaway top · 04 cutaway isometric · 05 Antony's room from the south-east corner (C3) · 06 Antony's room from the passage through his door (C4) · 07 Antony's room straight down (C1, west wall at the top as on `@antonyroomc1plate`) · 08 the passage from the front door · 09 the kitchen from the south entry · 10 the veranda from the steps · 11 Antony's room from just inside his door (C2) · 12 the kitchen's west wall · 13 the west side from outside · 14 the lane at the west side looking up toward the front (c2, as `@houseexteriorc2plate`).
- Colours are measured from the reference sheets (walls, base band, red-oxide floor, doors, cot, blue checked sheet with a check pattern, rose-pink sheet, trunk, aduppu, soot, clay, roof tiles and laterite with a block pattern), so each element reads as itself.

## Built from
`house-exterior/card.md`, `elevations.webp` (@housefullview), `environment.webp` (@houseout), `map.png` (@housemap), `house-layout-block.txt`; `antony-room/card.md`, `antonyroom.webp`; `kitchen/card.md`, `map.png`; `hall/card.md`. Rosamma's room is a shell only (door and windows), as asked.

## Layout (metres; x = east, y = north, the house faces south)
- Main block 9 × 5 m: Antony's room west (x −4.5 … −1.0), passage 2 m wide in the middle, Rosamma's room east. Floor and plinth 0.45 m up; walls 3.0 m to the eaves.
- Veranda 2.6 m deep across the front: four turned white pillars, blue plinth, red-oxide floor, three central steps; easy chair west of the door, bench east; a wooden cross above the blue double door and a small holy picture to its right.
- Antony's room: cot along the west wall under the side window, head to the north, blue checked sheet and pillow, rose-pink cover sheet; shelf with books, tumbler and a small carved figure on the north wall; hooks with navy and white cloths in the north-west corner; grey trunk against the north wall, east side; the one clock on the front wall beside the front window, near the west corner, at 9:20.
- Kitchen 7.8 × 3.6 m across the back, under a lower hipped roof with the chimney at the north-west: aduppu on its red-oxide platform in the north-west corner with the soot stain; barred north window with white shutters; doors in the west and east walls and, high toward the back of each side wall, a small barred window without shutters (as on the side elevations); niche shelves, vessel shelf, switchboard and the two Sacred Heart pictures on the west wall; dried fish and a winnow on the east wall; grinder, milk can, stool with coconut halves, lantern, water pot.
- Compound (measured on the c1 plate against the 9.6 m veranda): about 11.6 m wide, the west wall ~1 m and the east wall ~1.2 m beyond the house, the front wall ~7.5 m in front of the veranda with a 2.2 m gap on line with the steps. Four palms inside: by the front-west corner, beside the west corner of the veranda, and a pair at the front-east corner leaning out toward the cliff.
- Headland and cliff (`@houseout`, c1 plate): red laterite ground runs past the east wall and in front of the compound on the right to a cliff edge that cuts back diagonally (about 7 m east of the house at the back, wider toward the front); the cliff drops about 10 m to the beach with boats; the bay's beach curves away north-east to the white church about 250 m off; green hills beyond the bay; a palm grove behind the village on the west.
- `CAM_ext_front` is c1-wide: on the sand about 30 m from the door, 3.5 m up, looking slightly down, 55°.
- The lane along the WEST side (`@houseexteriorc2plate`, `@houseexteriorc1plate`): the west compound wall stands close beside the house (about 1 m); outside it a sandy lane about 3 m wide falls gently toward the back (2.5 cm per metre), level with the front sand at the front corner; a low red earth bank (about 0.8 m) on its far side with a wooden electric pole at its foot (c2 plate); past the back of the compound the lane falls faster, and beyond the bank the ground drops away to the west, so the neighbours' tiled cottages and the palm grove sit below the yard (c1 plate; Ananthu chose c1 for the village side, 2026-11-12).
- Outside: rear clothesline, stone platform with a clay pot and two cans, firewood; low laterite compound wall with the open gap on line with the steps; red-earth yard, sand in front and on the west lane; the cliff and beach to the east; six coconut palms.
- Morning sun from the east.

## Kitchen checked against `@kitchenclean` (2026-11-12)
Fixed to match the sheet: the north window is now a double window (two barred panes and a centre mullion) in a white surround, with four white shutters folded back flat on the inside wall, its sill above the blue band; the soot is a plume that narrows as it climbs to the roof (it was a black box); a small black pan and a round tray leaning on the wall were added to the aduppu.
Still different from the sheet (left as the house plans have them):
- **Proportion:** the sheet reads as a nearly square room; the plans make the kitchen 7.8 m wide and 3.6 m deep across the back of the house.
- **View from the north window:** the sheet shows the open sea with boats; in the model the north window looks out over the yard toward the bay, the hills and the church, because the sea is east of the house (`@houseout`).
- **Small barred side windows** high on the west and east walls come from the side elevations; the sheet does not show them.

## Open conflicts kept as the interior sheets show them
- Kitchen doors: the rear elevation shows a centre back door; the kitchen sheet and the cutaway show doors in the west and east walls only (L10). The model follows the kitchen sheet.
- Clock time: the Scene 1 ledger says 7:45; the latest clock frames are at 9:20. The model shows 9:20; change the two `Clock_*_0920` hands if the ledger stays at 7:45.
