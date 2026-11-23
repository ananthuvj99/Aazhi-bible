"""Clear sheet for the SB026 30 s escape: Part A s20-sh01 v4 + Part B s20-sh02."""
from PIL import Image, ImageDraw, ImageFont

def F(sz, b=False):
    return ImageFont.truetype("C:/Windows/Fonts/" + ("segoeuib.ttf" if b else "segoeui.ttf"), sz)
W = 1800
INK, GREY, CAM, URU, MOT, VAL, NET, HAZE, JOIN = "#1d1d1f", "#6b6b6b", "#7a4fd0", "#3f5f7a", "#2f3f36", "#8a5a2b", "#e07b22", "#c9b8c0", "#d9432b"
im = Image.new("RGB", (W, 2300), "#f7f5f0"); d = ImageDraw.Draw(im)
def tag(xy, text, col, f=None):
    f = f or F(20, True); x, y = xy; tw = d.textlength(text, font=f)
    d.rounded_rectangle([x - 6, y - 4, x + tw + 8, y + 28], 8, fill=col); d.text((x + 1, y - 2), text, font=f, fill="white")

d.text((50, 30), "SB026 · the 30 s escape · Part A (s20-sh01 v4) + Part B (s20-sh02 v3)", font=F(46, True), fill=INK)
d.text((50, 92), "silent · 2 × 15 s joined on the instant the motorboats hit the nets · the camera HOLDS its place and rises 3 → 12 → 25 m (L172)", font=F(25), fill=GREY)

# 1 start frame + side view of the rise-over reveal
y0 = 150
d.text((50, y0), "1  START FRAME  and  THE RISE", font=F(32, True), fill=INK)
pw = 830; ph = int(pw / 2.333)
a = Image.open("scenes/showreel/attach/s20-sh01/00-START-s20sh01start.png").convert("RGB").resize((pw, ph))
im.paste(a, (50, y0 + 50)); d.rectangle([50, y0 + 50, 50 + pw, y0 + 50 + ph], outline=INK, width=2)
tag((60, y0 + 60), "0 s: five vallams already far on the horizon (L173)", URU)
d.text((50, y0 + 60 + ph), "0 s = @s20sh01start (Part B last frame + far vallams)", font=F(21, True), fill=INK)
# side view
sx, sy = 920, y0 + 50; sw, sh = 830, ph
d.rectangle([sx, sy, sx + sw, sy + sh], fill="#eef1f3", outline=INK, width=2)
sea = sy + sh - 70
d.line([sx, sea, sx + sw, sea], fill="#7f98a6", width=3)
d.polygon([(sx + 90, sea), (sx + 110, sea - 18), (sx + 170, sea - 18), (sx + 180, sea)], fill=MOT)           # motorboat
d.rectangle([sx + 330, sea - 120, sx + 460, sea], fill=URU); d.rectangle([sx + 340, sea - 175, sx + 450, sea - 120], fill="#7a5436")  # uru + deckhouse
d.line([sx + 395, sea - 175, sx + 395, sea - 235], fill="#7a5436", width=4)
for k in range(3): d.polygon([(sx + 620 + k * 60, sea), (sx + 630 + k * 60, sea - 12), (sx + 670 + k * 60, sea - 12), (sx + 675 + k * 60, sea)], fill=VAL)
for k in range(8): d.ellipse([sx + 600 + k * 22, sea - 4, sx + 608 + k * 22, sea + 4], fill=NET)
for (cx, cy, lab) in [(sx + 40, sea - 30, "A 0 s  3 m"), (sx + 40, sea - 150, "A 15 s = B 0 s  ~5 m"), (sx + 40, sea - 260, "B 13 s  22 m")]:
    d.ellipse([cx - 12, cy - 12, cx + 12, cy + 12], fill=CAM); d.text((cx + 18, cy - 14), lab, font=F(18, True), fill=CAM)
    d.line([cx, cy, sx + 700, sea - 6], fill="#b9a6e6", width=2)
d.text((sx + 12, sy + sh - 30), "side view: rises straight up, never forward; the vallams are always visible far ahead", font=F(18, True), fill=INK)
d.text((sx + 330, sea + 10), "uru", font=F(18, True), fill=URU); d.text((sx + 600, sea + 10), "vallams + nets ~60 m ahead", font=F(18, True), fill=VAL)

# 2 top view
y1 = y0 + 120 + ph
d.text((50, y1), "2  FROM ABOVE: through the gap; all three motorboats finished", font=F(32, True), fill=INK)
mx, my, mw, mh = 50, y1 + 50, 1700, 520
d.rectangle([mx, my, mx + mw, my + mh], fill="#dfe7ea", outline=INK, width=2)
cx = mx + 850
# vallams: two left, three right, nets reaching toward the gap
for vx, vy in [(cx - 520, my + 80), (cx - 300, my + 100), (cx + 220, my + 100), (cx + 420, my + 80), (cx + 620, my + 90)]:
    d.polygon([(vx, vy), (vx + 50, vy - 8), (vx + 60, vy), (vx + 50, vy + 8)], fill=VAL)
