# Grey-box blocking for s21-sh04 (SB027 night watch), built from Ranjith's map
# scenes/showreel/storyboards/s21-sh01-sh02-sightlines.json and
# continuity/night-rescue-distances.md. Every position below comes from those files.
#
# Axes (metres): x = starboard (+) / port (-), y = forward (+, bow) / aft (-), z = up, deck at z = 0.
# Run:  /Applications/Blender.app/Contents/MacOS/Blender -b -P build_blocking.py -- <out_dir> [preview]
# Writes <out_dir>/blocking.blend, <out_dir>/blocking-playblast.mp4 and stills.
import bpy, math, sys, os
from mathutils import Vector

argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
OUT = os.path.abspath(argv[0] if argv else os.path.dirname(__file__))
PREVIEW = len(argv) > 1 and argv[1] == "preview"
os.makedirs(OUT, exist_ok=True)

FPS = 24
# Sacks: Ranjith's map puts them forward of the mast, on the starboard side (centre y 3.4). The plate-high frame (02)
# shows them beside / aft of the mast instead. Change SACKS_Y here to move them; every view follows.
SACKS_Y = 3.4
CUT = 378            # shot 1 = frames 1..378 (15.75 s, as in the take); shot 2 = 379..720
END = 720            # 30 s

# ---------------------------------------------------------------- reset
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
sc.render.fps = FPS
sc.frame_start, sc.frame_end = 1, END

def mat(name, rgb, emit=0.0):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*rgb, 1)
    b.inputs["Roughness"].default_value = 0.85
    if emit:
        b.inputs["Emission Color"].default_value = (*rgb, 1)
        b.inputs["Emission Strength"].default_value = emit
    m.diffuse_color = (*rgb, 1)
    return m

M = {
    "hull": mat("hull", (0.18, 0.24, 0.30)),
    "deck": mat("deck", (0.32, 0.30, 0.27)),
    "rail": mat("rail", (0.20, 0.17, 0.14)),
    "house": mat("house", (0.36, 0.36, 0.36)),
    "window": mat("window", (1.0, 0.55, 0.18), 6),
    "bowblue": mat("bowblue", (0.12, 0.28, 0.55)),
    "bitt": mat("bitt", (0.45, 0.18, 0.12)),
    "mast": mat("mast", (0.30, 0.22, 0.14)),
    "sack": mat("sack", (0.55, 0.52, 0.45)),
    "rope": mat("rope", (0.55, 0.42, 0.22)),
    "mat": mat("mat", (0.45, 0.40, 0.30)),
    "lantern": mat("lantern", (1.0, 0.6, 0.2), 15),
    "sea": mat("sea", (0.006, 0.014, 0.035)),
    "moon": mat("moon", (0.9, 0.93, 1.0), 25),
    "fire": mat("fire", (1.0, 0.35, 0.05), 40),
    "skin": mat("skin", (0.42, 0.28, 0.20)),
    "white": mat("white", (0.85, 0.84, 0.80)),
    "cream": mat("cream", (0.80, 0.74, 0.60)),
    "check": mat("check", (0.40, 0.38, 0.35)),
    "greencheck": mat("greencheck", (0.30, 0.36, 0.30)),
    "redcheck": mat("redcheck", (0.80, 0.25, 0.30)),
    "hair": mat("hair", (0.05, 0.05, 0.05)),
    "greyhair": mat("greyhair", (0.6, 0.6, 0.6)),
    "antony": mat("antony", (0.62, 0.60, 0.55)),
}

def box(name, c, s, m, rot=(0, 0, 0)):
    bpy.ops.mesh.primitive_cube_add(size=1, location=c, rotation=rot)
    o = bpy.context.object
    o.name = name
    o.scale = s
    o.data.materials.append(m)
    return o

def cyl(name, c, r, h, m, rot=(0, 0, 0), v=12):
    bpy.ops.mesh.primitive_cylinder_add(vertices=v, radius=r, depth=h, location=c, rotation=rot)
    o = bpy.context.object
    o.name = name
    o.data.materials.append(m)
    return o

def sph(name, c, r, m, seg=12):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=seg, ring_count=seg // 2, radius=r, location=c)
    o = bpy.context.object
    o.name = name
    o.data.materials.append(m)
    return o

