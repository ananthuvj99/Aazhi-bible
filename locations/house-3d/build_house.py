# Antony's house in Blender — low-poly but detailed, built from the approved references:
#   locations/house-exterior/card.md, elevations.webp (@housefullview), environment.webp (@houseout), map.png (@housemap)
#   locations/house-exterior/house-layout-block.txt
#   locations/antony-room/card.md and antonyroom.webp (@antonyroom)   locations/kitchen/card.md, map.png (@kitchenmapped)
#   locations/hall/card.md (@hallclean)
# Rosamma's room is a shell only (door and windows), as asked.
#
# Axes (metres): x = EAST (+) / west (-), y = NORTH (+, back) / south (-, front), z = up.
# The house faces SOUTH. Ground (yard) at z = 0; plinth and all floors at z = FL.
# Run:  /Applications/Blender.app/Contents/MacOS/Blender -b -P build_house.py -- <out_dir> [preview]
import bpy, math, sys, os
from mathutils import Vector

argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
OUT = os.path.abspath(argv[0] if argv else os.path.dirname(__file__))
PREVIEW = len(argv) > 1 and argv[1] == "preview"
os.makedirs(OUT, exist_ok=True)

FL = 0.45          # plinth / floor height
WH = 3.0           # wall height to the eaves (above floor)
T = 0.2            # wall thickness
BAND = 0.9         # deep blue base band height

# Plan (inside faces of the outer walls)
X0, X1 = -4.5, 4.5           # main block, west to east
Y0, Y1 = 0.0, 5.0            # main block, front (south) wall to the back of the bedrooms
PX0, PX1 = -1.0, 1.0         # central passage
KX0, KX1 = -3.9, 3.9         # kitchen (a little narrower than the main block, as on the cutaway)
KY1 = 8.6                    # kitchen back (north) wall
VY0 = -2.6                   # veranda front edge
WX = -5.7                    # the WEST compound wall, close beside the house (c2 plate)
EWX = 5.9                    # the EAST compound wall, about 1.2 m beyond the veranda (c1 plate: the compound is ~house width + 1 m a side)
FWY = -10.0                  # the FRONT compound wall, about 7.5 m in front of the veranda edge (measured on the c1 plate)
def cliff_x(y):
    """The headland's cliff edge east of the house: close behind the house, cutting away wider toward the front."""
    return 7.2 if y >= 10.0 else 7.2 + (10.0 - y) * 0.27
LX1, LX0 = WX - 0.2, WX - 3.4   # the lane: about 3 m wide, just outside that wall
LANE_GRADE = 0.025           # the lane falls gently, about 2.5 cm per metre, toward the back (wall chest-high from the lane, c2 plate)

bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene

# ---------------------------------------------------------------- materials
def lin(hexstr):
    """sRGB hex from the reference sheets -> linear RGB for Blender."""
    h = hexstr.lstrip("#")
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    return tuple(v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4 for v in c)

def mat(name, hexstr, rough=0.85, emit=0.0, pattern=None, hex2=None, scale=8.0):
    """pattern: None, 'checker' (two colours) or 'brick' (blocks with darker mortar)."""
    rgb = lin(hexstr)
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    b = nt.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*rgb, 1)
    b.inputs["Roughness"].default_value = rough
    if pattern:
        coord = nt.nodes.new("ShaderNodeTexCoord")
        if pattern == "checker":
            t = nt.nodes.new("ShaderNodeTexChecker")
            t.inputs["Color1"].default_value = (*rgb, 1)
            t.inputs["Color2"].default_value = (*lin(hex2), 1)
        else:
            t = nt.nodes.new("ShaderNodeTexBrick")
            t.inputs["Color1"].default_value = (*rgb, 1)
            t.inputs["Color2"].default_value = (*lin(hex2 or hexstr), 1)
            t.inputs["Mortar"].default_value = tuple(v * 0.45 for v in rgb) + (1,)
            t.inputs["Mortar Size"].default_value = 0.03
        t.inputs["Scale"].default_value = scale
        nt.links.new(coord.outputs["Object"], t.inputs["Vector"])
        nt.links.new(t.outputs["Color"], b.inputs["Base Color"])
    if emit:
        b.inputs["Emission Color"].default_value = (*rgb, 1)
        b.inputs["Emission Strength"].default_value = emit
    m.diffuse_color = (*rgb, 1)
    return m

# Colours measured from the reference sheets (antonyroom.webp, kitchen map.png, elevations.webp, environment.webp)
M = dict(
    wall=mat("pale sky-blue wall", "#bccfe6"),
    band=mat("deep blue base band", "#0c5aa8"),
    trim=mat("white trim", "#eef1f2"),
    floor=mat("red-oxide floor", "#a24a3c", 0.45),
    plinth=mat("blue plinth", "#0a72c4"),
    door=mat("blue door", "#2f63a5"),
    brown=mat("brown wood", "#6b4a2c"),
    rafter=mat("dark rafter", "#644733"),
    tile=mat("terracotta tiles", "#9a4a32", pattern="brick", hex2="#8a3f2a", scale=14),
    pillar=mat("white pillar", "#e8eef2"),
    bars=mat("blue iron bars", "#2f63a5", 0.4),
    shutter=mat("white shutter", "#e3e3df"),
    glass=mat("bright outside", "#f2efe4", 0.5, 1.5),
    earth=mat("packed red earth", "#aa6b45"),
    sand=mat("pale sand", "#d8c4a4"),
    lane=mat("lane sand", "#c9a882"),
    pole=mat("electric pole", "#6a5a48"),
    laterite=mat("laterite blocks", "#7a3f28", pattern="brick", hex2="#8c4a30", scale=3),
    cot=mat("cot wood", "#9c7448"),
    bluecheck=mat("blue checked sheet", "#7f90b2", pattern="checker", hex2="#c5cfe0", scale=40),
    rosesheet=mat("rose-pink cover sheet", "#d99aa6"),
    trunk=mat("grey metal trunk", "#8a8a86", 0.5),
    steel=mat("steel", "#c8ccd0", 0.3),
    navy=mat("navy cloth", "#17152c"),
    white=mat("white cloth", "#ecebe6"),
    clockcase=mat("clock case", "#3a2418"),
    dial=mat("cream dial", "#e9dfc0"),
    mud=mat("mud stove", "#8b6a4c"),
    soot=mat("soot", "#2a221c"),
    clay=mat("clay pot", "#8a3f22"),
    fire=mat("fire", "#ff8a2a", 0.5, 2.5),
    stone=mat("grinding stone", "#7a6b5c"),
    coir=mat("coir", "#a07446"),
    fish=mat("dried fish", "#6b3a22"),
    picture=mat("holy picture", "#b04a3a"),
    palmtrunk=mat("palm trunk", "#7a6a50"),
    frond=mat("palm frond", "#3e6a2a"),
    sea=mat("sea", "#5a9aa6", 0.2),
    cliff=mat("laterite cliff", "#6a3420"),
    green=mat("shrub", "#3d5f2a"),
    platform=mat("aduppu platform", "#8c3f2c"),
)

