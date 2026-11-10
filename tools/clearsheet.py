"""Clear storyboard sheet for one AAZHI shot (Ranjith, 2026-11-10).

Four parts, top to bottom:
  1 WHAT YOU WILL SEE   the start frame (or nearest approved frame) with name tags and coloured movement arrows
  2 MAP FROM ABOVE      the deck as a simple plan: people, door/props, camera and its move
  3 SECOND BY SECOND    one row per person and one for the camera
  4 ON THE PLATFORM     start image slot, IDs, duration, QA score, what to watch

Usage:  python tools/clearsheet.py scenes/showreel/storyboards/<shot>-clear.json
Coordinates: "frame" items use the frame image's own pixels; "map" items use a 1000 x 520 plan
(x = aft at 0 to bow at 1000, y = left rail at 0 to right rail at 520).
"""
import json, math, sys
from PIL import Image, ImageDraw, ImageFont

def F(sz, b=False):
    for name in (("segoeuib.ttf" if b else "segoeui.ttf"), ("DejaVuSans-Bold.ttf" if b else "DejaVuSans.ttf")):
        for d in ("C:/Windows/Fonts", "/usr/share/fonts/truetype/dejavu"):
            try:
                return ImageFont.truetype(f"{d}/{name}", sz)
            except OSError:
                pass
    return ImageFont.load_default()

INK, GREY = "#1d1d1f", "#6b6b6b"

def arrow(d, p0, p1, col, w=8):
    d.line([p0, p1], fill=col, width=w)
    a = math.atan2(p1[1] - p0[1], p1[0] - p0[0])
    for s in (2.6, -2.6):
        d.line([p1, (p1[0] + 26 * math.cos(a + s), p1[1] + 26 * math.sin(a + s))], fill=col, width=w)

def tag(d, xy, text, col, f=None):
    f = f or F(24, True)
    x, y = xy
    tw = d.textlength(text, font=f)
    d.rounded_rectangle([x - 6, y - 4, x + tw + 8, y + 34], 8, fill=col)
    d.text((x + 1, y - 2), text, font=f, fill="white")

def main(path):
    J = json.load(open(path, encoding="utf-8"))
    W = 1800
    im = Image.new("RGB", (W, 3200), "#f7f5f0")
    d = ImageDraw.Draw(im)
    d.text((50, 30), J["title"], font=F(52, True), fill=INK)
    d.text((50, 100), J["subtitle"], font=F(28), fill=GREY)
    # 1 frame
    y0 = 160
    d.text((50, y0), "1  WHAT YOU WILL SEE  " + J.get("frame_note", ""), font=F(32, True), fill=INK)
    fr = Image.open(J["frame"]).convert("RGB")
    fw = W - 100
    fh = int(fr.height * fw / fr.width)
    im.paste(fr.resize((fw, fh)), (50, y0 + 50))
    s = fw / fr.width
    P = lambda x, y: (50 + x * s, y0 + 50 + y * s)
    for t in J.get("frame_tags", []):
        tag(d, P(t["x"], t["y"]), t["text"], t["color"])
    for a in J.get("frame_arrows", []):
        arrow(d, P(*a["from"]), P(*a["to"]), a["color"])
        if a.get("label"):
            tag(d, P(*a["label_at"]), a["label"], a["color"])
    cy = y0 + 50 + fh + 20
    if J.get("frame_caption"):
        d.text((50, cy), J["frame_caption"], font=F(26), fill=GREY)
    # 2 map
    y1 = cy + 70
    d.text((50, y1), "2  MAP FROM ABOVE  (who stands where, and the camera)", font=F(32, True), fill=INK)
    mx, my, mw, mh = 120, y1 + 60, 1000, 520
    M = lambda x, y: (mx + x, my + y)
    d.rectangle([mx, my, mx + mw, my + mh], fill="#c9b99a", outline=INK, width=3)
    d.rectangle([mx, my, mx + mw, my + 40], fill="#6d7b8f")
    d.text((mx + mw / 2 - 120, my + 5), "LEFT RAIL (sea side)", font=F(22, True), fill="white")
    d.rectangle([mx + 20, my + mh - 200, mx + 260, my + mh - 20], fill="#7a5233")
    d.text((mx + 45, my + mh - 130), "DECKHOUSE", font=F(26, True), fill="white")
    d.text((mx + 40, my + mh - 95), J.get("deckhouse_note", "(Aashaan at the wheel)"), font=F(20), fill="white")
    d.rectangle([mx + 250, my + mh - 170, mx + 270, my + mh - 120], fill="#ffd23f")
    d.text((mx + 280, my + mh - 175), "door", font=F(22, True), fill="#7a5a00")
    d.text((mx + mw - 120, my + mh / 2 - 15), "BOW →", font=F(28, True), fill=INK)
    for p in J.get("map_people", []):
        x, y = M(p["x"], p["y"])
        d.ellipse([x - 18, y - 18, x + 18, y + 18], fill=p["color"])
        d.text((x - 30 + p.get("dx", 0), y + 22 + p.get("dy", 0)), p["name"], font=F(22, True), fill=p.get("text_color", INK))
    for a in J.get("map_arrows", []):
        arrow(d, M(*a["from"]), M(*a["to"]), a["color"], 6)
    c = J.get("map_camera")
    if c:
        cx, cy2 = M(c["x"], c["y"])
        d.polygon([(cx, cy2), (cx - 28, cy2 + 50), (cx + 28, cy2 + 50)], fill="#7a4fd0")
        d.text((cx + 40, cy2 + 5), c["label"], font=F(22, True), fill="#7a4fd0")
        if c.get("turn"):
            r = 70
            start, end = (200, 300) if c["turn"] == "left" else (240, 340)
            d.arc([cx - r, cy2 - r + 25, cx + r, cy2 + r + 25], start, end, fill="#7a4fd0", width=6)
    for i, t in enumerate(J.get("map_notes", [])):
        d.text((mx + mw + 30, my + 20 + i * 35), t, font=F(24, i == 0), fill=INK if i == 0 else GREY)
    # 3 timeline
    y2 = my + mh + 60
    d.text((50, y2), "3  SECOND BY SECOND", font=F(32, True), fill=INK)
    tx, tw_ = 260, 1460
    ty = y2 + 60
    dur = J.get("duration", 8)
    rows = J["timeline"]
    for sec in range(dur + 1):
        x = tx + tw_ * sec / dur
        d.line([x, ty, x, ty + 72 * len(rows) + 10], fill="#d8d4cc", width=2)
        d.text((x - 8, ty - 34), f"{sec}s", font=F(22), fill=GREY)
    for i, r in enumerate(rows):
        yy = ty + 10 + i * 72
        d.text((50, yy + 8), r["who"], font=F(26, True), fill=r["color"])
        for a, b, t in r["segments"]:
            x0, x1 = tx + tw_ * a / dur, tx + tw_ * b / dur
            d.rounded_rectangle([x0 + 3, yy, x1 - 3, yy + 52], 10, fill=r["color"])
            d.text((x0 + 14, yy + 10), t, font=F(22, True), fill="white")
    # 4 platform
    y3 = ty + 72 * len(rows) + 50
    d.text((50, y3), "4  ON THE PLATFORM", font=F(32, True), fill=INK)
    for i, t in enumerate(J["platform"]):
        d.text((70, y3 + 55 + i * 42), "•  " + t, font=F(27), fill=INK)
    im = im.crop((0, 0, W, y3 + 55 + len(J["platform"]) * 42 + 40))
    im.save(J["out"])
    print(J["out"], im.size)

if __name__ == "__main__":
    main(sys.argv[1])
