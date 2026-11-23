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

d.text((50, 30), "s20-sh03 v3 · Part A of the 30 s getaway: the hard cut round the nets", font=F(46, True), fill=INK)
d.text((50, 92), "silent · 15 s · fast low TRACKING shot behind the vallams · SLOW MOTION 6–9 s at the hard cut · Part B from its last frame", font=F(25), fill=GREY)

# 1 start frame + side view of the rise-over reveal
y0 = 150
d.text((50, y0), "1  START FRAME  and  THE CAMERA", font=F(32, True), fill=INK)
pw = 830; ph = int(pw / 2.333)
a = Image.open("scenes/showreel/attach/s20-sh03/00-START-s20sh03start.png").convert("RGB").resize((pw, ph))
im.paste(a, (50, y0 + 50)); d.rectangle([50, y0 + 50, 50 + pw, y0 + 50 + ph], outline=INK, width=2)
tag((60, y0 + 60), "0 s: behind the five vallams; the uru head-on", URU)
d.text((50, y0 + 60 + ph), "0 s = @s20sh03start", font=F(21, True), fill=INK)
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
for (cx, cy, lab) in [(sx + 40, sea - 30, "0 s  1.5 m, tracking right"), (sx + 40, sea - 150, "6–9 s slow motion: the hard cut"), (sx + 40, sea - 260, "15 s motorboats reach the floats")]:
    d.ellipse([cx - 12, cy - 12, cx + 12, cy + 12], fill=CAM); d.text((cx + 18, cy - 14), lab, font=F(18, True), fill=CAM)
    d.line([cx, cy, sx + 700, sea - 6], fill="#b9a6e6", width=2)
d.text((sx + 12, sy + sh - 30), "side view: camera low, tracking fast to the right behind the line of vallams", font=F(18, True), fill=INK)
d.text((sx + 330, sea + 10), "uru", font=F(18, True), fill=URU); d.text((sx + 600, sea + 10), "vallams + nets close", font=F(18, True), fill=VAL)

# 2 top view
y1 = y0 + 120 + ph
d.text((50, y1), "2  FROM ABOVE: the uru cuts round the end of the line; the motorboats run at the floats", font=F(32, True), fill=INK)
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
for bx, ex, ey, lab, t_ in [(cx - 150, cx - 240, my + 160, "uru never touches a float", (cx - 640, my + 230)),
                            (cx + 150, cx + 200, my + 160, "6 s uru cuts HARD RIGHT round the open end (slow motion)", (cx + 300, my + 230)),
                            (cx, cx + 150, my + 185, "15 s motorboats reach the floats (Part B: stuck)", (cx + 300, my + 290))]:
    d.polygon([(bx - 20, my + 470), (bx, my + 440), (bx + 20, my + 470)], fill=MOT)
    d.line([(bx, my + 440), (ex, ey)], fill=JOIN, width=4); d.ellipse([ex - 22, ey - 22, ex + 22, ey + 22], outline=JOIN, width=4)
    tag(t_, lab, JOIN)
d.rectangle([mx + 380, my + 38, mx + 1300, my + 58], fill=HAZE)
d.text((mx + 1320, my + 30), "fishermen shout, grab their nets to save them", font=F(18, True), fill=INK)
d.ellipse([cx - 15, my + mh - 40, cx + 15, my + mh - 10], fill=CAM); tag((cx + 25, my + mh - 45), "camera: fast track right; holds at 9 s looking back at the floats", CAM)

# 3 timeline
y2 = my + mh + 60
d.text((50, y2), "3  SECOND BY SECOND", font=F(32, True), fill=INK)
tx, tw_ = 260, 1480; ty = y2 + 80; S = 15
rows = [("Camera", CAM, [(0, 6, "fast track right, low"), (6, 9, "SLOW MOTION"), (9, 15, "holds, looking back")]),
        ("Uru", URU, [(0, 6, "head-on at the line"), (6, 9, "HARD CUT right, heels 12°"), (9, 15, "clear, pulls away")]),
        ("Fishermen", VAL, [(0, 6, "turn to look, tense"), (6, 9, "duck in the bow wave"), (9, 15, "shout, grab their nets")]),
        ("Motorboats", MOT, [(0, 9, "close behind the uru"), (9, 15, "run straight at the floats")]),
        ("Crew", "#1f7a45", [(0, 6, "grip the rail"), (6, 9, "cling through the heel"), (9, 15, "look back")])]
xj = -1000
for sec in range(0, 16):
    x = tx + tw_ * sec / S; d.line([x, ty, x, ty + 70 * len(rows) + 10], fill="#d8d4cc", width=2); d.text((x - 10, ty - 32), f"{sec}", font=F(18), fill=GREY)
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
lines = ["Part A = s20-sh03 v3 · 15 s · 21:9 · START @s20sh03start · Raghavan + Babu at the top rail · silent",
         "Attach: @uru (full), @raghavan, @babu (small at the rail) · remove everything else",
         "Watch for: uru never touches a float · one slow-mo ramp only · motorboats stay behind · nothing fades · no VFX"]
for i, t in enumerate(lines): d.text((70, y3 + 55 + i * 42), "•  " + t, font=F(25), fill=INK)
im = im.crop((0, 0, W, y3 + 55 + len(lines) * 42 + 40))
im.save("scenes/showreel/storyboards/s20-sh03-clear.png"); print(im.size)