COLS = {}
def col(name):
    if name not in COLS:
        c = bpy.data.collections.new(name)
        sc.collection.children.link(c)
        COLS[name] = c
    return COLS[name]

CUR = ["House"]
def put(o):
    for c in o.users_collection:
        c.objects.unlink(o)
    col(CUR[0]).objects.link(o)
    return o

def box(name, x0, y0, z0, x1, y1, z1, m):
    bpy.ops.mesh.primitive_cube_add(size=1, location=((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2))
    o = bpy.context.object
    o.name = name
    o.scale = (abs(x1 - x0), abs(y1 - y0), abs(z1 - z0))
    o.data.materials.append(m)
    return put(o)

def boxc(name, c, s, m, rz=0.0):
    bpy.ops.mesh.primitive_cube_add(size=1, location=c, rotation=(0, 0, rz))
    o = bpy.context.object
    o.name = name
    o.scale = s
    o.data.materials.append(m)
    return put(o)

def cyl(name, c, r, h, m, v=12, rot=(0, 0, 0)):
    bpy.ops.mesh.primitive_cylinder_add(vertices=v, radius=r, depth=h, location=c, rotation=rot)
    o = bpy.context.object
    o.name = name
    o.data.materials.append(m)
    return put(o)

def sph(name, c, r, m, scale=(1, 1, 1)):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=14, ring_count=8, radius=r, location=c)
    o = bpy.context.object
    o.name = name
    o.scale = scale
    o.data.materials.append(m)
    return put(o)

def beam(name, a, b, w, h, m):
    a, b = Vector(a), Vector(b)
    d = b - a
    bpy.ops.mesh.primitive_cube_add(size=1, location=(a + b) / 2)
    o = bpy.context.object
    o.name = name
    o.scale = (w, h, d.length)
    o.rotation_euler = d.to_track_quat("Z", "Y").to_euler()
    o.data.materials.append(m)
    return put(o)

# ---------------------------------------------------------------- walls with openings
def wall(name, axis, fixed, a0, a1, openings=(), band_in=True, band_out=True, inner_sign=1):
    """Axis-aligned wall. axis 'x' = runs along x at y = fixed; 'y' = runs along y at x = fixed.
    openings: (start, end, sill, head) along the wall, heights above the floor.
    inner_sign: which side gets the inside band (+1 = toward +y / +x)."""
    z0, z1 = FL, FL + WH
    cuts = sorted(openings)
    segs, cur = [], a0
    for s, e, sill, head in cuts:
        if s > cur:
            segs.append((cur, s, 0, WH))
        if sill > 0:
            segs.append((s, e, 0, sill))
        segs.append((s, e, head, WH))
        cur = e
    if cur < a1:
        segs.append((cur, a1, 0, WH))
    for i, (s, e, b, t) in enumerate(segs):
        if t - b <= 0.001:
            continue
        if axis == "x":
            box(f"{name}_{i}", s, fixed - T / 2, z0 + b, e, fixed + T / 2, z0 + t, M["wall"])
        else:
            box(f"{name}_{i}", fixed - T / 2, s, z0 + b, fixed + T / 2, e, z0 + t, M["wall"])
        # base band, a thin skin on each face, only where the segment reaches the floor
        if b == 0:
            bt = min(BAND, t)
            for side, on in ((inner_sign, band_in), (-inner_sign, band_out)):
                if not on:
                    continue
                off = side * (T / 2 + 0.005)
                if axis == "x":
                    box(f"{name}_{i}_band{side}", s, fixed + off - 0.004, z0, e, fixed + off + 0.004, z0 + bt, M["band"])
                else:
                    box(f"{name}_{i}_band{side}", fixed + off - 0.004, s, z0, fixed + off + 0.004, e, z0 + bt, M["band"])
    # white trim round each opening (outer face)
    for k, (s, e, sill, head) in enumerate(cuts):
        for part in ((s - 0.06, s, sill, head), (e, e + 0.06, sill, head), (s - 0.06, e + 0.06, head, head + 0.06)):
            ps, pe, pb, pt = part
            if axis == "x":
                box(f"{name}_trim{k}", ps, fixed - T / 2 - 0.02, FL + pb, pe, fixed + T / 2 + 0.02, FL + pt, M["trim"])
            else:
                box(f"{name}_trim{k}", fixed - T / 2 - 0.02, ps, FL + pb, fixed + T / 2 + 0.02, pe, FL + pt, M["trim"])

def window(name, axis, fixed, s, e, sill, head, shutters=True, out_sign=-1):
    """Blue bars across the opening and white shutters folded open on the outside face."""
    n = 6
    for k in range(n):
        a = s + (k + 0.5) * (e - s) / n
        if axis == "x":
            cyl(f"{name}_bar{k}", (a, fixed, FL + (sill + head) / 2), 0.015, head - sill, M["bars"])
        else:
            cyl(f"{name}_bar{k}", (fixed, a, FL + (sill + head) / 2), 0.015, head - sill, M["bars"])
    for z in (sill + 0.02, head - 0.02):
        if axis == "x":
            box(f"{name}_rail", s, fixed - 0.03, FL + z - 0.02, e, fixed + 0.03, FL + z + 0.02, M["bars"])
        else:
            box(f"{name}_rail", fixed - 0.03, s, FL + z - 0.02, fixed + 0.03, e, FL + z + 0.02, M["bars"])
    if shutters:
        w = (e - s) / 2
        o = out_sign * (T / 2 + 0.03)
        for k, (a0, a1) in enumerate(((s - w - 0.05, s - 0.05), (e + 0.05, e + w + 0.05))):
            if axis == "x":
                box(f"{name}_shutter{k}", a0, fixed + o - 0.02, FL + sill, a1, fixed + o + 0.02, FL + head, M["shutter"])
            else:
                box(f"{name}_shutter{k}", fixed + o - 0.02, a0, FL + sill, fixed + o + 0.02, a1, FL + head, M["shutter"])

def door_leaf(name, hinge, length, angle_deg, h, m, thick=0.05):
    """A door leaf hinged at `hinge` (x, y), `length` wide, rotated angle_deg about z (0 = along +x)."""
    a = math.radians(angle_deg)
    c = (hinge[0] + math.cos(a) * length / 2, hinge[1] + math.sin(a) * length / 2, FL + h / 2)
    return boxc(name, c, (length, thick, h), m, rz=a)

