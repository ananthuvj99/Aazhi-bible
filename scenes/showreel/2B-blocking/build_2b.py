# 2B blocking (Scene 2 Part B, approved v8): Antony leaves home, Rosamma calls from the door.
# Opens the Blender house (locations/house-3d/house.blend) so every position comes from that model,
# adds two low-poly characters in distinct costume colours, animates them to the v8 beats, adds wind
# to every palm, and renders a 15 s playblast from the v8 camera.
#
# Run: /Applications/Blender.app/Contents/MacOS/Blender -b -P build_2b.py -- <out_dir> [preview] [nomovie]
import bpy, math, sys, os, random
from mathutils import Vector, Euler

argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
OUT = os.path.abspath(argv[0] if argv else os.path.dirname(__file__))
PREVIEW = "preview" in argv
NOMOVIE = "nomovie" in argv
HERE = os.path.dirname(os.path.abspath(__file__))
HOUSE = os.path.join(HERE, "..", "..", "..", "locations", "house-3d", "house.blend")
os.makedirs(OUT, exist_ok=True)

bpy.ops.wm.open_mainfile(filepath=os.path.abspath(HOUSE))
sc = bpy.context.scene
FPS = 24
sc.render.fps = FPS
sc.frame_start, sc.frame_end = 1, 15 * FPS
random.seed(7)

# ---- the house model's numbers (locations/house-3d/build_house.py)
FL, VY0, FWY = 0.45, -2.6, -10.0
LANE_GRADE = 0.025
def lane_z(y):
    if y <= FWY:
        return 0.0
    if y <= 11.0:
        return -(y - FWY) * LANE_GRADE
    return -(11.0 - FWY) * LANE_GRADE - (y - 11.0) * 0.09
def ground(x, y):
    """Floor height Antony walks on: veranda, steps, yard, sand, the lane."""
    if y > VY0 and abs(x) < 4.7:
        return FL
    if VY0 - 1.05 <= y <= VY0 and abs(x) <= 1.1:            # the three steps
        return FL * max(0.0, min(1.0, (y - (VY0 - 1.05)) / 1.05))
    if x < -5.9 and y > FWY:                                   # in the lane
        return lane_z(y)
    return 0.0

def lin(h):
    h = h.lstrip("#")
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    return tuple(v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4 for v in c)
def mat(name, hexstr, rough=0.8, pattern=None, hex2=None, scale=20):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    b = nt.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*lin(hexstr), 1)
    b.inputs["Roughness"].default_value = rough
    if pattern == "checker":
        t = nt.nodes.new("ShaderNodeTexChecker")
        t.inputs["Color1"].default_value = (*lin(hexstr), 1)
        t.inputs["Color2"].default_value = (*lin(hex2), 1)
        t.inputs["Scale"].default_value = scale
        co = nt.nodes.new("ShaderNodeTexCoord")
        nt.links.new(co.outputs["Object"], t.inputs["Vector"])
        nt.links.new(t.outputs["Color"], b.inputs["Base Color"])
    m.diffuse_color = (*lin(hexstr), 1)
    return m

# Costume colours from the character sheets, chosen so the two never read alike
C = dict(
    skin=mat("skin", "#8a5a40"), hair=mat("black hair", "#151210"), greyhair=mat("grey bun", "#6e6a66"),
    a_shirt=mat("Antony shirt lavender-grey stripe", "#9c93c8", pattern="checker", hex2="#d9d4ec", scale=60),
    a_mundu=mat("Antony mundu grey-green check", "#6f8a6a", pattern="checker", hex2="#93a88e", scale=30),
    a_bag=mat("Antony bag faded beige", "#d8c8a0"),
    r_saree=mat("Rosamma saree cream", "#f0e6cc"),
    r_blouse=mat("Rosamma blouse mid-blue", "#2f5fb0"),
    r_border=mat("Rosamma saree blue flowers", "#5a7fc8"),
    steel=mat("steel plate", "#cfd3d8", 0.25), puttu=mat("puttu white", "#f4f1e8"), curry=mat("fish curry", "#b5532a"),
    cross=mat("gold cross", "#d8b04a", 0.3),
)

