"""Clear sheet for s20-sh05: the long view of the uru escaping (SB026)."""
from PIL import Image, ImageDraw, ImageFont

def F(sz, b=False):
    return ImageFont.truetype("C:/Windows/Fonts/" + ("segoeuib.ttf" if b else "segoeui.ttf"), sz)
def ML(sz):
    for f in ("C:/Windows/Fonts/Nirmala.ttc", "C:/Windows/Fonts/Nirmala.ttf", "C:/Windows/Fonts/kartika.ttf"):
        try:
            return ImageFont.truetype(f, sz)
        except OSError:
            pass
    return F(sz)

W = 1800
INK, GREY, CAM, URU, MOT, RAG, BAB, SUN = "#1d1d1f", "#6b6b6b", "#7a4fd0", "#3f5f7a", "#2f3f36", "#b5452f", "#c07a1a", "#e0a030"
im = Image.new("RGB", (W, 1900), "#f7f5f0"); d = ImageDraw.Draw(im)
def tag(xy, text, col, f=None):
    f = f or F(20, True); x, y = xy; tw = d.textlength(text, font=f)
    d.rounded_rectangle([x - 6, y - 4, x + tw + 8, y + 28], 8, fill=col); d.text((x + 1, y - 2), text, font=f, fill="white")

d.text((50, 30), "s20-sh05 v1 · the long view: the uru escapes", font=F(46, True), fill=INK)
d.text((50, 92), "15 s · silent · drone pull-back and rise ahead of the uru · after s20-sh04 v2 (motorboat flips) · before the SB026 dialogue", font=F(25), fill=GREY)
y0 = 150
d.text((50, y0), "1  START FRAME  and  WHERE EVERYONE IS", font=F(32, True), fill=INK)
pw = 830; ph = int(pw / 2.333)
a = Image.open("scenes/showreel/approved/sb026-clear/s20-sh05-start.png").convert("RGB").resize((pw, ph))
im.paste(a, (50, y0 + 50)); d.rectangle([50, y0 + 50, 50 + pw, y0 + 50 + ph], outline=INK, width=2)
tag((60, y0 + 60), "0 s = @s20sh05start · high view · wreck LEFT · no sun", URU)
sx, sy, sw, sh = 920, y0 + 50, 830, ph
d.rectangle([sx, sy, sx + sw, sy + sh], fill="#dfe7ea", outline=INK, width=2)
# uru heading up (bow up) toward the drone at top
ux, uy = sx + 470, sy + 200
d.polygon([(ux, uy - 70), (ux + 28, uy - 30), (ux + 28, uy + 50), (ux - 28, uy + 50), (ux - 28, uy - 30)], fill=URU)
d.rectangle([ux - 22, uy + 20, ux + 22, uy + 48], fill="#7a5436")
for i, c in enumerate((RAG, BAB, "#8a6a3a", "#1f7a45")):
    d.ellipse([ux - 20 + i * 11, uy + 24, ux - 12 + i * 11, uy + 32], fill=c)
d.text((ux + 36, uy + 20), "4 tiny on deck", font=F(15, True), fill=INK)
# wake to wreck lower-left (astern; uru starboard = frame left from ahead)
d.polygon([(ux - 20, uy + 50), (ux + 20, uy + 50), (sx + 230, sy + sh - 20), (sx + 120, sy + sh - 20)], fill="#ffffff")
for bx, by in ((sx + 60, sy + sh - 60), (sx + 110, sy + sh - 40), (sx + 160, sy + sh - 70), (sx + 210, sy + sh - 45), (sx + 250, sy + sh - 80)):
    d.ellipse([bx - 8, by - 4, bx + 8, by + 4], fill="#9a7a50")
for bx, by in ((sx + 130, sy + sh - 75), (sx + 185, sy + sh - 55), (sx + 230, sy + sh - 30)):
    d.rectangle([bx - 8, by - 4, bx + 8, by + 4], fill=MOT)
tag((sx + 15, sy + sh - 125), "wreck ~150 m astern, uru's starboard", MOT)
# drone
d.ellipse([ux - 10, sy + 20, ux + 10, sy + 40], fill=CAM); d.text((ux + 16, sy + 18), "drone 90 m ahead, 40 m → 70 m up, flying back", font=F(16, True), fill=CAM)
d.line([ux, sy + 42, ux, uy - 75], fill=CAM, width=2)
d.ellipse([sx + 250, sy + 15, sx + 290, sy + 55], fill=SUN); d.text((sx + 160, sy + 60), "sun behind drone", font=F(16, True), fill=SUN)
# 2 beats
y1 = y0 + 90 + ph
d.text((50, y1), "2  BEATS", font=F(32, True), fill=INK)
beats = [("0–2.5 s", "Hold the start frame as the drone starts back: uru head-on, bow wave, four men face forward."),
         ("2.5–5 s", "Babu turns and points back along the wake; the other three turn and look back with him."),
         ("5–9 s", "Babu whirls his towel overhead, Raghavan arms up, Antony leans back, Aashaan a slow salute."),
         ("9–12 s", "Raghavan claps Antony's back; Aashaan's hand on Antony's shoulder; drone still climbing."),
         ("12–15 s", "Hold the wide: the uru comes on free; the wreck small and solid far back on the LEFT.")]
yy = y1 + 50
for t, s in beats:
    d.text((60, yy), t, font=F(24, True), fill=CAM); d.text((230, yy), s, font=F(24), fill=INK); yy += 42
d.text((230, yy), "Silent: wind, engine, bow wave, faint far shouts. No music.", font=F(22), fill=GREY)
y2 = yy + 70
d.text((50, y2), "3  SECOND BY SECOND", font=F(32, True), fill=INK)
tx, tw_ = 260, 1480; ty = y2 + 80; S = 15
rows = [("Drone", CAM, [(0, 2.5, "hold"), (2.5, 12, "flies back + climbs 40 m → 70 m"), (12, 15, "wide hold")]),
        ("Crew (4)", RAG, [(0, 2.5, "face forward"), (2.5, 5, "turn, look back"), (5, 9, "towel, arms up, salute"), (9, 12, "clap, hand on shoulder"), (12, 15, "forward")]),
        ("Uru", URU, [(0, 15, "head-on, same size, a little right of centre, 13 km/h")]),
        ("Wreck", MOT, [(0, 15, "5 vallams + 3 motorboats (1 capsized) on the LEFT, small, solid")])]
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
d.text((50, y3), "4  ATTACH  (folder scenes/showreel/attach/s20-sh05)", font=F(32, True), fill=INK)
d.text((60, y3 + 50), "@s20sh05start (start) · @uru · @raghavan · @babu · @aashaan · @antony20 (all full) · 15 s · 21:9 · silent", font=F(24), fill=INK)
d.text((60, y3 + 90), "Left out: @s20sh04last / @s20sh04start, @s17sh04last, @s20sh02last (other angle, L61)", font=F(22), fill=GREY)
d.text((60, y3 + 130), "Checks: wreck on the LEFT (uru's starboard) · four on deck · no sun · nothing fades · no VFX look · QC 100 · image QA 90", font=F(22), fill=GREY)
im = im.crop((0, 0, W, y3 + 190))
im.save("scenes/showreel/storyboards/s20-sh05-clear.png")
print(im.size)
