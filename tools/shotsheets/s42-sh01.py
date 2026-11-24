"""Clear sheet for s42-sh01: SB049 opening, the complaint and the letter (silent)."""
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

d.text((50, 30), "s42-sh01 v1 · SB049 the complaint and the letter: opening", font=F(46, True), fill=INK)
d.text((50, 92), "10 s · silent · the SI's office at dusk (camera C3) · slow push between Balan and Jaison onto Ramachandran", font=F(25), fill=GREY)

y0 = 150
d.text((50, y0), "1  START FRAME  and  WHERE EVERYONE IS", font=F(32, True), fill=INK)
pw = 830; ph = int(pw / 2.333)
src = "approved/sb049-station/s42-sh01-start.png"
p = "scenes/showreel/" + src if os.path.exists("scenes/showreel/" + src) else "scenes/showreel/image-qa/candidates/s42-sh01-start.png"
a = Image.open(p).convert("RGB").resize((pw, ph))
im.paste(a, (50, y0 + 50)); d.rectangle([50, y0 + 50, 50 + pw, y0 + 50 + ph], outline=INK, width=2)
tag((60, y0 + 60), "0 s = @s42sh01start · dusk · Gandhiji above him", RAM)
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
d.text((sx + 430, sy + 285), "camera C3, pushes ~1 m in", font=F(15, True), fill=CAM)

y1 = y0 + 90 + ph
d.text((50, y1), "2  BEATS", font=F(32, True), fill=INK)
beats = [("0–2.5 s", "Hold: Balan leans in with the folded letter; Ramachandran upright, hands folded, eyes on Balan."),
         ("2.5–4.5 s", "Balan lays the letter down and slides it across with two fingers; Jaison glances at him. Push starts."),
         ("4.5–7 s", "Ramachandran picks it up, unfolds it once, reads it in the lamp light."),
         ("7–9 s", "His eyes rise over his glasses to Balan: doubt. Camera settles, 50mm, medium shot under Gandhiji."),
         ("9–10 s", "Hold, mouth closed. His first line follows in sh02.")]
yy = y1 + 50
for t, s in beats:
    d.text((60, yy), t, font=F(24, True), fill=CAM); d.text((230, yy), s, font=F(24), fill=INK); yy += 42
d.text((230, yy), "Silent: crickets, a far bus horn, cane creaks, paper rasp, a clock ticking. No music.", font=F(22), fill=GREY)

y2 = yy + 70
d.text((50, y2), "3  SECOND BY SECOND", font=F(32, True), fill=INK)
tx, tw_ = 260, 1480; ty = y2 + 80; S = 10
rows = [("Camera", CAM, [(0, 2.5, "hold, 35mm"), (2.5, 9, "slow push ~1 m, to 50mm"), (9, 10, "hold")]),
        ("Ramachandran", RAM, [(0, 4.5, "hands folded, on Balan"), (4.5, 7, "reads the letter"), (7, 10, "eyes to Balan")]),
        ("Balan", BAL, [(0, 2.5, "leans in"), (2.5, 4.5, "slides letter"), (4.5, 10, "sits back, watches")]),
        ("Jaison", JAI, [(0, 2.5, "still"), (2.5, 4.5, "glance at Balan"), (4.5, 10, "watches")])]
for sec in range(0, 11):
    x = tx + tw_ * sec / S; d.line([x, ty, x, ty + 70 * len(rows) + 10], fill="#d8d4cc", width=2); d.text((x - 10, ty - 32), f"{sec}", font=F(18), fill=GREY)
for i, (lab, col, segs) in enumerate(rows):
    yy = ty + 10 + i * 70; d.text((50, yy + 8), lab, font=F(22, True), fill=col)
    for a2, b2, t in segs:
        x0, x1 = tx + tw_ * a2 / S, tx + tw_ * b2 / S
        d.rounded_rectangle([x0 + 2, yy, x1 - 2, yy + 50], 8, fill=col)
        f = F(16, True)
        if d.textlength(t, font=f) < x1 - x0 - 10:
            d.text((x0 + 8, yy + 14), t, font=f, fill="white")

y3 = ty + 70 * len(rows) + 60
d.text((50, y3), "4  ATTACH  (folder scenes/showreel/attach/s42-sh01)", font=F(32, True), fill=INK)
d.text((60, y3 + 50), "@s42sh01start (start) · @siramachandran · @balanbrown · @jaison20 (all full) · 10 s · 21:9 · silent", font=F(24), fill=INK)
d.text((60, y3 + 90), "Left out: @policestationc3platedusk (same angle as the start frame, L180) · @balan (blue look)", font=F(22), fill=GREY)
d.text((60, y3 + 130), "Checks: eyes off the lens · one letter moves, no readable words · nothing fades · no VFX look · QC 100 · image QA 90", font=F(22), fill=GREY)
im = im.crop((0, 0, W, y3 + 190))
os.makedirs("scenes/showreel/storyboards", exist_ok=True)
im.save("scenes/showreel/storyboards/s42-sh01-clear.png")
print(im.size)