def col(name):
    c = bpy.data.collections.get(name)
    if not c:
        c = bpy.data.collections.new(name)
        sc.collection.children.link(c)
    return c
CHAR = col("Characters_2B")

def link(o):
    for c in list(o.users_collection):
        c.objects.unlink(o)
    CHAR.objects.link(o)
    return o
def empty(name, loc=(0, 0, 0), parent=None):
    o = bpy.data.objects.new(name, None)
    o.empty_display_size = 0.15
    link(o)
    o.parent = parent
    o.location = loc
    return o
def part(name, kind, loc, scale, m, parent, rot=(0, 0, 0)):
    if kind == "box":
        bpy.ops.mesh.primitive_cube_add(size=1)
    elif kind == "cyl":
        bpy.ops.mesh.primitive_cylinder_add(vertices=12, radius=0.5, depth=1)
    elif kind == "cone":
        bpy.ops.mesh.primitive_cone_add(vertices=14, radius1=0.5, radius2=0.32, depth=1)
    else:
        bpy.ops.mesh.primitive_uv_sphere_add(segments=12, ring_count=8, radius=0.5)
    o = bpy.context.object
    o.name = name
    o.data.materials.append(m)
    link(o)
    o.parent = parent
    o.location = loc
    o.rotation_euler = rot
    o.scale = scale
    return o

# ---------------------------------------------------------------- Antony (1.72 m), faces +y in his own frame
A = empty("Antony_root")
A_hip = empty("Antony_hips", (0, 0, 0.92), A)
legs = {}
for side, x in (("L", -0.1), ("R", 0.1)):
    pv = empty(f"Antony_leg{side}", (x, 0, 0), A_hip)
    part(f"Antony_mundu_leg{side}", "box", (0, 0, -0.45), (0.17, 0.2, 0.9), C["a_mundu"], pv)
    part(f"Antony_foot{side}", "box", (0, 0.06, -0.9), (0.1, 0.24, 0.05), C["skin"], pv)
    legs[side] = pv
part("Antony_mundu_hips", "box", (0, 0, 0.0), (0.38, 0.25, 0.22), C["a_mundu"], A_hip)
A_chest = empty("Antony_chest", (0, 0, 0.12), A_hip)
part("Antony_shirt", "box", (0, 0, 0.3), (0.42, 0.24, 0.58), C["a_shirt"], A_chest)
A_neck = empty("Antony_neck", (0, 0, 0.62), A_chest)
part("Antony_head", "sph", (0, 0.01, 0.13), (0.2, 0.22, 0.25), C["skin"], A_neck)
part("Antony_hair", "sph", (0, -0.02, 0.2), (0.21, 0.22, 0.16), C["hair"], A_neck)
# eyes, moustache and nose, so the way he faces always reads
for ex in (-0.045, 0.045):
    part(f"Antony_eye{ex}", "sph", (ex, 0.105, 0.16), (0.035, 0.02, 0.025), C["hair"], A_neck)
part("Antony_nose", "box", (0, 0.12, 0.12), (0.03, 0.03, 0.06), C["skin"], A_neck)
part("Antony_moustache", "box", (0, 0.11, 0.075), (0.08, 0.02, 0.018), C["hair"], A_neck)
arms = {}
for side, x in (("L", -0.27), ("R", 0.27)):
    pv = empty(f"Antony_arm{side}", (x, 0, 0.55), A_chest)
    part(f"Antony_sleeve{side}", "box", (0, 0, -0.1), (0.12, 0.12, 0.22), C["a_shirt"], pv)
    part(f"Antony_forearm{side}", "box", (0, 0, -0.38), (0.08, 0.08, 0.36), C["skin"], pv)
    arms[side] = pv
# the large faded beige canvas bag on his LEFT shoulder, at his left hip
part("Antony_bag_strap", "box", (-0.05, 0.0, 0.32), (0.04, 0.26, 0.62), C["a_bag"], A_chest, rot=(0, math.radians(-28), 0))
part("Antony_bag", "box", (-0.3, 0.02, -0.08), (0.12, 0.42, 0.36), C["a_bag"], A_chest)

