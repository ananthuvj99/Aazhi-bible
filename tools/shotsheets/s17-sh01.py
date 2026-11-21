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

d.text((50, 30), "s17-sh01 v4 · SB025 · Sea, then the engines, then the chase", font=F(48, True), fill=INK)
d.text((50, 96), "12 s · no dialogue · grey dawn · drone 35mm, 6 m → 14 m · uru about 150 m ahead → 130 m · everyone moves", font=F(26), fill=GREY)

# 1. start and end frames
y0 = 155
d.text((50, y0), "1  WHAT YOU WILL SEE  (start frame and end frame)", font=F(32, True), fill=INK)
fw = (W - 140) // 2
for i, (path, lab) in enumerate([("scenes/showreel/attach/s17-sh01/01-START-s17sh01seastart.png", "0–3 s · START: empty sea, engines rising from behind"),
                                  ("scenes/showreel/attach/s17-sh01/05-END-s17sh01end.png", "12 s · END: the chase, uru ~130 m ahead")]):
    fr = Image.open(path).convert("RGB"); fh = int(fr.height * fw / fr.width); fr = fr.resize((fw, fh))
    x = 50 + i * (fw + 40); y = y0 + 50
    im.paste(fr, (x, y)); d.rectangle([x, y, x + fw, y + fh], outline=INK, width=2)
    d.text((x, y + fh + 8), lab, font=F(23, True), fill=INK)
    if i == 0:
        arrow((x + fw / 2, y + fh - 10), (x + fw / 2, y + fh - 120), MOT); tag((x + fw / 2 + 14, y + fh - 90), "boats burst in here at 3 s", MOT)
        tag((x + 14, y + 14), "engine sound from behind · score enters (edit)", SND)
    else:
        s = fw / 3136
        ux, uy = x + 1572 * s, y + 340 * s
        tag((x + 30, y + 40), "uru · ~130 m ahead", URU); arrow((x + 245, y + 58), (ux - 22, uy), URU, 4)
        tag((x + 30, y + 92), "Raghavan + Babu: alarm", MEN); arrow((x + 290, y + 110), (ux - 14, y + 245 * s), MEN, 4)
        tag((x + 30, y + fh - 46), "3 motorboats · 2 men each", MOT)
ye = y0 + 50 + fh + 50

# 2. side view of the camera move
y1 = ye + 20
d.text((50, y1), "2  CAMERA FROM THE SIDE  (height and tilt over time)", font=F(32, True), fill=INK)
mx, my, mw, mh = 60, y1 + 55, 1680, 330
d.rectangle([mx, my, mx + mw, my + mh], fill="#dfe8ee")
sea = my + mh - 60
d.rectangle([mx, sea, mx + mw, my + mh], fill="#5f7f94")
X = lambda m: mx + 60 + m * 9 if m < 5 else mx + 60 + m * 9 + 60
Z = lambda h: sea - h * 12
for k, (xm, h, tilt, lab) in enumerate([(0, 6, 45, "0 s · 6 m up, 45° down"), (12, 6, 45, "3 s · boats pass under"), (60, 14, 25, "8 s · 14 m up, 25°"), (100, 14, 25, "12 s")]):
    cx, cy = X(xm), Z(h) - (0 if k != 1 else 0)
    d.rectangle([cx - 16, cy - 10, cx + 16, cy + 10], fill=CAM)
    a = math.radians(tilt); arrow((cx + 16, cy), (cx + 16 + 70 * math.cos(a), cy + 70 * math.sin(a)), CAM, 4)
    d.text((cx - 40, cy - (46 if k != 1 else 82)), lab, font=F(19, True), fill=CAM)
bx = X(118)
d.polygon([(bx, sea - 4), (bx + 70, sea - 4), (bx + 84, sea + 4), (bx, sea + 4)], fill=MOT); d.text((bx - 20, sea + 12), "motorboats (12 s)", font=F(19, True), fill="white")
d.rectangle([mx + mw - 200, sea - 12, mx + mw - 30, sea + 4], fill=URU)
d.text((mx + mw - 330, sea + 12), "uru ~130 m ahead →", font=F(19, True), fill="white")
d.text((mx + 20, my + 12), "Starts low over empty sea; the boats overtake the camera from behind; it rises and tilts up to reveal the uru far ahead.", font=F(20), fill=INK)

# 3. timeline
y2 = my + mh + 60
d.text((50, y2), "3  SECOND BY SECOND", font=F(32, True), fill=INK)
tx, tw_ = 270, 1470; ty = y2 + 60
rows = [("Camera", CAM, [(0, 3, "6 m, 45° down, drifting"), (3, 5, "boats pass under"), (5, 8, "tilt up + rise to 14 m"), (8, 12, "trail 20 m behind")]),
        ("Sound", SND, [(0, 1, "wind"), (1, 3, "engines rise behind"), (3, 5, "roar past"), (5, 12, "engines scream ahead, hull slams")]),
        ("Motorboats", MOT, [(3, 5, "burst in, race away"), (5, 12, "slam, brace, half-rise · gap 150 → 130 m")]),
        ("Raghavan", MEN, [(5, 9, "leans out, peers back"), (9, 10.5, "waves down"), (10.5, 12, "leans out")]),
        ("Babu", MEN2, [(5, 9, "points back (R arm)"), (9, 12, "grips rail, steps, looks back")]),
        ("Uru", URU, [(5, 12, "revealed far ahead · small · COCHIN")])]
for sec in range(13):
    x = tx + tw_ * sec / 12; d.line([x, ty, x, ty + 72 * len(rows) + 10], fill="#d8d4cc", width=2); d.text((x - 10, ty - 34), f"{sec}s", font=F(22), fill=GREY)
for i, (lab, col, segs) in enumerate(rows):
    yy = ty + 10 + i * 72; d.text((50, yy + 8), lab, font=F(26, True), fill=col)
    for a, b, t in segs:
        x0, x1 = tx + tw_ * a / 12, tx + tw_ * b / 12
        d.rounded_rectangle([x0 + 3, yy, x1 - 3, yy + 52], 10, fill=col); d.text((x0 + 10, yy + 11), t, font=F(19, True), fill="white")

# 4. platform
y3 = ty + 72 * len(rows) + 60
d.text((50, y3), "4  ON THE PLATFORM", font=F(32, True), fill=INK)
lines = ["Start: 01-START-s17sh01seastart.png (@s17sh01seastart) · End: 05-END-s17sh01end.png (@s17sh01end)",
         "Attach: @s17sh01seastart · @s17sh01end · @uru · @raghavan · @babu (full) · remove everything else",
         "Duration 12 s · 21:9 · no dialogue · no music in the clip (tense score in the edit) · QA 100 / 100",
         "Watch for: 3 s of empty sea · boats enter from under the camera · uru small and far · everyone moving"]
for i, t in enumerate(lines): d.text((70, y3 + 55 + i * 42), "•  " + t, font=F(25), fill=INK)
im = im.crop((0, 0, W, y3 + 55 + len(lines) * 42 + 40))
im.save("scenes/showreel/storyboards/s17-sh01-clear.png"); print(im.size)
