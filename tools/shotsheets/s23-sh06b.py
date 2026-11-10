from PIL import Image, ImageDraw, ImageFont
import math
def F(sz, b=False):
    return ImageFont.truetype("C:/Windows/Fonts/" + ("segoeuib.ttf" if b else "segoeui.ttf"), sz)
W, H = 1800, 2600
im = Image.new("RGB", (W, H), "#f7f5f0"); d = ImageDraw.Draw(im)
INK = "#1d1d1f"; GREY = "#6b6b6b"
SUR = "#e8892b"; BAL = "#2f7fd8"; CAM = "#7a4fd0"; MEN = "#2e9e5b"
def arrow(d, p0, p1, col, w=8):
    d.line([p0, p1], fill=col, width=w)
    a = math.atan2(p1[1]-p0[1], p1[0]-p0[0]); L = 26
    for s in (2.6, -2.6):
        d.line([p1, (p1[0]+L*math.cos(a+s), p1[1]+L*math.sin(a+s))], fill=col, width=w)
def tag(d, xy, text, col, f=F(24, True)):
    x, y = xy; tw = d.textlength(text, font=f)
    d.rounded_rectangle([x-6, y-4, x+tw+8, y+34], 8, fill=col); d.text((x+1, y-2), text, font=f, fill="white")

# Title
d.text((50, 30), "s23-sh06b · Suresh and Balan come up on deck", font=F(52, True), fill=INK)
d.text((50, 100), "8 seconds · no dialogue · straight after Antony's \"Bring the rope, fast!\" · same camera as the last two shots", font=F(28), fill=GREY)

# 1. The frame with arrows
y0 = 160
d.text((50, y0), "1  WHAT YOU WILL SEE  (starting frame, with who goes where)", font=F(32, True), fill=INK)
fr = Image.open("scenes/showreel/approved/s23-sh05-last.jpg").convert("RGB")
fw = W - 100; fh = int(fr.height * fw / fr.width); fr = fr.resize((fw, fh))
im.paste(fr, (50, y0 + 50)); s = fw / 1567; ox, oy = 50, y0 + 50
P = lambda x, y: (ox + x * s, oy + y * s)
for name, (x, y) in {"Sasi": (930, 250), "Babu": (1075, 225), "Raghavan": (1190, 215), "Antony": (1330, 240), "Aashaan (inside)": (370, 300)}.items():
    tag(d, P(x, y), name, MEN)
d.ellipse([P(840, 330)[0]-14, P(840, 330)[1]-14, P(840, 330)[0]+14, P(840, 330)[1]+14], outline="#ffd23f", width=6)
tag(d, P(700, 345), "doorway", "#b8860b")
arrow(d, P(845, 400), P(905, 560), SUR); tag(d, P(330, 590), "1  Suresh comes out, stops behind Sasi", SUR)
arrow(d, P(860, 380), P(1280, 470), BAL); tag(d, P(980, 590), "2  Balan crosses to Antony's side", BAL)
cy = oy + fh + 20
d.text((50, cy), "The camera starts close on the four men (end of sh06) and pulls back to this view, so the doorway comes into frame.", font=F(26), fill=GREY)

# 2. Top-down map
y1 = cy + 70
d.text((50, y1), "2  MAP FROM ABOVE  (who stands where, and the camera)", font=F(32, True), fill=INK)
mx, my, mw, mh = 120, y1 + 60, 1000, 520
d.rectangle([mx, my, mx+mw, my+mh], fill="#c9b99a", outline=INK, width=3)          # deck
d.rectangle([mx, my, mx+mw, my+40], fill="#6d7b8f"); d.text((mx+mw/2-120, my+5), "LEFT RAIL (sea side)", font=F(22, True), fill="white")
d.rectangle([mx+20, my+mh-200, mx+260, my+mh-20], fill="#7a5233"); d.text((mx+45, my+mh-130), "DECKHOUSE", font=F(26, True), fill="white")
d.text((mx+40, my+mh-95), "(Aashaan at the wheel)", font=F(20), fill="white")
d.rectangle([mx+250, my+mh-170, mx+270, my+mh-120], fill="#ffd23f"); d.text((mx+280, my+mh-175), "door", font=F(22, True), fill="#7a5a00")
d.text((mx+mw-120, my+mh/2-15), "BOW →", font=F(28, True), fill=INK)
pts = {"Sasi": (430, 80), "Babu": (560, 80), "Raghavan": (690, 80), "Antony": (820, 75)}
for n, (x, y) in pts.items():
    d.ellipse([mx+x-18, my+y-18, mx+x+18, my+y+18], fill=MEN); d.text((mx+x-30, my+y+22), n, font=F(22, True), fill=INK)
