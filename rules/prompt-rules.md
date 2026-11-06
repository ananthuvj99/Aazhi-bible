# Prompt rules — Techjays AI film platform

## Dialogue language
- Spoken lines in **Malayalam script only**. No English translation and no romanised copy inside a prompt — the platform speaks extra text or hallucinates.
- Stressed words in delivery notes are quoted in Malayalam script.
- Register: spoken Alappad / Kollam Latin Catholic coastal Malayalam, not literary.
- Every line: accent stated, approximate duration, speed, pitch movement, stressed word, pauses, volume.
- Speech rate check: ~5–6 syllables per second (up to 7 when angry or rushed). No line may run past a HARD CUT.

## Emotion tags (platform "How it is said" list — only these 32)
- Emotion: happy, excited, playful, sad, angry, annoyed, scared, worried, anxious, surprised, curious, thoughtful, sarcastic, tired
- Voice: whispers, hushed, quietly, softly, shouts
- Pace: slowly, rushed, drawn out, pause, long pause
- Reaction: laughs, chuckles, sighs, exhales, gasps, crying, swallows, clears throat

UPDATED (L33, one emotion per scene): one emotion tag for the whole scene, from the list above, written once before the first line. No tags on other lines or on ACTION beats; pauses are written as timing. If the mood changes mid-scene, split it into two generations. One tag per bracket: `[scared]`, never `[scared, rushed]`, and never inside a line. Screenshots: `platform-emotion-tags/`.

## Lip-sync block (external lip-sync platform) — paste verbatim into every prompt with dialogue
> Dialogue rules: whenever a character speaks, frame them in a medium close-up with their face filling at least a third of the frame height. The speaking face is turned toward the camera, no more than 30 degrees from the lens, upright and not lying sideways. Only one person speaks in the shot; everyone else keeps their mouth closed. The speaker's head stays steady during the line; head turns, gestures and camera moves happen only in pauses between lines. The mouth is always fully visible, with nothing in front of the face, and the face is lit with soft, even frontal light. Natural, clearly articulated mouth movements matching the dialogue.

Consequence: one speaker per shot, and the speaker ALONE in frame while speaking — clean singles, no over-the-shoulder during lines (L34). Speakers are always front-facing in MCU — never profile or side view; place the camera beside whatever the speaker is talking toward (a door, another person) so their eyeline falls just beside the lens. Multi-speaker beats are split into separate shots.

## Timing
- Hold 2–3 s still at the start and 2–3 s after the last line/action of every shot, for the edit (L14).
- Set the platform's duration to the prompt's total length.

## Audio
- Sound effects only, no background music (music is added in the edit). Every AUDIO block opens with: "Sound effects only — natural on-location sound, the soundtrack carries no music."

## Detail level (Ananthu) + scope (L27)
- Prompts are fully detailed but SCOPED: only what is visible. Blocks: ON SCREEN STATE (wardrobe/props/mood as they appear, no back-story), WARDROBE, PROPS (exact counts), THIS SPACE (the one room on screen, wall by wall, 'contains only'), FRAME BREAKDOWN per cut with a LOCATION line, references assigned to cuts, then the standard blocks.
- One location per generation when there is dialogue.

## Prompt length
- Keep every prompt under ~6,500 characters (L18). Approved/working prompts were 6,000–7,000; a 9,500-character prompt errored.

## House layout block — RETIRED (L27)
- Do not include. Old rule: every prompt set inside Antony's house includes the HOUSE LAYOUT block from `locations/house-exterior/house-layout-block.txt`, placed right after ACTIVE REFERENCES, so the model never invents rooms, doors or directions.

## References
- Tag a character/location only in shots where it is on screen — and also tag the location the camera stands in when its walls or door frame frame the shot (e.g. @hallclean for a view from the passage into a bedroom).
- Attach the **clean** location sheet. Never attach a `map.png` — its text labels can print on screen.
- Wardrobe and hair come from the character sheet; write "costume exactly as in the reference" unless the user has stated something specific.

## Seedance 2.5 structure
SCENE CONTEXT → ACTIVE REFERENCES → LOCATION MAP → FIRST FRAME → FORMAT MODE → OPTICS → CAMERA → ACTION → DIALOGUE RULES → PERFORMANCE → (PHYSICS) → LIGHTING → AUDIO → STYLE → POSITIVE LOCKS.
Positive phrasing, FOV from the anchor table (12/29/47/63/84°), speed in km/h, atmosphere in % / meters, left/right from camera, no director names, and no equipment names except the one camera below.

## Camera: Sony Venice 2 (Ranjith, 2026-11-04; approved by Ananthu 2026-11-06 as the team rule)
Every shot is filmed as if on a Sony Venice 2. Every prompt names it once, in STYLE, followed by the look it gives, described by its qualities (W5, W7). Paste this line, adapting only the light words to the scene:
> Shot on a Sony Venice 2 full-frame digital cinema camera: very wide dynamic range that holds the brightest light and the deepest shade in one frame; clean, low-noise shadows; soft, gradual highlight roll-off; accurate, natural colour with rich, true skin tones; gentle filmic contrast; fine, organic texture; no over-sharpening, no glossy or video look.
- Name it only in STYLE, never in CAMERA, OPTICS or ACTION, and never as an object ("the camera" never appears in a shot).
- Keep "Every frame looks like the film itself, with nothing from the making of it" in WHAT IS IN FRAME, so the camera itself is never drawn (L46).
- Still no rig words (tripod, dolly, gimbal, crane, slider, drone, microphone) and no lens or film-stock names.
- Why the old rule said no names: names can be ignored or can upset complex moves. Test the first generation with the name at 480p; if a move breaks, report it as a lesson.

## Project locks
- 1998 Alappad coast, Latin Catholic fishing family. Act 1 grade: warm golden, fine natural grain.
- No tulsi pot or Hindu household element in Antony's home. No organisation named on screen.
- Vessel is a Beypore uru (wooden dhow), never a fishing boat.
- Pre-arrest tone: casual and day-to-day.
