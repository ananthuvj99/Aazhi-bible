---
id: L89
type: lesson
category: platform
shot: s23-sh05-v1
author: Ranjith
date: 2026-11-08
---

**L89 — The content filter blocked men waking on mats: body words add up** (s23-sh05 v1, blocked, nothing rendered)

Symptom: Higgsfield's content filter refused s23-sh05 (three crewmen wake on their mats and hurry to the rail) before rendering.

Cause (the exact trigger is unknown): the prompt broke L72 ("barefoot" twice, "sleeveless vest") and added words that read badly together with men lying on mats: "jerk awake", "breathes hard", "hard breathing", "curled up", "bare feet thudding". The SB031 prompts written with it also had "grunt", "a hand slapping onto skin", "skin sliding", "clamped", "fingers digging in".

Rule (adds to L72):
1. Apply L72 every time: no "barefoot/bare", no "sleeveless"; a "white cotton vest"; leave feet out.
2. Never "jerk", "hard breathing / breathes hard", "grunt", "moan", "panting"; write "wakes with a start", "breathes fast", "a short breath out".
3. No skin-on-skin sounds or touch words ("slapping onto skin", "skin sliding", "clamped", "digging in"); write the action plainly: "holds his wrist tightly", "a quick pull".
4. Several men lying or sleeping together: keep it plain ("asleep on their mats", "get up"), no body-state words.
5. If a prompt is refused, reword first; if it still fails, take out reference images one at a time.

Checklist line: item 106 in `rules/pre-delivery-checklist.md`.
