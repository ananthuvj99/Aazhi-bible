---
id: L71
type: lesson
category: platform
shot: s13-sh05-v1
author: Ranjith
date: 2026-11-06
---

**L71 — The clip's length comes from the platform's duration setting, not from the prompt** (s13-sh05 v1)

Symptom: Antony's line shot was written for 7 seconds ("runs the full 7 seconds", timings to 7.0 s), but the platform returned a clip of about 4 seconds, cut right after his line, so the silent tail (L70) was lost.

Cause: the platform makes the clip as long as its duration field says; the prompt text cannot lengthen it. An odd length like 7 s is easy to leave at the platform's default, or may not be one of its options.

Rule:
1. Write dialogue and walk shots at **8 s** (or 12 s / 15 s for long ones, L58); avoid odd lengths like 7 s.
2. In every delivery, put the duration first in the settings line, in bold: **Duration: set the platform to 8 s**.
3. If a take comes back shorter than the prompt, check the duration field before changing the prompt.

Checklist line: item 84 in `rules/pre-delivery-checklist.md`.
