"""Clear sheet for s17-sh01 (SB025, the chase begins: top shot). Frames are drawn from the shot's geometry:
24mm on full frame (74 deg wide), 21:9, the camera straight down; all positions in metres in the uru's own frame."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math

def F(sz, b=False):
    return ImageFont.truetype("C:/Windows/Fonts/" + ("segoeuib.ttf" if b else "segoeui.ttf"), sz)
INK, GREY = "#1d1d1f", "#6b6b6b"
URU, MOT, VAL, CAM = "#b5651d", "#2f6f4f", "#8a6d3b", "#7a4fd0"

# ---------------- geometry (uru frame: uru fixed, x = direction of travel, y = across, + down)
URU_X, URU_L, URU_B = 42.0, 25.0, 7.0
REL = 3.3                                    # motorboats gain 3.3 m/s (25 vs 13 km/h)
LEAD_END = URU_X - URU_L / 2 - 50 - 4        # lead centre 50 m behind the stern at 12 s
def boats(t):
    lead = LEAD_END - REL * (12 - t)
    return [(lead, 0.0), (lead - 15, -6.0), (lead - 15, 6.0)]
VALLAMS = [(70, -18), (78, -6), (74, 9), (86, 2), (82, 20)]
def ease(u): return u * u * (3 - 2 * u)
def cam(t):
    x0 = boats(0)[0][0] - 5                  # over the boats at the start, they sit left-centre
    if t <= 2.5: return boats(t)[0][0] - 5, 60.0
    if t >= 9: return 0.0, 90.0
    u = ease((t - 2.5) / 6.5)
    xa = boats(2.5)[0][0] - 5
    return xa + (0 - xa) * u, 60 + 30 * u
def foot(h): return 2 * h * math.tan(math.radians(37)), 2 * h * math.tan(math.radians(37)) / 2.39

# ---------------- draw one frame
def frame(t, W=1680):
    H = int(W / 2.39)
    cx, h = cam(t); fw, fh = foot(h); s = W / fw
    P = lambda x, y: ((x - cx) * s + W / 2, y * s + H / 2)
    im = Image.new("RGB", (W, H)); d = ImageDraw.Draw(im)
    for yy in range(H):                                             # sea, warmer toward upper right
        k = yy / H
        d.line([(0, yy), (W, yy)], fill=(int(52 + 18 * (1 - k)), int(84 + 14 * (1 - k)), int(108 + 10 * (1 - k))))
    glow = Image.new("RGB", (W, H), (0, 0, 0)); g = ImageDraw.Draw(glow)
    g.ellipse([W * 0.62, -H * 0.55, W * 1.25, H * 0.45], fill=(196, 160, 92))
    im = Image.blend(im, Image.composite(glow, im, glow.convert("L").point(lambda v: 255 if v else 0)).filter(ImageFilter.GaussianBlur(60)), 0.22)
    im = im.filter(ImageFilter.GaussianBlur(0)); d = ImageDraw.Draw(im)
    for k in range(-8, 30):                                          # swell lines, diagonal
        x0 = (k * 40 - cx - 200) * s + W / 2
        d.line([(x0, 0), (x0 + H * 0.7, H)], fill=(70, 102, 124), width=max(1, int(s * 0.6)))
    def wake(x, y, L, spread, col, wid):
        for sgn in (-1, 1):
            d.line([P(x, y), P(x - L, y + sgn * spread)], fill=col, width=max(2, int(wid * s)))
    # uru wake (soft, wide) and hull
    us = URU_X - URU_L / 2
    wake(us + 4, 0, 150, 30, (150, 175, 185), 1.6)
    d.line([P(us, 0), P(us - 120, 0)], fill=(120, 150, 165), width=max(2, int(2.5 * s)))
    hull = [P(us, -URU_B / 2), P(us + URU_L - 7, -URU_B / 2), P(us + URU_L, 0), P(us + URU_L - 7, URU_B / 2), P(us, URU_B / 2)]
    d.polygon([P(x + 1.5, y + 1.5) for x, y in [(us, -URU_B / 2), (us + URU_L - 7, -URU_B / 2), (us + URU_L, 0), (us + URU_L - 7, URU_B / 2), (us, URU_B / 2)]], fill=(28, 44, 58))
    d.polygon(hull, fill=(110, 125, 135))                                            # blue-grey hull rim
    inner = [P(us + 0.6, -URU_B / 2 + 0.6), P(us + URU_L - 7.3, -URU_B / 2 + 0.6), P(us + URU_L - 1.2, 0), P(us + URU_L - 7.3, URU_B / 2 - 0.6), P(us + 0.6, URU_B / 2 - 0.6)]
    d.polygon(inner, fill=(139, 103, 66))                                            # brown plank deck
    d.polygon([P(us + URU_L - 7, -URU_B / 2 + 0.6), P(us + URU_L - 1.2, 0), P(us + URU_L - 7, URU_B / 2 - 0.6)], fill=(52, 92, 150))  # blue bow deck
    d.rectangle([P(us + 0.6, -URU_B / 2 + 0.6), P(us + 8.5, URU_B / 2 - 0.6)], fill=(96, 70, 48), outline=(60, 42, 28))  # deckhouse
    d.rectangle([P(us + 2.0, -1.6), P(us + 6.5, 1.6)], outline=(170, 140, 100), width=max(1, int(0.3 * s)))  # top deck rail
    m = P(us + 13.5, 0); r = 0.6 * s
    d.ellipse([m[0] - r, m[1] - r, m[0] + r, m[1] + r], fill=(60, 40, 25))          # mast base
    d.line([P(us + 9, 0.3), P(us + 20, 0.3)], fill=(70, 50, 30), width=max(1, int(0.35 * s)))  # boom
    for yy in (-2, 0, 2):                                                            # three men at the stern rail
        q = P(us + 9.3, yy); rr = 0.35 * s; d.ellipse([q[0] - rr, q[1] - rr, q[0] + rr, q[1] + rr], fill=(30, 25, 22))
    # motorboats
    for x, y in boats(t):
        wake(x - 4, y, 70, 9, (235, 240, 240), 1.0)
        d.line([P(x - 4, y), P(x - 60, y)], fill=(245, 248, 248), width=max(2, int(1.4 * s)))
        d.polygon([P(x - 4, y - 1.2), P(x + 2, y - 1.2), P(x + 4, y), P(x + 2, y + 1.2), P(x - 4, y + 1.2)], fill=(40, 70, 58))
        d.polygon([P(x - 3.6, y - 0.8), P(x + 1.8, y - 0.8), P(x + 3.2, y), P(x + 1.8, y + 0.8), P(x - 3.6, y + 0.8)], fill=(150, 155, 150))
        d.rectangle([P(x - 4.6, y - 0.4), P(x - 3.9, y + 0.4)], fill=(25, 25, 25))
        for k in range(4):
            q = P(x - 2.5 + k * 1.3, y); rr = 0.32 * s; d.ellipse([q[0] - rr, q[1] - rr, q[0] + rr, q[1] + rr], fill=(30, 30, 30))
        d.polygon([P(x + 4, y), P(x + 5.5, y - 1.8), P(x + 5.5, y + 1.8)], fill=(235, 240, 240))  # bow spray
    # vallams (only once they are in reach of the frame)
    for x, y in VALLAMS:
        d.polygon([P(x - 4.5, y), P(x - 3, y - 0.9), P(x + 3, y - 0.9), P(x + 4.5, y), P(x + 3, y + 0.9), P(x - 3, y + 0.9)], fill=(92, 66, 40))
        d.arc([P(x - 2, y + 0.5), P(x + 6, y + 6)], 180, 360, fill=(200, 200, 190), width=max(1, int(0.25 * s)))
    return im.filter(ImageFilter.GaussianBlur(0.6)), (cx, h)

# ---------------- sheet
W = 1800
sheet = Image.new("RGB", (W, 3400), "#f7f5f0"); d = ImageDraw.Draw(sheet)
def tag(xy, text, col, f=None):
    f = f or F(24, True); x, y = xy; tw = d.textlength(text, font=f)
    d.rounded_rectangle([x - 6, y - 4, x + tw + 8, y + 34], 8, fill=col); d.text((x + 1, y - 2), text, font=f, fill="white")
def arrow(p0, p1, col, w=6):
    d.line([p0, p1], fill=col, width=w); a = math.atan2(p1[1] - p0[1], p1[0] - p0[0])
    for sg in (2.6, -2.6): d.line([p1, (p1[0] + 24 * math.cos(a + sg), p1[1] + 24 * math.sin(a + sg))], fill=col, width=w)

d.text((50, 30), "s17-sh01 · SB025 · The chase begins: top shot", font=F(52, True), fill=INK)
d.text((50, 100), "12 seconds · no dialogue · dawn, Sri Lankan waters · drone straight down, 24mm, rising 60 m → 90 m · three motorboats behind our uru", font=F(27), fill=GREY)

y0 = 165
d.text((50, y0), "1  WHAT YOU WILL SEE  (drawn to scale from the prompt's numbers; boats move toward screen right)", font=F(32, True), fill=INK)
FW = 830; FH = int(FW / 2.39)
for i, (t, lab) in enumerate([(0.0, "0 s · over the three motorboats, 60 m up"), (6.0, "6 s · forward and rising: the uru's stern comes in at the right"),
                              (8.0, "8 s · the whole uru in frame"), (12.0, "12 s · 90 m up: uru right, motorboats left, vallams at the edge")]):
    fr, (cx, h) = frame(t); fr = fr.resize((FW, FH))
    x = 50 + (i % 2) * (FW + 40); y = y0 + 60 + (i // 2) * (FH + 80)
    sheet.paste(fr, (x, y)); d.rectangle([x, y, x + FW, y + FH], outline=INK, width=2)
    d.text((x, y + FH + 8), lab, font=F(24, True), fill=INK)
    fw, fh = foot(h); sc = FW / fw
    PX = lambda wx, wy: (x + (wx - cx) * sc + FW / 2, y + wy * sc + FH / 2)
    if t == 12.0:
        tag(PX(URU_X - 10, -9), "OUR URU 25 m", URU); tag(PX(boats(t)[0][0] - 25, -11), "3 MOTORBOATS 8 m", MOT)
        tag(PX(58, 14), "VALLAMS", VAL)
    if t == 0.0:
        tag(PX(boats(t)[0][0] - 12, -15), "3 MOTORBOATS", MOT)
        arrow((x + FW - 230, y + FH - 40), (x + FW - 40, y + FH - 40), CAM); d.text((x + FW - 330, y + FH - 80), "camera moves →", font=F(20, True), fill="white")
    if t == 6.0:
        tag(PX(URU_X - 40, 9), "uru stern enters", URU)

# 2. map
y1 = y0 + 60 + 2 * (FH + 80) + 10
d.text((50, y1), "2  MAP FROM ABOVE  (camera path and what each frame covers)", font=F(32, True), fill=INK)
mx, my, mw, mh = 60, y1 + 60, 1680, 480
x_lo, x_hi = -150, 95; sc = mw / (x_hi - x_lo)
M = lambda wx, wy: (mx + (wx - x_lo) * sc, my + mh / 2 + wy * sc)
d.rectangle([mx, my, mx + mw, my + mh], fill="#5a7f97")
for t, col, dash in [(0.0, "#ffd23f", "0 s footprint (60 m up, 90 × 38 m)"), (12.0, "#ffffff", "12 s footprint (90 m up, 136 × 57 m)")]:
    cx, h = cam(t); fw, fh = foot(h)
    d.rectangle([M(cx - fw / 2, -fh / 2), M(cx + fw / 2, fh / 2)], outline=col, width=4)
    d.text(M(cx - fw / 2 + 2, fh / 2 - 7 if t else -fh / 2 + 1), dash, font=F(20, True), fill=col)
us = URU_X - URU_L / 2
d.polygon([M(us, -3.5), M(us + 18, -3.5), M(us + 25, 0), M(us + 18, 3.5), M(us, 3.5)], fill=URU); d.text(M(us, 5), "uru (12 s)", font=F(22, True), fill="white")
for t, col in [(0.0, "#a7c3b3"), (12.0, MOT)]:
    for x, y in boats(t):
        d.polygon([M(x - 4, y - 1.4), M(x + 4, y), M(x - 4, y + 1.4)], fill=col)
    d.text(M(boats(t)[0][0] - 12, 9), f"motorboats {int(t)} s", font=F(20, True), fill="white")
arrow(M(boats(0)[0][0] + 6, -14), M(boats(12)[0][0] - 6, -14), MOT, 5); d.text(M(boats(0)[0][0] - 20, -21), "they gain 3.3 m every second: 90 m gap → 50 m", font=F(20, True), fill="white")
for x, y in VALLAMS: d.polygon([M(x - 4, y - 1), M(x + 4, y), M(x - 4, y + 1)], fill=VAL)
d.text(M(68, 23), "5 vallams", font=F(20, True), fill="white")
pts = [M(cam(t)[0], 0) for t in [i * 0.5 for i in range(25)]]
d.line(pts, fill=CAM, width=5); arrow(pts[-3], pts[-1], CAM, 5)
d.text(M(cam(0)[0], -2), "camera", font=F(22, True), fill="#e9ddff")
d.text((mx + mw - 330, my + 10), "sun: low, upper right", font=F(22, True), fill="#ffd23f")

# 3. timeline
y2 = my + mh + 60
d.text((50, y2), "3  SECOND BY SECOND", font=F(32, True), fill=INK)
tx, tw_ = 270, 1470; ty = y2 + 60
for sec in range(13):
    x = tx + tw_ * sec / 12; d.line([x, ty, x, ty + 300], fill="#d8d4cc", width=2); d.text((x - 10, ty - 34), f"{sec}s", font=F(22), fill=GREY)
rows = [("Camera", CAM, [(0, 2.5, "hold, 60 m"), (2.5, 9, "forward + rise 60 → 90 m"), (9, 12, "hold, 90 m")]),
        ("Motorboats", MOT, [(0, 12, "three, arrowhead, racing up the uru's wake, gap 90 m → 50 m")]),
        ("Our uru", URU, [(6, 8, "stern enters"), (8, 12, "whole uru, right third")]),
        ("Vallams", VAL, [(9, 12, "tips at right edge")])]
for i, (lab, col, segs) in enumerate(rows):
    yy = ty + 10 + i * 72; d.text((50, yy + 8), lab, font=F(26, True), fill=col)
    for a, b, t in segs:
        x0, x1 = tx + tw_ * a / 12, tx + tw_ * b / 12
        d.rounded_rectangle([x0 + 3, yy, x1 - 3, yy + 52], 10, fill=col); d.text((x0 + 14, yy + 10), t, font=F(22, True), fill="white")

# 4. platform
y3 = ty + 340
d.text((50, y3), "4  ON THE PLATFORM", font=F(32, True), fill=INK)
lines = ["Start image slot: empty (no start frame; text-to-video with @uru)",
         "Attach: @uru (full)  ·  remove everything else",
         "Duration 12 s · 21:9 · no dialogue        QA score 100 / 100",
         "Watch for: exactly 3 motorboats · uru 3× longer than each · no flags, guns or lettering · camera never tilts to the horizon"]
for i, t in enumerate(lines): d.text((70, y3 + 55 + i * 42), "•  " + t, font=F(27), fill=INK)
sheet = sheet.crop((0, 0, W, y3 + 55 + len(lines) * 42 + 40))
sheet.save("scenes/showreel/storyboards/s17-sh01-clear.png"); print(sheet.size)
for t in (0, 2.5, 4, 4.5, 7, 9, 12):
    cx, h = cam(t); fw, fh = foot(h); print(t, 'cam', round(cx, 1), 'h', round(h), 'frame x', round(cx - fw / 2), round(cx + fw / 2), 'uru stern', URU_X - URU_L / 2, 'lead', round(boats(t)[0][0], 1))
