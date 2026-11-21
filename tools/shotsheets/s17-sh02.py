"""Clear sheet for s17-sh02 v1 (SB025): Antony comes to the wheel and says his line to Aashaan."""
from PIL import Image, ImageDraw, ImageFont
import math

def F(sz, b=False):
    return ImageFont.truetype("C:/Windows/Fonts/" + ("segoeuib.ttf" if b else "segoeui.ttf"), sz)
W = 1800
INK, GREY = "#1d1d1f", "#6b6b6b"
ANT, AAS, CAM, LINE, VAL, RED = "#2e9e5b", "#b5651d", "#7a4fd0", "#c0392b", "#8a6d3b", "#d9432b"
im = Image.new("RGB", (W, 3000), "#f7f5f0"); d = ImageDraw.Draw(im)
def arrow(p0, p1, col, w=7):
    d.line([p0, p1], fill=col, width=w); a = math.atan2(p1[1] - p0[1], p1[0] - p0[0])
    for s in (2.6, -2.6): d.line([p1, (p1[0] + 24 * math.cos(a + s), p1[1] + 24 * math.sin(a + s))], fill=col, width=w)
def tag(xy, text, col, f=None):
    f = f or F(22, True); x, y = xy; tw = d.textlength(text, font=f)
    d.rounded_rectangle([x - 6, y - 4, x + tw + 8, y + 32], 8, fill=col); d.text((x + 1, y - 2), text, font=f, fill="white")

d.text((50, 30), "s17-sh02 v1.1 · SB025 · Antony comes to the wheel", font=F(50, True), fill=INK)
d.text((50, 98), "12 s · Malayalam line 3.5–9.3 s · [worried] · voice Mahendran J · camera at Aashaan's shoulder, 50mm, push-in after the line", font=F(25), fill=GREY)

# 1. start frame with tags and arrows
y0 = 155
d.text((50, y0), "1  WHAT YOU WILL SEE  (illustration only, not attached; who moves where)", font=F(32, True), fill=INK)
fr = Image.open("scenes/showreel/storyboards/s17-sh02-illustration.png").convert("RGB")
fw = W - 100; fh = int(fr.height * fw / fr.width); fr = fr.resize((fw, fh)); ox, oy = 50, y0 + 50
im.paste(fr, (ox, oy)); s = fw / 3136
P = lambda x, y: (ox + x * s, oy + y * s)
tag(P(700, 130), "Antony steps in (0 s)", ANT)
arrow(P(1080, 780), P(1500, 640), ANT); tag(P(1120, 800), "1 · two steps to the window", ANT)
arrow(P(1200, 520), P(2600, 510), RED); tag(P(1700, 420), "2 · points with his LEFT arm at the vallams", RED)
tag(P(2450, 560), "5 fishing vallams", VAL)
tag(P(2050, 1180), "wheel · Aashaan beside the camera (never in frame)", AAS)
cy = oy + fh + 14
d.text((50, cy), "3 · At 2.5 s he turns to Aashaan (20° right of the lens) and says the line in MCU, head steady, the window and the vallams behind him.", font=F(24), fill=GREY)

