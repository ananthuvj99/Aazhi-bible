# 1D-oner blocking (Scene 1): Antony from his room, down the passage, to the kitchen doorway — one unbroken 14 s take.
# Opens the Blender house (locations/house-3d/house.blend), adds Antony (home look) and Rosamma at the aduppu,
# animates them to the 1D-oner beats, and renders a normal-quality playblast.
# Run: /Applications/Blender.app/Contents/MacOS/Blender -b -P build_1d.py -- <out_dir> [nomovie]
import bpy, math, sys, os
from mathutils import Vector

argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
OUT = os.path.abspath(argv[0] if argv else os.path.dirname(__file__))
NOMOVIE = "nomovie" in argv
HERE = os.path.dirname(os.path.abspath(__file__))
bpy.ops.wm.open_mainfile(filepath=os.path.abspath(os.path.join(HERE, "..", "..", "..", "locations", "house-3d", "house.blend")))
os.makedirs(OUT, exist_ok=True)
sc = bpy.context.scene
FPS = 24
DUR = 14.0
sc.render.fps = FPS
sc.frame_start, sc.frame_end = 1, int(DUR * FPS)
FL = 0.45

def lin(h):
    h = h.lstrip("#")
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    return tuple(v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4 for v in c)
def mat(name, hexstr, rough=0.8, hex2=None, scale=30):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    b = nt.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*lin(hexstr), 1)
    b.inputs["Roughness"].default_value = rough
    if hex2:
        t = nt.nodes.new("ShaderNodeTexChecker")
        t.inputs["Color1"].default_value = (*lin(hexstr), 1)
        t.inputs["Color2"].default_value = (*lin(hex2), 1)
        t.inputs["Scale"].default_value = scale
        co = nt.nodes.new("ShaderNodeTexCoord")
        nt.links.new(co.outputs["Object"], t.inputs["Vector"])
        nt.links.new(t.outputs["Color"], b.inputs["Base Color"])
    m.diffuse_color = (*lin(hexstr), 1)
    return m

# Costume colours from the sheets; Antony (home look) and Rosamma never read alike
C = dict(
    skin=mat("skin", "#8a5a40"), hair=mat("black hair", "#151210"), greyhair=mat("grey bun", "#6e6a66"),
    a_vest=mat("Antony white sleeveless vest", "#f2f2ee"),
    a_mundu=mat("Antony checked mundu", "#6f8a6a", hex2="#93a88e"),
    a_chain=mat("silver chain", "#d0d4d8", 0.2),
    r_saree=mat("Rosamma saree cream", "#f0e6cc"), r_blouse=mat("Rosamma blouse mid-blue", "#2f5fb0"),
    r_border=mat("Rosamma saree blue border", "#5a7fc8"), ladle=mat("long wooden ladle", "#6b4a2c"),
)
CH = bpy.data.collections.new("Characters_1D")
sc.collection.children.link(CH)
def link(o):
    for c in list(o.users_collection):
        c.objects.unlink(o)
    CH.objects.link(o)
    return o
def empty(name, loc=(0, 0, 0), parent=None):
    o = bpy.data.objects.new(name, None)
    link(o)
    o.parent = parent
    o.location = loc
    return o
def part(name, kind, loc, scale, m, parent, rot=(0, 0, 0)):
    {"box": lambda: bpy.ops.mesh.primitive_cube_add(size=1),
     "cyl": lambda: bpy.ops.mesh.primitive_cylinder_add(vertices=12, radius=0.5, depth=1),
     "cone": lambda: bpy.ops.mesh.primitive_cone_add(vertices=14, radius1=0.5, radius2=0.32, depth=1),
     "sph": lambda: bpy.ops.mesh.primitive_uv_sphere_add(segments=12, ring_count=8, radius=0.5)}[kind]()
    o = bpy.context.object
    o.name = name
    o.data.materials.append(m)
    link(o)
    o.parent = parent
    o.location = loc
    o.rotation_euler = rot
    o.scale = scale
    return o

