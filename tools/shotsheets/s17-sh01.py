"""Clear sheet for s17-sh01 v4 (SB025): empty sea, engine sound, motorboats burst in, reveal of the uru ~150 m ahead.
Earlier versions are in git history and scenes/showreel/retired/."""
from PIL import Image, ImageDraw, ImageFont
import math

def F(sz, b=False):
    return ImageFont.truetype("C:/Windows/Fonts/" + ("segoeuib.ttf" if b else "segoeui.ttf"), sz)
W = 1800
INK, GREY = "#1d1d1f", "#6b6b6b"
URU, MOT, CAM, MEN, MEN2, SND = "#b5651d", "#2f6f4f", "#7a4fd0", "#2e9e5b", "#1f7a45", "#3a6ea5"
im = Image.new("RGB", (W, 3200), "#f7f5f0"); d = ImageDraw.Draw(im)
def arrow(p0, p1, col, w=7):
    d.line([p0, p1], fill=col, width=w); a = math.atan2(p1[1] - p0[1], p1[0] - p0[0])
    for s in (2.6, -2.6): d.line([p1, (p1[0] + 24 * math.cos(a + s), p1[1] + 24 * math.sin(a + s))], fill=col, width=w)
def tag(xy, text, col, f=None):
    f = f or F(22, True); x, y = xy; tw = d.textlength(text, font=f)
    d.rounded_rectangle([x - 6, y - 4, x + tw + 8, y + 32], 8, fill=col); d.text((x + 1, y - 2), text, font=f, fill="white")

d.text((50, 30), "s17-sh01 v5 · SB025 · Sea, then the engines, then the chase", font=F(48, True), fill=INK)
d.text((50, 96), "15 s · assets only, no start frame · drone 35mm, 75° → 25°, 6 m → 14 m · uru ~150 m → 135 m · everyone moves", font=F(26), fill=GREY)

# 1. what you will see (illustrations: the steep sea and frames from the v4 take)
y0 = 155
d.text((50, y0), "1  WHAT YOU WILL SEE  (no start frame; pictures are illustrations from the v4 take)", font=F(32, True), fill=INK)
S = "scenes/showreel/evidence/s17-sh01-v4/frames/"
pics = [(S + "sea-steep-illustration.jpg", "0–3.5 s · only sea, looking steeply down · engines rise"),
        (S + "take-4.0s.jpg", "3.5–5.5 s · boats burst in from under the camera"),
        (S + "take-8.0s.jpg", "~7 s · horizon slides in from the top WITH the uru on it"),
        (S + "take-14.9s.jpg", "15 s · the chase, uru ~135 m ahead")]
