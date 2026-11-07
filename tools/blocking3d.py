"""Blender-style grey-box blocking view for an AAZHI scene: where every person and camera stands.

Usage:  python tools/blocking3d.py scenes/showreel/storyboards/<scene>-blocking.json
Writes: the PNG named in "out". Plain PIL, no other packages.

Units are metres. Axes: x = across the boat (+ right when looking forward), y = along the boat
(+ toward the bow), z = up. The view is a perspective from "eye" looking at "target".

JSON:
{
  "title": "...", "subtitle": "...", "out": "...png",
  "eye": [12, -14, 10], "target": [0, 2, 0], "size": [1600, 1000],
  "objects": [
     {"type": "box", "center": [0,0,0.1], "size": [6,24,0.2], "color": "#9a8a74", "label": "deck"},
     {"type": "cylinder", "center": [0,4,0], "radius": 0.25, "height": 9, "color": "#7a5a3a", "label": "mast"},
     {"type": "figure", "pos": [0,-6,0.2], "color": "#d9534f", "label": "Aashaan", "lying": false},
     {"type": "camera", "pos": [0,-8,1.8], "look": [0,6,1.5], "label": "sh02"}
  ]
}
Figures stand 1.7 m (or lie down with "lying": true). Cameras are drawn as small pyramids pointing where they look.
"""
import json, math, sys
from PIL import Image, ImageDraw, ImageFont

def font(size, bold=False):
    for name in (("segoeuib.ttf" if bold else "segoeui.ttf"), ("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf")):
        for d in ("C:/Windows/Fonts", "/usr/share/fonts/truetype/dejavu"):
            try:
                return ImageFont.truetype(f"{d}/{name}", size)
            except OSError:
                pass
    return ImageFont.load_default()

def sub(a, b): return [a[0]-b[0], a[1]-b[1], a[2]-b[2]]
def dot(a, b): return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
def cross(a, b): return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]
def norm(a):
    l = math.sqrt(dot(a, a)) or 1
    return [a[0]/l, a[1]/l, a[2]/l]

def hex2rgb(h):
    h = h.lstrip('#'); return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

class Cam:
    def __init__(self, eye, target, W, H, fov=40):
        self.eye = eye
        self.f = norm(sub(target, eye))
        self.r = norm(cross(self.f, [0, 0, 1]))
        self.u = cross(self.r, self.f)
        self.W, self.H = W, H
        self.k = (H / 2) / math.tan(math.radians(fov / 2))
    def proj(self, p):
        v = sub(p, self.eye)
        z = dot(v, self.f)
        if z <= 0.1: z = 0.1
        return (self.W / 2 + self.k * dot(v, self.r) / z, self.H / 2 - self.k * dot(v, self.u) / z, z)

LIGHT = norm([0.4, -0.5, 0.8])

def box_faces(c, s, color):
    x, y, z = c; a, b, h = s[0]/2, s[1]/2, s[2]/2
    P = [[x+i*a, y+j*b, z+k*h] for i in (-1, 1) for j in (-1, 1) for k in (-1, 1)]
    F = [((0, 1, 3, 2), [-1, 0, 0]), ((4, 6, 7, 5), [1, 0, 0]), ((0, 4, 5, 1), [0, -1, 0]),
         ((2, 3, 7, 6), [0, 1, 0]), ((0, 2, 6, 4), [0, 0, -1]), ((1, 5, 7, 3), [0, 0, 1])]
    return [([P[i] for i in idx], n, color) for idx, n in F]

def cyl_faces(c, r, h, color, n=14, axis='z'):
    faces = []
    def pt(ang, t):
        if axis == 'z': return [c[0]+r*math.cos(ang), c[1]+r*math.sin(ang), c[2]+t]
        if axis == 'y': return [c[0]+r*math.cos(ang), c[1]+t, c[2]+r*math.sin(ang)]
        return [c[0]+t, c[1]+r*math.cos(ang), c[2]+r*math.sin(ang)]
    for i in range(n):
        a0, a1 = 2*math.pi*i/n, 2*math.pi*(i+1)/n
        q = [pt(a0, 0), pt(a1, 0), pt(a1, h), pt(a0, h)]
        am = (a0+a1)/2
        nn = [math.cos(am), math.sin(am), 0] if axis == 'z' else ([math.cos(am), 0, math.sin(am)] if axis == 'y' else [0, math.cos(am), math.sin(am)])
        faces.append((q, nn, color))
    top = [pt(2*math.pi*i/n, h) for i in range(n)]
    faces.append((top, [0, 0, 1] if axis == 'z' else ([0, 1, 0] if axis == 'y' else [1, 0, 0]), color))
    return faces

