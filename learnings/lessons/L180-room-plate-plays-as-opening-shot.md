---
id: L180
type: lesson
category: in-frame
shot: s17-sh04 v4
author: Ranjith
date: 2026-11-24
---

Symptom: the take opened on a different view of the wheelhouse (side door closed, lantern lit, from the night room plate) for about 4 s, then morphed into the real start frame (door open, dawn). Antony's line ran across both views, so the dialogue came "in different frames" (Ranjith: "first three frames look different").
Cause: the room plate `@urudeckc3platenight2` was attached as the room's design, but it is shot from nearly the same angle as the start frame; the model played the plate as an opening shot and only reached the start frame later.
Rule: when the start frame already shows the room from the shot's own angle, do not attach a room plate from a similar angle; the start frame carries the room. Attach a room plate only for parts of the room the start frame does not show, and never one from the same view. Put the line early, on the start frame's view, with the camera locked until it ends.
Checklist line: no room plate from the start frame's own angle; if the start frame shows the room, the plate stays out (L180).