# 2. top-down map of the wheelhouse
y1 = cy + 70
d.text((50, y1), "2  MAP FROM ABOVE  (the wheelhouse)", font=F(32, True), fill=INK)
mx, my, mw, mh = 300, y1 + 60, 1100, 520
d.rectangle([mx, my, mx + mw, my + mh], fill="#c9b99a", outline=INK, width=4)
d.rectangle([mx + 80, my - 14, mx + mw - 80, my + 6], fill="#9ec3d6"); d.text((mx + mw / 2 - 160, my - 46), "glass front windows → bow, vallams ahead", font=F(22, True), fill=INK)
d.rectangle([mx - 10, my + 60, mx + 10, my + 260], fill="#f7f5f0"); d.text((mx - 260, my + 140), "side door (deck) →", font=F(22, True), fill=INK)
wx, wy = mx + mw / 2 + 60, my + 330
d.ellipse([wx - 70, wy - 20, wx + 70, wy + 20], outline="#6b4a2b", width=8); d.text((wx - 30, wy + 26), "wheel", font=F(20, True), fill=INK)
ax, ay = wx, wy + 90
d.ellipse([ax - 20, ay - 20, ax + 20, ay + 20], fill=AAS); d.text((ax - 70, ay + 26), "Aashaan (off-screen)", font=F(20, True), fill=AAS)
cx, cy2 = wx + 120, wy + 70
d.polygon([(cx - 40, cy2 - 20), (cx + 10, cy2 - 10), (cx - 10, cy2 + 30)], fill=CAM); d.text((cx + 10, cy2 + 10), "camera 1.6 m, 50mm", font=F(20, True), fill=CAM)
arrow((cx - 20, cy2 - 10), (mx + 300, my + 140), CAM, 3)
sx, sy = mx + 40, my + 160; ex, ey = mx + 230, my + 110
d.ellipse([sx - 18, sy - 18, sx + 18, sy + 18], outline=ANT, width=5); arrow((sx + 20, sy - 5), (ex - 22, ey + 5), ANT, 6)
d.ellipse([ex - 20, ey - 20, ex + 20, ey + 20], fill=ANT); d.text((ex - 40, ey + 28), "Antony speaks here", font=F(20, True), fill=ANT)
arrow((ex + 20, ey - 10), (mx + 700, my - 20), RED, 4)

# 3. timeline
y2 = my + mh + 70
d.text((50, y2), "3  SECOND BY SECOND", font=F(32, True), fill=INK)
tx, tw_ = 270, 1470; ty = y2 + 60
rows = [("Camera", CAM, [(0, 9.3, "locked at Aashaan's shoulder"), (9.3, 12, "push-in 0.3 m")]),
        ("Antony", ANT, [(0, 1.2, "steps in"), (1.2, 2.5, "points (L arm)"), (2.5, 3.5, "turns"), (3.5, 9.3, "LINE · head steady · eyes 20° right"), (9.3, 12, "breathes, glances back")]),
        ("Dialogue", LINE, [(3.5, 9.3, "Antony's Malayalam line to Aashaan (about 5.8 s)")])]
for sec in range(13):
    x = tx + tw_ * sec / 12; d.line([x, ty, x, ty + 72 * len(rows) + 10], fill="#d8d4cc", width=2); d.text((x - 10, ty - 34), f"{sec}s", font=F(22), fill=GREY)
ML = ImageFont.truetype("C:/Windows/Fonts/Nirmala.ttc", 19) if True else None
for i, (lab, col, segs) in enumerate(rows):
    yy = ty + 10 + i * 72; d.text((50, yy + 8), lab, font=F(26, True), fill=col)
    for a, b, t in segs:
        x0, x1 = tx + tw_ * a / 12, tx + tw_ * b / 12
        d.rounded_rectangle([x0 + 3, yy, x1 - 3, yy + 52], 10, fill=col)
        d.text((x0 + 10, yy + 12), t, font=F(19, True), fill="white")

# 4. platform
y3 = ty + 72 * len(rows) + 60
d.text((50, y3), "4  ON THE PLATFORM", font=F(32, True), fill=INK)
lines = ["No start image, no end image: assets only (Ranjith, v1.1)",
         "Attach: @antony20 (full) · @urudeckc3platedawn (background only) · remove everything else",
         "Duration 12 s · 21:9 · Malayalam · voice Mahendran J · [worried] · QA 100 / 100",
         "Watch for: Malayalam only · LEFT arm points · only Antony in frame · head steady on the line · wheel only inside"]
for i, t in enumerate(lines): d.text((70, y3 + 55 + i * 42), "•  " + t, font=F(25), fill=INK)
im = im.crop((0, 0, W, y3 + 55 + len(lines) * 42 + 40))
im.save("scenes/showreel/storyboards/s17-sh02-clear.png"); print(im.size)
