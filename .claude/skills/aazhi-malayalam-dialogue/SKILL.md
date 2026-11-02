---
name: aazhi-malayalam-dialogue
description: Write spoken-register Malayalam dialogue for the film ആഴി / AAZHI (Alappad coast, Kollam; Latin Catholic fishing community; 1998–2026). Use this skill whenever the user dictates or types a scene idea, beat, or line in Malayalam, Manglish, or English and wants dialogue, a scene, or script pages back — including when the input is a messy voice transcription that needs repairing first. Also use for cleaning up garbled Malayalam dictation, converting formal/literary Malayalam into natural spoken Malayalam, writing Manglish versions of lines, or building bilingual shooting-script pages. Trigger even when the user does not name this skill or the film — any request involving Malayalam dialogue, Malayalam script writing, "make this sound natural in Malayalam", or a dictated Malayalam scene description should use this skill.
---

# AAZHI — Malayalam Dialogue

Write dialogue people would actually say on the Alappad coast — not dialogue that reads well on a page.

## The two failures this skill exists to prevent

**Failure 1 — literary drift.** Written Malayalam is overwhelmingly *granthika*-flavoured: newspapers, textbooks, subtitles, Wikipedia. So the default pull is toward `ആയിരിക്കുന്നു`, `എന്നാൽ`, `അതിനാൽ`, `പോകുകയാണ്`. Nobody on a boat talks like that. Every line must be run against `references/register-conversion.md` before it ships.

**Failure 2 — transcription rot.** Malayalam speech-to-text does two damaging things: it mangles proper nouns and coastal vocabulary, and it *auto-normalises spoken forms into written forms*. If the user said `ഞാൻ പോവാ`, the transcript may arrive as `ഞാൻ പോകുകയാണ്`. Treat formal endings in dictated input as **transcription artifacts, not authorial choices**. De-formalise by default. See `references/transcription-repair.md`.

## Intake protocol — do this before writing anything

When the input is dictated (Malayalam audio, Manglish, or broken transcript), do not start writing dialogue. First:

1. **Repair the transcript** against `references/transcription-repair.md` — restore names, place names, and sea vocabulary from the gazetteer.
2. **Confirm back in one line.** Give a single-line Manglish + English restatement of the beat as understood. Keep it to two lines total so it can be corrected in five seconds.

   > *Understood: Antony vallathil ninnu Balane nokkunnu, onnum parayunnilla. Clara-ye patti Balan oru comment idunnu.*
   > *(Antony watches Balan from the boat, says nothing. Balan makes a remark about Clara.)*

3. **Flag anything genuinely unclear** as a bullet — never guess silently on plot facts.
4. Then write.

Skip the confirm-back only when the user has typed clean input themselves or explicitly says to go straight to pages.

## Register rules — the non-negotiables

Read `references/register-conversion.md` for the full substitution table. The core habits:

- **Contract everything.** `എവിടെ → എവ്ടെ`, `ഉണ്ട് → ഒണ്ട്`, `ആയിരുന്നു → ആരുന്നു`, `അതുകൊണ്ട് → അതോണ്ട്`.
- **Kill the copula where speech kills it.** `ആയിരിക്കുന്നു` never appears in dialogue. `ആണ്` or nothing.
- **Verbs end in speech forms.** `പോകുകയാണ് → പോവാ`. `ചെയ്യുന്നു → ചെയ്യുവാ`. `സാധിക്കുകയില്ല → പറ്റില്ല`.
- **Use the low word, not the Sanskritic one.** `സമുദ്രം → കടല്`, `ജലം → വെള്ളം`, `ഗൃഹം → വീട്`, `വിവാഹം → കല്യാണം`, `മത്സ്യം → മീൻ`.
- **Sentences run short.** Coastal speech is clipped. If a line is over about twelve words, it is probably a monologue pretending to be dialogue.
- **Interruption and overlap are normal.** Characters cut each other off. Leave the sentence unfinished with `—`.

## Formality is a character weapon, not a default

This is the creative inversion that makes the register problem useful:

**The people who put Antony in prison speak formal Malayalam. Antony does not.** Ramachandran's precise bureaucratic register, Jaison's English-padded corporate speech, the courtroom's `പ്രകാരം` and `ആയതിനാൽ` — that is the cold-daylight grammar of the antagonist era, rendered in language instead of colour temperature.

So never sand formality out of Ramachandran or the court. Sand it out of everyone on the coast.

Per-character speech fingerprints are in `references/character-voices.md`. Read it before writing any scene with two or more named characters.

## Era discipline — 1998 vs 2026

Antony's speech is **frozen in 1998**. He goes into a cell with the vocabulary of a 24-year-old sailor and comes out in a world of English loanwords he did not learn naturally. This is a characterisation device, not an oversight:

- 1998 Antony: fast, warm, teasing, filler-heavy (`എടാ`, `പിന്നെ`, `അല്ലേ`), laughs mid-line.
- 2026 Antony: slow, few words, no filler, no laughter. Asks questions instead of asserting. When he uses a modern English word it lands slightly over-precise, like a word learned from print rather than from people.

Full era vocabulary split in `references/register-conversion.md` (§ Era drift).

## Output format

Default to the project's bilingual shooting-script format — parallel Malayalam, English subtitle, and a bracketed direction note. The direction note is for review only: in video prompts the scene carries one emotion tag for the whole scene, never one per line.

```
ANTONY
ML:  നീയെന്താ ഇവ്ടെ? കടല് കാണാൻ വന്നതാ?
EN:  What are you doing here? Come to look at the sea?
     [flat, not unkind — he already knows the answer]
```

Add a `MANG:` line (romanised Malayalam) **only when asked**, or when the line will be handed to a voice pipeline where the operator does not read Malayalam script. Romanisation convention is in `references/transcription-repair.md`.

For full styled HTML script pages, follow the established project format — scene heading, colour-grammar note, then the dialogue blocks above.

## Self-check before delivering

Run every line through this:

- Would a 24-year-old on a fishing boat say this out loud, or is it subtitle Malayalam?
- Any `ആയിരിക്കുന്നു` / `എന്നാൽ` / `അതിനാൽ` / `-കുകയാണ്` survivors? Remove unless the speaker is Ramachandran, the court, or Varkey.
- Is the vocabulary right for the year — no post-2000 loanwords in a 1998 scene?
- Are the sea and church words the ones the community uses, or generic dictionary words?
- Did any character get more than twelve words without being interrupted or without a reason?

## Reference files

- `references/register-conversion.md` — formal→spoken substitution table, contractions, era drift
- `references/coastal-lexicon.md` — Alappad/Kollam Latin Catholic fishing vocabulary, oaths, kinship, sea and church words
- `references/character-voices.md` — per-character speech fingerprints
- `references/transcription-repair.md` — ASR failure patterns, name gazetteer, romanisation convention

`coastal-lexicon.md` is a **living file**. When the user supplies a real line, phrase, or correction heard from the coast, add it there rather than only using it once. That file is the thing that makes this skill get better over time.
