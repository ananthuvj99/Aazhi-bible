"""Clear sheet for s17-sh01 v2 (SB025, the chase begins: trailing drone behind three motorboats).
v1 (straight-down top shot) is in git history and retired/s17-sh01-v1.md."""
from PIL import Image, ImageDraw, ImageFont
import math

def F(sz, b=False):
    return ImageFont.truetype("C:/Windows/Fonts/" + ("segoeuib.ttf" if b else "segoeui.ttf"), sz)
W = 1800
INK, GREY = "#1d1d1f", "#6b6b6b"
URU, MOT, CAM, MEN, RED = "#b5651d", "#2f6f4f", "#7a4fd0", "#2e9e5b", "#d9432b"
im = Image.new("RGB", (W, 3000), "#f7f5f0"); d = ImageDraw.Draw(im)
def arrow(p0, p1, col, w=7):
    d.line([p0, p1], fill=col, width=w); a = math.atan2(p1[1] - p0[1], p1[0] - p0[0])
    for s in (2.6, -2.6): d.line([p1, (p1[0] + 24 * math.cos(a + s), p1[1] + 24 * math.sin(a + s))], fill=col, width=w)
def tag(xy, text, col, f=None):
    f = f or F(24, True); x, y = xy; tw = d.textlength(text, font=f)
    d.rounded_rectangle([x - 6, y - 4, x + tw + 8, y + 34], 8, fill=col); d.text((x + 1, y - 2), text, font=f, fill="white")

d.text((50, 30), "s17-sh01 v2 · SB025 · The chase begins", font=F(52, True), fill=INK)
d.text((50, 100), "10 seconds · no dialogue · grey dawn, Sri Lankan waters · drone 14 m up behind the motorboats, 35mm · they close from 80 m to 40 m", font=F(27), fill=GREY)

# 1. start frame with tags and arrows
y0 = 165
d.text((50, y0), "1  WHAT YOU WILL SEE  (the start frame, and what moves)", font=F(32, True), fill=INK)
fr = Image.open("scenes/showreel/attach/s17-sh01/01-START-s17sh01start.png").convert("RGB")
fw = W - 100; fh = int(fr.height * fw / fr.width); fr = fr.resize((fw, fh)); ox, oy = 50, y0 + 50
im.paste(fr, (ox, oy)); s = fw / 2000 * (3168 / 3136)
P = lambda x, y: (ox + (x * 1.584 - 16) * fw / 3136, oy + y * 1.584 * fh / 1344)
tag(P(1100, 300), "OUR URU · 80 m ahead · COCHIN", URU)
tag(P(1080, 205), "2 men look back", MEN)
tag(P(330, 470), "motorboat · 2 men", MOT); tag(P(1180, 470), "motorboat · 2 men", MOT); tag(P(780, 760), "motorboat · 2 men", MOT)
for bx, by in [(570, 540), (1015, 560), (1490, 540)]:
    arrow(P(bx, by), P(bx + (1010 - bx) * 0.45, by - 140), RED)
tag(P(1500, 140), "dull red sun", "#9c3b2a")
cy = oy + fh + 16
d.text((50, cy), "Red arrows: the three boats push on along the uru's wake and close the gap to about 40 m. The camera follows them and creeps closer (20 m → 14 m).", font=F(25), fill=GREY)

# 2. map from above
y1 = cy + 70
d.text((50, y1), "2  MAP FROM ABOVE  (0 s faded, 10 s solid)", font=F(32, True), fill=INK)
mx, my, mw, mh = 60, y1 + 60, 1680, 420
d.rectangle([mx, my, mx + mw, my + mh], fill="#5f7f94")
x_lo, x_hi = -30, 135; sc = mw / (x_hi - x_lo)
M = lambda wx, wy: (mx + (wx - x_lo) * sc, my + mh / 2 + wy * sc)
def boat(x, y, L, B, col):
    d.polygon([M(x, y - B / 2), M(x + L * 0.75, y - B / 2), M(x + L, y), M(x + L * 0.75, y + B / 2), M(x, y + B / 2)], fill=col)
