"""Sight lines: what each camera really sees of each person (L146).

Before making a new angle of a set that an approved image already shows, measure that
image into a JSON map, then run this tool for every camera. It draws a top-down map
(positions, which way each body and face points, every camera's view) and writes a table:
for each camera and each person, VISIBLE or HIDDEN (and by what), and whether the camera
sees the face, the back or the side. The image prompt then describes exactly that.

Usage:  python tools/sightlines.py scenes/showreel/storyboards/<name>-sightlines.json
Writes: <out>.png (map) and <out>.md (table).

Units are metres. x = across the boat (+ toward starboard, the right when facing the bow),
y = along the boat (+ toward the bow), z = up. Headings in degrees: 0 = toward the bow,
90 = toward starboard, 180 = aft, 270 = toward port.

JSON:
{
  "title": "...", "out": "scenes/showreel/storyboards/x-sightlines",
  "deck": {"x": [-3, 3], "y": [-13, 13]},
  "boxes": [ {"label": "lashed sacks", "center": [1.7, 3.4, 0.5], "size": [1.4, 1.8, 1.0], "blocks": true} ],
  "people": [
    {"name": "Sasi", "pos": [1.7, 4.9], "pose": "lying", "head": 270, "face": 0},
    {"name": "Aashaan", "pos": [0, -8.2], "pose": "standing", "face": 0}
  ],
  "cameras": [ {"name": "helm", "pos": [0, -9.6, 1.75], "look": [0, 10, 0.8], "fov": 60} ]
}
pose: "standing" (eyes 1.6 m), "sitting" (0.9 m), "lying" (0.3 m). For lying, "head" is the way
the head points from the feet; "face" is the way the face points: a heading, or "up"/"down".
"""
import json, math, sys, io
from PIL import Image, ImageDraw, ImageFont

def font(n, b=False):
    try:
        return ImageFont.truetype('C:/Windows/Fonts/' + ('segoeuib.ttf' if b else 'segoeui.ttf'), n)
    except OSError:
        return ImageFont.load_default()

def hvec(deg):
    r = math.radians(deg)
    return (math.sin(r), math.cos(r))

def ray_hits_box(p0, p1, c, s):
    """Segment p0->p1 crosses the axis-aligned box (centre c, size s)?"""
    t0, t1 = 0.0, 1.0
    for i in range(3):
        lo, hi = c[i] - s[i] / 2, c[i] + s[i] / 2
        d = p1[i] - p0[i]
        if abs(d) < 1e-9:
            if p0[i] < lo or p0[i] > hi:
                return False
        else:
            a, b = (lo - p0[i]) / d, (hi - p0[i]) / d
            if a > b: a, b = b, a
            t0, t1 = max(t0, a), min(t1, b)
            if t0 > t1:
                return False
    return t1 > 0.02 and t0 < 0.98

def points_of(p):
    x, y = p['pos']; pose = p.get('pose', 'standing')
    if pose == 'lying':
        hx, hy = hvec(p.get('head', 0))
        head = [x + hx * 0.75, y + hy * 0.75, 0.3]
        return {'head': head, 'body': [x, y, 0.25], 'feet': [x - hx * 0.75, y - hy * 0.75, 0.2]}
    zh = 1.6 if pose == 'standing' else 0.9
    return {'head': [x, y, zh], 'body': [x, y, zh * 0.6], 'feet': [x, y, 0.2]}

def view_of(cam, p, boxes):
    pts = points_of(p)
    seen = {}
    for k, q in pts.items():
        blocker = None
        for b in boxes:
            if b.get('blocks') and ray_hits_box(cam['pos'], q, b['center'], b['size']):
                blocker = b['label']; break
        seen[k] = blocker
    vis = [k for k, v in seen.items() if v is None]
    # in the field of view?
    lx, ly = cam['look'][0] - cam['pos'][0], cam['look'][1] - cam['pos'][1]
    hx, hy = pts['head'][0] - cam['pos'][0], pts['head'][1] - cam['pos'][1]
    ang = math.degrees(math.atan2(lx * hy - ly * hx, lx * hx + ly * hy))
    infov = abs(ang) <= cam.get('fov', 60) / 2
    # face, back or side
    f = p.get('face', 0)
    to_cam = [cam['pos'][i] - pts['head'][i] for i in range(3)]
    n = math.sqrt(sum(v * v for v in to_cam)) or 1
    to_cam = [v / n for v in to_cam]
    if f == 'up': fv = [0, 0, 1]
    elif f == 'down': fv = [0, 0, -1]
    else:
        a, b = hvec(f); fv = [a, b, 0]
    d = sum(fv[i] * to_cam[i] for i in range(3))
    side = 'FACE' if d > 0.45 else ('BACK of the head' if d < -0.45 else 'SIDE / profile')
    if f == 'up' and d <= 0.45: side = 'top of the head and body from the side'
    if not infov:
        return 'OUT OF FRAME', '', ''
    if not vis:
        blk = sorted(set(v for v in seen.values() if v))
        return 'HIDDEN', 'by ' + ', '.join(blk), ''
    part = 'whole body' if len(vis) == 3 else ('head only' if vis == ['head'] else ', '.join(vis) + ' only')
    return 'VISIBLE', part, side