# ================================================================ ground, plinth, floors
CUR[0] = "Ground"
box("Yard_red_earth", WX, FWY, -0.05, EWX, 12.0, 0.0, M["earth"])
box("Sand_front", -40, -40, -0.06, EWX - 1.0, FWY, -0.01, M["sand"])
# ---- the lane along the WEST side (@houseexteriorc2plate, @houseexteriorc1plate): sandy, just outside the close
# west compound wall, sloping DOWN toward the back (north) and on past the neighbours' cottages; level with the front
# sand at the front corner. A red earth bank rises on its far (west) side with palms and a wooden electric pole.
def mesh(name, verts, faces, m):
    me = bpy.data.meshes.new(name)
    me.from_pydata(verts, [], faces)
    me.update()
    o = bpy.data.objects.new(name, me)
    col(CUR[0]).objects.link(o)
    o.data.materials.append(m)
    return o

def lane_z(y):
    """Gentle beside the house (c2 plate), then falling faster past the back of the compound toward the village (c1 plate)."""
    if y <= FWY:
        return 0.0
    if y <= 11.0:
        return -(y - FWY) * LANE_GRADE
    return -(11.0 - FWY) * LANE_GRADE - (y - 11.0) * 0.09

# west of the lane: a low bank (c2 plate), then the ground falls away to the village below the yard (c1 plate)
BANK = [(0.0, 0.0), (-2.0, 0.8), (-6.0, -1.2), (-12.0, -2.4), (-40.0, -3.0)]   # (x offset from the lane edge, height above the lane)
def ground_z(x, y):
    if x >= LX0:
        return lane_z(y) if x <= LX1 else 0.0
    d = x - LX0
    for (x0, z0), (x1, z1) in zip(BANK, BANK[1:]):
        if x1 <= d <= x0:
            return lane_z(y) + z0 + (z1 - z0) * (d - x0) / (x1 - x0)
    return lane_z(y) + BANK[-1][1]

ys = [FWY + k * 2.0 for k in range(22)]                      # from the front wall to y 32
lv, lf = [], []
for i, y in enumerate(ys):
    z = lane_z(y)
    lv += [(LX0, y, z - 0.01), (LX1, y, z - 0.01)]
    if i:
        a = 2 * (i - 1)
        lf.append((a, a + 1, a + 3, a + 2))
mesh("Lane_sand", lv, lf, M["lane"])
# the bank and the falling ground beyond it: bare red earth on the slope, green on the village side
for part, (pa, pb), m_ in (("slope", (0, 2), M["earth"]), ("village", (1, 5), M["green"])):
    pts = BANK[pa:pb]
    bv, bf = [], []
    n = len(pts)
    for i, y in enumerate(ys):
        z = lane_z(y)
        bv += [(LX0 + dx, y, z + dz - 0.01) for dx, dz in pts]
        if i:
            a = n * (i - 1)
            bf += [(a + j, a + n + j, a + n + j + 1, a + j + 1) for j in range(n - 1)]
    mesh(f"Lane_bank_{part}", bv, bf, m_)
# under the close west compound wall: its foot follows the lane down (the wall face grows as the lane falls)
box("Lane_kerb_under_wall", LX1, FWY, -3.4, WX - 0.15, 11.3, 0.0, M["laterite"])
# past the back of the compound the headland edge beside the falling lane is a red earth slope
lv2, lf2 = [], []
for i, y in enumerate([y for y in ys if y >= 11.0]):
    lv2 += [(LX1, y, lane_z(y)), (WX + 0.4, y, 0.0)]
    if i:
        a = 2 * (i - 1)
        lf2.append((a, a + 2, a + 3, a + 1))
mesh("Lane_east_slope", lv2, lf2, M["earth"])
# ---- the headland east of the house and the cliff (@houseout, c1 plate): red laterite ground from the east wall
# (and in front of the compound on the right) out to the cliff edge, which cuts back diagonally; the cliff drops
# about 10 m to the beach; boats on the sand, the white church on the shore, green hills beyond.
CY = [-40.0 + k * 4.0 for k in range(21)]                       # y -40 .. 40
hv, hf, cv, cf = [], [], [], []
for i, y in enumerate(CY):
    ex = cliff_x(y)
    x_in = EWX if y >= FWY else EWX - 1.0
    hv += [(x_in, y, -0.02), (ex, y, -0.35)]
    cv += [(ex, y, -0.35), (ex + 1.2, y, -4.0), (ex + 2.6, y, -10.0)]
    if i:
        a, b = 2 * (i - 1), 3 * (i - 1)
        hf.append((a, a + 2, a + 3, a + 1))
        cf += [(b, b + 3, b + 4, b + 1), (b + 1, b + 4, b + 5, b + 2)]
mesh("Headland_red_laterite", hv, hf, M["earth"])
mesh("Cliff_face", cv, cf, M["cliff"])
box("Headland_north", WX + 0.3, 11.0, -0.06, 7.2, 40, -0.01, M["earth"])
bv2, bf2 = [], []
for i, y in enumerate(CY):
    ex = cliff_x(y) + 2.6
    bv2 += [(ex, y, -10.0), (ex + 22.0, y, -10.2)]
    if i:
        a = 2 * (i - 1)
        bf2.append((a, a + 2, a + 3, a + 1))
mesh("Beach_sand", bv2, bf2, M["sand"])
# the bay's beach curving away north-east toward the church, where the boats are pulled up
bpy.ops.mesh.primitive_cylinder_add(vertices=40, radius=1, depth=0.2, location=(58, 160, -10.05))
o = bpy.context.object; o.name = "Bay_beach_curve"; o.scale = (28, 110, 1); o.data.materials.append(M["sand"]); put(o)
for k in range(10):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=12, ring_count=6, radius=1, location=(38 + k * 2.2, 70 + k * 14, -9.8), rotation=(0, 0, math.radians(30 + k * 5)))
    o = bpy.context.object; o.name = f"Bay_boat{k}"; o.scale = (3.5, 0.7, 0.35); o.data.materials.append(M["brown"]); put(o)
for k in range(9):                                                   # wooden fishing boats pulled up on the beach
    y = -14 + k * 5.5
    bx = cliff_x(y) + 9 + (k % 3) * 2.5
    bpy.ops.mesh.primitive_uv_sphere_add(segments=12, ring_count=6, radius=1, location=(bx, y, -9.75), rotation=(0, 0, math.radians(70 + k * 4)))
    o = bpy.context.object; o.name = f"Boat{k}"; o.scale = (3.5, 0.7, 0.35); o.data.materials.append(M["brown"]); put(o)
# the white church with a tall spire, on the shore beyond the headland to the north-east
box("Church_nave", 62, 222, -10, 72, 240, -1, M["trim"])          # far along the shore, about 250 m off
box("Church_tower", 65, 218, -10, 69, 222, 12, M["trim"])
bpy.ops.mesh.primitive_cone_add(vertices=8, radius1=2.4, depth=10, location=(67, 220, 17))
o = bpy.context.object; o.name = "Church_spire"; o.data.materials.append(M["trim"]); put(o)
# green hills beyond the bay and behind the village
# only beyond the bay, far to the north-east and east (the village side, left, is a palm grove)
for k, (x, y, r, h) in enumerate(((210, 330, 110, 34), (320, 200, 90, 28), (120, 420, 120, 30))):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=16, ring_count=8, radius=1, location=(x, y, -10))
    o = bpy.context.object; o.name = f"Hill{k}"; o.scale = (r, r * 0.7, h); o.data.materials.append(M["frond"]); put(o)
