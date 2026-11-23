"""Clear sheet for s17-sh01b: Raghavan's LTTE alarm from the uru's top deck (SB025)."""
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

d.text((50, 30), "s17-sh01b v1 · Raghavan's alarm: \"they look like the Tigers, LTTE\"", font=F(46, True), fill=INK)
d.text((50, 92), "15 s · handheld on the top deck · between s17-sh01 (chase begins) and s17-sh02 (Antony to the wheel) · emotion: worried", font=F(25), fill=GREY)

# 1 start frame + top view
y0 = 150
d.text((50, y0), "1  START FRAME  and  WHERE EVERYONE IS", font=F(32, True), fill=INK)
pw = 830; ph = int(pw / 2.333)
a = Image.open("scenes/showreel/approved/sb025-chase/s17-sh01b-start.png").convert("RGB").resize((pw, ph))
im.paste(a, (50, y0 + 50)); d.rectangle([50, y0 + 50, 50 + pw, y0 + 50 + ph], outline=INK, width=2)
tag((60, y0 + 60), "0 s = @s17sh01bstart · boats ~90 m, head-on · no sun", URU)
# top view
sx, sy, sw, sh = 920, y0 + 50, 830, ph
d.rectangle([sx, sy, sx + sw, sy + sh], fill="#dfe7ea", outline=INK, width=2)
# uru (bow at bottom, stern at top), top deck
ux = sx + 415
d.polygon([(ux - 60, sy + 120), (ux + 60, sy + 120), (ux + 60, sy + sh - 60), (ux, sy + sh - 10), (ux - 60, sy + sh - 60)], fill=URU)
d.rectangle([ux - 45, sy + 125, ux + 45, sy + 215], fill="#7a5436")
d.text((ux + 66, sy + 140), "top deck", font=F(17, True), fill=INK)
d.text((ux + 66, sy + sh - 70), "bow", font=F(17, True), fill=URU)
# wake + motorboats astern (top)
d.polygon([(ux - 40, sy + 120), (ux + 40, sy + 120), (ux + 160, sy + 5), (ux - 160, sy + 5)], fill="#ffffff")
for bx in (ux - 110, ux, ux + 110):
    d.polygon([(bx - 10, sy + 20), (bx + 10, sy + 20), (bx, sy + 40)], fill=MOT)
tag((sx + 15, sy + 15), "3 motorboats ~90 m → 60 m", MOT)
# men at stern rail
d.ellipse([ux - 30, sy + 128, ux - 14, sy + 144], fill=RAG); d.text((ux - 150, sy + 120), "Raghavan", font=F(16, True), fill=RAG)
d.ellipse([ux + 14, sy + 128, ux + 30, sy + 144], fill=BAB); d.text((ux + 66, sy + 165), "Babu → out left", font=F(16, True), fill=BAB)
# camera
d.ellipse([ux - 9, sy + 175, ux + 9, sy + 193], fill=CAM); d.text((sx + 20, sy + 230), "camera 1.6 m up, 1.5 m behind", font=F(16, True), fill=CAM)
# Antony on main deck
d.ellipse([ux - 8, sy + 260, ux + 8, sy + 276], fill="#1f7a45"); d.text((ux + 70, sy + 262), "Antony on the main deck below (off screen)", font=F(16, True), fill="#1f7a45")
# sun
d.ellipse([sx + 70, sy + sh - 70, sx + 110, sy + sh - 30], fill=SUN); d.text((sx + 120, sy + sh - 62), "sun: ahead-right of the bow", font=F(16, True), fill=SUN)

# 2 beats
y1 = y0 + 90 + ph
d.text((50, y1), "2  BEATS", font=F(32, True), fill=INK)
beats = [("0–2.5 s", "Over their shoulders, 35mm: Babu jabs his arm at the boats, Raghavan shades his eyes and leans out."),
         ("2.5–5 s", "Raghavan's hand falls slowly; Babu glances at him and hurries LEFT along the rail, out of frame."),
         ("5–6 s", "Raghavan turns to face forward; camera pushes ~1 m to an MCU (50mm), wake and boats behind him."),
         ("6–10.5 s", "LOCKED. Raghavan alone, ~20° off the lens, shouting down to Antony:"),
         ("10.5–15 s", "He waves Antony on toward the bow twice, then points back over his shoulder at the boats.")]
yy = y1 + 50
for t, s in beats:
    d.text((60, yy), t, font=F(24, True), fill=CAM); d.text((230, yy), s, font=F(24), fill=INK); yy += 42
d.text((230, yy), "RAGHAVAN: \"aantanee! athu pulikalaannaa thonnunne… el-ti-ti-ee! nammakku rakshappedanam!\"", font=F(26, True), fill=RAG); yy += 50
d.text((230, yy), "Antony! They look like the Tigers… LTTE! We have to get away!  ·  voice: Nguyen Tue · [worried]", font=F(22), fill=GREY)

# 3 timeline
y2 = yy + 70
d.text((50, y2), "3  SECOND BY SECOND", font=F(32, True), fill=INK)
tx, tw_ = 260, 1480; ty = y2 + 80; S = 15
rows = [("Camera", CAM, [(0, 5, "over the shoulders, 35mm"), (5, 6, "push"), (6, 10.5, "locked MCU, 50mm"), (10.5, 15, "breathing")]),
        ("Raghavan", RAG, [(0, 2.5, "shades eyes"), (2.5, 5, "hand falls"), (5, 6, "turns"), (6, 10.5, "THE LINE"), (10.5, 15, "waves, points back")]),
        ("Babu", BAB, [(0, 2.5, "points"), (2.5, 5, "hurries out left")]),
        ("Motorboats", MOT, [(0, 15, "head-on up the wake, ~90 m closing to ~60 m")])]
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

# 4 attach + checklist
y3 = ty + 70 * len(rows) + 60
d.text((50, y3), "4  ATTACH  (folder scenes/showreel/attach/s17-sh01b)", font=F(32, True), fill=INK)
d.text((60, y3 + 50), "@s17sh01bstart (start) · @raghavan (full) · @babu (full, 0–5.5 s) · @uru (full) · 15 s · 21:9 · Malayalam", font=F(24), fill=INK)
d.text((60, y3 + 90), "Left out: @s17sh01last / @s17sh04last (other angle, L61) · @antony20 (off screen) · @aashaan (not seen)", font=F(22), fill=GREY)
d.text((60, y3 + 130), "Checks: no sun in frame · boats match the chase (dark grey-green, outboards, dark shirts) · nothing fades · no VFX look · QC 100", font=F(22), fill=GREY)

im = im.crop((0, 0, W, y3 + 190))
im.save("scenes/showreel/storyboards/s17-sh01b-clear.png")
print(im.size)
