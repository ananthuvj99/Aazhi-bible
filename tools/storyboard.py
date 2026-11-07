"""Make a storyboard sheet for an AAZHI scene: one panel per shot.

Usage:  python tools/storyboard.py scenes/showreel/storyboards/<scene>.json
Writes: the PNG named in the JSON ("out"), next to it by default.

JSON:
{
  "title": "SB027 · The night watch",
  "subtitle": "Source scene 21–22 · silent · Quiet",
  "out": "scenes/showreel/storyboards/sb027-storyboard.png",
  "panels": [
    {"shot": "s21-sh01", "image": "locations/uru-deck/plates/urudeck-c1-plate-night.png",
     "title": "Wide: men asleep on deck", "time": "8 s",
     "beats": ["0–2 s hold", "2–6 s ...", "6–8 s hold"],
     "refs": "@urudeckc1platenight · @crew (men 1, 7) · @uru"}
  ],
  "footer": "Storyboard only. Never attach this sheet to a generation."
}
Panel images are the shot's plate or start image (repo paths). Arrows or figures are not drawn:
the beats under each panel say what happens. Text is only on the sheet, never in a plate.
"""
import json, os, sys, textwrap
from PIL import Image, ImageDraw, ImageFont

def font(size, bold=False):
    for name in (("segoeuib.ttf" if bold else "segoeui.ttf"), ("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf")):
        for d in ("C:/Windows/Fonts", "/usr/share/fonts/truetype/dejavu"):
            p = os.path.join(d, name)
            if os.path.exists(p):
                return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def main(path):
    spec = json.load(open(path, encoding="utf-8"))
    panels = spec["panels"]
    cols = 2 if len(panels) <= 4 else 3
    PW, PH = 760, 428
    M, CAP = 36, 230
    rows = (len(panels) + cols - 1) // cols
    W = M + cols * (PW + M)
    HEAD = 150
    H = HEAD + rows * (PH + CAP + M) + 70
    sheet = Image.new("RGB", (W, H), "#faf8f2")
    d = ImageDraw.Draw(sheet)
    d.text((M, 30), spec["title"], font=font(40, True), fill="#1a1a1a")
    d.text((M, 86), spec.get("subtitle", ""), font=font(24), fill="#555555")
    for i, p in enumerate(panels):
        c, r = i % cols, i // cols
        x, y = M + c * (PW + M), HEAD + r * (PH + CAP + M)
        try:
            im = Image.open(p["image"]).convert("RGB")
            im.thumbnail((PW, PH))
            bg = Image.new("RGB", (PW, PH), "#222222")
            bg.paste(im, ((PW - im.width) // 2, (PH - im.height) // 2))
        except Exception:
            bg = Image.new("RGB", (PW, PH), "#cccccc")
        sheet.paste(bg, (x, y))
        d.rectangle([x, y, x + PW - 1, y + PH - 1], outline="#bbbbbb", width=2)
        d.text((x, y + PH + 10), f"{i+1} · {p['shot']} · {p.get('time','')} · {p['title']}", font=font(24, True), fill="#1a1a1a")
        yy = y + PH + 46
        for b in p.get("beats", []):
            for ln in textwrap.wrap(b, 64):
                d.text((x, yy), ln, font=font(20), fill="#333333"); yy += 26
        for ln in textwrap.wrap("Attach: " + p.get("refs", ""), 70):
            d.text((x, yy + 4), ln, font=font(19), fill="#7a4a10"); yy += 25
    d.text((M, H - 50), spec.get("footer", "Storyboard only. Never attach this sheet to a generation."), font=font(20), fill="#9a5a1a")
    out = spec.get("out") or os.path.splitext(path)[0] + ".png"
    sheet.save(out)
    print(out, sheet.size)

if __name__ == "__main__":
    main(sys.argv[1])
