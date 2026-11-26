"""Clear sheet for s44g-sh01: SB061, the corridor goodbye, one 30 s take."""
from PIL import Image, ImageDraw, ImageFont

def F(sz, b=False):
    return ImageFont.truetype("C:/Windows/Fonts/" + ("segoeuib.ttf" if b else "segoeui.ttf"), sz)

INK, GREY, CAM, CLA, ANT, CON = "#1d1d1f", "#6b6b6b", "#7a4fd0", "#b07a2a", "#b03a2e", "#5a6a3a"
W = 1800
im = Image.new("RGB", (W, 1500), "#f7f5f0"); d = ImageDraw.Draw(im)
d.text((50, 30), "s44g-sh01 v1 · SB061 \"Just one minute\" · the corridor goodbye, one 30 s take", font=F(40, True), fill=INK)
d.text((50, 88), "30 s · Malayalam · Clara (Aadhira) LEFT looks RIGHT · Antony (Mahendran J) RIGHT looks LEFT · constable (pending) last · [sad] · 21:9", font=F(23), fill=GREY)
pw = 830; ph = int(pw / 2.333)
a = Image.open("scenes/showreel/approved/sb061-corridor/s44g-sh01-start.png").convert("RGB").resize((pw, ph))
im.paste(a, (50, 150)); d.rectangle([50, 150, 50 + pw, 150 + ph], outline=INK, width=2)
d.rounded_rectangle([54, 154, 380, 184], 7, fill=ANT); d.text((60, 156), "0 s = @s44gsh01start", font=F(19, True), fill="white")
b = Image.open("locations/court-1998/sb061-panel-reference.png").convert("RGB")
bw = 830; bh = int(bw * b.size[1] / b.size[0]); b = b.resize((bw, min(bh, ph))) if bh > ph else b.resize((bw, bh))
im.paste(b, (920, 150)); d.rectangle([920, 150, 920 + bw, 150 + b.size[1]], outline=INK, width=2)
d.rounded_rectangle([924, 154, 1250, 184], 7, fill=GREY); d.text((930, 156), "storyboard frame (staging only)", font=F(19, True), fill="white")
y = 150 + ph + 40
d.text((50, y), "LINES (one at a time, a pause between speakers, the listener's mouth closed)", font=F(28, True), fill=INK); y += 46
L = [("2.2 s", "CLARA", "vedhanayundo?", CLA), ("3.5 s", "ANTONY", "ammaye nokkikkone.", ANT), ("5.8 s", "CLARA", "njaan nokkikkollaam.", CLA),
     ("7.8 s", "ANTONY", "aashaanodu paranjo? aashaan paranjaal ivarkku manassilaavum.", ANT), ("12.6 s", "CLARA", "paranju. vakkeel addehathe kaanum.", CLA),
     ("16.0 s", "ANTONY", "njaan ayaale rakshichathaa, claare. veronnumilla njangal thammil.", ANT), ("20.6 s", "CLARA", "enikkariyaam.", CLA),
     ("24.0 s", "CONSTABLE", "samayam kazhinju. vaadaa.", CON)]
for t, w, s, c in L:
    d.text((60, y), t, font=F(21, True), fill=CAM); d.text((170, y), w, font=F(21, True), fill=c); d.text((340, y), s, font=F(21), fill=INK); y += 34
y += 20
tx, tw_, S = 260, 1480, 30; ty = y + 40
d.text((50, y), "SECOND BY SECOND", font=F(28, True), fill=INK)
rows = [("Camera", CAM, [(0, 24, "slow creep in, medium to tight two-shot"), (24, 30, "held; ends on Clara")]),
        ("Clara", CLA, [(0, 2, "takes his hand"), (2.2, 3, ""), (5.8, 7.2, ""), (12.6, 15.4, "C3"), (20.6, 21.6, ""), (27.5, 30, "hand in the air")]),
        ("Antony", ANT, [(3.5, 5.3, "A1"), (7.8, 12, "A2"), (16, 20, "A3"), (25.8, 30, "led away RIGHT")]),
        ("Constable", CON, [(24, 25.8, "line"), (25.8, 30, "pulls him")])]
for sec in range(0, S + 1, 2):
    x = tx + tw_ * sec / S; d.line([x, ty, x, ty + 64 * len(rows)], fill="#d8d4cc", width=2); d.text((x - 10, ty - 28), str(sec), font=F(16), fill=GREY)
for i, (lab, col, segs) in enumerate(rows):
    yy = ty + 8 + i * 64; d.text((50, yy + 8), lab, font=F(21, True), fill=col)
    for a2, b2, t in segs:
        x0, x1 = tx + tw_ * a2 / S, tx + tw_ * b2 / S
        d.rounded_rectangle([x0 + 2, yy, x1 - 2, yy + 46], 8, fill=col)
        if t and d.textlength(t, font=F(15, True)) < x1 - x0 - 10: d.text((x0 + 8, yy + 13), t, font=F(15, True), fill="white")
y = ty + 64 * len(rows) + 30
d.text((50, y), "ATTACH  @s44gsh01start (start) · @claracourt · @antonycustody · @constables · @courtcorridorc1plate (place) · 30 s · 21:9 · Malayalam", font=F(21), fill=INK)
d.text((50, y + 36), "Watch: a line on the wrong mouth, voices blended · fallback: six single-voice takes · QC 100", font=F(21), fill=GREY)
im = im.crop((0, 0, W, y + 80)); im.save("scenes/showreel/storyboards/s44g-sh01-clear.png"); print(im.size)