def torus(name, c, r, m):
    bpy.ops.mesh.primitive_torus_add(location=c, major_radius=r, minor_radius=0.07, major_segments=16, minor_segments=6)
    o = bpy.context.object
    o.name = name
    o.data.materials.append(m)
    return o

# ---------------------------------------------------------------- sea and hull
box("Sea", (0, 0, -2.3), (4000, 4000, 0.01), M["sea"])
box("Hull", (0, -0.25, -1.2), (6.2, 21.5, 2.3), M["hull"])           # y -11 .. +10.5
box("Deck", (0, -0.25, -0.03), (6.0, 21.5, 0.06), M["deck"])
# bow: tapering wedge from y = 10.5 to the stem at 13
for i in range(5):
    y0 = 10.5 + i * 0.5
    w = 6.0 * (1 - (i + 1) / 5.6)
    box(f"Hull_bow{i}", (0, y0 + 0.25, -1.2), (w + 0.2, 0.5, 2.3), M["hull"])
    box(f"Deck_bow{i}", (0, y0 + 0.25, -0.03), (w, 0.5, 0.06), M["bowblue"])
cyl("Stem", (0, 13.0, 0.4), 0.15, 2.6, M["bowblue"], rot=(math.radians(-15), 0, 0))
# four red-brown mooring bitts in pairs, forward of the mast (as on the @uru sheet and @urubowplate)
for x in (-0.45, 0.45):
    for y in (7.6, 8.4):
        cyl(f"Bitt_{x}_{y}", (x, y, 0.35), 0.16, 0.7, M["bitt"])

# bulwark rails along both sides (0.9 m), with posts, converging at the bow
def rail_line(name, a, b, posts=True):
    a, b = Vector(a), Vector(b)
    d = b - a
    L = d.length
    mid = (a + b) / 2
    ang = math.atan2(d.x, d.y)
    box(name, (mid.x, mid.y, 0.9), (0.12, L, 0.10), M["rail"], rot=(0, 0, -ang))
    box(name + "_wall", (mid.x, mid.y, 0.25), (0.08, L, 0.5), M["rail"], rot=(0, 0, -ang))
    if posts:
        n = max(2, int(L / 0.8))
        for k in range(n + 1):
            p = a + d * (k / n)
            box(f"{name}_p{k}", (p.x, p.y, 0.7), (0.07, 0.07, 0.4), M["rail"])

for sgn, side in ((-1, "Port"), (1, "Stbd")):
    rail_line(f"Rail{side}", (3.0 * sgn, -11.0), (3.0 * sgn, 10.5))
    rail_line(f"Rail{side}Bow", (3.0 * sgn, 10.5), (0.15 * sgn, 13.0))
rail_line("RailStern", (-3.0, -11.0), (3.0, -11.0))

# ---------------------------------------------------------------- deckhouse (centre y -9, 5 x 4 x 2.6), wheel inside
box("House", (0, -9.0, 1.3), (5.0, 4.0, 2.6), M["house"])
box("HouseRoof", (0, -9.0, 2.7), (5.4, 4.4, 0.2), M["house"])
for i, x in enumerate((-1.6, -0.8, 0.0, 0.8, 1.6)):
    if x == -1.6:
        continue                                  # door is on the port side of the front face
    box(f"Window{i}", (x + 0.3, -6.98, 1.55), (0.55, 0.05, 0.7), M["window"])
box("Door", (-1.75, -6.97, 1.0), (0.8, 0.06, 2.0), M["window"])         # open, lit doorway (port side)
cyl("Wheel", (0, -8.2, 1.2), 0.45, 0.06, M["rail"], rot=(math.radians(90), 0, 0), v=16)
# upper gallery railing on the roof
for name, a, b in (("GalFront", (-2.6, -6.9), (2.6, -6.9)), ("GalBack", (-2.6, -11.1), (2.6, -11.1)),
                   ("GalPort", (-2.6, -11.1), (-2.6, -6.9)), ("GalStbd", (2.6, -11.1), (2.6, -6.9))):
    a3, b3 = Vector((*a, 0)), Vector((*b, 0))
    d = b3 - a3
    mid = (a3 + b3) / 2
    ang = math.atan2(d.x, d.y)
    box(name, (mid.x, mid.y, 3.65), (0.10, d.length, 0.10), M["rail"], rot=(0, 0, -ang))
    n = max(2, int(d.length / 0.5))
    for k in range(n + 1):
        p = a3 + d * (k / n)
        box(f"{name}_p{k}", (p.x, p.y, 3.2), (0.08, 0.08, 0.8), M["rail"])

