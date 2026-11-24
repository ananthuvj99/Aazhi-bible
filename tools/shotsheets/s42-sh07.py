"""Clear sheet for s42-sh07: SB051, Ramachandran's three questions (C3)."""
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

d.text((50, 30), "s42-sh07 v1 · SB051 Ramachandran: his questions change", font=F(46, True), fill=INK)
d.text((50, 92), "18 s · Malayalam · C3 visitors' side · Ramachandran close-up, locked · voice Rudra · [thoughtful]", font=F(25), fill=GREY)

y0 = 150
d.text((50, y0), "1  START FRAME  and  WHERE EVERYONE IS", font=F(32, True), fill=INK)
pw = 830; ph = int(pw / 2.333)
src = "approved/sb049-station/s42-sh07-start.png"
p = "scenes/showreel/" + src if os.path.exists("scenes/showreel/" + src) else "scenes/showreel/image-qa/candidates/s42-sh05-start2.png"
a = Image.open(p).convert("RGB").resize((pw, ph))
im.paste(a, (50, y0 + 50)); d.rectangle([50, y0 + 50, 50 + pw, y0 + 50 + ph], outline=INK, width=2)
tag((60, y0 + 60), "0 s = @s42sh07start · CU, looks LEFT at Balan", RAM)
sx, sy, sw, sh = 920, y0 + 50, 830, ph
d.rectangle([sx, sy, sx + sw, sy + sh], fill="#e3ece6", outline=INK, width=2)
# room: back wall at top
d.line([sx + 60, sy + 40, sx + 770, sy + 40], fill=WOOD, width=6); d.text((sx + 330, sy + 12), "Gandhiji's portrait", font=F(15, True), fill=INK)
d.line([sx + 60, sy + 40, sx + 60, sy + sh - 20], fill=WOOD, width=6); d.text((sx + 70, sy + 60), "window (dusk)", font=F(15, True), fill=CAM)
d.rectangle([sx + 250, sy + 110, sx + 580, sy + 170], fill="#6b4a2e"); d.text((sx + 360, sy + 128), "desk", font=F(16, True), fill="white")
d.ellipse([sx + 560, sy + 100, sx + 580, sy + 120], fill="#e0a030"); d.text((sx + 590, sy + 98), "lamp", font=F(15, True), fill=INK)
d.ellipse([sx + 400, sy + 65, sx + 430, sy + 95], fill=RAM); d.text((sx + 470, sy + 72), "Ramachandran", font=F(16, True), fill=RAM)
d.ellipse([sx + 290, sy + 200, sx + 320, sy + 230], fill=BAL); d.text((sx + 150, sy + 205), "Balan (brown)", font=F(16, True), fill=BAL)
d.ellipse([sx + 510, sy + 200, sx + 540, sy + 230], fill=JAI); d.text((sx + 550, sy + 205), "Jaison (blue)", font=F(16, True), fill=JAI)
d.polygon([(sx + 405, sy + 300), (sx + 425, sy + 300), (sx + 415, sy + 278)], fill=CAM)
d.line([sx + 415, sy + 278, sx + 415, sy + 240], fill=CAM, width=3)
d.text((sx + 430, sy + 285), "C3 (THIS SHOT): faces him, 85mm CU", font=F(15, True), fill=CAM)
d.polygon([(sx + 445, sy + 46), (sx + 465, sy + 46), (sx + 455, sy + 66)], fill="#c0392b"); d.text((sx + 600, sy + 44), "C4: Balan's answers (s42-sh08)", font=F(15, True), fill="#c0392b")

y1 = y0 + 90 + ph
d.text((50, y1), "2  BEATS", font=F(32, True), fill=INK)
beats = [("0–2 s", "Locked CU: he holds Balan's eyes, the folded letter at his chest."), ("2–5 s", "Q1, even and quiet."), ("5–7.5 s", "SILENT: listens (Balan's answer 1 cut in)."), ("7.5–8.6 s", "Q2, one word, harder."), ("8.6–10.5 s", "SILENT: listens (\"illa\" cut in); slow breath."), ("10.5–13 s", "Q3, quietest."), ("13–18 s", "SILENT: listens (Katchatheevu cut in); eyes to the letter and back at 15.5 s: the decision.")]
yy = y1 + 50
for t, s in beats:
    d.text((60, yy), t, font=F(24, True), fill=CAM); d.text((230, yy), s, font=F(24), fill=INK); yy += 42
d.text((230, yy), "RAM: \"ee kathu ningalallaathe vere aarenkilum vaayicho?\"  /  \"antony?\"  /  \"aa selvane evideyaa irakkiyathu?\"", font=F(24, True), fill=RAM); yy += 40
d.text((230, yy), "Has anyone besides you read this letter? / Antony? / Where did you put Selvan ashore?", font=F(20), fill=GREY); yy += 34
d.text((230, yy), "voice: Rudra · [thoughtful] · about 6.1 s of speech in 18 s · intercut with s42-sh08", font=F(20), fill=GREY)

y2 = yy + 70
d.text((50, y2), "3  SECOND BY SECOND", font=F(32, True), fill=INK)
tx, tw_ = 260, 1480; ty = y2 + 80; S = 18
rows = [("Camera", CAM, [(0, 18, "locked CU, 85mm, C3")]), ("Ramachandran", RAM, [(0, 2, "holds"), (2, 5, "Q1"), (5, 7.5, "listens"), (7.5, 8.6, "Q2"), (8.6, 10.5, "listens"), (10.5, 13, "Q3"), (13, 15.5, "listens"), (15.5, 18, "decides")]), ("Balan (edit)", BAL, [(5, 7.5, "A1"), (8.6, 10.5, "A2"), (13, 15.5, "A3")])]
for sec in range(0, 19):
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
d.text((50, y3), "4  ATTACH  (folder scenes/showreel/attach/s42-sh07)", font=F(32, True), fill=INK)
d.text((60, y3 + 50), "@s42sh07start (start) · @siramachandran · @s42sh01start (ref) · 18 s · 21:9 · Malayalam", font=F(22), fill=INK)
d.text((60, y3 + 90), "Left out: @balanbrown (off frame left) · @s42sh04start (wider frame of this angle, L180)", font=F(22), fill=GREY)
d.text((60, y3 + 130), "Checks: fresh 2k frame (L182) · portrait RIGHT of his head as in sh04 · gaps silent · locked · QC 100", font=F(22), fill=GREY)
im = im.crop((0, 0, W, y3 + 190))
im.save("scenes/showreel/storyboards/s42-sh07-clear.png")
print(im.size)
