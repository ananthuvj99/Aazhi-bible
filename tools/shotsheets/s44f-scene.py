"""Scene storyboard for SB060 (s44f-sh04..sh14): one panel per take, plus the court map with camera positions."""
import os, json
from PIL import Image, ImageDraw, ImageFont

def F(sz, b=False):
    return ImageFont.truetype("C:/Windows/Fonts/" + ("segoeuib.ttf" if b else "segoeui.ttf"), sz)

INK, GREY, CAM = "#1d1d1f", "#6b6b6b", "#7a4fd0"
A = "scenes/showreel/approved/sb060-court/"
IMG = {"@s44fsh01start": A + "s44f-sh01-start.png", "@s44fmagstart": A + "s44f-mag-start.png", "@s44fsistart": A + "s44f-si-start.png",
       "@s44flawstart": A + "s44f-law-start.png", "@s44fantstart": A + "s44f-ant-start.png", "@s44fclarastart": A + "s44f-clara-start.png"}
COL = {"mag": "#3a3a3a", "si": "#8a6a2a", "law": "#1f4e79", "ant": "#b03a2e", None: "#5a7a5a"}
SHOTS = [
 ("s44f-sh04", 12, "@s44fsh01start", None, "WIDE, silent: slow push up the room", "everyone in place; Antony faces the judge"),
 ("s44f-sh05", 8, "@s44fmagstart", "mag", "MAGISTRATE: enthaanu policinte aavashyam?", "eyes RIGHT to the SI · 1.5–3.3 s"),
 ("s44f-sh06", 10, "@s44fsistart", "si", "SI: anveshanam nadakkukayaanu... report.", "eyes up-LEFT to the judge · 1.8–6.2 s · Rudra"),
 ("s44f-sh07", 15, "@s44flawstart", "law", "LAWYER: ithu kadalil nadanna... jaamyam anuvadikkanam.", "eyes up-RIGHT to the judge · 1.8–12.3 s"),
 ("s44f-sh08", 10, "@s44fantstart", None, "ANTONY listens (silent)", "under the SI and the plea; hope flickers"),
 ("s44f-sh09", 15, "@s44fmagstart", "mag", "MAGISTRATE: mukhathu enthu patti, antony?", "eyes LEFT to Antony · 1.5–3.5 s · then listens"),
 ("s44f-sh10", 12, "@s44fantstart", "ant", "ANTONY: stationil vachu adichathaanu...", "eyes up-RIGHT to the judge · 1.8–8.4 s · Mahendran J"),
 ("s44f-sh11", 10, "@s44fsistart", None, "SI listens (silent)", "nothing on his face; thumb on the file"),
 ("s44f-sh12", 15, "@s44fmagstart", "mag", "MAGISTRATE: the medical order · the remand", "down to the clerk 1.0–5.8 s · LEFT to Antony 8.2–14.8 s"),
 ("s44f-sh13", 12, "@s44fantstart", None, "ANTONY: the remand lands (silent)", "hands leave the rail; the constable's grip; he looks for Clara"),
 ("s44f-sh14", 10, "@s44fclarastart", None, "CLARA (silent)", "hand over her mouth; Rosamma; Jaison's hand on her shoulder"),
]
W = 1800; PW = 560; PH = int(PW / 2.333); COLS = 3
rows = (len(SHOTS) + COLS - 1) // COLS
H = 170 + 380 + rows * (PH + 150) + 60
im = Image.new("RGB", (W, H), "#f7f5f0"); d = ImageDraw.Draw(im)
d.text((50, 30), "SB060 · the magistrate's court · 11 takes, one voice each · edit plan in s44f-edit.md", font=F(40, True), fill=INK)
d.text((50, 88), "Screen direction from the wide: Antony and the lawyer look RIGHT to the judge · the SI looks LEFT · the magistrate looks LEFT to Antony, RIGHT to the SI · [anxious] · 21:9", font=F(22), fill=GREY)
# map
sx, sy, sw, sh = 50, 150, 1700, 360
d.rectangle([sx, sy, sx + sw, sy + sh], fill="#eef0ee", outline=INK, width=2)
d.rectangle([sx + 550, sy + 20, sx + 1150, sy + 60], fill="#6b3a22"); d.text((sx + 570, sy + 28), "BENCH", font=F(18, True), fill="white")
d.ellipse([sx + 840, sy + 28, sx + 862, sy + 50], fill=COL["mag"]); d.text((sx + 870, sy + 27), "magistrate", font=F(16, True), fill="white")
d.rectangle([sx + 790, sy + 80, sx + 910, sy + 105], fill="#8a6a4a"); d.text((sx + 820, sy + 82), "clerk", font=F(15, True), fill="white")
d.rectangle([sx + 120, sy + 110, sx + 290, sy + 190], outline="#6b3a22", width=4); d.text((sx + 130, sy + 194), "DOCK", font=F(16, True), fill="#6b3a22")
d.ellipse([sx + 195, sy + 135, sx + 217, sy + 157], fill=COL["ant"]); d.text((sx + 170, sy + 160), "Antony", font=F(15, True), fill=COL["ant"])
d.rectangle([sx + 700, sy + 140, sx + 1000, sy + 180], fill="#9a7a5a"); d.text((sx + 760, sy + 148), "advocates' table", font=F(15, True), fill="white")
d.ellipse([sx + 740, sy + 185, sx + 762, sy + 207], fill=COL["law"]); d.text((sx + 768, sy + 186), "lawyer", font=F(15, True), fill=COL["law"])
d.rectangle([sx + 1380, sy + 110, sx + 1480, sy + 165], outline="#6b3a22", width=4); d.text((sx + 1380, sy + 168), "witness box", font=F(15, True), fill="#6b3a22")
d.ellipse([sx + 1420, sy + 190, sx + 1442, sy + 212], fill=COL["si"]); d.text((sx + 1450, sy + 190), "SI", font=F(15, True), fill=COL["si"])
d.text((sx + sw - 90, sy + 100), "windows", font=F(15, True), fill=CAM)
d.line([sx + 40, sy + 250, sx + 780, sy + 250], fill="#6b3a22", width=4); d.line([sx + 920, sy + 250, sx + sw - 40, sy + 250], fill="#6b3a22", width=4)
d.ellipse([sx + 120, sy + 280, sx + 142, sy + 302], fill="#c08a5a"); d.text((sx + 150, sy + 280), "Clara, Rosamma, Jaison", font=F(15, True), fill=INK)
def cam(x, y, lab):
    d.polygon([(sx + x - 11, sy + y + 12), (sx + x + 11, sy + y + 12), (sx + x, sy + y - 12)], fill=CAM); d.text((sx + x + 14, sy + y - 8), lab, font=F(14, True), fill=CAM)