for k in range(14): d.ellipse([cx - 330 + k * 20, my + 150 + abs(7 - k) * 2, cx - 324 + k * 20, my + 156 + abs(7 - k) * 2], fill=NET)
for k in range(14): d.ellipse([cx + 60 + k * 20, my + 150 + abs(7 - k) * 2, cx + 66 + k * 20, my + 156 + abs(7 - k) * 2], fill=NET)
tag((cx - 560, my + 20), "2 vallams + net", VAL); tag((cx + 260, my + 20), "3 vallams + net", VAL)
tag((cx - 75, my + 185), "the gap", URU)
# uru path straight through the gap
d.line([(cx, my + mh - 30), (cx, my + 30)], fill="#ffffff", width=14); d.line([(cx, my + mh - 30), (cx, my + 30)], fill=URU, width=4)
d.rectangle([cx - 20, my + 260, cx + 20, my + 360], fill=URU); d.text((cx + 28, my + 290), "uru", font=F(20, True), fill=URU)
# three motorboats abreast and where they end
for bx, ex, ey, lab, t_ in [(cx - 150, cx - 240, my + 160, "B 3 s LEFT fouls, swamps", (cx - 640, my + 230)),
                            (cx + 150, cx + 200, my + 160, "B 1.5 s RIGHT fouls, man overboard", (cx + 300, my + 230)),
                            (cx, cx + 150, my + 185, "B 4.5 s MIDDLE rams the stalled boat", (cx + 300, my + 290))]:
    d.polygon([(bx - 20, my + 470), (bx, my + 440), (bx + 20, my + 470)], fill=MOT)
    d.line([(bx, my + 440), (ex, ey)], fill=JOIN, width=4); d.ellipse([ex - 22, ey - 22, ex + 22, ey + 22], outline=JOIN, width=4)
    tag(t_, lab, JOIN)
d.rectangle([mx + 380, my + 38, mx + 1300, my + 58], fill=HAZE)
d.text((mx + 1320, my + 30), "no haze over the uru; nothing fades", font=F(18, True), fill=INK)
d.ellipse([cx - 15, my + mh - 40, cx + 15, my + mh - 10], fill=CAM); tag((cx + 25, my + mh - 45), "camera: HOLDS here and rises to 25 m; every boat stays in frame", CAM)

# 3 timeline
y2 = my + mh + 60
d.text((50, y2), "3  SECOND BY SECOND", font=F(32, True), fill=INK)
tx, tw_ = 260, 1480; ty = y2 + 80; S = 30
rows = [("Camera", CAM, [(0, 15, "Part A (kept): holds, rises a little"), (15, 28, "Part B: rises 5 → 22 m"), (28, 30, "holds")]),
        ("Uru", URU, [(0, 15, "runs at the vallams (A, kept)"), (15, 30, "pulls away, solid and clear")]),
        ("Motorboats", MOT, [(0, 16.5, "three abreast in the wake"), (16.5, 18, "R fouls"), (18, 19.5, "L swamps"), (19.5, 21, "M rams"), (21, 30, "all dead, IN FRAME")]),
        ("Vallams", VAL, [(0, 8, "far, nearing"), (8, 30, "fishermen shout, wave, shake fists")]),
        ("Haze", HAZE, [(15, 30, "far horizon only")]),
        ("Crew", "#1f7a45", [(0, 15, "at the rail (A)"), (15, 19, "stern corner, breath held"), (19, 24, "fist, laugh, clap"), (24, 30, "towels, turn to each other")])]
xj = tx + tw_ * 15 / S
for sec in range(0, 31, 2):
    x = tx + tw_ * sec / S; d.line([x, ty, x, ty + 70 * len(rows) + 10], fill="#d8d4cc", width=2); d.text((x - 10, ty - 32), f"{sec}", font=F(18), fill=GREY)
d.line([xj, ty - 10, xj, ty + 70 * len(rows) + 20], fill=JOIN, width=4); tag((xj - 120, ty + 70 * len(rows) + 22), "JOIN: A last = B first", JOIN)
for i, (lab, col, segs) in enumerate(rows):
    yy = ty + 10 + i * 70; d.text((50, yy + 8), lab, font=F(24, True), fill=col)
    for a2, b2, t in segs:
        x0, x1 = tx + tw_ * a2 / S, tx + tw_ * b2 / S
        d.rounded_rectangle([x0 + 2, yy, x1 - 2, yy + 50], 8, fill=col)
        f = F(16, True)
        if d.textlength(t, font=f) < x1 - x0 - 12: d.text((x0 + 8, yy + 14), t, font=f, fill="white" if col != HAZE else INK)

# 4 platform
y3 = ty + 70 * len(rows) + 50
d.text((50, y3), "4  ON THE PLATFORM", font=F(32, True), fill=INK)
lines = ["Part A = s20-sh01 v4 · KEPT (partial): the chase reached the vallam line · last frame = @s20sh01last",
         "Part B = s20-sh02 v3 · 15 s · START @s20sh02start (nets close) · @uru, @raghavan, @babu · snags 1.5 / 3 / 4.5 s",
         "Watch for: vallams stay put · motorboats always in frame · all 3 finished in B · nets = floats only · crew moving · no VFX"]
for i, t in enumerate(lines): d.text((70, y3 + 55 + i * 42), "•  " + t, font=F(25), fill=INK)
im = im.crop((0, 0, W, y3 + 55 + len(lines) * 42 + 40))
im.save("scenes/showreel/storyboards/s20-run-30s-clear.png"); print(im.size)