def main(path):
    S = json.load(io.open(path, encoding='utf-8'))
    W, H = 1500, 1500
    img = Image.new('RGB', (W, H + 60), '#f6f5f1'); d = ImageDraw.Draw(img)
    d.text((20, 15), S.get('title', 'Sight lines'), font=font(30, True), fill='#1d1d1f')
    X0, X1 = S['deck']['x']; Y0, Y1 = S['deck']['y']
    sc = min((W - 300) / (X1 - X0 + 8), (H - 120) / (Y1 - Y0 + 4))
    cx, cy = W / 2, 60 + (Y1 + 2) * sc
    P = lambda x, y: (cx + x * sc, cy - y * sc)
    d.rectangle([*P(X0, Y1), *P(X1, Y0)], fill='#c9b48f', outline='#333', width=3)
    d.text(P(X0 - 2.6, Y1 - 0.5), 'BOW ^', font=font(22, True), fill='#333')
    d.text(P(X0 - 2.9, 0), 'PORT', font=font(20, True), fill='#333')
    d.text(P(X1 + 0.4, 0), 'STBD', font=font(20, True), fill='#333')
    for b in S.get('boxes', []):
        c, s = b['center'], b['size']
        d.rectangle([*P(c[0] - s[0] / 2, c[1] + s[1] / 2), *P(c[0] + s[0] / 2, c[1] - s[1] / 2)],
                    fill='#8b6d47' if b.get('blocks') else '#a89272', outline='#333')
        d.text(P(c[0] + s[0] / 2 + 0.1, c[1]), b['label'], font=font(15), fill='#222')
    cols = ['#d9534f', '#2e9e5b', '#f0ad4e', '#5bc0de', '#e8892b', '#8e44ad', '#2b6cb0']
    for i, p in enumerate(S['people']):
        col = cols[i % len(cols)]; pts = points_of(p)
        if p.get('pose') == 'lying':
            d.line([P(*pts['feet'][:2]), P(*pts['head'][:2])], fill=col, width=int(0.36 * sc))
        hx, hy = P(*pts['head'][:2]); r = 0.17 * sc
        d.ellipse([hx - r, hy - r, hx + r, hy + r], fill='#e8c39e', outline=col, width=3)
        f = p.get('face', 0)
        if f in ('up', 'down'):
            d.text((hx - 8, hy - 10), 'U' if f == 'up' else 'D', font=font(16, True), fill='#000')
        else:
            a, b = hvec(f); ex, ey = P(pts['head'][0] + a * 0.7, pts['head'][1] + b * 0.7)
            d.line([(hx, hy), (ex, ey)], fill='#000', width=4)
            d.ellipse([ex - 5, ey - 5, ex + 5, ey + 5], fill='#000')
        d.text((hx + r + 4, hy - 12), p['name'], font=font(18, True), fill=col)
    for c in S['cameras']:
        px, py = P(*c['pos'][:2])
        lx, ly = c['look'][0] - c['pos'][0], c['look'][1] - c['pos'][1]
        base = math.degrees(math.atan2(lx, ly)); half = c.get('fov', 60) / 2
        for a in (base - half, base + half):
            vx, vy = hvec(a); d.line([(px, py), P(c['pos'][0] + vx * 9, c['pos'][1] + vy * 9)], fill='#2b6cb0', width=2)
        d.polygon([(px, py - 10), (px - 9, py + 8), (px + 9, py + 8)], fill='#2b6cb0')
        d.text((px + 12, py), c['name'], font=font(18, True), fill='#2b6cb0')
    d.text((20, H + 20), 'Black line = where the face points (U = face up). Brown boxes block sight. Blue lines = each camera\'s field of view.', font=font(17), fill='#444')
    out = S['out']; img.save(out + '.png')
    rows = ['# ' + S.get('title', 'Sight lines'), '', 'Made with `tools/sightlines.py` (L146).', '']
    for c in S['cameras']:
        rows += [f"## Camera: {c['name']}", '', '| Person | Seen? | What part | Face, back or side |', '|---|---|---|---|']
        for p in S['people']:
            v, part, side = view_of(c, p, S.get('boxes', []))
            rows.append(f"| {p['name']} | {v} | {part} | {side} |")
        rows.append('')
    io.open(out + '.md', 'w', encoding='utf-8').write('\n'.join(rows))
    print(out + '.png'); print('\n'.join(rows))

if __name__ == '__main__':
    main(sys.argv[1])