def figure_faces(o):
    x, y, z = o['pos']; col = o.get('color', '#d9534f')
    if o.get('lying'):
        return cyl_faces([x, y-0.85, z+0.18], 0.18, 1.45, col, axis='y') + box_faces([x, y+0.75, z+0.15], [0.26, 0.26, 0.26], '#e8c39e')
    return cyl_faces([x, y, z], 0.22, 1.45, col) + box_faces([x, y, z+1.6], [0.26, 0.26, 0.28], '#e8c39e')

def camera_faces(o):
    p = o['pos']; d = norm(sub(o['look'], p)); r = norm(cross(d, [0, 0, 1])); u = cross(r, d)
    tip = p; s = 0.55
    base = [[p[i] + d[i]*0.9 + (r[i]*a + u[i]*b)*s for i in range(3)] for a, b in ((-1, -0.6), (1, -0.6), (1, 0.6), (-1, 0.6))]
    col = o.get('color', '#2b6cb0')
    return [([tip, base[0], base[1]], [0, 0, 1], col), ([tip, base[1], base[2]], [0, 0, 1], col),
            ([tip, base[2], base[3]], [0, 0, 1], col), ([tip, base[3], base[0]], [0, 0, 1], col)]

def main(path):
    S = json.load(open(path, encoding='utf-8'))
    W, H = S.get('size', [1600, 1000])
    cam = Cam(S['eye'], S['target'], W, H - 120, S.get('fov', 40))
    img = Image.new('RGB', (W, H), '#2c3440')
    d = ImageDraw.Draw(img)
    # sky/sea gradient
    for yy in range(120, H):
        t = (yy - 120) / (H - 120)
        d.line([(0, yy), (W, yy)], fill=(int(40+25*t), int(52+30*t), int(70+35*t)))
    faces, labels = [], []
    for o in S['objects']:
        t = o['type']
        if t == 'box': fs = box_faces(o['center'], o['size'], o.get('color', '#9a9a9a'))
        elif t == 'cylinder': fs = cyl_faces(o['center'], o['radius'], o['height'], o.get('color', '#9a9a9a'))
        elif t == 'figure': fs = figure_faces(o)
        elif t == 'camera': fs = camera_faces(o)
        else: continue
        faces += fs
        if o.get('label'):
            anchor = o.get('pos') or o.get('center')
            lift = 2.1 if t == 'figure' and not o.get('lying') else (0.9 if t == 'figure' else (o.get('height', 0) + 0.3 if t == 'cylinder' else 0.6))
            labels.append(([anchor[0], anchor[1], anchor[2] + lift], o['label'], t))
    drawn = []
    for pts, n, col in faces:
        P = [cam.proj(p) for p in pts]
        depth = sum(p[2] for p in P) / len(P)
        shade = 0.45 + 0.55 * max(0, dot(norm(n), LIGHT))
        rgb = hex2rgb(col)
        drawn.append((depth, [(p[0], p[1] + 120) for p in P], tuple(int(c*shade) for c in rgb)))
    for depth, poly, c in sorted(drawn, key=lambda t: -t[0]):
        d.polygon(poly, fill=c, outline=(30, 30, 30))
    for pos, text, t in labels:
        x, y, _ = cam.proj(pos)
        f = font(22, True)
        w = d.textlength(text, font=f)
        col = '#9ecbff' if t == 'camera' else '#ffffff'
        d.rectangle([x - w/2 - 6, y + 120 - 16, x + w/2 + 6, y + 120 + 14], fill=(0, 0, 0))
        d.text((x - w/2, y + 120 - 15), text, font=f, fill=col)
    d.rectangle([0, 0, W, 118], fill='#faf8f2')
    d.text((24, 18), S.get('title', ''), font=font(36, True), fill='#1a1a1a')
    d.text((24, 70), S.get('subtitle', ''), font=font(22), fill='#555555')
    img.save(S['out'])
    print(S['out'], img.size)

if __name__ == '__main__':
    main(sys.argv[1])