box("Sea", 10, -300, -10.6, 400, 300, -10.5, M["sea"])

CUR[0] = "House"
# plinth under the whole house and veranda (blue), red-oxide floors on top
box("Plinth_main", X0 - T, VY0, 0, X1 + T, Y1, FL - 0.02, M["plinth"])
box("Plinth_kitchen", KX0 - T, Y1, 0, KX1 + T, KY1 + T / 2, FL - 0.02, M["plinth"])
box("Floor_veranda", X0 - T, VY0, FL - 0.03, X1 + T, 0, FL, M["floor"])
box("Floor_edge", X0 - T, VY0 - 0.04, FL - 0.08, X1 + T, VY0 + 0.06, FL + 0.01, M["floor"])
box("Floor_main", X0, Y0, FL - 0.03, X1, Y1, FL, M["floor"])
box("Floor_kitchen", KX0, Y1, FL - 0.03, KX1, KY1, FL, M["floor"])
# central red-oxide entry steps
for k in range(3):
    h = FL * (k + 1) / 3
    box(f"Step{k}", -1.1, VY0 - 0.35 * (3 - k), 0, 1.1, VY0 - 0.35 * (2 - k), h, M["floor"])

# ---------------------------------------------------------------- outer walls of the main block
D_FRONT = (-0.6, 0.6, 0, 2.1)                 # front double door (passage)
W_ANT_F = (-3.35, -2.15, 0.9, 2.2)            # Antony's front window
W_AMM_F = (2.15, 3.35, 0.9, 2.2)              # Rosamma's front window
wall("Wall_front", "x", Y0, X0 - T / 2, X1 + T / 2, [D_FRONT, W_ANT_F, W_AMM_F], inner_sign=1)
window("Win_ant_front", "x", Y0, W_ANT_F[0], W_ANT_F[1], W_ANT_F[2], W_ANT_F[3], out_sign=-1)
window("Win_amm_front", "x", Y0, W_AMM_F[0], W_AMM_F[1], W_AMM_F[2], W_AMM_F[3], out_sign=-1)
W_ANT_W = (2.5, 3.6, 0.9, 2.2)                # Antony's west window, above the cot's head end (north end)
wall("Wall_west", "y", X0, Y0, Y1, [W_ANT_W], inner_sign=1)
window("Win_ant_west", "y", X0, W_ANT_W[0], W_ANT_W[1], W_ANT_W[2], W_ANT_W[3], out_sign=-1)
W_AMM_E = (2.4, 3.5, 0.9, 2.2)
wall("Wall_east", "y", X1, Y0, Y1, [W_AMM_E], inner_sign=-1)
window("Win_amm_east", "y", X1, W_AMM_E[0], W_AMM_E[1], W_AMM_E[2], W_AMM_E[3], out_sign=1)
# back of the bedrooms (shared with the kitchen): the kitchen double doors at the end of the passage
D_KIT = (-0.6, 0.6, 0, 2.1)
wall("Wall_mid_back", "x", Y1, X0 - T / 2, X1 + T / 2, [D_KIT], inner_sign=-1)
# passage walls with the two bedroom doors near the front end
D_ANT = (0.5, 1.4, 0, 2.1)
D_AMM = (0.5, 1.4, 0, 2.1)
wall("Wall_passage_west", "y", PX0, Y0, Y1, [D_ANT], inner_sign=1)
wall("Wall_passage_east", "y", PX1, Y0, Y1, [D_AMM], inner_sign=-1)

# doors: blue leaves standing open
door_leaf("Door_front_L", (-0.6, Y0 + T / 2 + 0.03), 0.6, 172, 2.1, M["door"])   # wide open, back against the front wall
door_leaf("Door_front_R", (0.6, Y0 + T / 2 + 0.03), 0.6, 8, 2.1, M["door"])
door_leaf("Door_ant", (PX0 - T / 2 - 0.04, 1.4), 0.9, 95, 2.1, M["door"])   # opens into Antony's room, back against the wall
door_leaf("Door_amm", (PX1 + T / 2 + 0.04, 1.4), 0.9, 85, 2.1, M["door"])   # opens into Rosamma's room
door_leaf("Door_kit_L", (-0.6, Y1 - T / 2 - 0.03), 0.6, -80, 2.1, M["door"])   # swing back into the passage
door_leaf("Door_kit_R", (0.6, Y1 - T / 2 - 0.03), 0.6, -100, 2.1, M["door"])

# ---------------------------------------------------------------- kitchen walls (doors west and east, window north)
D_KW = (6.2, 7.1, 0, 2.1)
D_KE = (6.2, 7.1, 0, 2.1)
W_KN = (0.2, 1.8, 0.95, 2.25)
# small barred side windows toward the rear, no shutters (side elevations of @housefullview), set high so the
# kitchen sheet's doors, vessel shelf (west) and dried fish (east) stay where they are
W_KSW = (7.65, 8.25, 1.75, 2.35)
W_KSE = (7.65, 8.25, 1.75, 2.35)
wall("Wall_kit_west", "y", KX0, Y1, KY1 + T / 2, [D_KW, W_KSW], inner_sign=1)
wall("Wall_kit_east", "y", KX1, Y1, KY1 + T / 2, [D_KE, W_KSE], inner_sign=-1)
window("Win_kit_side_west", "y", KX0, W_KSW[0], W_KSW[1], W_KSW[2], W_KSW[3], shutters=False)
window("Win_kit_side_east", "y", KX1, W_KSE[0], W_KSE[1], W_KSE[2], W_KSE[3], shutters=False)
wall("Wall_kit_north", "x", KY1, KX0 - T / 2, KX1 + T / 2, [W_KN], inner_sign=-1)
window("Win_kit_north", "x", KY1, W_KN[0], W_KN[1], W_KN[2], W_KN[3], out_sign=-1)   # shutters open inward, as on the sheet
door_leaf("Door_kit_west", (KX0 + T / 2 + 0.04, 6.2), 0.9, -90, 2.1, M["door"])   # open, flat against the wall
door_leaf("Door_kit_east", (KX1 - T / 2 - 0.04, 6.2), 0.9, -90, 2.1, M["door"])