# ---------------------------------------------------------------- Antony, home look: white vest, checked mundu, silver chain, messy hair
A = empty("Antony_root")
A_hip = empty("Antony_hips", (0, 0, 0.92), A)
legs = {}
for side, x in (("L", -0.1), ("R", 0.1)):
    pv = empty(f"Antony_leg{side}", (x, 0, 0), A_hip)
    part(f"Antony_mundu_leg{side}", "box", (0, 0, -0.45), (0.17, 0.2, 0.9), C["a_mundu"], pv)
    part(f"Antony_foot{side}", "box", (0, 0.06, -0.9), (0.1, 0.24, 0.05), C["skin"], pv)
    legs[side] = pv
part("Antony_mundu_hips", "box", (0, 0, 0.0), (0.38, 0.25, 0.22), C["a_mundu"], A_hip)
part("Antony_mundu_knot", "box", (0.06, 0.13, 0.06), (0.08, 0.04, 0.08), C["a_mundu"], A_hip)
A_chest = empty("Antony_chest", (0, 0, 0.12), A_hip)
part("Antony_vest", "box", (0, 0, 0.3), (0.38, 0.22, 0.58), C["a_vest"], A_chest)
part("Antony_shoulders_skin", "box", (0, 0, 0.53), (0.44, 0.2, 0.1), C["skin"], A_chest)
part("Antony_chain", "box", (0, 0.115, 0.48), (0.12, 0.01, 0.015), C["a_chain"], A_chest)
A_neck = empty("Antony_neck", (0, 0, 0.62), A_chest)
part("Antony_head", "sph", (0, 0.01, 0.13), (0.2, 0.22, 0.25), C["skin"], A_neck)
part("Antony_hair_messy", "sph", (0, -0.02, 0.21), (0.23, 0.24, 0.18), C["hair"], A_neck, rot=(0.2, 0.1, 0.3))
for ex in (-0.045, 0.045):
    part(f"Antony_eye{ex}", "sph", (ex, 0.105, 0.16), (0.035, 0.02, 0.025), C["hair"], A_neck)
part("Antony_nose", "box", (0, 0.12, 0.12), (0.03, 0.03, 0.06), C["skin"], A_neck)
part("Antony_moustache", "box", (0, 0.11, 0.075), (0.08, 0.02, 0.018), C["hair"], A_neck)
arms = {}
for side, x in (("L", -0.25), ("R", 0.25)):
    pv = empty(f"Antony_arm{side}", (x, 0, 0.55), A_chest)
    part(f"Antony_arm{side}_m", "box", (0, 0, -0.3), (0.09, 0.09, 0.6), C["skin"], pv)
    arms[side] = pv

# ---------------------------------------------------------------- Rosamma at the aduppu (north-west corner of the kitchen), her back to the passage, stirring
R = empty("Rosamma_root", (-2.75, 6.95, FL))
part("Rosamma_saree_skirt", "cone", (0, 0, 0.42), (0.5, 0.42, 0.84), C["r_saree"], R)
part("Rosamma_saree_border", "cyl", (0, 0, 0.04), (0.5, 0.42, 0.06), C["r_border"], R)
R_chest = empty("Rosamma_chest", (0, 0, 0.84), R)
part("Rosamma_blouse", "box", (0, 0, 0.22), (0.38, 0.22, 0.44), C["r_blouse"], R_chest)
part("Rosamma_pallu", "box", (-0.12, -0.02, 0.24), (0.2, 0.25, 0.5), C["r_saree"], R_chest, rot=(0, math.radians(18), 0))
R_neck = empty("Rosamma_neck", (0, 0, 0.47), R_chest)
part("Rosamma_head", "sph", (0, 0.01, 0.12), (0.19, 0.2, 0.23), C["skin"], R_neck)
part("Rosamma_hair", "sph", (0, -0.03, 0.17), (0.2, 0.2, 0.15), C["greyhair"], R_neck)
part("Rosamma_bun", "sph", (0, -0.13, 0.12), (0.1, 0.1, 0.1), C["greyhair"], R_neck)
R_arm = empty("Rosamma_armR", (0.21, 0, 0.4), R_chest)
part("Rosamma_armR_m", "box", (0, 0, -0.2), (0.08, 0.08, 0.4), C["skin"], R_arm)
part("Rosamma_ladle", "box", (0, 0.02, -0.48), (0.03, 0.03, 0.5), C["ladle"], R_arm)
pvL = empty("Rosamma_armL", (-0.21, 0, 0.4), R_chest)
pvL.rotation_euler = (math.radians(-40), 0, math.radians(15))
part("Rosamma_armL_m", "box", (0, 0, -0.2), (0.08, 0.08, 0.4), C["skin"], pvL)

