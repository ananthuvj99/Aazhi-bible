"""Clear sheet for the SB025 30 s run: Part A (s17-sh03 v2) + Part B (s17-sh04 v2), joined on the spinning wheel.
Reuses the drawn frames of the s17-sh03 and s17-sh04 sheets and draws the reveal from above."""
from PIL import Image, ImageDraw, ImageFont
import math

def F(sz, b=False):
    return ImageFont.truetype("C:/Windows/Fonts/" + ("segoeuib.ttf" if b else "segoeui.ttf"), sz)
W = 1800
INK, GREY = "#1d1d1f", "#6b6b6b"
ANT, AAS, CAM, LINE, MOT, URU, CREW, JOIN = "#2e9e5b", "#b5651d", "#7a4fd0", "#c0392b", "#2f3f36", "#3f5f7a", "#1f7a45", "#d9432b"
im = Image.new("RGB", (W, 3400), "#f7f5f0"); d = ImageDraw.Draw(im)
def tag(xy, text, col, f=None):
    f = f or F(21, True); x, y = xy; tw = d.textlength(text, font=f)
    d.rounded_rectangle([x - 6, y - 4, x + tw + 8, y + 30], 8, fill=col); d.text((x + 1, y - 2), text, font=f, fill="white")

d.text((50, 30), "SB025 · the 30 s run · Part A + Part B", font=F(50, True), fill=INK)
d.text((50, 98), "two 15 s generations joined on the spinning wheel · one speaker each (L58) · each starts on the previous end frame · [worried]", font=F(25), fill=GREY)

# 1. three key frames
y0 = 155
d.text((50, y0), "1  WHAT YOU WILL SEE  (drawn frames)", font=F(32, True), fill=INK)
pw = (W - 140) // 3; ph = int(pw / 2.333)
a = Image.open("scenes/showreel/approved/sb025-chase/s17-sh02-end.png").convert("RGB").resize((pw, ph))
b = Image.open("scenes/showreel/storyboards/s17-sh04-clear.png").crop((50, 210, 1750, 210 + 728)).resize((pw, ph))
# reveal from above (drawn)
r = Image.new("RGB", (pw, ph), "#8fa6b2"); rd = ImageDraw.Draw(r)
for k in range(6): rd.arc([-200, 30 + k * 40, pw + 200, 160 + k * 40], 200, 340, fill="#a9bcc5", width=2)
rd.polygon([(pw * .2, ph), (pw * .32, ph * .62), (pw * .48, ph * .62), (pw * .6, ph)], fill="#3f5f7a")      # uru stern from above
rd.rectangle([pw * .25, ph * .66, pw * .55, ph * .82], fill="#7a5436")
rd.line([(pw * .4, ph * .62), (pw * .5, ph * .2), (pw * .6, 0)], fill="#f1f4f5", width=10)               # wake
for k in range(9): rd.ellipse([pw * .62 + k * 9, ph * .42 - k * 6, pw * .62 + k * 9 + 6, ph * .42 - k * 6 + 6], fill="#f6efe4")  # float line
rd.polygon([(pw * .78, ph * .25), (pw * .86, ph * .23), (pw * .88, ph * .25), (pw * .86, ph * .27)], fill="#6b4a2b")
rd.polygon([(pw * .55, ph * .3), (pw * .6, ph * .28), (pw * .62, ph * .3), (pw * .6, ph * .32)], fill=MOT); rd.ellipse([pw * .54, ph * .25, pw * .64, ph * .36], outline=JOIN, width=3)
rd.polygon([(pw * .35, ph * .15), (pw * .4, ph * .13), (pw * .42, ph * .15), (pw * .4, ph * .17)], fill=MOT)
rd.polygon([(pw * .8, ph * .1), (pw * .85, ph * .08), (pw * .87, ph * .1), (pw * .85, ph * .12)], fill=MOT)
rd.rectangle([0, 0, pw, ph * .12], fill="#e9dde0")
rd.ellipse([pw * .2, ph * .7, pw * .24, ph * .76], fill="#f3f3f0"); rd.ellipse([pw * .5, ph * .7, pw * .54, ph * .76], fill="#efe6d6")
y = y0 + 50
for i, (img, lab) in enumerate([(a, "A 0 s: START = end of s17-sh02 → swing round to Aashaan"), (b, "A 13 s → B 7 s: Antony at the wheel, the order"), (r, "B 9–15 s: from above, the nets catch the motorboat")]):
    x = 50 + i * (pw + 20); im.paste(img, (x, y)); d.rectangle([x, y, x + pw, y + ph], outline=INK, width=2)
    d.text((x, y + ph + 8), lab, font=F(21, True), fill=INK)
x3 = 50 + 2 * (pw + 20)
tag((x3 + 8, y + 8), "lead boat fouls, spins", JOIN); tag((x3 + 8, y + ph - 40), "Raghavan + Babu at the rail", CREW)

