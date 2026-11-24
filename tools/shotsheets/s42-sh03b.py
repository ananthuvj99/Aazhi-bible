"""Clear sheet for s42-sh03b: SB049, insert: the cap comes off the files."""
import os
from PIL import Image, ImageDraw, ImageFont

def F(sz, b=False):
    return ImageFont.truetype("C:/Windows/Fonts/" + ("segoeuib.ttf" if b else "segoeui.ttf"), sz)

W = 1800
INK, GREY, CAM, RAM, BAL, JAI, WOOD = "#1d1d1f", "#6b6b6b", "#7a4fd0", "#8a6a2a", "#8a4a2a", "#3a5f8a", "#5a3a22"
im = Image.new("RGB", (W, 1700), "#f7f5f0"); d = ImageDraw.Draw(im)
def tag(xy, text, col, f=None):
    f = f or F(20, True); x, y = xy; tw = d.textlength(text, font=f)
    d.rounded_rectangle([x - 6, y - 4, x + tw + 8, y + 28], 8, fill=col); d.text((x + 1, y - 2), text, font=f, fill="white")

d.text((50, 30), "s42-sh03b v1 · SB049 insert: the cap comes off the files", font=F(46, True), fill=INK)
d.text((50, 92), "4 s · silent · C3 side, close insert at desk height (85mm), locked · between sh03 and sh04", font=F(25), fill=GREY)

y0 = 150
d.text((50, y0), "1  START FRAME  and  WHERE EVERYONE IS", font=F(32, True), fill=INK)
pw = 830; ph = int(pw / 2.333)
src = "approved/sb049-station/s42-sh03b-start.png"
p = "scenes/showreel/" + src if os.path.exists("scenes/showreel/" + src) else "scenes/showreel/image-qa/candidates/s42-sh03b-start.png"
a = Image.open(p).convert("RGB").resize((pw, ph))
im.paste(a, (50, y0 + 50)); d.rectangle([50, y0 + 50, 50 + pw, y0 + 50 + ph], outline=INK, width=2)
tag((60, y0 + 60), "0 s = @s42sh03bstart · cap on the files", RAM)
sx, sy, sw, sh = 920, y0 + 50, 830, ph
d.rectangle([sx, sy, sx + sw, sy + sh], fill="#e3ece6", outline=INK, width=2)
# room: back wall at top
d.line([sx + 60, sy + 40, sx + 770, sy + 40], fill=WOOD, width=6); d.text((sx + 330, sy + 12), "Gandhiji's portrait", font=F(15, True), fill=INK)
d.line([sx + 60, sy + 40, sx + 60, sy + sh - 20], fill=WOOD, width=6); d.text((sx + 70, sy + 60), "window (dusk)", font=F(15, True), fill=CAM)
d.rectangle([sx + 250, sy + 110, sx + 580, sy + 170], fill="#6b4a2e"); d.text((sx + 360, sy + 128), "desk", font=F(16, True), fill="white")
d.ellipse([sx + 560, sy + 100, sx + 580, sy + 120], fill="#e0a030"); d.text((sx + 590, sy + 98), "lamp", font=F(15, True), fill=INK)
d.ellipse([sx + 400, sy + 65, sx + 430, sy + 95], fill=RAM); d.text((sx + 440, sy + 68), "Ramachandran", font=F(16, True), fill=RAM)
d.ellipse([sx + 290, sy + 200, sx + 320, sy + 230], fill=BAL); d.text((sx + 150, sy + 205), "Balan (brown)", font=F(16, True), fill=BAL)
d.ellipse([sx + 510, sy + 200, sx + 540, sy + 230], fill=JAI); d.text((sx + 550, sy + 205), "Jaison (blue)", font=F(16, True), fill=JAI)
d.polygon([(sx + 405, sy + 300), (sx + 425, sy + 300), (sx + 415, sy + 278)], fill=CAM)
d.line([sx + 415, sy + 278, sx + 415, sy + 240], fill=CAM, width=3)
d.text((sx + 430, sy + 285), "C3 side, close insert on the desk", font=F(15, True), fill=CAM)

y1 = y0 + 90 + ph
d.text((50, y1), "2  BEATS", font=F(32, True), fill=INK)
beats = [("0–1 s", "Hold: the cap on the tied file stack under the lit lamp, badge to the camera."),
         ("1–1.8 s", "His LEFT hand (watch on the wrist) comes in from the top and takes the cap by the visor."),
         ("1.8–3.3 s", "He lifts it off the files and sets it down on the desk in front of them, slowly; the hand leaves."),
         ("3.3–4 s", "Hold: the cap on the desk, badge to the camera, as it is in sh04.")]
yy = y1 + 50
for t, s in beats:
    d.text((60, yy), t, font=F(24, True), fill=CAM); d.text((230, yy), s, font=F(24), fill=INK); yy += 42
d.text((230, yy), "Silent: the soft tap of the cap on the wood, files rustle, a clock ticking. No music.", font=F(22), fill=GREY)

y2 = yy + 70
d.text((50, y2), "3  SECOND BY SECOND", font=F(32, True), fill=INK)
tx, tw_ = 260, 1480; ty = y2 + 80; S = 4
rows = [("Camera", CAM, [(0, 4, "locked close insert, 85mm")]),
        ("Hand / cap", RAM, [(0, 1, "cap on files"), (1, 1.8, "hand in"), (1.8, 3.3, "lift, set down"), (3.3, 4, "on desk")])]
for sec in range(0, 5):
    x = tx + tw_ * sec / S; d.line([x, ty, x, ty + 70 * len(rows) + 10], fill="#d8d4cc", width=2); d.text((x - 10, ty - 32), f"{sec}", font=F(18), fill=GREY)
for i, (lab, col, segs) in enumerate(rows):
    yy = ty + 10 + i * 70; d.text((50, yy + 8), lab, font=F(22, True), fill=col)
    for a2, b2, t in segs:
        x0, x1 = tx + tw_ * a2 / S, tx + tw_ * b2 / S
        d.rounded_rectangle([x0 + 2, yy, x1 - 2, yy + 50], 8, fill=col)
        f = F(16, True)
        if t and d.textlength(t, font=f) < x1 - x0 - 10:
            d.text((x0 + 8, yy + 14), t, font=f, fill="white")

y3 = ty + 70 * len(rows) + 60
d.text((50, y3), "4  ATTACH  (folder scenes/showreel/attach/s42-sh03b)", font=F(32, True), fill=INK)
d.text((60, y3 + 50), "@s42sh03bstart (start) · @siramachandran (hand, watch) · @s42sh01start (reference: room, props, light) · 4 s · 21:9 · silent", font=F(22), fill=INK)
d.text((60, y3 + 90), "Why: carries the cap from the files (sh01, sh02) to the desk (sh04)", font=F(22), fill=GREY)
d.text((60, y3 + 130), "Checks: one cap, one hand, slow beats (L179) · badge to camera · no readable text · QC 100 · image QA 90", font=F(22), fill=GREY)
im = im.crop((0, 0, W, y3 + 190))
im.save("scenes/showreel/storyboards/s42-sh03b-clear.png")
print(im.size)