# ---------------------------------------------------------------- Antony's path (house coordinates: x east, y north)
# 0.0-3.8 standing by the cot; 3.8-5.5 quickly to his door (passage wall, near the front); 5.5-6.5 through it and LEFT (north);
# 6.5-11.5 up the passage; 11.5-14.0 stopped in the kitchen doorway, shoulder on the frame
KEYS = [(0.0, -2.75, 3.05), (3.8, -2.75, 3.05), (5.5, -1.45, 0.95), (6.3, -0.35, 1.1), (6.8, 0.1, 1.6),
        (11.5, 0.15, 4.4), (12.0, 0.3, 4.95), (14.0, 0.3, 4.95)]     # stops against the RIGHT side of the kitchen doorway
def pos_at(t):
    for (t0, x0, y0), (t1, x1, y1) in zip(KEYS, KEYS[1:]):
        if t0 <= t <= t1:
            u = (t - t0) / (t1 - t0)
            u = u * u * (3 - 2 * u) if (t0 in (3.8, 6.8, 11.5) or t1 == 11.5) else u
            return Vector((x0 + (x1 - x0) * u, y0 + (y1 - y0) * u))
    return Vector(KEYS[-1][1:])

def smooth_ang(prev, target, k):
    d = (target - prev + math.pi) % (2 * math.pi) - math.pi
    return prev + d * k

frames = range(1, sc.frame_end + 1)
yaw = math.atan2(-(-1.45 + 2.75), (0.95 - 3.05))          # by the cot, facing his door (listening toward it)
dist, prev_p = 0.0, pos_at(0)
HEAD = {}
for f in frames:
    t = (f - 1) / FPS
    p = pos_at(t)
    step = (p - prev_p).length
    dist += step
    speed = step * FPS
    ahead = pos_at(min(DUR, t + 0.3)) - p
    if ahead.length > 0.02:
        yaw = smooth_ang(yaw, math.atan2(-ahead.x, ahead.y), 0.25)
    if t >= 11.6:                                         # in the doorway he turns a little toward his mother at the stove
        yaw = smooth_ang(yaw, math.atan2(-(-2.75 - p.x), 6.95 - p.y), 0.08)
    walk = min(1.0, speed / 1.0)
    phase = dist / 1.3 * 2 * math.pi
    A.location = (p.x, p.y, FL + 0.02 * walk * abs(math.sin(phase)))
    A.rotation_euler = (0, 0, yaw)
    A.keyframe_insert("location", frame=f)
    A.keyframe_insert("rotation_euler", frame=f)
    for side, s_ in (("L", 1), ("R", -1)):
        legs[side].rotation_euler = (math.radians(28) * walk * math.sin(phase) * s_, 0, 0)
        legs[side].keyframe_insert("rotation_euler", frame=f)
    # arms: scratch his head with both hands (1.0-3.0), tug the mundu knot (3.0-3.8), swing while walking,
    # a hand through his hair in the passage (8.0-9.2), right hand rubs the back of his neck in the doorway (12.0-14.0)
    for side, s_ in (("L", -1), ("R", 1)):
        rx = math.radians(18) * walk * math.sin(phase) * s_
        rz = 0.0
        if 1.0 <= t <= 3.0:
            u = min(1, (t - 1.0) / 0.3, (3.0 - t) / 0.3)
            rx = math.radians(-160 + 10 * math.sin(t * 14)) * u
            rz = math.radians(25 * (1 if side == "L" else -1)) * u
        elif 3.0 < t <= 3.8 and side == "R":
            u = math.sin((t - 3.0) / 0.8 * math.pi)
            rx = math.radians(-35) * u
        elif 8.0 <= t <= 9.2 and side == "R":
            u = math.sin((t - 8.0) / 1.2 * math.pi)
            rx = rx * (1 - u) + math.radians(-165) * u
        elif t >= 12.0 and side == "R":
            u = min(1, (t - 12.0) / 0.4)
            rx = math.radians(-150 + 8 * math.sin(t * 9)) * u
            rz = math.radians(-30) * u
        arms[side].rotation_euler = (rx, 0, rz)
        arms[side].keyframe_insert("rotation_euler", frame=f)
    # 0-1 listens toward the door, a guilty half-smile; shakes his head at himself while scratching
    nz = math.radians(6) * math.sin(t * 9) if 1.2 <= t <= 2.8 else 0.0
    A_neck.rotation_euler = (math.radians(-6) if t < 1.0 else 0, 0, nz)
    A_neck.keyframe_insert("rotation_euler", frame=f)
    # leans his shoulder on the doorframe at the end
    A_chest.rotation_euler = (0, math.radians(6) * min(1, max(0, (t - 11.8) / 0.6)), 0)
    A_chest.keyframe_insert("rotation_euler", frame=f)
    HEAD[f] = Vector((p.x, p.y, FL + 1.62))
    prev_p = p

