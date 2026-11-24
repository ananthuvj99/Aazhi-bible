"""Clear sheet for s17-sh04 v4: "ropes up" from behind Antony, then out of the side door to Aashaan at the bow and the five vallams (SB025)."""
from PIL import Image, ImageDraw, ImageFont

def F(sz, b=False):
    return ImageFont.truetype("C:/Windows/Fonts/" + ("segoeuib.ttf" if b else "segoeui.ttf"), sz)

W = 1800
INK, GREY, CAM, ANT, AAS, WOOD, URU, VAL, SUN = "#1d1d1f", "#6b6b6b", "#7a4fd0", "#1f7a45", "#8a6a3a", "#7a5436", "#3f5f7a", "#9a7a50", "#e0a030"
im = Image.new("RGB", (W, 1800), "#f7f5f0"); d = ImageDraw.Draw(im)
def tag(xy, text, col, f=None):
    f = f or F(20, True); x, y = xy; tw = d.textlength(text, font=f)
    d.rounded_rectangle([x - 6, y - 4, x + tw + 8, y + 28], 8, fill=col); d.text((x + 1, y - 2), text, font=f, fill="white")

d.text((50, 30), "s17-sh04 v4.1 · \"ropes up\", then forward to Aashaan and the vallams", font=F(46, True), fill=INK)
d.text((50, 92), "15 s · from BEHIND Antony, out the side door to the bow · after s17-sh03 · emotion: worried · line spoken with his back to camera (Ranjith)", font=F(25), fill=GREY)

y0 = 150
d.text((50, y0), "1  START FRAME  and  WHERE EVERYONE IS", font=F(32, True), fill=INK)
pw = 830; ph = int(pw / 2.333)
a = Image.open("scenes/showreel/approved/sb025-chase/s17-sh04-start.png").convert("RGB").resize((pw, ph))
im.paste(a, (50, y0 + 50)); d.rectangle([50, y0 + 50, 50 + pw, y0 + 50 + ph], outline=INK, width=2)
tag((60, y0 + 60), "0 s = @s17sh04start · Antony faces the bow, back to camera", ANT)
# top view: bow to the RIGHT, starboard is DOWN
sx, sy, sw, sh = 920, y0 + 50, 830, ph
d.rectangle([sx, sy, sx + sw, sy + sh], fill="#dfe7ea", outline=INK, width=2)
my = sy + 150
d.polygon([(sx + 40, my - 45), (sx + 360, my - 45), (sx + 450, my), (sx + 360, my + 45), (sx + 40, my + 45)], fill=URU)
d.rectangle([sx + 60, my - 35, sx + 170, my + 35], fill=WOOD); d.text((sx + 66, my - 70), "wheelhouse", font=F(15, True), fill=WOOD)
d.ellipse([sx + 120, my - 8, sx + 136, my + 8], outline="white", width=3)
d.ellipse([sx + 100, my - 7, sx + 114, my + 7], fill=ANT); d.text((sx + 40, my + 95), "Antony → faces bow", font=F(15, True), fill=ANT)
d.ellipse([sx + 380, my - 7, sx + 394, my + 7], fill=AAS); d.text((sx + 340, my - 70), "Aashaan, ropes", font=F(15, True), fill=AAS)
path = [(sx + 80, my), (sx + 160, my + 30), (sx + 180, my + 60), (sx + 300, my + 60), (sx + 400, my + 20), (sx + 520, my)]
d.line(path, fill=CAM, width=4)
d.polygon([(sx + 520, my - 8), (sx + 520, my + 8), (sx + 536, my)], fill=CAM)
d.text((sx + 40, my + 120), "camera: out the side door, along the side deck, over the bow", font=F(15, True), fill=CAM)
for i in range(5):
    vx, vy = sx + 600 + i * 40, my + 10 + i * 26
    d.ellipse([vx - 12, vy - 5, vx + 12, vy + 5], fill=VAL)
    d.line([vx + 12, vy, vx + 30, vy + 20], fill="#e07a40", width=2)
d.text((sx + 560, my - 60), "5 vallams ~150 m,", font=F(15, True), fill=VAL); d.text((sx + 560, my - 42), "angled to starboard", font=F(15, True), fill=VAL)
d.ellipse([sx + 770, sy + 15, sx + 805, sy + 50], fill=SUN); d.text((sx + 540, sy + 15), "sun ahead-right, out of frame", font=F(15, True), fill=SUN)
tag((sx + 15, sy + 15), "bow →  (starboard is down)", URU)

y1 = y0 + 90 + ph
d.text((50, y1), "2  BEATS", font=F(32, True), fill=INK)
beats = [("0–1 s", "The START FRAME exactly (door open, lantern unlit), still: Antony braces, sharp breath; his back to us."),
         ("1–3.8 s", "STILL, same view: Antony calls forward to the bow (face not seen):"),
         ("3.8–4.8 s", "STILL: a quarter turn of the wheel, hand over hand."),
         ("4.8–7 s", "Camera turns right, past the compass, out of the open side door onto the side deck."),
         ("7–10 s", "Forward along the side deck: Aashaan at the bow hauling the ropes up; he glances back, lifts a hand."),
         ("10–13 s", "Up past his shoulder and over the bow: the five vallams with their nets rise into view ahead, angled right."),
         ("13–15 s", "Keep moving forward over the water toward the vallams.")]
yy = y1 + 50
for t, s in beats:
    d.text((60, yy), t, font=F(24, True), fill=CAM); d.text((230, yy), s, font=F(24), fill=INK); yy += 42
d.text((230, yy), "ANTONY: \"munnile kayarokke mukalilekku uyarthu, aashaane.\"", font=F(26, True), fill=ANT); yy += 50
d.text((230, yy), "Lift all the ropes up front, Aashaan.  ·  voice: Mahendran J · [worried]", font=F(22), fill=GREY)

y2 = yy + 70
d.text((50, y2), "3  SECOND BY SECOND", font=F(32, True), fill=INK)
tx, tw_ = 260, 1480; ty = y2 + 80; S = 15
rows = [("Camera", CAM, [(0, 4.8, "still, behind Antony"), (4.8, 7, "out the door"), (7, 10, "along side deck"), (10, 13, "over the bow"), (13, 15, "on to vallams")]),
        ("Antony", ANT, [(0, 1, "brace"), (1, 3.8, "THE LINE"), (3.8, 4.8, "wheel"), (4.8, 7, "at the wheel")]),
        ("Aashaan", AAS, [(7, 10, "hauls ropes, hand up"), (10, 15, "eyes ahead")]),
        ("Vallams", VAL, [(10, 15, "5 vallams, nets, angled right")])]
for sec in range(0, 16):
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
d.text((60, y3 + 50), "@s17sh04start (start) · @antony20 · @urubowplate · @aashaan · @uru · @s20sh03start (vallams)", font=F(22), fill=INK)
d.text((60, y3 + 90), "Left out: @urudeckc3platenight2 (played as opening shot, L180) · @s17sh03last (L171) · @raghavan, @babu (aft, not in frame) · s20 frames (other angles, L61) · 15 s · 21:9 · Malayalam", font=F(22), fill=GREY)
d.text((60, y3 + 130), "Checks: Antony faces the bow, back to camera · vallams on the uru's starboard (L178) · no sun · nothing fades · no VFX look · QC 96 (Ranjith's dialogue exception)", font=F(22), fill=GREY)
im = im.crop((0, 0, W, y3 + 190))
im.save("scenes/showreel/storyboards/s17-sh04-clear.png")
print(im.size)