# ---------------------------------------------------------------- veranda: four turned white pillars, cross, picture, furniture
for i, x in enumerate((-4.4, -1.45, 1.45, 4.4)):
    y = VY0 + 0.3
    box(f"Pillar{i}_base", x - 0.22, y - 0.22, FL, x + 0.22, y + 0.22, FL + 0.35, M["pillar"])
    cyl(f"Pillar{i}_shaft", (x, y, FL + 0.35 + 1.1), 0.13, 2.2, M["pillar"], v=16)
    sph(f"Pillar{i}_bulge", (x, y, FL + 1.0), 0.17, M["pillar"], scale=(1, 1, 1.8))
    sph(f"Pillar{i}_bulge2", (x, y, FL + 2.2), 0.15, M["pillar"], scale=(1, 1, 1.6))
    box(f"Pillar{i}_cap", x - 0.2, y - 0.2, FL + WH - 0.25, x + 0.2, y + 0.2, FL + WH, M["pillar"])
box("Veranda_beam", X0 - T, VY0 + 0.1, FL + WH - 0.05, X1 + T, VY0 + 0.5, FL + WH + 0.2, M["trim"])
# wooden cross above the door, small framed holy picture to the right of the door
box("Cross_v", -0.04, Y0 - T / 2 - 0.04, FL + 2.3, 0.04, Y0 - T / 2, FL + 2.75, M["brown"])
box("Cross_h", -0.14, Y0 - T / 2 - 0.04, FL + 2.55, 0.14, Y0 - T / 2, FL + 2.62, M["brown"])
box("Holy_picture", 0.85, Y0 - T / 2 - 0.03, FL + 1.5, 1.15, Y0 - T / 2, FL + 1.9, M["picture"])
# easy chair (west of the door) and long bench (east)
ex, ey = -2.4, -1.0
box("Easychair_seat", ex - 0.3, ey - 0.35, FL + 0.35, ex + 0.3, ey + 0.35, FL + 0.4, M["brown"])
beam("Easychair_back", (ex, ey + 0.35, FL + 0.38), (ex, ey + 0.75, FL + 1.05), 0.6, 0.04, M["brown"])
for dx in (-0.3, 0.3):
    beam(f"Easychair_arm{dx}", (ex + dx, ey - 0.45, FL + 0.6), (ex + dx, ey + 0.5, FL + 0.6), 0.06, 0.06, M["brown"])
    for dy in (-0.35, 0.35):
        box(f"Easychair_leg{dx}{dy}", ex + dx - 0.03, ey + dy - 0.03, FL, ex + dx + 0.03, ey + dy + 0.03, FL + 0.6, M["brown"])
box("Bench_top", 1.9, -0.75, FL + 0.42, 3.6, -0.4, FL + 0.47, M["brown"])
for bx in (2.0, 3.5):
    box(f"Bench_leg{bx}", bx - 0.04, -0.72, FL, bx + 0.04, -0.43, FL + 0.42, M["brown"])

# ================================================================ Antony's room (west half): x -4.5 .. -1.0, y 0 .. 5
CUR[0] = "Antony_room"
# cot along the west wall under the side window, head end at the NORTH, made up with the blue checked sheet
cx0, cx1, cy0, cy1 = X0 + 0.1, X0 + 1.0, 1.5, 3.45      # in the middle of the west wall, seen through the door (C4)
for (lx, ly) in ((cx0 + 0.04, cy0 + 0.04), (cx1 - 0.04, cy0 + 0.04), (cx0 + 0.04, cy1 - 0.04), (cx1 - 0.04, cy1 - 0.04)):
    box("Cot_leg", lx - 0.04, ly - 0.04, FL, lx + 0.04, ly + 0.04, FL + 0.5, M["cot"])
box("Cot_frame", cx0, cy0, FL + 0.38, cx1, cy1, FL + 0.45, M["cot"])
box("Cot_sheet_bluecheck", cx0 + 0.03, cy0 + 0.03, FL + 0.45, cx1 - 0.03, cy1 - 0.03, FL + 0.47, M["bluecheck"])
boxc("Cot_pillow", ((cx0 + cx1) / 2, cy1 - 0.3, FL + 0.53), (0.6, 0.35, 0.12), M["bluecheck"])
boxc("Cot_rosepink_coversheet", ((cx0 + cx1) / 2, cy0 + 0.45, FL + 0.5), (0.85, 0.7, 0.05), M["rosesheet"])
# north (back) wall: shelf with books and a steel tumbler; hooks in the NW corner with a navy and a white cloth
sy = Y1 - T / 2
box("Shelf", -3.6, sy - 0.25, FL + 1.55, -2.4, sy, FL + 1.59, M["brown"])
for k in range(7):
    box(f"Book{k}", -3.55 + k * 0.06, sy - 0.2, FL + 1.59, -3.5 + k * 0.06, sy - 0.04, FL + 1.82 - (k % 3) * 0.03, M["picture" if k % 2 else "navy"])
for bx in (-3.5, -2.5):
    beam(f"Shelf_bracket{bx}", (bx, sy - 0.02, FL + 1.3), (bx, sy - 0.22, FL + 1.55), 0.04, 0.04, M["brown"])
cyl("Tumbler", (-2.75, sy - 0.12, FL + 1.66), 0.04, 0.13, M["steel"])
box("Carved_figure", -2.55, sy - 0.14, FL + 1.59, -2.47, sy - 0.08, FL + 1.75, M["brown"])
box("Hook_rail", X0 + 0.15, sy - 0.05, FL + 1.85, X0 + 0.65, sy, FL + 1.9, M["brown"])
box("Cloth_navy", X0 + 0.2, sy - 0.08, FL + 1.05, X0 + 0.38, sy - 0.04, FL + 1.85, M["navy"])
box("Cloth_white", X0 + 0.42, sy - 0.08, FL + 1.15, X0 + 0.6, sy - 0.04, FL + 1.85, M["white"])
# grey metal trunk on the floor against the back wall, east side
box("Trunk", -2.1, sy - 0.5, FL, -1.2, sy - 0.02, FL + 0.45, M["trunk"])
# the one wall clock: front (south) wall, beside the front window, near the outer (west) corner, above the cot's foot
cyl("Clock_case", (-3.9, Y0 + T / 2 + 0.04, FL + 2.35), 0.17, 0.07, M["clockcase"], v=24, rot=(math.radians(90), 0, 0))
cyl("Clock_dial", (-3.9, Y0 + T / 2 + 0.08, FL + 2.35), 0.14, 0.01, M["dial"], v=24, rot=(math.radians(90), 0, 0))
box("Clock_block", -3.98, Y0 + T / 2 + 0.01, FL + 2.08, -3.82, Y0 + T / 2 + 0.08, FL + 2.2, M["clockcase"])
# hands at 9:20: hour hand a third of the way from 9 to 10, minute hand on 4
for nm, ang, ln in (("Clock_hour_0920", 280, 0.07), ("Clock_minute_0920", 120, 0.11)):
    a = math.radians(ang)
    beam(nm, (-3.9, Y0 + T / 2 + 0.09, FL + 2.35), (-3.9 + math.sin(a) * ln * -1, Y0 + T / 2 + 0.09, FL + 2.35 + math.cos(a) * ln), 0.012, 0.005, M["soot"])

