"""Clear sheet for s17-sh03 v1 (SB025): Aashaan's line and the handover of the wheel. Drawn frame (assets only, no start image)."""
from PIL import Image, ImageDraw, ImageFont
import math

def F(sz, b=False):
    return ImageFont.truetype("C:/Windows/Fonts/" + ("segoeuib.ttf" if b else "segoeui.ttf"), sz)
W = 1800
INK, GREY = "#1d1d1f", "#6b6b6b"
ANT, AAS, CAM, LINE, WOOD = "#2e9e5b", "#b5651d", "#7a4fd0", "#c0392b", "#4a3424"
im = Image.new("RGB", (W, 3000), "#f7f5f0"); d = ImageDraw.Draw(im)
def arrow(p0, p1, col, w=7):
    d.line([p0, p1], fill=col, width=w); a = math.atan2(p1[1] - p0[1], p1[0] - p0[0])
    for s in (2.6, -2.6): d.line([p1, (p1[0] + 24 * math.cos(a + s), p1[1] + 24 * math.sin(a + s))], fill=col, width=w)
def tag(xy, text, col, f=None):
    f = f or F(22, True); x, y = xy; tw = d.textlength(text, font=f)
    d.rounded_rectangle([x - 6, y - 4, x + tw + 8, y + 32], 8, fill=col); d.text((x + 1, y - 2), text, font=f, fill="white")

d.text((50, 30), "s17-sh03 · SB025 · Aashaan gives Antony the wheel", font=F(50, True), fill=INK)
d.text((50, 98), "10 s · Malayalam line 3.0–5.8 s · [worried] · voice Rinoy · reverse of s17-sh02 · assets only, no start image", font=F(25), fill=GREY)

# 1. drawn frame
y0 = 155
d.text((50, y0), "1  WHAT YOU WILL SEE  (drawn frame: the camera at Antony's spot looks back at the wheel)", font=F(32, True), fill=INK)
fx, fy, fw = 50, y0 + 55, W - 100; fh = int(fw / 2.333)
d.rectangle([fx, fy, fx + fw, fy + fh], fill="#3b2a1e", outline=INK, width=3)
for k in range(1, 14):
    x = fx + k * fw / 14; d.line([x, fy, x, fy + fh], fill="#2f2117", width=3)          # back-wall planks
d.rectangle([fx, fy + 40, fx + fw, fy + 70], fill="#2a1d14")                                # beam
d.rectangle([fx, fy, fx + 70, fy + fh], fill="#d9cfd3"); d.text((fx + 6, fy + fh / 2), "door", font=F(20, True), fill=INK)
d.ellipse([fx + fw - 330, fy + 110, fx + fw - 270, fy + 190], outline="#b8902e", width=6); d.text((fx + fw - 350, fy + 200), "lantern (unlit)", font=F(19, True), fill="#e8d7a0")
# Aashaan MCU
cx = fx + fw / 2 + 40
d.ellipse([cx - 95, fy + 120, cx + 95, fy + 330], fill="#8a5a3c")                        # head
d.rectangle([cx - 80, fy + 115, cx + 80, fy + 150], fill="#9a9a9a")                     # grey hair
d.rectangle([cx - 40, fy + 255, cx + 40, fy + 272], fill="#b5b5b5")                     # moustache
d.polygon([(cx - 260, fy + fh), (cx - 200, fy + 360), (cx + 200, fy + 360), (cx + 260, fy + fh)], fill="#e8dfc8")  # shirt
d.rectangle([cx - 60, fy + 360, cx + 60, fy + fh], fill="#f4f4f0")                       # vest
d.rectangle([cx + 120, fy + 340, cx + 200, fy + fh], fill="#ffffff")                     # towel on HIS left = frame right
# wheel top
layer = im.crop((fx, fy, fx + fw, fy + fh)); ld = ImageDraw.Draw(layer)
ld.arc([cx - fx - 330, fh - 120, cx - fx + 330, fh + 420], 200, 340, fill="#6b4a2b", width=26)
im.paste(layer, (fx, fy)); d = ImageDraw.Draw(im)
tag((cx - 120, fy + 60), "AASHAAN · MCU · eyes 20° LEFT of lens", AAS)
tag((cx + 210, fy + 380), "towel on his LEFT shoulder", AAS)
tag((fx + 120, fy + fh - 60), "6–7 s: Antony's hands come in from the LEFT, take the spokes", ANT)
arrow((fx + 140, fy + fh - 80), (cx - 260, fy + fh - 60), ANT)
arrow((cx - 120, fy + 220), (fx + 90, fy + 230), AAS); tag((fx + 100, fy + 160), "0.6 s glance back · 9.5 s exits left to the door", AAS)
cy = fy + fh + 14
d.text((50, cy), "Antony stands at the camera, about 20° left of the lens (he looked 20° RIGHT to Aashaan in s17-sh02: screen direction kept).", font=F(24), fill=GREY)

