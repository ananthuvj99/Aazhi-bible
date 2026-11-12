# MEMORY block: the full-moon night (SB027–SB032)

Kept by Ranjith (2026-11-12). The video model remembers nothing between generations, so every prompt in this sequence carries the same MEMORY block, word for word. It holds everything that stays the same all night: the place, the light, the plates, the people and their clothes, the props. Each shot adds one `NOW:` line for what is true at that moment: where each person is, what is in their hands, how each face looks.

Rules (see `rules/prompt-rules.md`, "Memory block"):
- Copy the block below unchanged into every prompt, right after SCENE. Never paraphrase it.
- Change it only when a shot shows the change (a person comes up from below, the fire comes closer). Then update this file first, in the same commit as the shot, and the change carries into every later prompt.
- (L145) The People line lists only the people in THIS shot, copied from the master list below; everyone else goes in NOW as "below / out of view". Each person in frame still keeps a full reference line with what tells him apart. In a view facing away from the moon, the Light line says only "the full moon is behind the camera".

## The block (copy from here)

```
MEMORY (the same night in every shot; nothing changes unless this block says so)
Place: 1998, open sea off Kerala, aboard our wooden cargo uru: blue-grey hull, carved two-deck deckhouse aft with the wheel inside, one mast with a lantern at its foot, our bow as on @urubowplate (blue triangular bow deck, pointed stem, red-brown bitts, rope coils).
Light: clear full-moon night; the moon high, ahead and RIGHT of the bow (forward views: top right with its silver path; aft views: behind the camera, never in the sky). Blue and readable, never black; warm light only from the lanterns.
People: Antony: lavender-grey striped shirt, grey-green checked mundu, barefoot. Aashaan: cream shirt over white vest, towel on LEFT shoulder, white mundu. Raghavan: thin, grey, white vest, checked towel round his neck. Babu: heavy-set, checked towel on his head, checked lungi. Sasi: long curly hair, full beard. Suresh: cream shirt, sleeves rolled, green check mundu. Balan: light-blue shirt, two pens, white mundu. One of each, never a copy or a stranger.
Fire: one burning vallam ahead-LEFT, about 500 m away until a shot shows it closer.
```

## NOW lines (one per shot, written in the shot file)
Format: `NOW: <who is where>; <what is in their hands>; <each face, in a few words>; <the fire's distance>.`

| Shot | NOW |
|---|---|
| s21-sh01 | Raghavan, Babu and Sasi asleep on mats on the main deck; Aashaan at the wheel inside, calm; Antony on watch at the bow (out of view); Suresh and Balan asleep below; no fire yet. |
| s21-sh02 | Aashaan at the wheel, both hands on the spokes, calm, steady; Antony small at the bow, relaxed; the others asleep; no fire yet. |
| s21-sh03 | Antony alone at the bow bulwark, tired but awake, at ease; the others asleep or at the wheel; no fire yet. |
| s23-sh01 … s24-sh02 | written when each shot is redone with this block (positions from `continuity/night-rescue-distances.md`). |

## Master list of people (copy only those in frame into the People line)
- Antony: lavender-grey striped shirt, grey-green checked mundu, barefoot.
- Aashaan: about 60, grey hair combed back, grey moustache, cream shirt over white vest, white towel on his LEFT shoulder, white mundu.
- Raghavan: about 60, thin, grey hair and moustache, white sleeveless vest, red-and-white checked towel round his NECK, white mundu.
- Babu: about 40, heavy-set, black moustache, red-and-white checked towel tied on his HEAD, off-white shirt, grey-brown checked LUNGI.
- Sasi: about 35, long black curly hair, full black beard, off-white shirt, white mundu.
- Suresh: curly hair, moustache, stained cream shirt, sleeves rolled, green check mundu.
- Balan: about 35, oiled hair, thin moustache, light-blue full-sleeve shirt, two pens in the left pocket, white mundu, black shoes.
