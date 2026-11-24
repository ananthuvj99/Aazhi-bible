"""Clear sheet for s17-sh04 v4: Antony's order at the helm, from the front windows looking aft (SB025)."""
from PIL import Image, ImageDraw, ImageFont

def F(sz, b=False):
    return ImageFont.truetype("C:/Windows/Fonts/" + ("segoeuib.ttf" if b else "segoeui.ttf"), sz)

W = 1800
INK, GREY, CAM, ANT, WOOD, SEA, WIN = "#1d1d1f", "#6b6b6b", "#7a4fd0", "#1f7a45", "#7a5436", "#3f5f7a", "#b5452f"
im = Image.new("RGB", (W, 1700), "#f7f5f0"); d = ImageDraw.Draw(im)
def tag(xy, text, col, f=None):
    f = f or F(20, True); x, y = xy; tw = d.textlength(text, font=f)
    d.rounded_rectangle([x - 6, y - 4, x + tw + 8, y + 28], 8, fill=col); d.text((x + 1, y - 2), text, font=f, fill="white")

d.text((50, 30), "s17-sh04 v4 · Antony's order at the helm: \"ropes up\"", font=F(46, True), fill=INK)
d.text((50, 92), "8 s · from the FRONT windows looking aft · after s17-sh03 (the hard turn) · emotion: worried · v3 failed: he faced away from the bow", font=F(25), fill=GREY)

y0 = 150
d.text((50, y0), "1  START FRAME  and  WHERE EVERYONE IS", font=F(32, True), fill=INK)
pw = 830; ph = int(pw / 2.333)
a = Image.open("scenes/showreel/approved/sb025-chase/s17-sh04-start.png").convert("RGB").resize((pw, ph))
im.paste(a, (50, y0 + 50)); d.rectangle([50, y0 + 50, 50 + pw, y0 + 50 + ph], outline=INK, width=2)
tag((60, y0 + 60), "0 s = @s17sh04start · back wall + open door behind him", ANT)
# top view of the wheelhouse: bow at the top
sx, sy, sw, sh = 920, y0 + 50, 830, ph
d.rectangle([sx, sy, sx + sw, sy + sh], fill="#dfe7ea", outline=INK, width=2)
rx0, ry0, rx1, ry1 = sx + 250, sy + 40, sx + 580, sy + sh - 30
d.rectangle([rx0, ry0, rx1, ry1], fill="#e9dcc8", outline=WOOD, width=6)
d.line([rx0 + 40, ry0, rx1 - 40, ry0], fill=WIN, width=8); d.text((rx0 + 70, ry0 - 30), "front windows → bow (behind camera)", font=F(16, True), fill=WIN)
d.line([rx1, ry0 + 150, rx1, ry0 + 220], fill="#f7f5f0", width=8); d.text((rx1 + 12, ry0 + 160), "open side door", font=F(16, True), fill=WOOD)
d.text((rx0 + 90, ry1 - 34), "back wall + lantern", font=F(16, True), fill=WOOD)
cx = (rx0 + rx1) // 2
d.ellipse([cx - 30, ry0 + 140, cx + 30, ry0 + 160], outline=WOOD, width=4); d.text((cx + 40, ry0 + 140), "wheel", font=F(16, True), fill=WOOD)
d.ellipse([cx - 14, ry0 + 180, cx + 14, ry0 + 208], fill=ANT); d.text((cx + 22, ry0 + 184), "Antony, aft of wheel, faces ↑", font=F(16, True), fill=ANT)
d.polygon([(cx - 12, ry0 + 30), (cx + 12, ry0 + 30), (cx, ry0 + 55)], fill=CAM); d.text((cx + 20, ry0 + 30), "camera, looking aft", font=F(16, True), fill=CAM)
tag((sx + 15, sy + 15), "bow UP", SEA)

y1 = y0 + 90 + ph
d.text((50, y1), "2  BEATS", font=F(32, True), fill=INK)
beats = [("0–2 s", "Hold: a quarter turn of the wheel hand over hand, feet braced, sharp breath, eyes on the bow past the camera."),
         ("2–4.8 s", "LOCKED MCU, about 20° off the lens to frame left: Antony calls forward to Aashaan:"),
         ("4.8–6.5 s", "Eyes flick to the open door (motorboats astern); nudges the wheel; slow 0.5 m push toward the door."),
         ("6.5–8 s", "Hold: eyes forward on the bow again, the door bright at the right.")]
yy = y1 + 50
for t, s in beats:
    d.text((60, yy), t, font=F(24, True), fill=CAM); d.text((230, yy), s, font=F(24), fill=INK); yy += 42
d.text((230, yy), "ANTONY: \"munnile kayarokke mukalilekku uyarthu, aashaane.\"", font=F(26, True), fill=ANT); yy += 50
d.text((230, yy), "Lift all the ropes up front, Aashaan.  ·  voice: Mahendran J · [worried]", font=F(22), fill=GREY)

y2 = yy + 70
d.text((50, y2), "3  SECOND BY SECOND", font=F(32, True), fill=INK)
tx, tw_ = 260, 1480; ty = y2 + 80; S = 8
rows = [("Camera", CAM, [(0, 4.8, "locked, 40mm, from the front windows"), (4.8, 6.5, "push to door"), (6.5, 8, "hold")]),
        ("Antony", ANT, [(0, 2, "wheel, brace"), (2, 4.8, "THE LINE"), (4.8, 6.5, "glance to door"), (6.5, 8, "eyes on bow")])]
for sec in range(0, 9):
    x = tx + tw_ * sec / S; d.line([x, ty, x, ty + 70 * len(rows) + 10], fill="#d8d4cc", width=2); d.text((x - 10, ty - 32), f"{sec}", font=F(18), fill=GREY)
for i, (lab, col, segs) in enumerate(rows):
    yy = ty + 10 + i * 70; d.text((50, yy + 8), lab, font=F(24, True), fill=col)
    for a2, b2, t in segs:
        x0, x1 = tx + tw_ * a2 / S, tx + tw_ * b2 / S
        d.rounded_rectangle([x0 + 2, yy, x1 - 2, yy + 50], 8, fill=col)
        f = F(16, True)
        if d.textlength(t, font=f) < x1 - x0 - 10:
            d.text((x0 + 8, yy + 14), t, font=f, fill="white")

y3 = ty + 70 * len(rows) + 60
d.text((50, y3), "4  ATTACH  (folder scenes/showreel/attach/s17-sh04)", font=F(32, True), fill=INK)
d.text((60, y3 + 50), "@s17sh04start (start) · @antony20 (full) · @urudeckc3platenight2 (room design) · 8 s · 21:9 · Malayalam", font=F(24), fill=INK)
d.text((60, y3 + 90), "Left out: @s17sh03last (forward angle, L171) · @urubowplate (bow behind camera) · reveal shots (s20 carries the escape)", font=F(22), fill=GREY)
d.text((60, y3 + 130), "Checks: Antony aft of the wheel facing the bow · no front windows behind him · nothing fades · no VFX look · QC 100 · image QA 92", font=F(22), fill=GREY)
im = im.crop((0, 0, W, y3 + 190))
im.save("scenes/showreel/storyboards/s17-sh04-clear.png")
print(im.size)
