"""Clear sheet for s17-sh04 v1 (SB025): Antony cuts hard and calls the order. Drawn frame (assets only)."""
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

d.text((50, 30), "s17-sh04 · SB025 · Cut hard — ropes up!", font=F(50, True), fill=INK)
d.text((50, 98), "10 s · Malayalam line 3.0–5.8 s · [worried] · voice Mahendran J · camera at the front windows looking aft · assets only", font=F(25), fill=GREY)

# 1. drawn frame
y0 = 155
d.text((50, y0), "1  WHAT YOU WILL SEE  (drawn frame: the camera at the front windows looks aft at Antony)", font=F(32, True), fill=INK)
fx, fy, fw = 50, y0 + 55, W - 100; fh = int(fw / 2.333)
frame = Image.new("RGB", (fw, fh), "#3b2a1e"); fd = ImageDraw.Draw(frame)
for k in range(1, 14):
    x = k * fw / 14; fd.line([x, 0, x, fh], fill="#2f2117", width=3)
fd.rectangle([0, 40, fw, 70], fill="#2a1d14")
fd.rectangle([fw - 300, 90, fw - 60, fh], fill="#d9cfd3"); fd.rectangle([fw - 300, int(fh * .55), fw - 60, fh], fill="#8fa6b2")
fd.polygon([(fw - 250, int(fh * .6)), (fw - 150, int(fh * .58)), (fw - 120, int(fh * .62)), (fw - 150, int(fh * .66)), (fw - 250, int(fh * .66))], fill="#2f3f36")
for k in range(8): fd.ellipse([fw - 125 + k * 6, int(fh * .58) - k * 4, fw - 117 + k * 6, int(fh * .58) - k * 4 + 8], fill="#ffffff")
fd.ellipse([250, 110, 310, 190], outline="#b8902e", width=6)
cx = fw / 2 - 80
fd.ellipse([cx - 95, 120, cx + 95, 330], fill="#8a5a3c"); fd.rectangle([cx - 85, 112, cx + 85, 160], fill="#1d1d1d")
fd.polygon([(cx - 260, fh), (cx - 200, 360), (cx + 200, 360), (cx + 260, fh)], fill="#b9b2c8")
for k in range(-9, 10): fd.line([cx + k * 22, 365, cx + k * 26, fh], fill="#a49cb6", width=3)
fd.arc([cx - 330, fh - 120, cx + 330, fh + 420], 200, 340, fill="#6b4a2b", width=26)
frame = frame.rotate(-4, resample=Image.BICUBIC, fillcolor="#1d1d1f")
im.paste(frame, (fx, fy)); d = ImageDraw.Draw(im)
cxa = fx + cx
tag((cxa - 140, fy + 60), "ANTONY · MCU · eyes 15° LEFT (to the bow)", ANT)
tag((fx + fw - 460, fy + 110), "side door: motorboat close astern", "#2f3f36")
tag((cxa - 330, fy + fh - 60), "0.3–2.3 s: spins the wheel hard", ANT)
tag((fx + 20, fy + 20), "room heels ~6° (camera rolls with the boat)", CAM)
cy = fy + fh + 14
d.text((50, cy), "Aashaan is at the bow, behind the camera, about 15° left of the lens. After the line: fast 0.4 m push-in, the boat comes upright.", font=F(24), fill=GREY)