# ---------------------------------------------------------------- Rosamma (1.55 m) at the open front door, facing out (south)
R = empty("Rosamma_root", (0.0, -0.25, FL))
R.rotation_euler = (0, 0, math.radians(180))
part("Rosamma_saree_skirt", "cone", (0, 0, 0.42), (0.5, 0.42, 0.84), C["r_saree"], R)
part("Rosamma_saree_border", "cyl", (0, 0, 0.04), (0.5, 0.42, 0.06), C["r_border"], R)
R_chest = empty("Rosamma_chest", (0, 0, 0.84), R)
part("Rosamma_blouse", "box", (0, 0, 0.22), (0.38, 0.22, 0.44), C["r_blouse"], R_chest)
part("Rosamma_pallu", "box", (-0.12, -0.02, 0.24), (0.2, 0.25, 0.5), C["r_saree"], R_chest, rot=(0, math.radians(18), 0))
part("Rosamma_cross", "box", (0, 0.12, 0.36), (0.03, 0.01, 0.05), C["cross"], R_chest)
R_neck = empty("Rosamma_neck", (0, 0, 0.47), R_chest)
part("Rosamma_head", "sph", (0, 0.01, 0.12), (0.19, 0.2, 0.23), C["skin"], R_neck)
part("Rosamma_hair", "sph", (0, -0.03, 0.17), (0.2, 0.2, 0.15), C["greyhair"], R_neck)
part("Rosamma_bun", "sph", (0, -0.13, 0.12), (0.1, 0.1, 0.1), C["greyhair"], R_neck)
for ex in (-0.04, 0.04):
    part(f"Rosamma_eye{ex}", "sph", (ex, 0.095, 0.15), (0.032, 0.02, 0.022), C["hair"], R_neck)
part("Rosamma_nose", "box", (0, 0.11, 0.11), (0.028, 0.03, 0.05), C["skin"], R_neck)
for side, x in (("L", -0.21), ("R", 0.21)):
    pv = empty(f"Rosamma_arm{side}", (x, 0, 0.4), R_chest)
    pv.rotation_euler = (math.radians(-55), 0, math.radians(18 if x < 0 else -18))
    part(f"Rosamma_arm{side}_m", "box", (0, 0, -0.2), (0.08, 0.08, 0.4), C["skin"], pv)
# the full steel plate (puttu and curry), held at waist height in both hands, untouched
P = empty("Rosamma_plate", (0, 0.32, 0.12), R_chest)
part("Plate_steel", "cyl", (0, 0, 0), (0.3, 0.3, 0.02), C["steel"], P)
part("Plate_puttu1", "cyl", (-0.05, 0, 0.04), (0.06, 0.06, 0.12), C["puttu"], P, rot=(0, math.radians(90), 0))
part("Plate_puttu2", "cyl", (-0.05, 0.07, 0.04), (0.06, 0.06, 0.12), C["puttu"], P, rot=(0, math.radians(90), 0))
part("Plate_curry", "cyl", (0.08, -0.03, 0.03), (0.07, 0.07, 0.03), C["curry"], P)

# ---------------------------------------------------------------- Antony's path, timed to the v8 beats
# 0.0-1.5 out from behind the white pillar left of the door, down the steps beside his mother
# 1.5-5.0 across the yard and out through the wall gap; begins to turn left
# 5.0-9.0 across the sand to the lane at the west side   8.0-11.5 answers over his right shoulder, lifts his right hand once
# 9.0-15.0 up the lane along the west wall, smaller
KEYS = [  # time (s), x, y
    (0.0, -1.5, -1.9), (0.6, -1.15, -2.45), (1.5, -0.45, -3.75),   # starts on the camera's line through the pillar
    (3.4, -0.75, -7.0), (5.0, -0.2, -10.2), (6.0, -1.0, -10.9),    # crosses the yard a little left, so she stays in view
    (9.0, -6.6, -11.0), (10.2, -7.4, -9.6), (15.0, -7.5, -1.9),
]
def pos_at(t):
    for (t0, x0, y0), (t1, x1, y1) in zip(KEYS, KEYS[1:]):
        if t0 <= t <= t1:
            u = (t - t0) / (t1 - t0)
            u = u * u * (3 - 2 * u) if t0 == 0 else u        # eases only the first step out from behind the pillar
            return Vector((x0 + (x1 - x0) * u, y0 + (y1 - y0) * u))
    return Vector(KEYS[-1][1:])

