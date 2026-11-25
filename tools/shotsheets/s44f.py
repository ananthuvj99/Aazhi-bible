"""Clear sheets for SB060, the magistrate's court: s44f-sh01, sh02, sh03 (one file renders all three)."""
import os
from PIL import Image, ImageDraw, ImageFont

def F(sz, b=False):
    return ImageFont.truetype("C:/Windows/Fonts/" + ("segoeuib.ttf" if b else "segoeui.ttf"), sz)

INK, GREY, CAM, MAG, RAM, LAW, ANT, CON, WOOD = "#1d1d1f", "#6b6b6b", "#7a4fd0", "#3a3a3a", "#8a6a2a", "#1f4e79", "#b03a2e", "#6b7a3a", "#6b3a22"
START = "scenes/showreel/approved/sb060-court/s44f-sh01-start.png"

def court_map(d, sx, sy, sw, sh, cams):
    d.rectangle([sx, sy, sx + sw, sy + sh], fill="#eef0ee", outline=INK, width=2)
    d.rectangle([sx + 200, sy + 20, sx + 630, sy + 60], fill=WOOD); d.text((sx + 215, sy + 28), "BENCH", font=F(16, True), fill="white")
    d.ellipse([sx + 405, sy + 30, sx + 425, sy + 50], fill=MAG); d.text((sx + 432, sy + 28), "magistrate", font=F(15, True), fill="white")
    d.rectangle([sx + 360, sy + 72, sx + 470, sy + 98], fill="#8a6a4a"); d.text((sx + 372, sy + 76), "clerk", font=F(14, True), fill="white")
    d.rectangle([sx + 40, sy + 110, sx + 150, sy + 180], outline=WOOD, width=4); d.text((sx + 52, sy + 184), "DOCK", font=F(15, True), fill=WOOD)
    d.ellipse([sx + 85, sy + 135, sx + 105, sy + 155], fill=ANT); d.text((sx + 70, sy + 158), "Antony", font=F(14, True), fill=ANT)
    d.ellipse([sx + 50, sy + 115, sx + 64, sy + 129], fill=CON); d.ellipse([sx + 126, sy + 115, sx + 140, sy + 129], fill=CON)
    d.rectangle([sx + 330, sy + 130, sx + 500, sy + 170], fill="#9a7a5a"); d.text((sx + 345, sy + 138), "advocates' table", font=F(14, True), fill="white")
    d.ellipse([sx + 405, sy + 175, sx + 425, sy + 195], fill=LAW); d.text((sx + 430, sy + 176), "lawyer", font=F(14, True), fill=LAW)
    d.rectangle([sx + 680, sy + 100, sx + 760, sy + 150], outline=WOOD, width=4); d.text((sx + 672, sy + 154), "witness box", font=F(14, True), fill=WOOD)
    d.ellipse([sx + 700, sy + 170, sx + 720, sy + 190], fill=RAM); d.text((sx + 640, sy + 194), "Ramachandran", font=F(14, True), fill=RAM)
    d.text((sx + sw - 70, sy + 80), "windows", font=F(14, True), fill=CAM)
    d.line([sx + 20, sy + 230, sx + 360, sy + 230], fill=WOOD, width=4); d.line([sx + 470, sy + 230, sx + sw - 20, sy + 230], fill=WOOD, width=4)
    d.text((sx + 40, sy + 240), "Clara, Rosamma, Jaison (front-left bench)", font=F(14, True), fill=INK)
    for (x, y, lab, col) in cams:
        d.polygon([(sx + x - 10, sy + y + 12), (sx + x + 10, sy + y + 12), (sx + x, sy + y - 10)], fill=col)
        d.text((sx + x + 14, sy + y - 6), lab, font=F(14, True), fill=col)