# 2. map
y1 = cy + 70
d.text((50, y1), "2  MAP FROM ABOVE  (camera at the front windows, looking aft)", font=F(32, True), fill=INK)
mx, my, mw, mh = 300, y1 + 60, 1100, 460
d.rectangle([mx, my, mx + mw, my + mh], fill="#c9b99a", outline=INK, width=4)
d.rectangle([mx + 80, my - 14, mx + mw - 80, my + 6], fill="#9ec3d6"); d.text((mx + mw / 2 - 260, my + 14), "front windows → bow, Aashaan 15 m ahead", font=F(22, True), fill=INK)
d.rectangle([mx - 10, my + 60, mx + 10, my + 240], fill="#f7f5f0"); d.text((mx - 280, my + 140), "side door (port)", font=F(22, True), fill=INK)
wx, wy = mx + mw / 2 + 60, my + 300
d.ellipse([wx - 70, wy - 20, wx + 70, wy + 20], outline="#6b4a2b", width=8); d.text((wx + 80, wy - 12), "wheel", font=F(20, True), fill=INK)
ax, ay = wx, wy + 70
d.ellipse([ax - 22, ay - 22, ax + 22, ay + 22], fill=ANT); d.text((ax + 30, ay - 10), "Antony (speaks)", font=F(20, True), fill=ANT)
c = (wx, my + 60); d.polygon([(c[0], c[1] + 34), (c[0] - 22, c[1]), (c[0] + 22, c[1])], fill=CAM)
arrow((c[0], c[1] + 36), (wx, wy - 30), CAM, 3); d.text((c[0] + 30, c[1] + 4), "camera 1.6 m, 50mm", font=F(20, True), fill=CAM)
d.polygon([(mx - 200, my + mh - 40), (mx - 120, my + mh - 50), (mx - 100, my + mh - 40), (mx - 120, my + mh - 30)], fill="#2f3f36"); d.text((mx - 290, my + mh - 20), "motorboat, port quarter", font=F(19, True), fill=INK)

# 3. timeline
y2 = my + mh + 70
d.text((50, y2), "3  SECOND BY SECOND", font=F(32, True), fill=INK)
tx, tw_ = 270, 1470; ty = y2 + 60
rows = [("Camera", CAM, [(0, 5.8, "locked, rolls with the heel"), (5.8, 7.3, "fast push-in"), (7.3, 10, "hold close")]),
        ("Antony", ANT, [(0.3, 2.3, "spins the wheel"), (2.3, 3, "braces"), (3, 5.8, "LINE · head steady"), (5.8, 10, "glance at door, eases wheel")]),
        ("Boat", "#2f3f36", [(0.5, 7, "motorboat looms in the door"), (1, 6, "heel 6°"), (6, 8, "upright")]),
        ("Dialogue", LINE, [(3, 5.8, "Antony's order (2.8 s)")])]
for sec in range(11):
    x = tx + tw_ * sec / 10; d.line([x, ty, x, ty + 72 * len(rows) + 10], fill="#d8d4cc", width=2); d.text((x - 10, ty - 34), f"{sec}s", font=F(22), fill=GREY)
for i, (lab, col, segs) in enumerate(rows):
    yy = ty + 10 + i * 72; d.text((50, yy + 8), lab, font=F(26, True), fill=col)
    for j, (a2, b2, t2) in enumerate(segs):
        x0, x1 = tx + tw_ * a2 / 10, tx + tw_ * b2 / 10
        o = 26 if (lab == "Boat" and j > 0) else 0
        d.rounded_rectangle([x0 + 3, yy + o, x1 - 3, yy + 26 + o if lab == "Boat" else yy + 52], 8, fill=col); d.text((x0 + 10, yy + 2 + o if lab == "Boat" else yy + 12), t2, font=F(17 if lab == "Boat" else 19, True), fill="white")

# 4. platform
y3 = ty + 72 * len(rows) + 60
d.text((50, y3), "4  ON THE PLATFORM", font=F(32, True), fill=INK)
lines = ["No start image, no end image: assets only",
         "Attach: @antony20 (full) · remove everything else",
         "Duration 10 s · 21:9 · Malayalam · voice Mahendran J · [worried] · QA 100 / 100",
         "Watch for: only Antony in frame · eyes 15° LEFT · wheel only inside · motorboat only in the door · head steady on the line"]
for i, t in enumerate(lines): d.text((70, y3 + 55 + i * 42), "•  " + t, font=F(25), fill=INK)
im = im.crop((0, 0, W, y3 + 55 + len(lines) * 42 + 40))
im.save("scenes/showreel/storyboards/s17-sh04-clear.png"); print(im.size)
