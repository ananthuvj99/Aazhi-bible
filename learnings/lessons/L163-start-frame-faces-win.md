---
id: L163
type: lesson
category: characters
shot: s23-sh02e v2
author: Ranjith
date: 2026-11-13
---

**L163: The video takes faces from the start image, not from the sheets**

What happened: in s23-sh02e v2 Antony and Babu came out looking different. Ranjith: "it is picking from the image we gave; the references given should be taken". The start frame, made by the image model, already had faces that had drifted from the sheets, and the video followed the start frame.

Rule:
1. Every start frame and keyframe is checked face by face against the character sheets (face shape, eyes, nose, moustache, hair, age, build) before it is delivered; a face that is not the sheet face fails QC, like a wrong shirt.
2. Build the start frame with the character sheets as the first references, and re-run or inpaint the face with the sheet when it drifts.
3. Prefer angles where faces are small, in profile or from behind for wide and reaction shots; save large faces for close-ups built straight from the sheet.
4. Follow the sheet for everything it shows, including small things (Babu's red wrist thread): the sheet beats an older general rule.
