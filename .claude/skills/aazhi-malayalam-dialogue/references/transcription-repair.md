# Transcription repair

When input arrives from Malayalam voice dictation, assume it is roughly 80% right and that the errors cluster in predictable places. Repair before writing.

## The four failure modes

### 1. Auto-formalisation (the invisible one)

Malayalam speech-to-text is trained largely on read speech and normalises spoken forms into written ones. The user says `ഞാൻ പോവാ` and the transcript says `ഞാൻ പോകുകയാണ്`.

**Consequence:** formal endings in a dictated transcript are usually the machine's, not the author's. De-formalise by default. Do not treat `-കുകയാണ്` in a transcript as an instruction to write formal dialogue.

### 2. Proper noun mangling

Names and place names are the most likely words to be wrong and the most damaging to get wrong. Snap them back to the gazetteer below by sound, not spelling.

### 3. English-in-Malayalam collapse

Code-mixed English words spoken inside a Malayalam sentence come back as nonsense Malayalam. If a word in the transcript is semantically impossible in context, try reading it as a mis-transcribed English word.

*Example:* a stray `ഷോട്ട്` or `ഷോർട്ട്` in a scene-direction sentence is almost always the English *shot*.

### 4. Homophone and near-homophone swaps

| Likely wrong | Probably meant |
|---|---|
| അഴി | ആഴി *(the title — always long-aa)* |
| കഥ | കടല് |
| വല്ലം | വള്ളം |
| ഉറു | ഉരു |
| കത്തി | കത്ത് |
| ക്ഷമ | ക്ഷമ *(verify — thematic word, do not swap out)* |

## Name gazetteer

Snap any near-match in a transcript to these spellings.

**Characters**

| Malayalam | Roman |
|---|---|
| അന്തോണി | Antony |
| ക്ലാര | Clara |
| ബാലൻ | Balan |
| ജെയ്സൺ ഫെർണാണ്ടസ് | Jaison Fernandes |
| രാമചന്ദ്രൻ | Ramachandran |
| വർക്കി | Varkey |
| സെൽവൻ | Selvan |

**Places and objects**

| Malayalam | Roman |
|---|---|
| ആഴി | AAZHI *(long aa — never അഴി / AZHI)* |
| ആലപ്പാട് | Alappad |
| കൊല്ലം | Kollam |
| കച്ചത്തീവ് | Katchatheevu |
| ബേപ്പൂർ | Beypore |
| പാക് കടലിടുക്ക് | Palk Strait |
| ഉരു | uru |
| വിശുദ്ധ അന്തോണീസ് പള്ളി | St. Anthony's Church |

## Confirm-back format

After repair, restate the beat in two lines only:

```
Understood: <one line Manglish>
(<one line English>)
```

Then list only genuinely ambiguous points as bullets. Do not restate what was clear — the whole value of the confirm-back is that it is fast enough to correct in seconds.

## Romanisation convention (Manglish)

Used for `MANG:` lines and confirm-backs. Consistency matters more than linguistic precision — this is for a human operator reading quickly, not for a phonetician.

- Long vowels doubled: `aa`, `ee`, `oo` — *kadal*, *aazhi*, *veedu*
- ഴ → `zh` — *aazhi*, *kozhi*
- ള → `l` or `ll` — *valam*, *vallam*
- ണ → `n` / `nn` — *pani*, *panni* (mind the minimal pairs)
- റ → `r`; ററ → `tt` — *thatta*
- Geminates doubled: *vallam*, *chetta*, *ammachi*
- Retroflex vs dental is not marked. Context carries it.
- English words inside a Malayalam sentence stay in English spelling: *ee deal close cheythaa*

**Note for the voice pipeline.** Romanisation is for humans. Feed Malayalam script, not Manglish, to ElevenLabs — Manglish will be read as English phonetics and produce wrong output.
