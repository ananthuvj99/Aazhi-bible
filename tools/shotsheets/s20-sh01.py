"""Clear sheet for s20-sh01 (SB026 Clear of pursuit, 1): the nets break the chase. Silent, 15 s."""
from PIL import Image, ImageDraw, ImageFont

def F(sz, b=False):
    return ImageFont.truetype("C:/Windows/Fonts/" + ("segoeuib.ttf" if b else "segoeui.ttf"), sz)
W = 1800
INK, GREY, CAM, URU, MOT, VAL, NET, HAZE, JOIN = "#1d1d1f", "#6b6b6b", "#7a4fd0", "#3f5f7a", "#2f3f36", "#8a5a2b", "#e07b22", "#c9b8c0", "#d9432b"
im = Image.new("RGB", (W, 2300), "#f7f5f0"); d = ImageDraw.Draw(im)
def tag(xy, text, col, f=None):
    f = f or F(20, True); x, y = xy; tw = d.textlength(text, font=f)
    d.rounded_rectangle([x - 6, y - 4, x + tw + 8, y + 28], 8, fill=col); d.text((x + 1, y - 2), text, font=f, fill="white")

d.text((50, 30), "s20-sh01 v2 · SB026 Clear of pursuit, 1: the nets break the chase", font=F(46, True), fill=INK)
d.text((50, 92), "silent · 15 s · 21:9 · starts on Part B's last frame (@s17sh04last) · the camera HOLDS its place and rises; the boats run away into the frame (L172)", font=F(25), fill=GREY)

# 1 start frame + side view of the rise-over reveal
y0 = 150
d.text((50, y0), "1  START FRAME  and  THE RISE-OVER REVEAL", font=F(32, True), fill=INK)
pw = 830; ph = int(pw / 2.333)
a = Image.open("scenes/showreel/attach/s20-sh01/00-START-s17sh04last.png").convert("RGB").resize((pw, ph))
im.paste(a, (50, y0 + 50)); d.rectangle([50, y0 + 50, 50 + pw, y0 + 50 + ph], outline=INK, width=2)
tag((60, y0 + 60), "0 s: the vallams are hidden behind the uru", URU)
d.text((50, y0 + 60 + ph), "A 0 s = exactly @s17sh04last", font=F(21, True), fill=INK)
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
for (cx, cy, lab) in [(sx + 40, sea - 30, "0 s  3 m"), (sx + 40, sea - 150, "4 s  10 m"), (sx + 40, sea - 260, "12 s  25 m")]:
    d.ellipse([cx - 12, cy - 12, cx + 12, cy + 12], fill=CAM); d.text((cx + 18, cy - 14), lab, font=F(18, True), fill=CAM)
    d.line([cx, cy, sx + 700, sea - 6], fill="#b9a6e6", width=2)
d.text((sx + 12, sy + sh - 30), "side view: rises straight up, never forward; low = vallams hidden, high = seen beyond the roof", font=F(18, True), fill=INK)
d.text((sx + 330, sea + 10), "uru", font=F(18, True), fill=URU); d.text((sx + 600, sea + 10), "vallams + nets ~80 m ahead", font=F(18, True), fill=VAL)

# 2 top view
y1 = y0 + 120 + ph
d.text((50, y1), "2  FROM ABOVE: the turn round the end of the nets", font=F(32, True), fill=INK)
mx, my, mw, mh = 50, y1 + 50, 1700, 520
d.rectangle([mx, my, mx + mw, my + mh], fill="#dfe7ea", outline=INK, width=2)
# net line ahead (top), running from just ahead of the bow out to the right
for i in range(5):
    vx = mx + 760 + i * 170; vy = my + 90 + (i % 2) * 20
    d.polygon([(vx, vy), (vx + 50, vy - 8), (vx + 60, vy), (vx + 50, vy + 8)], fill=VAL)
    for k in range(10): d.ellipse([vx - 60 + k * 14, vy + 30 + abs(5 - k) * 3, vx - 54 + k * 14, vy + 36 + abs(5 - k) * 3], fill=NET)