def head_track(nx, ny):
    return math.atan2(-nx, ny)

frames = range(1, sc.frame_end + 1)
prev_yaw = math.radians(170)
dist = 0.0
prev_p = pos_at(0)
for f in frames:
    t = (f - 1) / FPS
    p = pos_at(t)
    ahead = pos_at(min(15, t + 0.35)) - p
    speed = (p - prev_p).length * FPS
    dist += (p - prev_p).length
    if ahead.length > 0.02:
        target = math.atan2(-ahead.x, ahead.y)
        d = (target - prev_yaw + math.pi) % (2 * math.pi) - math.pi
        prev_yaw += d * 0.25                       # turns are smooth, never snapped
    z = ground(p.x, p.y)
    phase = dist / 1.5 * 2 * math.pi               # one stride cycle per 1.5 m
    walk = min(1.0, speed / 1.2)
    A.location = (p.x, p.y, z + 0.02 * walk * abs(math.sin(phase)))
    A.rotation_euler = (0, 0, prev_yaw)
    A.keyframe_insert("location", frame=f)
    A.keyframe_insert("rotation_euler", frame=f)
    for side, s_ in (("L", 1), ("R", -1)):
        legs[side].rotation_euler = (math.radians(26) * walk * math.sin(phase) * s_, 0, 0)
        legs[side].keyframe_insert("rotation_euler", frame=f)
    # arms swing opposite the legs; the LEFT arm stays at the bag strap
    arms["L"].rotation_euler = (math.radians(-6), 0, math.radians(-10))
    arms["L"].keyframe_insert("rotation_euler", frame=f)
    rx = -math.radians(18) * walk * math.sin(phase)
    if 9.6 <= t <= 10.6:                           # lifts his right hand once
        u = math.sin((t - 9.6) / 1.0 * math.pi)
        rx = rx * (1 - u) + math.radians(-150) * u
    arms["R"].rotation_euler = (rx, 0, 0)
    arms["R"].keyframe_insert("rotation_euler", frame=f)
    # 8.0-11.5: half turns his head and right shoulder back toward the house while he answers
    turn = 0.0
    if 7.6 <= t <= 11.8:
        turn = math.sin(min(1.0, (t - 7.6) / 0.6) * math.pi / 2) * (1 if t < 11.2 else max(0, (11.8 - t) / 0.6))
    A_chest.rotation_euler = (0, 0, math.radians(-10) * turn)     # a small look back toward the house: his face stays
    A_neck.rotation_euler = (0, 0, math.radians(-25) * turn)      # readable to the close camera while he speaks
    A_chest.keyframe_insert("rotation_euler", frame=f)
    A_neck.keyframe_insert("rotation_euler", frame=f)
    prev_p = p

# Rosamma: looks down at the plate, lifts her head and watches him go (calls at 3.0 s), small shake of her head
# while he answers, keeps watching the lane, then looks down at the plate. She never leaves the door.
for f in frames:
    t = (f - 1) / FPS
    ap = pos_at(t)
    rel = ap - Vector((0.0, -0.25))
    look = math.atan2(-rel.x, rel.y) - math.radians(180)
    look = (look + math.pi) % (2 * math.pi) - math.pi
    look = max(-1.2, min(1.2, look))
    tilt = 0.0
    if t < 1.5 or t > 13.5:
        tilt = math.radians(28)                     # eyes down to the plate
    shake = math.radians(7) * math.sin((t - 8.5) * 2 * math.pi * 1.6) if 8.5 <= t <= 10.0 else 0.0
    R_neck.rotation_euler = (tilt, 0, (0 if t < 1.5 else look * 0.6) + shake)
    R_chest.rotation_euler = (0, 0, 0 if t < 1.5 else look * 0.3)
    R_neck.keyframe_insert("rotation_euler", frame=f)
    R_chest.keyframe_insert("rotation_euler", frame=f)
    lean = math.radians(6) * math.sin(min(1, max(0, (t - 3.0) / 0.4)) * math.pi) if 3.0 <= t <= 3.4 + 3.6 else 0
    R.rotation_euler = (lean * 0.4, 0, math.radians(180))
    R.keyframe_insert("rotation_euler", frame=f)