def sheet(name, title, sub, tag, beats, lines, rows, S, attach, cams):
    W = 1800
    im = Image.new("RGB", (W, 1700), "#f7f5f0"); d = ImageDraw.Draw(im)
    d.text((50, 30), title, font=F(44, True), fill=INK)
    d.text((50, 92), sub, font=F(24), fill=GREY)
    y0 = 150
    d.text((50, y0), "1  START FRAME  and  WHERE EVERYONE IS", font=F(32, True), fill=INK)
    pw = 830; ph = int(pw / 2.333)
    a = Image.open(START).convert("RGB").resize((pw, ph))
    im.paste(a, (50, y0 + 50)); d.rectangle([50, y0 + 50, 50 + pw, y0 + 50 + ph], outline=INK, width=2)
    f = F(20, True); tw = d.textlength(tag, font=f)
    d.rounded_rectangle([54, y0 + 56, 70 + tw, y0 + 88], 8, fill=RAM); d.text((60, y0 + 58), tag, font=f, fill="white")
    court_map(d, 920, y0 + 50, 830, ph, cams)
    y1 = y0 + 90 + ph
    d.text((50, y1), "2  BEATS", font=F(32, True), fill=INK)
    yy = y1 + 50
    for t, s in beats:
        d.text((60, yy), t, font=F(22, True), fill=CAM); d.text((230, yy), s, font=F(22), fill=INK); yy += 38
    for s, col in lines:
        d.text((230, yy), s, font=F(20, True), fill=col); yy += 32
    y2 = yy + 50
    d.text((50, y2), "3  SECOND BY SECOND", font=F(32, True), fill=INK)
    tx, tw_ = 260, 1480; ty = y2 + 80
    for sec in range(0, S + 1):
        x = tx + tw_ * sec / S; d.line([x, ty, x, ty + 70 * len(rows) + 10], fill="#d8d4cc", width=2); d.text((x - 10, ty - 32), f"{sec}", font=F(18), fill=GREY)
    for i, (lab, col, segs) in enumerate(rows):
        yy = ty + 10 + i * 70; d.text((50, yy + 8), lab, font=F(22, True), fill=col)
        for a2, b2, t in segs:
            x0, x1 = tx + tw_ * a2 / S, tx + tw_ * b2 / S
            d.rounded_rectangle([x0 + 2, yy, x1 - 2, yy + 50], 8, fill=col)
            ff = F(16, True)
            if t and d.textlength(t, font=ff) < x1 - x0 - 10:
                d.text((x0 + 8, yy + 14), t, font=ff, fill="white")
    y3 = ty + 70 * len(rows) + 60
    d.text((50, y3), "4  ATTACH  (folder scenes/showreel/attach/" + name + ")", font=F(32, True), fill=INK)
    for k, s in enumerate(attach):
        d.text((60, y3 + 50 + 40 * k), s, font=F(21), fill=INK if k == 0 else GREY)
    im = im.crop((0, 0, W, y3 + 60 + 40 * len(attach)))
    im.save("scenes/showreel/storyboards/" + name + "-clear.png"); print(name, im.size)

sheet("s44f-sh01", "s44f-sh01 v1 · SB060 the hearing opens (take 1 of 3)",
      "30 s · Malayalam · push from the back benches to the dock · magistrate (voice pending), Ramachandran (Rudra), lawyer (pending) · [anxious]",
      "0 s = @s44fsh01start · court C1",
      [("0–3 s", "Hold on the start frame; the magistrate looks up."), ("3–4.8 s", "MAGISTRATE asks; the push up the room begins."),
       ("5.3–9.6 s", "RAMACHANDRAN answers from the police side; Clara turns to him."), ("11–21.5 s", "LAWYER pleads; the camera drifts left to the dock."),
       ("21.5–30 s", "Silence: the magistrate turns the statements; settle on Antony's medium shot.")],
      [("M: enthaanu policinte aavashyam?   R: anveshanam nadakkukayaanu. prathiye remand cheyyanamennaanu report.", RAM),
       ("L: ithu kadalil nadanna oru rakshaapravarthanamaanu, your honour. ... jaamyam anuvadikkanam.", LAW)],
      [("Camera", CAM, [(0, 3, "C1 hold"), (3, 11, "push up the gap"), (11, 21.5, "drift left to dock"), (21.5, 30, "settle on Antony")]),
       ("Magistrate", MAG, [(3, 4.8, "Q"), (21.5, 30, "turns the statements")]), ("Ramachandran", RAM, [(5.3, 9.6, "report")]),
       ("Lawyer", LAW, [(11, 21.5, "the plea")]), ("Antony", ANT, [(0, 30, "silent, facing the bench")])],
      30,
      ["@s44fsh01start (start) · @magistrate · @siramachandran · @lawyer · @antonycustody · @constables · @claracourt · @jaison20 · 30 s · 21:9",
       "Left out: @courtc1plate (start angle, L180) · @sasi, @babu (removed) · optional @rosamma",
       "Watch: listeners' lips closed · three voices not swapped · Antony faces the bench · QC 100"],
      [(415, 300, "C1 START", CAM), (200, 200, "END (front of dock)", "#c0392b")])