# ================================================================ passage
CUR[0] = "Passage"
box("Coir_mat", -0.45, 2.0, FL, 0.45, 3.2, FL + 0.015, M["coir"])
cyl("Round_stool", (0.6, 2.2, FL + 0.18), 0.17, 0.36, M["brown"])

# ================================================================ Rosamma's room: shell only (no interior)

# ================================================================ kitchen (full width at the back)
CUR[0] = "Kitchen"
# aduppu: raised mud stove on a red-oxide platform in the NORTH-WEST corner, soot above it
box("Aduppu_platform", KX0 + 0.1, KY1 - 1.2, FL, KX0 + 2.2, KY1 - 0.1, FL + 0.3, M["platform"])
box("Aduppu_mud", KX0 + 0.3, KY1 - 0.95, FL + 0.3, KX0 + 2.0, KY1 - 0.15, FL + 0.8, M["mud"])
for k, x in enumerate((KX0 + 0.75, KX0 + 1.55)):
    box(f"Aduppu_fire{k}", x - 0.15, KY1 - 1.0, FL + 0.32, x + 0.15, KY1 - 0.9, FL + 0.5, M["fire"])
sph("Clay_pot", (KX0 + 0.75, KY1 - 0.55, FL + 0.95), 0.18, M["clay"])
cyl("Steel_pot", (KX0 + 1.55, KY1 - 0.55, FL + 0.92), 0.17, 0.25, M["steel"])
box("Soot_stain", KX0 + 0.3, KY1 - T / 2 - 0.02, FL + 0.8, KX0 + 2.0, KY1 - T / 2 - 0.01, FL + WH, M["soot"])
bpy.ops.object.light_add(type="POINT", location=(KX0 + 1.1, KY1 - 1.1, FL + 0.6))
put(bpy.context.object).data.energy = 15
bpy.context.object.data.color = (1.0, 0.55, 0.2)
# floor props: stone grinder with roller in front of the aduppu, milk can, stool with coconut halves, lantern, water pot
box("Grinder_stone", KX0 + 0.5, KY1 - 2.1, FL, KX0 + 1.2, KY1 - 1.7, FL + 0.18, M["stone"])
cyl("Grinder_roller", (KX0 + 0.85, KY1 - 1.9, FL + 0.24), 0.06, 0.55, M["stone"], rot=(0, math.radians(90), 0))
cyl("Milk_can", (KX0 + 2.4, KY1 - 1.0, FL + 0.22), 0.13, 0.44, M["steel"])
cyl("Stool", (0.6, KY1 - 1.6, FL + 0.17), 0.18, 0.34, M["brown"])
sph("Coconut_half1", (0.53, KY1 - 1.6, FL + 0.36), 0.07, M["brown"])
sph("Coconut_half2", (0.68, KY1 - 1.55, FL + 0.36), 0.07, M["white"])
cyl("Lantern", (KX1 - 0.4, KY1 - 1.6, FL + 0.15), 0.08, 0.3, M["fire"])
sph("Water_pot", (KX1 - 0.45, Y1 + 0.5, FL + 0.32), 0.3, M["clay"])
# west wall: niche shelves with containers and jars, a small shelf with vessels and ladles,
# switchboard, and the TWO framed Sacred Heart pictures (kitchen only, L2): one near the niche, one above the west door
wx = KX0 + T / 2
for k, z in enumerate((0.9, 1.3, 1.7)):
    box(f"Niche_shelf{k}", wx, 5.3, FL + z, wx + 0.3, 6.0, FL + z + 0.03, M["trim"])
    for j in range(3):
        cyl(f"Jar{k}{j}", (wx + 0.15, 5.45 + j * 0.2, FL + z + 0.12), 0.06, 0.18, M["steel"] if j % 2 else M["glass"])
box("Vessel_shelf", wx, 7.6, FL + 1.5, wx + 0.25, 8.2, FL + 1.53, M["brown"])
box("Switchboard", wx, 7.3, FL + 1.4, wx + 0.02, 7.45, FL + 1.55, M["trim"])
box("SacredHeart_1", wx, 6.1, FL + 1.5, wx + 0.03, 6.4, FL + 1.9, M["picture"])
box("SacredHeart_2", wx, 6.5, FL + 2.2, wx + 0.03, 6.8, FL + 2.6, M["picture"])
# east wall: a string of dried fish and a large woven winnow
ex_ = KX1 - T / 2
for k in range(5):
    box(f"Dried_fish{k}", ex_ - 0.04, 7.6 + k * 0.12, FL + 1.4, ex_ - 0.01, 7.68 + k * 0.12, FL + 1.85, M["fish"])
box("Winnow", ex_ - 0.04, 5.4, FL + 1.3, ex_ - 0.01, 6.0, FL + 2.0, M["coir"])

# ================================================================ roofs: hipped main roof, lower rear (kitchen) roof, chimney
CUR[0] = "Roof"
def hip_roof(name, x0, x1, y0, y1, eave, pitch_deg, thick=0.14):
    """Hipped roof over the rectangle; ridge along the longer side."""
    w, d = x1 - x0, y1 - y0
    t = math.tan(math.radians(pitch_deg))
    if w >= d:
        r = d / 2
        rz = eave + r * t
        verts = [(x0, y0, eave), (x1, y0, eave), (x1, y1, eave), (x0, y1, eave),
                 (x0 + r, y0 + r, rz), (x1 - r, y0 + r, rz)]
        faces = [(0, 1, 5, 4), (2, 3, 4, 5), (1, 2, 5), (3, 0, 4)]
    else:
        r = w / 2
        rz = eave + r * t
        verts = [(x0, y0, eave), (x1, y0, eave), (x1, y1, eave), (x0, y1, eave),
                 (x0 + r, y0 + r, rz), (x0 + r, y1 - r, rz)]
        faces = [(0, 1, 4), (1, 2, 5, 4), (2, 3, 5), (3, 0, 4, 5)]
    me = bpy.data.meshes.new(name)
    me.from_pydata(verts, [], faces)
    me.update()
    o = bpy.data.objects.new(name, me)
    col(CUR[0]).objects.link(o)
    o.data.materials.append(M["tile"])
    mod = o.modifiers.new("thick", "SOLIDIFY")
    mod.thickness = thick
    return o, rz

EAVE = FL + WH
main_roof, main_ridge = hip_roof("Roof_main", X0 - 0.75, X1 + 0.75, VY0 - 0.35, Y1 + 0.5, EAVE, 27)
kit_roof, kit_ridge = hip_roof("Roof_kitchen", KX0 - 0.7, KX1 + 0.7, Y1 + 0.2, KY1 + 0.65, EAVE - 0.35, 25)
# exposed rafters inside, every 0.6 m, on the long south and north faces of the main roof
r = ((Y1 + 0.5) - (VY0 - 0.35)) / 2
ry = (VY0 - 0.35) + r
for k in range(int((X1 - X0) / 0.6) + 1):
    x = X0 + k * 0.6
    xr = min(max(x, X0 - 0.75 + r), X1 + 0.75 - r)
    beam(f"Rafter_s{k}", (x, VY0 - 0.2, EAVE - 0.08), (xr, ry, main_ridge - 0.12), 0.06, 0.1, M["rafter"])
    beam(f"Rafter_n{k}", (x, Y1 + 0.35, EAVE - 0.08), (xr, ry, main_ridge - 0.12), 0.06, 0.1, M["rafter"])