# ---------------------------------------------------------------- wind on every palm: a steady lean away from the sea
# (the wind comes off the sea from the EAST), a slow trunk sway, and fronds that flutter, each tree on its own rhythm
WIND = col("Wind_pivots")
def wind_link(o):
    for c in list(o.users_collection):
        c.objects.unlink(o)
    WIND.objects.link(o)
def frame_set_parent(child, parent):
    mw = child.matrix_world.copy()
    child.parent = parent
    child.matrix_world = mw

palms = sorted({o.name.split("_")[0] for o in bpy.data.objects if o.name.startswith("Palm") and o.name.endswith("_trunk")})
for pname in palms:
    trunk = bpy.data.objects[f"{pname}_trunk"]
    axis = trunk.matrix_world.to_3x3() @ Vector((0, 0, 1))
    half = trunk.scale.z / 2
    base = trunk.matrix_world.translation - axis * half
    top = trunk.matrix_world.translation + axis * half
    bp = bpy.data.objects.new(f"{pname}_wind_base", None); wind_link(bp); bp.location = base
    bpy.context.view_layer.update()
    frame_set_parent(trunk, bp)
    crowns = []
    for o in [o for o in bpy.data.objects if o.name.startswith(f"{pname}_frond")]:
        cp = bpy.data.objects.new(f"{o.name}_pivot", None); wind_link(cp); cp.location = top
        bpy.context.view_layer.update()
        frame_set_parent(cp, bp)
        frame_set_parent(o, cp)
        crowns.append(cp)
    bpy.context.view_layer.update()
    ph = random.uniform(0, 6.28)
    per = random.uniform(2.6, 3.6)
    for f in range(1, sc.frame_end + 1, 3):
        t = (f - 1) / FPS
        # the trunk does not move: only a fixed lean of about 2.5 deg toward the west (away from the sea)
        if f == 1:
            bp.rotation_euler = (0, math.radians(-2.5), 0)
            bp.keyframe_insert("rotation_euler", frame=f)
        # only the fronds move, gently: about 1.5 deg of flutter and 1 deg of lift and fall
        for j, cp in enumerate(crowns):
            pj = ph + j * 0.9
            cp.rotation_euler = (math.radians(1.5) * math.sin(2 * math.pi * t / 1.6 + pj),
                                 math.radians(-1.0 - 1.0 * (0.5 + 0.5 * math.sin(2 * math.pi * t / 2.2 + pj))),
                                 math.radians(0.8) * math.sin(2 * math.pi * t / 2.7 + pj))
            cp.keyframe_insert("rotation_euler", frame=f)

# ---------------------------------------------------------------- the v8 camera: on the sand about 25 m from the door, eye level 1.5 m.
# Perfectly still to 5.0 s, then it turns in place to the LEFT following Antony (it never travels), a beat behind him,
# easing in and out; Antony stays in the left third, Rosamma at the door in the right half; settled from 13.5 s.
bpy.ops.object.camera_add(location=(0.3, -25.0, 1.5))
cam = bpy.context.object
cam.name = "CAM_2B_v8"
cam.data.sensor_fit = "HORIZONTAL"
cam.data.angle = math.radians(63)
cam.data.clip_start = 0.1
cam.data.clip_end = 2000
link(cam)
pitch = math.radians(90 - 1.5)
yaw0 = math.atan2(-(0.0 - 0.3), (-1.5 - (-25.0)))           # at the door
def yaw_to(x, y):
    return math.atan2(-(x - 0.3), y - (-25.0))
lag = 0.0
for f in frames:
    t = (f - 1) / FPS
    ap = pos_at(max(0.0, t - 0.5))                            # a beat behind him
    want = yaw_to(ap.x, ap.y) - math.radians(9)              # keep him in the left third
    if t < 5.0:
        y_ = yaw0
    else:
        u = min(1.0, (t - 5.0) / 8.5)
        u = u * u * (3 - 2 * u)
        y_ = yaw0 + (max(yaw0, want) - yaw0) * u if want > yaw0 else yaw0
        if t >= 13.5:
            y_ = prev_cam
    prev_cam = y_
    cam.rotation_euler = (pitch, 0, y_)
    cam.keyframe_insert("rotation_euler", frame=f)