fw = (W - 140) // 2
for i, (path, lab) in enumerate(pics):
    fr = Image.open(path).convert("RGB"); fh = int(fw / 2.333); fr = fr.resize((fw, fh))
    x = 50 + (i % 2) * (fw + 40); y = y0 + 50 + (i // 2) * (fh + 60)
    im.paste(fr, (x, y)); d.rectangle([x, y, x + fw, y + fh], outline=INK, width=2)
    d.text((x, y + fh + 8), lab, font=F(23, True), fill=INK)
    if i == 1:
        tag((x + 20, y + 20), "v4 bug shown: ghost uru + horizon here. In v5 no horizon yet at 3.5–5.5 s", "#c0392b")
    if i == 2:
        tag((x + 20, y + 20), "uru solid from its first frame · never fades in (L170)", "#c0392b")
ye = y0 + 50 + 2 * (fh + 60)

# 2. side view of the camera move
y1 = ye + 20
d.text((50, y1), "2  CAMERA FROM THE SIDE  (height and tilt over time)", font=F(32, True), fill=INK)
mx, my, mw, mh = 60, y1 + 55, 1680, 330
d.rectangle([mx, my, mx + mw, my + mh], fill="#dfe8ee")
sea = my + mh - 60
d.rectangle([mx, sea, mx + mw, my + mh], fill="#5f7f94")
X = lambda m: mx + 60 + m * 9 if m < 5 else mx + 60 + m * 9 + 60
Z = lambda h: sea - h * 12
for k, (xm, h, tilt, lab) in enumerate([(0, 6, 75, "0 s · 6 m up, 75° down"), (12, 6, 75, "3.5 s · boats pass under"), (60, 14, 25, "9 s · 14 m up, 25°"), (100, 14, 25, "15 s")]):
    cx, cy = X(xm), Z(h) - (0 if k != 1 else 0)
    d.rectangle([cx - 16, cy - 10, cx + 16, cy + 10], fill=CAM)
    a = math.radians(tilt); arrow((cx + 16, cy), (cx + 16 + 70 * math.cos(a), cy + 70 * math.sin(a)), CAM, 4)
    d.text((cx - 40, cy - (46 if k != 1 else 82)), lab, font=F(19, True), fill=CAM)
bx = X(118)
d.polygon([(bx, sea - 4), (bx + 70, sea - 4), (bx + 84, sea + 4), (bx, sea + 4)], fill=MOT); d.text((bx - 20, sea + 12), "motorboats (15 s)", font=F(19, True), fill="white")
d.rectangle([mx + mw - 200, sea - 12, mx + mw - 30, sea + 4], fill=URU)
d.text((mx + mw - 330, sea + 12), "uru ~135 m ahead →", font=F(19, True), fill="white")
d.text((mx + 20, my + 12), "Starts low over empty sea; the boats overtake the camera from behind; it rises and tilts up to reveal the uru far ahead.", font=F(20), fill=INK)

# 3. timeline
y2 = my + mh + 60
d.text((50, y2), "3  SECOND BY SECOND", font=F(32, True), fill=INK)
tx, tw_ = 270, 1470; ty = y2 + 60
rows = [("Camera", CAM, [(0, 3.5, "6 m, 75° down"), (3.5, 5.5, "boats pass under"), (5.5, 9, "tilt up + rise to 14 m"), (9, 15, "trail 20 m behind")]),
        ("Sound", SND, [(0, 1, "wind"), (1, 3.5, "engines rise behind"), (3.5, 5.5, "roar past"), (5.5, 15, "engines scream ahead, hull slams")]),
        ("Motorboats", MOT, [(3.5, 5.5, "burst in"), (5.5, 15, "slam, brace, half-rise · gap 150 → 135 m")]),
        ("Uru", URU, [(7, 15, "enters with the horizon · solid · small, far, COCHIN")]),
        ("Raghavan", MEN, [(7, 10.5, "leans out, peers back"), (10.5, 12, "waves down"), (12, 15, "leans out, shades eyes")]),
        ("Babu", MEN2, [(7, 10, "points back (R arm)"), (10, 15, "grips rail, steps, looks back")])]
for sec in range(16):
    x = tx + tw_ * sec / 15; d.line([x, ty, x, ty + 72 * len(rows) + 10], fill="#d8d4cc", width=2); d.text((x - 10, ty - 34), f"{sec}s", font=F(22), fill=GREY)
for i, (lab, col, segs) in enumerate(rows):
    yy = ty + 10 + i * 72; d.text((50, yy + 8), lab, font=F(26, True), fill=col)
    for a, b, t in segs:
        x0, x1 = tx + tw_ * a / 15, tx + tw_ * b / 15
        d.rounded_rectangle([x0 + 3, yy, x1 - 3, yy + 52], 10, fill=col); d.text((x0 + 10, yy + 11), t, font=F(19, True), fill="white")

# 4. platform
y3 = ty + 72 * len(rows) + 60
d.text((50, y3), "4  ON THE PLATFORM", font=F(32, True), fill=INK)
lines = ["No start image, no end image: assets only (Ranjith's choice for v5)",
         "Attach: @uru · @raghavan · @babu (full)  ·  remove everything else",
         "Duration 15 s · 21:9 · no dialogue · no music in the clip (tense score in the edit) · QA 100 / 100",
         "Watch for: no horizon for 3.5 s · uru enters with the horizon, never fades in · uru small and far · everyone moving"]
for i, t in enumerate(lines): d.text((70, y3 + 55 + i * 42), "•  " + t, font=F(25), fill=INK)
im = im.crop((0, 0, W, y3 + 55 + len(lines) * 42 + 40))
im.save("scenes/showreel/storyboards/s17-sh01-clear.png"); print(im.size)
