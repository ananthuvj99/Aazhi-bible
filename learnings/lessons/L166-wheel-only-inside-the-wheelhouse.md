---
id: L166
type: lesson
category: uru
shot: s16b-sh46 v1
author: Aswanth
date: 2026-11-14
---

**L166: the steering wheel came out standing on the open deck by the mast** (s16b-sh46 v1)

Symptom: in a night front shot of the uru, the spoked steering wheel stood outside on the main deck between the mast and the deckhouse, as if the helm were on the open deck; the lantern sat on the mast base.
Cause: attaching `@wheelhouse` for its front wall (L165) also gave the model the wheel, and the prompt did not say where the wheel is.
Fix: whenever `@wheelhouse` is attached for an outside shot, write that the wheel is inside the wheelhouse, behind the glass, only faintly visible through the middle window, never on the open deck; describe the deck between the mast and the deckhouse as clear (planks, ropes, bitts only). Hang lanterns on a named hook.
