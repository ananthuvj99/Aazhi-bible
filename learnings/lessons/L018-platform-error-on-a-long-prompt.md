---
id: L18
type: lesson
category: platform
shot: "1B v6"
author: Ananthu
date: 2026-10-29
---

**L18 — Platform error on a long prompt** (1B v6) — SUPERSEDED by L19: v7 at 5,300 chars failed the same way, so length was not the cause. Keeping prompts compact is still good practice.
Symptom: generation failed with an error. Measured: 1A v4 (worked) 6,985 chars; 1B v1 (worked) 6,132; 1B v6 (error) 9,468.
Suspected cause: prompt length limit, likely ~8,000 characters.
Rule: keep prompts under ~6,500 characters — short HOUSE LAYOUT, minimal reference lines (the sheet carries the look), no repeated descriptions across blocks. Confirm the limit with the platform team.