beam("Ridge_beam", (X0 - 0.75 + r, ry, main_ridge - 0.15), (X1 + 0.75 - r, ry, main_ridge - 0.15), 0.12, 0.15, M["rafter"])
kr = ((KY1 + 0.65) - (Y1 + 0.2)) / 2
for k in range(int((KX1 - KX0) / 0.6) + 1):
    x = KX0 + k * 0.6
    xr = min(max(x, KX0 - 0.7 + kr), KX1 + 0.7 - kr)
    beam(f"KRafter_n{k}", (x, KY1 + 0.5, EAVE - 0.43), (xr, Y1 + 0.2 + kr, kit_ridge - 0.12), 0.06, 0.1, M["rafter"])
# wall plates (the tops of the walls under the roof)
box("Wallplate_front", X0 - T / 2, Y0 - 0.12, EAVE, X1 + T / 2, Y0 + 0.12, EAVE + 0.12, M["rafter"])
box("Wallplate_back", X0 - T / 2, Y1 - 0.12, EAVE, X1 + T / 2, Y1 + 0.12, EAVE + 0.12, M["rafter"])
# small chimney at the rear-left (north-west), above the aduppu
box("Chimney", KX0 + 0.5, KY1 - 0.6, kit_ridge - 0.6, KX0 + 1.0, KY1 - 0.1, kit_ridge + 0.5, M["tile"])

# ================================================================ rear exterior: clothesline, stone platform with pot and cans, firewood
CUR[0] = "Outside"
by = KY1 + T / 2
box("Stone_platform", -2.4, by, 0, -1.2, by + 0.6, 0.55, M["stone"])
sph("Platform_claypot", (-2.1, by + 0.3, 0.75), 0.2, M["clay"])
cyl("Platform_can1", (-1.7, by + 0.3, 0.72), 0.1, 0.35, M["steel"])
cyl("Platform_can2", (-1.45, by + 0.3, 0.7), 0.09, 0.3, M["steel"])
for k in range(6):
    box(f"Firewood{k}", -1.0, by + 0.05 + k * 0.08, 0, -0.5, by + 0.13 + k * 0.08, 0.9 - k * 0.05, M["brown"])
beam("Clothesline", (-3.7, by + 0.6, 2.2), (3.7, by + 0.6, 2.2), 0.01, 0.01, M["rope" if "rope" in M else "brown"])
for k, (x, m_) in enumerate(((-3.0, M["white"]), (-2.4, M["navy"]), (2.4, M["white"]), (3.0, M["navy"]))):
    box(f"Hanging_cloth{k}", x - 0.2, by + 0.58, 1.4, x + 0.2, by + 0.62, 2.2, m_)

# low laterite compound wall across the front with an open gap on line with the steps, and down both sides
def lwall(name, a, b):
    box(name, min(a[0], b[0]) - 0.15, min(a[1], b[1]) - 0.15, 0, max(a[0], b[0]) + 0.15, max(a[1], b[1]) + 0.15, 0.9, M["laterite"])
lwall("Compound_front_west", (WX, FWY), (-1.1, FWY))       # the open gap (2.2 m) is on line with the steps
lwall("Compound_front_east", (1.1, FWY), (EWX, FWY))
lwall("Compound_west", (WX, FWY), (WX, 11.0))
lwall("Compound_east", (EWX, FWY), (EWX, 11.0))
lwall("Compound_back", (WX, 11.0), (EWX, 11.0))
for x in (-1.1, 1.1):
    box(f"Gap_post{x}", x - 0.25 * (1 if x > 0 else -1) - 0.25, FWY - 0.25, 0, x + 0.25 * (1 if x > 0 else -1) + 0.25, FWY + 0.25, 1.1, M["laterite"])

# coconut palms around the house, two framing the front
def palm(name, x, y, h, lean=(0, 0)):
    gz = ground_z(x, y) if x < WX else 0.0
    top = Vector((x + lean[0], y + lean[1], gz + h))
    beam(f"{name}_trunk", (x, y, gz), top, 0.32, 0.32, M["palmtrunk"])
    for k in range(9):
        a = math.radians(k * 40)
        tip = top + Vector((math.cos(a) * 3.0, math.sin(a) * 3.0, -1.2))
        beam(f"{name}_frond{k}", top, tip, 0.5, 0.05, M["frond"])
PALMS = (
    # inside the compound (@houseout, c1 plate)
    (-5.0, -8.9, 11.5, (-0.5, 0.3)),     # by the front-west wall corner
    (-5.2, -2.6, 12.5, (-0.7, 0.0)),     # beside the west corner of the veranda
    (4.9, -4.6, 12.0, (1.8, 0.4)),       # the pair at the front-east corner, leaning out toward the cliff
    (5.4, -3.6, 13.0, (2.4, 0.2)),
    # outside: on the lane bank to the west, the front-west sand, behind the house
    (-11.5, 4.0, 10.0, (-0.8, 0.0)), (-11.0, 12.0, 12.0, (0.0, 1.0)), (-9.5, -12.5, 11.0, (-1.0, -0.3)),
    (-13.0, -5.0, 12.5, (-0.6, 0.4)), (-2.5, 15.0, 12.0, (0.3, 0.8)), (3.0, 16.5, 11.0, (0.6, 0.5)),
    # the palm grove behind the village on the left (west and north-west)
    (-16.0, 8.0, 13.0, (0.4, 0.2)), (-19.0, 18.0, 12.0, (-0.5, 0.6)), (-23.0, 6.0, 14.0, (0.3, -0.4)),
    (-21.0, 28.0, 13.0, (0.6, 0.3)), (-27.0, 16.0, 12.5, (-0.4, 0.5)), (-9.0, 22.0, 13.5, (0.2, 0.7)),
    (-14.0, 34.0, 12.0, (0.5, 0.4)), (-30.0, 30.0, 13.0, (0.3, 0.3)), (0.0, 26.0, 12.0, (0.4, 0.6)),
)
for k, (x, y, h, l) in enumerate(PALMS):
    palm(f"Palm{k}", x, y, h, l)
