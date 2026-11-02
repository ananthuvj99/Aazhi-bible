---
id: L19
type: lesson
category: platform
shot: "1B v6, v7"
author: Ananthu
date: 2026-10-29
---

**L19 — "Invented location_id not in allow-list"** (1B v6, v7) — evidence: `scenes/showreel/evidence/1B-v7-error-invented-location-id.png`
Symptom: platform error at "Understanding the prompt (OpenAI)": the planner returned a location_id that is not in the project's allow-list.
What changed vs. working prompts (1A v4, 1B v1): the HOUSE LAYOUT block naming other rooms (veranda, passage, kitchen, mother's bedroom), a second location tag @hallclean, and the new tag @wallclock.
Suspected cause: the planner maps every location it reads to a location ID; rooms that are named but not attached (or a tag not registered as a location) get an invented ID and are rejected.
Rule (until the dev team confirms): one location tag per generation; describe only the room on screen; never name other rooms; register every tag before use. HOUSE LAYOUT block suspended.
Questions for the dev team: (1) Does the planner create a location for every room named in the text? (2) Is @hallclean registered as a location? (3) What type is @wallclock (character/prop/location)? (4) Can one generation use more than one location?
Update (L19): the hall tag is registered as `@hallclean`, not `@hall_clean` — an unregistered location tag is the most likely trigger for the invented location_id. Rule: copy tags exactly as registered on the platform (IDs = sheet names with no spaces and no underscores).
