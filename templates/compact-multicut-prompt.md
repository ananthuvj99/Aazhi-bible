# Prompt template — compact multi-cut shot (W24)

Use for text-driven shots (no blocking video) of 5–13 s with one to three cuts, especially groups. Proven on s16b-sh19 (8 s, three cuts, eight attachments, approved first time) and s16b-sh18 v3/v4. Keep it to about 5,500–6,000 characters: longer prompts get refused by the platform planner.

Before writing: build from the creator's narration exactly (L125); trace every person he refers to in the earlier shot files and attach them with the IDs on his own account; fill the Continuity check table (L119) against the previous approved frames.

```
SCENE CONTEXT
Night, 1998, <place> (@<location>). <What happens, 3–4 sentences, in the creator's words>. One generation, <N> cuts. Nobody speaks.

ACTIVE REFERENCES
@<id>: <age, the ONLY man with…, clothes as on HIS sheet, where he is / what is in his hands>. 100% matches the reference.
… (one line per attached sheet; `(background only)` for plates)

THE <SPECIAL ELEMENT>        (one block each: THE FOOD, THE GROUP, THE SHUTTER…)
<sizes in cm/m, counts, positions; never "like" another object (L126)>
THE GROUP: not evenly spaced; each man's own posture; every person on the deck, inside the rails.

FORMAT MODE
One generation, <N> seconds, real time. Cut 1: 0 to <a> s. Hard cut. Cut 2: <a> to <b> s. Hard cut. Cut 3: <b> to <N> s. Exactly <N-1> cuts. Runs the full <N> seconds.

CAMERA AND ACTION
Cut 1 (<time>) — <camera in words: hand-held, height, distance>. <action with times; every person in frame gets his own action, man by man (L120)>.
Cut 2 (<time>) — <close-up of the key hands/object>.
Cut 3 (<time>) — <reaction close-up>.

PERFORMANCE
<the emotion in plain words; no two people move at the same moment or in the same way; eyes never on the lens; real skin, five fingers>.

LIGHTING
<practical light shown where the approved takes have it, Kelvin, direction; fill>.

AUDIO
Sound effects only — natural on-location sound, the soundtrack carries no music. <sounds>.

STYLE
Photoreal 1998 Kerala period feature film. Shot on a Sony Venice 2 full-frame digital cinema camera: wide dynamic range, clean shadows, soft highlight roll-off, true natural skin tones and skin texture, gentle filmic contrast.

POSITIVE LOCKS
Exactly <N-1> cuts, at <times>. Exactly <count> people, each once, each a different face: <who, where>. <key objects and counts>. <light, background>. Runs the full <N> seconds.
```

Uru deck shots: `@urubowplate` (background only) is always in the references, the locks and the Attach line (L131).

Delivery: "People in this shot" (name: ID, role), the Attach line (remove every other attachment, L88), duration and aspect. Fallback if the planner refuses: trim the text first; if an attachment must go, drop a far or minor one, never `@urubowplate` on an uru deck shot (L131).