# Rosamma stirs the pot: her right arm circles slowly; she never turns round
R.rotation_euler = (0, 0, 0)                                # facing north, the stove; her back to the passage
for f in frames:
    t = (f - 1) / FPS
    R_arm.rotation_euler = (math.radians(-55 + 8 * math.sin(t * 4.2)), 0, math.radians(-10 + 10 * math.cos(t * 4.2)))
    R_arm.keyframe_insert("rotation_euler", frame=f)

# the kitchen double doors stand wide open, flat against the end wall of the passage, so the doorway is clear
for nm, x in (("Door_kit_L", -0.9), ("Door_kit_R", 0.9)):
    d = bpy.data.objects.get(nm)
    if d:
        d.location = (x, 4.84, d.location.z)
        d.rotation_euler = (0, 0, 0)

# ---------------------------------------------------------------- the camera: one unbroken take at his shoulder height, a real operator's float, a beat behind him
bpy.ops.object.camera_add()
cam = bpy.context.object
cam.name = "CAM_1D_oner"
cam.data.sensor_fit = "HORIZONTAL"
cam.data.angle = math.radians(60)
cam.data.clip_start = 0.05
link(cam)
sc.camera = cam
cam.data.angle = math.radians(75)
# keyed positions to 6.5 s, then a weighted follow over his right shoulder, then an eased stop in the doorway
# opens from the room's north-east corner, by the trunk, looking toward the front wall: Antony in the middle, the barred
# front window and the one wall clock (front wall, near the west corner) behind him, the cot along the right of the frame;
# his door is off frame LEFT, so it pans left as he goes to the door, and follows him through it
CK = [(0.0, (-1.45, 4.55), None), (3.8, (-1.45, 4.55), None), (5.5, (-2.15, 2.3), None), (6.5, (-1.75, 1.0), None)]
def ck_at(t):
    for (t0, p0, _), (t1, p1, _) in zip(CK, CK[1:]):
        if t0 <= t <= t1:
            u = (t - t0) / (t1 - t0)
            u = u * u * (3 - 2 * u)
            return Vector((p0[0] + (p1[0] - p0[0]) * u, p0[1] + (p1[1] - p0[1]) * u, FL + 1.5))
    return Vector((*CK[-1][1], FL + 1.5))