# 2. the camera path
y1 = y + ph + 60
d.text((50, y1), "2  THE CAMERA PATH  (one move per part; the join is on the spinning wheel)", font=F(32, True), fill=INK)
steps = [("A 0–6.4 s", "start frame → arc 120° to Aashaan, his line", AAS), ("A 6–9.5 s", "tilt down: the handover", AAS), ("A 9.5–15 s", "arc 90° round the wheel → Antony mid-spin", ANT),
         ("B 0–5.3 s", "at the front windows: the order", ANT), ("B 5.3–9 s", "out of the side door, rise ~8 m", CAM), ("B 9–15 s", "over the stern: the snag, the haze", MOT)]
bx = 50; by = y1 + 60; bw = (W - 100 - 5 * 16) // 6
for i, (t1, t2, col) in enumerate(steps):
    x = bx + i * (bw + 16)
    d.rounded_rectangle([x, by, x + bw, by + 110], 12, fill=col)
    d.text((x + 12, by + 10), t1, font=F(22, True), fill="white")
    words = t2.split(); line = ""; yy = by + 44
    for w in words:
        if d.textlength(line + " " + w, font=F(18, True)) > bw - 24: d.text((x + 12, yy), line.strip(), font=F(18, True), fill="white"); yy += 24; line = w
        else: line += " " + w
    d.text((x + 12, yy), line.strip(), font=F(18, True), fill="white")
jx = bx + 3 * (bw + 16) - 8
d.line([jx, by - 14, jx, by + 124], fill=JOIN, width=5); tag((jx - 70, by + 130), "JOIN: A's last frame = B's first", JOIN)

# 3. timeline 0–30 s
y2 = by + 200
d.text((50, y2), "3  SECOND BY SECOND  (0–15 s = Part A, 15–30 s = Part B)", font=F(32, True), fill=INK)
tx, tw_ = 270, 1470; ty = y2 + 90; S = 30
rows = [("Camera", CAM, [(0, 5.8, "locked MCU"), (5.8, 9.5, "tilt down"), (9.5, 13, "arc 90°"), (13, 15, "hold"), (15, 20.3, "locked, rolls with heel"), (20.3, 24, "out + up"), (24, 30, "high over the stern")]),
        ("Aashaan", AAS, [(0.6, 1.6, "glance"), (3.6, 6.4, "LINE"), (5.8, 9.5, "lets go, exits")]),
        ("Antony", ANT, [(7, 9.5, "hands"), (9.5, 11.5, "steps in"), (11.5, 17, "spins hard"), (17.5, 20.3, "LINE"), (20.3, 21, "glance")]),
        ("Outside", MOT, [(14, 20.3, "motorboat in the door"), (24, 26, "SNAG"), (26, 27.5, "swerve"), (27.5, 30, "haze")]),
        ("Dialogue", LINE, [(3.6, 6.4, "Aashaan (2.8 s)"), (17.5, 20.3, "Antony (2.8 s)")])]
for sec in range(0, 31, 2):
    x = tx + tw_ * sec / S; d.line([x, ty, x, ty + 72 * len(rows) + 10], fill="#d8d4cc", width=2); d.text((x - 12, ty - 34), f"{sec}s", font=F(20), fill=GREY)
xj = tx + tw_ * 15 / S; d.line([xj, ty - 10, xj, ty + 72 * len(rows) + 20], fill=JOIN, width=4)
for i, (lab, col, segs) in enumerate(rows):
    yy = ty + 10 + i * 72; d.text((50, yy + 8), lab, font=F(26, True), fill=col)
    for a2, b2, t in segs:
        x0, x1 = tx + tw_ * a2 / S, tx + tw_ * b2 / S
        d.rounded_rectangle([x0 + 2, yy, x1 - 2, yy + 52], 8, fill=col)
        f = F(16, True)
        if d.textlength(t, font=f) < x1 - x0 - 12: d.text((x0 + 8, yy + 14), t, font=f, fill="white")

# 4. platform
y3 = ty + 72 * len(rows) + 60
d.text((50, y3), "4  ON THE PLATFORM", font=F(32, True), fill=INK)
lines = ["Part A = s17-sh03 v3 · 15 s · START @s17sh02end · @aashaan, @antony20, @urudeckc3platedawn (room) · Rinoy · QA 100",
         "Part B = s17-sh04 v2 · 15 s · @antony20, @uru, @raghavan, @babu, @urudeckc3platedawn (room), @s17sh01last (ref) · Mahendran J",
         "Generate A from the start frame; send me its last frame → it becomes B's start image (@s17sh03last). Cut on the wheel.",
         "Watch for: A ends with Antony behind the wheel mid-spin · B: exactly 3 motorboats, the lead one caught in the net · nothing fades in"]
for i, t in enumerate(lines): d.text((70, y3 + 55 + i * 42), "•  " + t, font=F(25), fill=INK)
im = im.crop((0, 0, W, y3 + 55 + len(lines) * 42 + 40))
im.save("scenes/showreel/storyboards/s17-run-30s-clear.png"); print(im.size)