sc.camera = cam
print("PAN degrees", round(math.degrees(prev_cam - yaw0), 1))

# ---------------------------------------------------------------- CUT 2 (8.0-11.5 s): close on Antony while he answers.
# The camera leads him, about 2.2 m ahead on his path, at face height, 47 deg (MCU), travelling backward as he walks
# toward it; he answers with his face to the lens (within ~30 deg). Hard cut in at 8.0 s and back to the wide at 11.5 s.
CUT2_IN, CUT2_OUT = 7.0, 11.5          # in a beat before his line (8.0 s) as he reaches the lane
bpy.ops.object.camera_add()
close = bpy.context.object
close.name = "CAM_2B_close_antony"
close.data.sensor_fit = "HORIZONTAL"
close.data.angle = math.radians(47)
close.data.clip_start = 0.05
close.data.clip_end = 2000
link(close)
f_in, f_out = int(CUT2_IN * FPS) + 1, int(CUT2_OUT * FPS) + 1
sm = None
for f in range(f_in - 2, f_out + 2):
    t = (f - 1) / FPS
    a = pos_at(t)
    ahead = pos_at(min(15.0, t + 1.6))
    if (ahead - a).length < 0.5:
        ahead = a + (ahead - a).normalized() * 2.2 if (ahead - a).length > 0 else a + Vector((0, 2.2))
    sm = ahead if sm is None else sm.lerp(ahead, 0.15)               # smooth, weighted, a beat behind
    cz = ground(sm.x, sm.y) + 1.55
    head = Vector((a.x, a.y, ground(a.x, a.y) + 1.6))
    close.location = (sm.x, sm.y, cz)
    close.rotation_euler = (head - Vector(close.location)).to_track_quat("-Z", "Y").to_euler()
    close.keyframe_insert("location", frame=f)
    close.keyframe_insert("rotation_euler", frame=f)
# ---- Rosamma's close (3.0-7.0 s): locked MCU from the veranda in front of her, 47 deg, at her eye level;
# she says her line looking just past the lens toward Antony (he is behind the camera, in the yard); she is alone in frame.
R_IN, R_OUT = 3.0, 7.0
bpy.ops.object.camera_add(location=(0.25, -2.15, FL + 1.38))
rcam = bpy.context.object
rcam.name = "CAM_2B_close_rosamma"
rcam.data.sensor_fit = "HORIZONTAL"
rcam.data.angle = math.radians(52)      # wide enough to keep the plate in her hands in frame
rcam.data.clip_start = 0.05
rcam.data.clip_end = 2000
link(rcam)
rcam.rotation_euler = (Vector((0.0, -0.25, FL + 1.18)) - Vector(rcam.location)).to_track_quat("-Z", "Y").to_euler()
fr_rin, fr_rout = int(R_IN * FPS) + 1, int(R_OUT * FPS) + 1
for nm, fr, c_ in (("CUT1_wide", 1, cam), ("CUT2_close_rosamma", fr_rin, rcam), ("CUT3_close_antony", f_in, close), ("CUT4_wide", f_out, cam)):
    m_ = sc.timeline_markers.new(nm, frame=fr)
    m_.camera = c_

# ---------------------------------------------------------------- render
r = sc.render
r.resolution_x, r.resolution_y = (1280, 548) if PREVIEW else (2206, 946)
r.resolution_percentage = 100
COLS_HIDE = []
roof = bpy.data.collections.get("Roof")
if roof:
    roof.hide_render = False
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUT, "2b-blocking.blend"))
for f_, nm in ((1, "still-0s"), (int(4.5 * FPS) + 1, "still-4.5s-her-line-close"), (int(9.5 * FPS) + 1, "still-9.5s-his-answer-close"), (int(12.5 * FPS) + 1, "still-12.5s-back-to-wide"), (sc.frame_end, "still-15s")):
    sc.frame_set(f_)
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
    r.ffmpeg.constant_rate_factor = "HIGH"
    r.filepath = os.path.join(OUT, "2b-blocking-playblast.mp4")
    bpy.ops.render.render(animation=True)
print("DONE", OUT)