tag((mx + 900, my + 20), "5 vallams, float lines (nets just under the surface)", VAL)
# uru path: up the middle then hooking right round the left end of the nets
pts = [(mx + 640, my + mh - 20), (mx + 640, my + 260), (mx + 650, my + 120), (mx + 700, my + 60), (mx + 820, my + 30)]
d.line(pts, fill="#ffffff", width=14); d.line(pts, fill=URU, width=4)
d.rectangle([mx + 620, my + 300, mx + 660, my + 400], fill=URU); d.text((mx + 670, my + 330), "uru", font=F(20, True), fill=URU)
# motorboats
d.polygon([(mx + 630, my + 470), (mx + 650, my + 440), (mx + 670, my + 470)], fill=MOT)
d.polygon([(mx + 560, my + 490), (mx + 580, my + 460), (mx + 600, my + 490)], fill=MOT)
d.polygon([(mx + 700, my + 490), (mx + 720, my + 460), (mx + 740, my + 490)], fill=MOT)
# lead boat cuts the corner into the net
d.line([(mx + 650, my + 440), (mx + 700, my + 250), (mx + 780, my + 140)], fill=JOIN, width=4)
d.ellipse([mx + 760, my + 115, mx + 810, my + 165], outline=JOIN, width=4); tag((mx + 820, my + 160), "7 s SNAG: lead boat cuts the corner, fouls, spins", JOIN)
d.line([(mx + 580, my + 460), (mx + 520, my + 260), (mx + 470, my + 200)], fill=MOT, width=3); tag((mx + 300, my + 230), "8.5 s second swerves, stops", MOT)
d.line([(mx + 720, my + 460), (mx + 1100, my + 300), (mx + 1650, my + 260)], fill=MOT, width=3); tag((mx + 1250, my + 320), "9.5 s third goes wide, slows", MOT)
d.rectangle([mx + 380, my + 180, mx + 1000, my + 230], fill=HAZE); d.text((mx + 400, my + 190), "11 s haze rolls in between", font=F(18, True), fill=INK)
# camera
d.ellipse([mx + 625, my + mh - 40, mx + 655, my + mh - 10], fill=CAM); tag((mx + 670, my + mh - 45), "camera: HOLDS here and rises to 25 m, tilting down; every boat stays in frame", CAM)

# 3 timeline
y2 = my + mh + 60
d.text((50, y2), "3  SECOND BY SECOND", font=F(32, True), fill=INK)
tx, tw_ = 260, 1480; ty = y2 + 80; S = 15
rows = [("Camera", CAM, [(0, 0.5, ""), (0.5, 5, "stops, rises: rise-over reveal"), (5, 12, "rising to 25 m, tilting down"), (12, 15, "high, holds")]),
        ("Uru", URU, [(0, 3, "running"), (3, 7, "turns right round the floats"), (7, 15, "pulls away, smaller")]),
        ("Motorboats", MOT, [(0, 7, "in the wake, in frame"), (7, 8.5, "SNAG"), (8.5, 9.5, "swerve"), (9.5, 15, "left behind, IN FRAME")]),
        ("Vallams", VAL, [(2, 5, "rise into view"), (5, 15, "fishermen wave")]),
        ("Haze", HAZE, [(11, 15, "rolls in between")])]
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
lines = ["s20-sh01 v2 · 15 s · 21:9 · START @s17sh04last · no end image · silent, no music",
         "Attach: @uru (full), @raghavan, @babu (small at the rail), @s17sh01last (reference) · remove everything else",
         "Watch for: the 3 motorboats never leave the frame · nets = floats on the water, no frames · snag at 7 s · no VFX look"]
for i, t in enumerate(lines): d.text((70, y3 + 55 + i * 42), "•  " + t, font=F(25), fill=INK)
im = im.crop((0, 0, W, y3 + 55 + len(lines) * 42 + 40))
im.save("scenes/showreel/storyboards/s20-sh01-clear.png"); print(im.size)