# 2. map
y1 = cy + 70
d.text((50, y1), "2  MAP FROM ABOVE  (same wheelhouse as s17-sh02, camera reversed)", font=F(32, True), fill=INK)
mx, my, mw, mh = 300, y1 + 60, 1100, 460
d.rectangle([mx, my, mx + mw, my + mh], fill="#c9b99a", outline=INK, width=4)
d.rectangle([mx + 80, my - 14, mx + mw - 80, my + 6], fill="#9ec3d6"); d.text((mx + mw / 2 - 150, my + 14), "front windows (bow ahead)", font=F(22, True), fill=INK)
d.rectangle([mx - 10, my + 60, mx + 10, my + 240], fill="#f7f5f0"); d.text((mx - 250, my + 140), "side door (deck)", font=F(22, True), fill=INK)
wx, wy = mx + mw / 2 + 60, my + 300
d.ellipse([wx - 70, wy - 20, wx + 70, wy + 20], outline="#6b4a2b", width=8); d.text((wx - 30, wy - 56), "wheel", font=F(20, True), fill=INK)
ax, ay = wx, wy + 70
d.ellipse([ax - 22, ay - 22, ax + 22, ay + 22], fill=AAS); d.text((ax + 30, ay - 10), "Aashaan (speaks)", font=F(20, True), fill=AAS)
arrow((ax - 20, ay + 10), (mx + 30, my + 200), AAS, 4); d.text((mx + 60, my + 330), "exits to the door after the line", font=F(19, True), fill=AAS)
ex, ey = mx + 230, my + 110
d.ellipse([ex - 20, ey - 20, ex + 20, ey + 20], fill=ANT); d.text((ex - 30, ey - 52), "Antony", font=F(20, True), fill=ANT)
c = (ex + 70, ey + 40); d.polygon([(c[0] + 30, c[1] + 22), (c[0] - 10, c[1] - 8), (c[0] - 22, c[1] + 26)], fill=CAM)
arrow((c[0] + 10, c[1] + 10), (ax - 30, ay - 30), CAM, 3); d.text((c[0] + 30, c[1] - 30), "camera 1.6 m, 50mm", font=F(20, True), fill=CAM)

# 3. timeline
y2 = my + mh + 70
d.text((50, y2), "3  SECOND BY SECOND", font=F(32, True), fill=INK)
tx, tw_ = 270, 1470; ty = y2 + 60
rows = [("Camera", CAM, [(0, 5.8, "locked MCU on Aashaan"), (5.8, 10, "slow tilt down to the wheel")]),
        ("Aashaan", AAS, [(0, 0.6, ""), (0.6, 1.6, "glance back"), (1.6, 3, "turns, nods"), (3, 5.8, "LINE · head steady"), (5.8, 9.5, "lets go, pats wheel, exits left")]),
        ("Antony", ANT, [(7, 10, "hands only: grips the spokes")]),
        ("Dialogue", LINE, [(3, 5.8, "Aashaan's Malayalam line (2.8 s)")])]
for sec in range(11):
    x = tx + tw_ * sec / 10; d.line([x, ty, x, ty + 72 * len(rows) + 10], fill="#d8d4cc", width=2); d.text((x - 10, ty - 34), f"{sec}s", font=F(22), fill=GREY)
for i, (lab, col, segs) in enumerate(rows):
    yy = ty + 10 + i * 72; d.text((50, yy + 8), lab, font=F(26, True), fill=col)
    for a, b, t in segs:
        x0, x1 = tx + tw_ * a / 10, tx + tw_ * b / 10
        d.rounded_rectangle([x0 + 3, yy, x1 - 3, yy + 52], 10, fill=col); d.text((x0 + 10, yy + 12), t, font=F(19, True), fill="white")

# 4. platform
y3 = ty + 72 * len(rows) + 60
d.text((50, y3), "4  ON THE PLATFORM", font=F(32, True), fill=INK)
lines = ["No start image, no end image: assets only",
         "Attach: @aashaan (full) · @antony20 (hands and sleeves only) · remove everything else",
         "Duration 10 s · 21:9 · Malayalam · voice Rinoy · [worried] · QA 100 / 100",
         "Watch for: only Aashaan's face while he speaks · eyes 20° LEFT · towel on his LEFT shoulder · Antony = hands only"]
for i, t in enumerate(lines): d.text((70, y3 + 55 + i * 42), "•  " + t, font=F(25), fill=INK)
im = im.crop((0, 0, W, y3 + 55 + len(lines) * 42 + 40))
im.save("scenes/showreel/storyboards/s17-sh03-clear.png"); print(im.size)