END_POS = Vector((0.6, 4.2, FL + 1.55))                    # close behind his right shoulder, in the passage at the doorway
END_LOOK = Vector((-2.2, 7.0, FL + 1.0))                  # past him into the kitchen: his mother at the stove, back-left
cpos, look = ck_at(0), HEAD[1].copy()
for f in frames:
    t = (f - 1) / FPS
    a = HEAD[f]
    if t <= 6.5:
        cpos = ck_at(t)
        want_look = (a.lerp(Vector((-3.2, 0.1, FL + 1.6)), 0.35) - Vector((0, 0, 0.4))) if t < 3.8 else (a if t < 6.0 else Vector((-0.1, 1.9, FL + 1.5)).lerp(a, 0.5))
        look = look.lerp(want_look, 0.35 if t < 3.8 else 0.18)        # holds him, then pans right with him
    elif t <= 11.5:
        heading = (pos_at(min(DUR, t + 0.4)) - pos_at(t))
        heading = heading.normalized() if heading.length > 0.02 else Vector((0.0, 1.0))
        right = Vector((heading.y, -heading.x))
        b2 = Vector((a.x, a.y)) - heading * 1.6 + right * 0.45   # a little behind and beside him: over his right shoulder
        cpos = cpos.lerp(Vector((b2.x, b2.y, FL + 1.52)), 0.08)  # a beat behind him, weighted
        look = look.lerp(Vector((0.0, 7.8, FL + 1.1)), 0.06)      # the open kitchen doors ahead
    else:
        u = min(1.0, (t - 11.5) / 1.6)
        u = u * u * (3 - 2 * u)
        cpos = cpos.lerp(END_POS, 0.05 + 0.1 * u)
        look = look.lerp(END_LOOK, 0.05 + 0.1 * u)
    float_ = Vector((0.012 * math.sin(t * 1.7), 0.01 * math.sin(t * 2.3 + 1), 0.008 * math.sin(t * 1.3 + 2)))
    cam.location = cpos + float_
    cam.rotation_euler = (look - cam.location).to_track_quat("-Z", "Y").to_euler()
    cam.keyframe_insert("location", frame=f)
    cam.keyframe_insert("rotation_euler", frame=f)
CAMPATH = {f: None for f in ()}

# ---------------------------------------------------------------- normal-quality render
r = sc.render
r.resolution_x, r.resolution_y, r.resolution_percentage = 1280, 548, 100
try:
    sc.eevee.taa_render_samples = 16
except Exception:
    pass
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUT, "1d-oner-blocking.blend"))
for t_, nm in ((0.5, "still-0.5s-by-the-cot"), (2.0, "still-2s-scratching"), (6.0, "still-6s-through-the-door"),
               (9.0, "still-9s-up-the-passage"), (13.0, "still-13s-kitchen-doorway")):
    sc.frame_set(int(t_ * FPS) + 1)
    r.image_settings.file_format = "PNG"
    r.filepath = os.path.join(OUT, nm + ".png")
    bpy.ops.render.render(write_still=True)
if not NOMOVIE:
    sc.frame_set(1)
    if hasattr(r.image_settings, "media_type"):
        r.image_settings.media_type = "VIDEO"
    r.image_settings.file_format = "FFMPEG"
    r.ffmpeg.format = "MPEG4"
    r.ffmpeg.codec = "H264"
    r.ffmpeg.constant_rate_factor = "MEDIUM"
    r.filepath = os.path.join(OUT, "1d-oner-blocking-playblast.mp4")
    bpy.ops.render.render(animation=True)
import json
json.dump({"antony": [list(pos_at((f - 1) / FPS)) for f in frames][::6],
           "camera": [list(cam.animation_data.action and (sc.frame_set(f) or cam.matrix_world.translation)[:2]) for f in list(frames)[::6]],
           "rosamma": [-2.75, 6.95]}, open(os.path.join(OUT, "paths.json"), "w"))
print("DONE", OUT)