sheet("s44f-sh02", "s44f-sh02 v1 · SB060 \"What happened to your face?\" (take 2 of 3)",
      "30 s · Malayalam · push to Antony, turn right to the bench · magistrate (pending), Antony (Mahendran J) · [anxious]",
      "0 s = @s44fsh01last (take 1's last frame) · shown: scene start",
      [("0–4 s", "On Antony; the MAGISTRATE's question heard OFF FRAME."), ("4–4.6 s", "He touches the bruise on his LEFT cheek."),
       ("4.6–11.2 s", "ANTONY answers; push in to his close-up."), ("11.2–15 s", "Turn right: the lawyer writing; RAMACHANDRAN's still face."),
       ("16.5–21.3 s", "MAGISTRATE orders the complaint and the medical."), ("21.3–30 s", "He writes; then a long look at Ramachandran.")],
      [("M: mukhathu enthu patti, antony?   A: stationil vachu adichathaanu. ... nirbandhichu oppideechathaanu saar.", ANT),
       ("M: paraathi rekhappeduthuka. vaidyaparishodhana nadathi report haajaraakkanam.", MAG)],
      [("Camera", CAM, [(0, 4.6, "on Antony"), (4.6, 11.2, "push in"), (11.2, 15, "turn right"), (15, 30, "magistrate MCU")]),
       ("Magistrate", MAG, [(2, 4, "Q off"), (16.5, 21.3, "order"), (21.3, 30, "writes, looks at R")]),
       ("Antony", ANT, [(4.6, 11.2, "the truth")]), ("Ramachandran", RAM, [(12.5, 15, "still")])],
      30,
      ["@s44fsh01last (start) · @antonycustody · @magistrate · @siramachandran · @lawyer · @constables · @s44fsh01start (ref) · 30 s · 21:9",
       "Needs the kept take-1 last frame first · left out: Clara, Rosamma, Jaison (behind the camera)",
       "Watch: Antony's lips closed during the off-frame question · bruise LEFT · QC 100"],
      [(200, 200, "START (front of dock)", CAM), (415, 110, "END below the bench", "#c0392b")])

sheet("s44f-sh03", "s44f-sh03 v1 · SB060 the remand order (take 3 of 3)",
      "15 s · Malayalam · magistrate MCU, pan left to Antony · magistrate (pending) · [anxious]",
      "0 s = @s44fsh02last (take 2's last frame) · shown: scene start",
      [("0–1.2 s", "The magistrate puts down his pen."), ("1.2–8 s", "MAGISTRATE: the remand order, head steady."),
       ("8–9 s", "He closes the file."), ("9–12 s", "Slow pan LEFT to the dock."), ("12–15 s", "Antony: his hands leave the rail; the constable grips his arm.")],
      [("M: raajyadrohakkuttamaayathukondu ippol jaamyam anuvadikkunnilla. judicial custodyil remand cheyyunnu.", MAG)],
      [("Camera", CAM, [(0, 9, "magistrate MCU"), (9, 12, "pan left"), (12, 15, "Antony MCU")]),
       ("Magistrate", MAG, [(1.2, 8, "the order")]), ("Antony", ANT, [(12, 15, "it lands")])],
      15,
      ["@s44fsh02last (start) · @magistrate · @antonycustody · @constables · @s44fsh01start (ref) · 15 s · 21:9",
       "Needs the kept take-2 last frame first · Clara's reaction belongs to SB061",
       "Watch: one speaker, head steady · Antony silent · QC 100"],
      [(415, 110, "START/END below the bench, pans to the dock", CAM)])