# ---------------------------------------------------------------- mast (y = 2, one only), lantern at its foot, stays
cyl("Mast", (0, 2.0, 4.5), 0.2, 9.0, M["mast"])
cyl("MastCollar", (0, 2.0, 0.35), 0.42, 0.7, M["rail"], v=16)
# the boom (the "pole"): fixed along the centreline from the mast back toward the deckhouse, as on the @uru sheet.
# It never moves or falls; the prompt must say where it is.
box("Boom", (0, -2.3, 2.9), (0.16, 8.6, 0.16), M["mast"], rot=(math.radians(-2), 0, 0))
for name, top, foot in (("StayFwd", (0, 2, 8.8), (0, 12.6, 0.9)), ("StayPort", (0, 2, 8.8), (-3.0, 0.5, 0.9)),
                        ("StayStbd", (0, 2, 8.8), (3.0, 0.5, 0.9))):
    t, f = Vector(top), Vector(foot)
    d = t - f
    cyl(name, (f + t) / 2, 0.02, d.length, M["rope"], rot=d.to_track_quat("Z", "Y").to_euler(), v=6)
cyl("Lantern", (0, 1.55, 0.18), 0.09, 0.3, M["lantern"])
bpy.ops.object.light_add(type="POINT", location=(0, 1.55, 0.5))
bpy.context.object.name = "LanternLight"
bpy.context.object.data.energy = 60
bpy.context.object.data.color = (1.0, 0.6, 0.25)
torus("RopeCoil1", (-1.0, 2.6, 0.08), 0.45, M["rope"])
torus("RopeCoil2", (1.1, 1.0, 0.08), 0.40, M["rope"])
torus("RopeCoil3", (-1.2, 9.6, 0.08), 0.45, M["rope"])
torus("RopeCoil4", (1.2, 9.6, 0.08), 0.45, M["rope"])

# ---------------------------------------------------------------- lashed sacks: centre (1.7, 3.4), 1.4 x 1.8 x 1.0 (starboard, forward of the mast)
k = 0
for iz in range(2):
    for ix in range(2):
        for iy in range(3):
            box(f"Sack{k}", (1.7 - 0.35 + ix * 0.7, SACKS_Y - 0.6 + iy * 0.6, 0.25 + iz * 0.5), (0.66, 0.56, 0.46), M["sack"])
            k += 1
box("SackRope1", (1.7, SACKS_Y, 1.02), (1.45, 0.06, 0.04), M["rope"])
box("SackRope2", (1.7, SACKS_Y, 1.02), (0.06, 1.85, 0.04), M["rope"])

# ---------------------------------------------------------------- people (low-poly mannequins)
def lying(name, pos, head_deg, torso_m, legs_m, hair_m, extra=None):
    """Body along the head direction; head_deg 0 = head toward the bow, 90 = to starboard, 270 = to port... measured clockwise from forward."""
    x, y = pos
    a = math.radians(head_deg)
    d = Vector((math.sin(a), math.cos(a), 0))
    rot = (0, 0, -a)
    box(f"{name}_mat", (x, y, 0.02), (0.75, 1.9, 0.04), M["mat"], rot=rot)
    box(f"{name}_torso", Vector((x, y, 0.16)) + d * 0.3, (0.42, 0.62, 0.22), torso_m, rot=rot)
    box(f"{name}_legs", Vector((x, y, 0.12)) - d * 0.45, (0.34, 0.85, 0.16), legs_m, rot=rot)
    h = sph(f"{name}_head", Vector((x, y, 0.16)) + d * 0.8, 0.11, M["skin"])
    sph(f"{name}_hair", Vector((x, y, 0.20)) + d * 0.84, 0.10, hair_m)
    if extra:
        extra(Vector((x, y, 0.16)) + d * 0.8, d, rot)