arrow(d, (mx+275, my+mh-150), (mx+410, my+150), SUR, 6); d.ellipse([mx+400, my+140, mx+436, my+176], fill=SUR); d.text((mx+330, my+185), "Suresh", font=F(22, True), fill=SUR)
arrow(d, (mx+275, my+mh-140), (mx+755, my+95), BAL, 6); d.ellipse([mx+737, my+77, mx+773, my+113], fill=BAL); d.text((mx+640, my+150), "Balan", font=F(22, True), fill=BAL)
cxp, cyp = mx+560, my+380
d.polygon([(cxp, cyp), (cxp-28, cyp+50), (cxp+28, cyp+50)], fill=CAM); d.text((cxp+40, cyp+5), "camera (pulls back)", font=F(22, True), fill=CAM)
arrow(d, (cxp, cyp+60), (cxp, cyp+120), CAM, 5)
d.text((mx+mw+30, my+20), "burning boat:", font=F(24, True), fill=INK)
d.text((mx+mw+30, my+55), "~500 m off, ahead-left", font=F(24), fill=INK)
d.text((mx+mw+30, my+90), "(out of this view)", font=F(24), fill=GREY)
arrow(d, (mx+mw+40, my+200), (mx+mw+220, my+140), "#e2462b", 6)

# 3. Timeline
y2 = my + mh + 60
d.text((50, y2), "3  SECOND BY SECOND", font=F(32, True), fill=INK)
tx, tw_ = 260, 1460; ty = y2 + 60
for sec in range(9):
    x = tx + tw_ * sec / 8; d.line([x, ty, x, ty + 300], fill="#d8d4cc", width=2); d.text((x-8, ty-34), f"{sec}s", font=F(22), fill=GREY)
rows = [("The four men", MEN, [(0, 8, "frightened at the rail, each moving his own way")]),
        ("Suresh", SUR, [(2, 4, "out of the door"), (5, 8, "walks over, stops behind Sasi")]),
        ("Balan", BAL, [(3, 6, "out after him, crosses to Antony"), (6, 8, "at Antony's side")]),
        ("Camera", CAM, [(0, 4, "pulls back ~1.5 m"), (4, 8, "holds")])]
for i, (lab, col, segs) in enumerate(rows):
    yy = ty + 10 + i * 72
    d.text((50, yy + 8), lab, font=F(26, True), fill=col)
    for a, b, t in segs:
        x0, x1 = tx + tw_ * a / 8, tx + tw_ * b / 8
        d.rounded_rectangle([x0 + 3, yy, x1 - 3, yy + 52], 10, fill=col)
        d.text((x0 + 14, yy + 10), t, font=F(22, True), fill="white")

# 4. Attach + settings
y3 = ty + 340
d.text((50, y3), "4  ON THE PLATFORM", font=F(32, True), fill=INK)
lines = ["Start image slot: the LAST FRAME of s23-sh06 (the take you keep)",
         "Attach: @urudeckc1platenight · @suresh · @balan · @antony20   (remove everything else)",
         "Duration 8 s · 16:9 · no dialogue        QA score 88 / 100",
         "Watch for: seven people at once — if anyone is copied or swapped, tell me and we re-attach his sheet"]
for i, t in enumerate(lines):
    d.text((70, y3 + 55 + i * 42), "•  " + t, font=F(27), fill=INK)
im = im.crop((0, 0, W, y3 + 55 + len(lines) * 42 + 40))
im.save("scenes/showreel/storyboards/s23-sh06b-clear.png"); print(im.size)