# 10 s positions (uru frame of reference: uru fixed)
URU0 = 108   # uru stern x
for t, alpha in [(0, True), (10, False)]:
    lead = URU0 - (80 if t == 0 else 40) - 8
    cols = "#9cb8a8" if alpha else MOT
    for dx, dy in [(0, 0), (-3, -8), (-3, 8)]:
        boat(lead + dx, dy, 8, 2.4, cols)
    camx = lead - (20 if t == 0 else 14) + 4
    c = M(camx, 0); col = "#c9b8ef" if alpha else CAM
    d.polygon([(c[0] + 26, c[1]), (c[0] - 14, c[1] - 18), (c[0] - 14, c[1] + 18)], fill=col)
    d.text((c[0] - 50, c[1] + 24), f"camera {t} s", font=F(20, True), fill="white")
    d.text(M(lead - 2, 12), f"motorboats {t} s", font=F(20, True), fill="white")
boat(URU0, 0, 25, 7, URU); d.text(M(URU0, 6), "uru (25 m, 13 km/h)", font=F(20, True), fill="white")
d.line([M(URU0, 0), M(-30, 0)], fill="#d8e4ea", width=3)
d.text(M(-25, -16), "the uru's wake: the motorboats ride along it", font=F(20, True), fill="#eef4f7")
arrow(M(URU0 - 80, -14), M(URU0 - 42, -14), RED, 5); d.text(M(URU0 - 80, -21), "gap 80 m → 40 m (4 m every second)", font=F(20, True), fill="white")
d.text((mx + mw - 200, my + 10), "sun →  (ahead, right)", font=F(20, True), fill="#ffd9c9")

# 3. timeline
y2 = my + mh + 60
d.text((50, y2), "3  SECOND BY SECOND", font=F(32, True), fill=INK)
tx, tw_ = 270, 1470; ty = y2 + 60
for sec in range(11):
    x = tx + tw_ * sec / 10; d.line([x, ty, x, ty + 300], fill="#d8d4cc", width=2); d.text((x - 10, ty - 34), f"{sec}s", font=F(22), fill=GREY)
rows = [("Camera", CAM, [(0, 2.5, "hold (start frame)"), (2.5, 8, "follows, creeps 20 m → 14 m"), (8, 10, "hold")]),
        ("Motorboats", MOT, [(0, 2.5, "racing on the wake"), (2.5, 8, "push harder, bows slam"), (8, 10, "40 m behind")]),
        ("Uru", URU, [(0, 10, "steady ahead, grows in frame: 80 m → 40 m")]),
        ("Uru men", MEN, [(0, 4.8, "look back"), (4.8, 6, "one looks down"), (6, 10, "look back")])]
for i, (lab, col, segs) in enumerate(rows):
    yy = ty + 10 + i * 72; d.text((50, yy + 8), lab, font=F(26, True), fill=col)
    for a, b, t in segs:
        x0, x1 = tx + tw_ * a / 10, tx + tw_ * b / 10
        d.rounded_rectangle([x0 + 3, yy, x1 - 3, yy + 52], 10, fill=col); d.text((x0 + 12, yy + 10), t, font=F(21, True), fill="white")

# 4. platform
y3 = ty + 340
d.text((50, y3), "4  ON THE PLATFORM", font=F(32, True), fill=INK)
lines = ["Start image slot: 01-START-s17sh01start.png (@s17sh01start)",
         "Attach: @s17sh01start · @uru (full)   ·  remove everything else",
         "Duration 10 s · 21:9 · no dialogue        QA score 100 / 100",
         "Watch for: boats stay BEHIND the uru on its wake · the gap closes · uru never ship-sized · only COCHIN as writing · no guns"]
for i, t in enumerate(lines): d.text((70, y3 + 55 + i * 42), "•  " + t, font=F(27), fill=INK)
im = im.crop((0, 0, W, y3 + 55 + len(lines) * 42 + 40))
im.save("scenes/showreel/storyboards/s17-sh01-clear.png"); print(im.size)