def standing(name, pos, face_deg, torso_m, legs_m, hair_m):
    x, y = pos
    a = math.radians(face_deg)
    rot = (0, 0, -a)
    box(f"{name}_legs", (x, y, 0.45), (0.34, 0.24, 0.9), legs_m, rot=rot)
    box(f"{name}_torso", (x, y, 1.2), (0.44, 0.26, 0.6), torso_m, rot=rot)
    sph(f"{name}_head", (x, y, 1.62), 0.11, M["skin"])
    sph(f"{name}_hair", (x, y, 1.68), 0.10, hair_m)

# Raghavan: on his back mid-deck just in front of the deckhouse; checked towel round his NECK (never on his eyes)
lying("Raghavan", (0, -4.6), 270, M["white"], M["white"], M["greyhair"],
      extra=lambda hp, d, rot: box("Raghavan_towel_NECK", hp - d * 0.2 + Vector((0, 0, 0.02)), (0.36, 0.14, 0.12), M["redcheck"], rot=rot))
# Babu: on his side near the port rail, head to port... map: head 270, facing the bow; towel tied on his HEAD (round the forehead)
lying("Babu", (-2.1, -1.6), 270, M["cream"], M["check"], M["hair"],
      extra=lambda hp, d, rot: box("Babu_towel_HEAD", hp + Vector((0, 0, 0.05)), (0.26, 0.26, 0.08), M["redcheck"], rot=rot))
# Sasi: curled on the bow side of the sacks
lying("Sasi", (2.0, SACKS_Y + 1.1), 270, M["cream"], M["white"], M["hair"])
# Antony: at the starboard bulwark of the bow, facing forward
standing("Antony", (2.2, 11.5), 0, M["antony"], M["greencheck"], M["hair"])
# Aashaan: at the wheel inside (hidden from the high camera by the roof)
standing("Aashaan", (0, -8.6), 0, M["cream"], M["white"], M["greyhair"])

# ---------------------------------------------------------------- moon (high, ahead-RIGHT, ~35 deg up) and the fire (ahead-LEFT, ~500 m)
# The distances sheet says about 35 deg up; frames 01, 02 and the take show it about 7 deg up and about
# 25 deg right of the bow (measured from the frames). The blocking follows the frames.
az, el, R = math.radians(25), math.radians(7), 600
moon_dir = Vector((math.sin(az) * math.cos(el), math.cos(az) * math.cos(el), math.sin(el)))
sph("Moon", moon_dir * R, 9, M["moon"], seg=24)
bpy.ops.object.light_add(type="SUN", location=(0, 0, 20))
sun = bpy.context.object
sun.name = "Moonlight"
sun.data.energy = 1.4
sun.data.use_shadow = False      # no big boat shadow spread on the sea
sun.data.color = (0.65, 0.75, 1.0)
sun.rotation_euler = (-moon_dir).to_track_quat("-Z", "Y").to_euler()
faz = math.radians(-35)
fire = sph("Fire_500m", (500 * math.sin(faz), 500 * math.cos(faz), -1.5), 3.0, M["fire"])
# the fire is not there until 13.5 s (frame 324): scale 0 -> 1
fire.scale = (0, 0, 0); fire.keyframe_insert("scale", frame=323)
fire.scale = (1, 1, 1); fire.keyframe_insert("scale", frame=330)

# ---------------------------------------------------------------- world
w = bpy.data.worlds.new("Night")
sc.world = w
w.use_nodes = True
w.node_tree.nodes["Background"].inputs[0].default_value = (0.015, 0.03, 0.07, 1)
w.node_tree.nodes["Background"].inputs[1].default_value = 0.8

# ---------------------------------------------------------------- cameras
def make_cam(name, lens_fov):
    bpy.ops.object.camera_add()
    c = bpy.context.object
    c.name = name
    c.data.sensor_fit = "HORIZONTAL"
    c.data.sensor_width = 36
    c.data.angle = math.radians(lens_fov)
    c.data.clip_end = 3000
    return c

def aim(cam, pos, look, frame):
    cam.location = pos
    d = Vector(look) - Vector(pos)
    cam.rotation_euler = d.to_track_quat("-Z", "Y").to_euler()
    cam.keyframe_insert("location", frame=frame)
    cam.keyframe_insert("rotation_euler", frame=frame)