# wooden electric pole on the bank, shrubs along the foot of the wall, neighbours' tiled cottages down the lane
# at the foot of the bank, at the lane's edge (c2 plate); base sunk a little into the slope
cyl("Electric_pole", (LX0 - 0.3, 3.0, lane_z(3.0) + 0.1 + 4.5), 0.12, 9.0, M["pole"])
box("Pole_crossarm", LX0 - 1.0, 2.95, lane_z(3.0) + 0.1 + 8.6, LX0 + 0.4, 3.05, lane_z(3.0) + 0.1 + 8.7, M["pole"])
for k, y in enumerate((-4.0, 0.5, 5.0, 8.5)):
    sph(f"Lane_weed{k}", (LX1 - 0.15, y, lane_z(y) + 0.1), 0.25, M["green"], scale=(1, 2, 0.5))
def cottage(name, x, y, w=4.0, d=5.0):
    z = ground_z(x, y)
    box(f"{name}_walls", x - w / 2, y - d / 2, z, x + w / 2, y + d / 2, z + 2.6, M["wall"])
    box(f"{name}_band", x - w / 2 - 0.01, y - d / 2 - 0.01, z, x + w / 2 + 0.01, y + d / 2 + 0.01, z + 0.7, M["band"])
    hip_roof(f"{name}_roof", x - w / 2 - 0.4, x + w / 2 + 0.4, y - d / 2 - 0.4, y + d / 2 + 0.4, z + 2.6, 28)
for k, (x, y) in enumerate(((-15.5, 13.0), (-17.0, 21.0), (-15.0, 29.0), (-21.0, 6.0))):
    cottage(f"Cottage{k}", x, y)
for k, (x, y) in enumerate(((-5.1, FWY + 0.7), (5.3, FWY + 0.7), (5.3, 8.5))):
    sph(f"Shrub{k}", (x, y, 0.3), 0.6, M["green"], scale=(1.3, 1, 0.7))

# ================================================================ light, world, cameras
sun_dir = Vector((-0.75, 0.35, -0.55)).normalized()   # morning sun from the EAST (and a little south), low
bpy.ops.object.light_add(type="SUN", location=(10, -5, 15))
sun = bpy.context.object
sun.name = "Morning_sun_east"
sun.data.energy = 3.5
sun.data.color = (1.0, 0.92, 0.80)
sun.rotation_euler = sun_dir.to_track_quat("-Z", "Y").to_euler()
w = bpy.data.worlds.new("Sky")
sc.world = w
w.use_nodes = True
w.node_tree.nodes["Background"].inputs[0].default_value = (0.62, 0.72, 0.85, 1)
w.node_tree.nodes["Background"].inputs[1].default_value = 0.9

def cam(name, pos, look, fov, ortho=None):
    bpy.ops.object.camera_add(location=pos)
    c = bpy.context.object
    c.name = name
    c.data.sensor_fit = "HORIZONTAL"
    c.data.angle = math.radians(fov)
    c.data.clip_start = 0.05
    c.data.clip_end = 1000
    if ortho:
        c.data.type = "ORTHO"
        c.data.ortho_scale = ortho
        c.rotation_euler = (0, 0, look or 0)      # for ortho views `look` is the turn about z
    else:
        d = Vector(look) - Vector(pos)
        c.rotation_euler = d.to_track_quat("-Z", "Y").to_euler()
    col("Cameras").objects.link(c)
    for cc in list(c.users_collection):
        if cc.name != "Cameras":
            cc.objects.unlink(c)
    return c

E = FL + 1.6   # eye height on the floors
VIEWS = [
    # name, camera, hide roof?, resolution
    ("01-exterior-front-wide", cam("CAM_ext_front", (0.3, -30.0, 3.5), (0.0, 0.0, 0.6), 55), False),
    ("02-exterior-three-quarter", cam("CAM_ext_34", (13.0, -14.0, 7.0), (0.0, 2.0, 1.5), 50), False),
    ("03-cutaway-top", cam("CAM_top", (0.0, 3.0, 40.0), None, 0, ortho=22), True),
    ("04-cutaway-isometric", cam("CAM_iso", (0.0, -14.0, 17.0), (0.0, 3.5, 0.0), 48), True),
    ("05-antony-room-C3-corner", cam("CAM_ant_C3", (-1.3, 0.3, E + 0.4), (-4.2, 4.4, FL + 0.7), 84), False),
    ("06-antony-room-C4-from-passage", cam("CAM_ant_C4", (0.85, 0.6, E - 0.1), (-4.5, 2.3, FL + 0.9), 50), False),
    ("07-antony-room-C1-overhead", cam("CAM_ant_C1", (-2.75, 2.5, 12.0), math.radians(90), 0, ortho=5.6), True),
    ("08-passage-from-front-door", cam("CAM_passage", (0.0, -0.6, E), (0.0, 8.0, FL + 1.2), 60), False),
    ("09-kitchen-from-south-entry", cam("CAM_kitchen", (0.4, 5.25, E), (-0.8, 8.6, FL + 1.1), 88), False),
    ("10-veranda-from-the-steps", cam("CAM_veranda", (-0.3, -3.6, FL + 1.4), (0.0, 0.0, FL + 1.2), 75), False),
    ("11-antony-room-C2-from-the-door", cam("CAM_ant_C2", (-1.25, 2.5, E), (-4.5, 2.5, FL + 1.25), 88), False),
    ("13-exterior-west-side", cam("CAM_ext_west", (-17.0, 3.5, 2.0), (0.0, 3.5, 2.0), 60), False),
    ("14-lane-c2-up-toward-the-headland", cam("CAM_lane_c2", (LX1 - 1.4, 10.5, lane_z(10.5) + 1.6), (WX - 0.9, -14.0, 0.9), 58), False),
    ("12-kitchen-west-wall", cam("CAM_kit_west", (3.2, 6.6, E), (KX0, 6.7, FL + 1.3), 80), False),
]

r = sc.render
eng = [e.identifier for e in bpy.types.RenderSettings.bl_rna.properties["engine"].enum_items]
r.engine = "BLENDER_EEVEE_NEXT" if "BLENDER_EEVEE_NEXT" in eng else ("BLENDER_EEVEE" if "BLENDER_EEVEE" in eng else "BLENDER_WORKBENCH")
try:
    sc.view_settings.view_transform = "Standard"
except Exception:
    pass
r.image_settings.file_format = "PNG"

bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUT, "house.blend"))

roof = COLS["Roof"]
for name, c, hide_roof, *_ in VIEWS:
    roof.hide_render = hide_roof
    sc.camera = c
    if c.name == "CAM_ant_C1":
        r.resolution_x, r.resolution_y = 1600, 1080          # the room only: 5.6 m by 3.8 m
    elif c.data.type == "ORTHO":
        r.resolution_x, r.resolution_y = (900, 900) if PREVIEW else (1600, 1600)
    else:
        r.resolution_x, r.resolution_y = (1280, 548) if PREVIEW else (2206, 946)
    r.filepath = os.path.join(OUT, "renders", name + ".png")
    bpy.ops.render.render(write_still=True)
roof.hide_render = False
sc.camera = VIEWS[0][1]
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUT, "house.blend"))
print("DONE", OUT, r.engine)
