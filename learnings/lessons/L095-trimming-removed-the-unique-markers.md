---
id: L95
type: lesson
category: characters
shot: s16b-sh05-v8
author: Aswanth
date: 2026-11-08
---

**L95 — Trimming the prompt removed the "only one who…" markers, and a man with Aashaan's look joined the dance** (s16b-sh05 v8) — evidence: `scenes/showreel/evidence/s16b-sh05-v8-aashaan-look-dancing.webp`

Symptom: a grey-haired man in a cream half-sleeve shirt and white mundu — Aashaan's look — danced round the mast, although Aashaan stays on the deckhouse roof in this scene and his sheet was not attached. A second grey-haired man appeared too, and Raghavan lost his plate and towel.

Cause: to get past the platform planner, v8 cut each reference line to a few words and dropped the markers that kept the men apart ("the only grey-haired man; white vest, no shirt; the plate in his hands"). With weaker anchors the model drew a generic old sailor, close to Aashaan, who is in the same project.

Rule: when shortening a prompt, cut scene prose first, never the identity markers. Each man keeps his "only one who…" line, his full costume (what he wears AND that he wears no shirt over a vest when that is his look) and his prop. When a principal who is elsewhere in the scene looks like a crewman, give the crewman a marker that rules the principal out (here: "Raghavan wears only a white cotton vest, no shirt").

Checklist line: item 112 in `rules/pre-delivery-checklist.md`.