cam(850, 335, "C1 wide (sh04)"); cam(850, 125, "MAG (below bench)"); cam(330, 215, "ANT (floor, front-right of dock)")
cam(1300, 215, "SI (floor, front-left of him)"); cam(470, 85, "LAWYER (beside bench)"); cam(420, 300, "CLARA (central gap)")
y0 = sy + sh + 40
for k, (n, dur, st, who, line, note) in enumerate(SHOTS):
    r, c = divmod(k, COLS); x = 50 + c * (PW + 30); y = y0 + r * (PH + 150)
    p = IMG[st] if os.path.exists(IMG[st]) else "C:/Users/ranji/AppData/Local/Temp/claude/a46a101416072ac0/1288b67a-9430-4c14-931f-e07fcdca45e7/scratchpad/hf/cl_a.png"
    im.paste(Image.open(p).convert("RGB").resize((PW, PH)), (x, y)); d.rectangle([x, y, x + PW, y + PH], outline=INK, width=2)
    tag = f"{n} · {dur} s"; f = F(18, True); tw = d.textlength(tag, font=f)
    d.rounded_rectangle([x + 4, y + 4, x + tw + 18, y + 32], 7, fill=COL[who]); d.text((x + 10, y + 5), tag, font=f, fill="white")
    d.text((x, y + PH + 8), line, font=F(17, True), fill=COL[who]); d.text((x, y + PH + 34), note, font=F(16), fill=GREY)
    d.text((x, y + PH + 58), "start " + st, font=F(15), fill=GREY)
im.save("scenes/showreel/storyboards/s44f-scene-clear.png"); print(im.size)