# Shot 1 (0.0-15.75 s): drone glide from ~40 m behind and 15 m above the stern, forward and down,
# settling just behind and above the deckhouse roof railing at 9.0 s, then a slow hold.
c1 = make_cam("CAM1_drone", 80)   # frames 01/02 fit the moon, horizon and deck only at about 80 deg
path = [  # frame, position, look-at
    # look-at heights keep the horizon about a quarter down the frame, as in frames 01 and 02
    # starts a little to starboard of the stern, as frame 01 (the boat's right side and stern in view), and
    # swings onto the centreline as it closes in
    (1,   (7.0, -34.0, 13.0), (0.0, 4.0, 4.0)),
    (72,  (4.5, -28.0, 11.0), (0.0, 6.0, 3.4)),
    (144, (1.5, -21.0, 8.6),  (0.0, 7.0, 2.8)),
    (216, (0.0, -13.6, 6.6),  (0.0, 7.0, 2.4)),    # 9.0 s: arrives above the deckhouse railing
    (378, (0.0, -12.9, 6.4),  (0.0, 7.0, 2.3)),    # 15.75 s: tiny settle, no further move
]
for f, p, l in path:
    aim(c1, p, l, f)
for fc in c1.animation_data.action.fcurves if hasattr(c1.animation_data.action, "fcurves") else []:
    for kp in fc.keyframe_points:
        kp.interpolation = "BEZIER"
        kp.easing = "AUTO"

# Shot 2 (15.75-30 s): main deck looking aft, Ranjith's c1 (map): (-0.6, 9.5, 1.7) -> (0, -8, 1.2), 64 deg, locked.
# framed like @s21sh01startfullmoon: sacks and Sasi at the left, the mast left of centre, the deckhouse and
# its lit door in the middle, Babu by the port rail at the right. Positions stay those of the map.
c2 = make_cam("CAM2_c1_aft", 70)
aim(c2, (-1.4, 9.0, 1.6), (0.6, -8.0, 1.0), 1)


# a top camera for the plan view still
top = make_cam("CAM_top", 50)
top.data.type = "ORTHO"
top.data.ortho_scale = 30
top.location = (0, 1, 60)
top.rotation_euler = (0, 0, 0)                     # straight down, bow at the top of the image

# ---------------------------------------------------------------- render settings: grey-box, readable
r = sc.render
r.resolution_x, r.resolution_y = (1280, 548) if PREVIEW else (2206, 946)
r.resolution_percentage = 100
eng = [e.identifier for e in bpy.types.RenderSettings.bl_rna.properties["engine"].enum_items]
r.engine = "BLENDER_EEVEE_NEXT" if "BLENDER_EEVEE_NEXT" in eng else ("BLENDER_EEVEE" if "BLENDER_EEVEE" in eng else "BLENDER_WORKBENCH")
try:
    sc.view_settings.view_transform = "Standard"
    sc.view_settings.exposure = 1.2
except Exception:
    pass

def still(cam, frame, fn):
    sc.camera = cam
    sc.frame_set(frame)
    r.filepath = os.path.join(OUT, fn)
    r.image_settings.file_format = "PNG"
    bpy.ops.render.render(write_still=True)

# stills: start, end of the glide, shot 2, plan view
still(c1, 1, "still-shot1-start.png")
still(c1, 216, "still-shot1-end.png")
still(c2, 400, "still-shot2.png")
top_prev = r.resolution_x, r.resolution_y
r.resolution_x, r.resolution_y = 1000, 1000
still(top, 1, "still-topview.png")
r.resolution_x, r.resolution_y = top_prev

# camera switching with markers (after the stills, so they do not override the still cameras)
m1 = sc.timeline_markers.new("shot1", frame=1); m1.camera = c1
m2 = sc.timeline_markers.new("shot2", frame=CUT + 1); m2.camera = c2
sc.camera = c1
sc.frame_set(1)
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUT, "blocking.blend"))

if not (len(argv) > 2 and argv[2] == "nomovie"):
    if hasattr(r.image_settings, "media_type"):      # Blender 5.x: video is a media type
        r.image_settings.media_type = "VIDEO"
    r.image_settings.file_format = "FFMPEG"
    r.ffmpeg.format = "MPEG4"
    r.ffmpeg.codec = "H264"
    r.ffmpeg.constant_rate_factor = "MEDIUM"
    r.filepath = os.path.join(OUT, "blocking-playblast.mp4")
    bpy.ops.render.render(animation=True)
print("DONE", OUT, r.engine)
