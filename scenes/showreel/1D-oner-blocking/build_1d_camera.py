# 1D-oner CAMERA-ONLY blocking (v2, 2026-11-12): the same 14 s take as build_1d.py with NO people in it, so the video
# model copies only the space and the camera move, not the grey-box figures' stiff motion.
# The camera flies one smooth curve: keyed positions and a keyed look-at target with Bezier (auto-clamped) easing,
# no follow-lag, no float, motion blur on. Beats and timing are the same as v1.
# Run: /Applications/Blender.app/Contents/MacOS/Blender -b -P build_1d_camera.py -- <out_dir> [nomovie]
import bpy, math, sys, os
from mathutils import Vector

argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
OUT = os.path.abspath(argv[0] if argv else os.path.dirname(__file__))
NOMOVIE = "nomovie" in argv
HERE = os.path.dirname(os.path.abspath(__file__))
bpy.ops.wm.open_mainfile(filepath=os.path.abspath(os.path.join(HERE, "..", "..", "..", "locations", "house-3d", "house.blend")))
os.makedirs(OUT, exist_ok=True)
sc = bpy.context.scene
FPS, DUR, FL = 24, 14.0, 0.45
sc.render.fps = FPS
sc.frame_start, sc.frame_end = 1, int(DUR * FPS)
EYE = FL + 1.5

# the kitchen double doors stand wide open, flat against the end wall of the passage, so the doorway is clear
for nm, x in (("Door_kit_L", -0.9), ("Door_kit_R", 0.9)):
    d = bpy.data.objects.get(nm)
    if d:
        d.location = (x, 4.84, d.location.z)
        d.rotation_euler = (0, 0, 0)

# (time, camera position, where it looks). Antony's beats, for the prompt: 0-3.8 in the middle of his room (listens,
# scratches his head, tugs the mundu knot); 3.8-5.5 to his door; 5.5-6.5 through it and LEFT; 6.5-11.5 up the
# passage; 11.5-14 stops in the kitchen doorway, his mother at the stove back-left.
KEYS = [
    (0.0,  (-1.35, 4.70, EYE),        (-3.35, 0.7, FL + 1.05)),   # NE corner by the trunk: the front window, the clock, the cot at right
    (3.8,  (-1.50, 4.35, EYE),        (-3.30, 0.9, FL + 1.05)),   # a barely-there creep forward while he stands
    (5.5,  (-2.10, 2.45, EYE),        (-1.00, 0.95, FL + 1.25)),  # pans LEFT and moves after him toward his door
    (6.6,  (-1.75, 0.98, EYE),        ( 0.60, 1.30, FL + 1.30)),  # at his door, looking out into the passage
    (7.8,  ( 0.00, 0.95, EYE),        ( 0.15, 6.50, FL + 1.25)),  # through the door, turning left up the passage
    (11.5, ( 0.30, 3.55, EYE + 0.02), ( 0.00, 8.00, FL + 1.15)),  # up the passage, the open kitchen doors ahead
    (14.0, ( 0.62, 4.32, EYE + 0.05), (-2.10, 7.00, FL + 1.00)),  # eases to a stop at the doorway: the stove back-left
]

bpy.ops.object.camera_add()
cam = bpy.context.object
cam.name = "CAM_1D_oner_v2"
cam.data.sensor_fit = "HORIZONTAL"
cam.data.angle = math.radians(75)
cam.data.clip_start = 0.05
sc.camera = cam
tgt = bpy.data.objects.new("CAM_1D_oner_v2_target", None)
sc.collection.objects.link(tgt)
con = cam.constraints.new("TRACK_TO")
con.target = tgt
con.track_axis, con.up_axis = "TRACK_NEGATIVE_Z", "UP_Y"

for t, p, l in KEYS:
    f = 1 + round(t * FPS)
    cam.location, tgt.location = p, l
    cam.keyframe_insert("location", frame=f)
    tgt.keyframe_insert("location", frame=f)
for o in (cam, tgt):
    ad = o.animation_data
    act = ad.action
    curves = []
    try:
        curves = list(act.fcurves)
    except Exception:
        for layer in act.layers:                       # Blender 5 layered actions
            for strip in layer.strips:
                for bag in strip.channelbags:
                    curves += list(bag.fcurves)
    for fc in curves:
        for kp in fc.keyframe_points:
            kp.interpolation = "BEZIER"
            kp.handle_left_type = kp.handle_right_type = "AUTO_CLAMPED"
        fc.update()

r = sc.render
r.resolution_x, r.resolution_y, r.resolution_percentage = 1280, 548, 100
r.use_motion_blur = True
try:
    r.motion_blur_shutter = 0.5
    sc.eevee.taa_render_samples = 24
except Exception:
    pass
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUT, "1d-oner-camera-v2.blend"))
for t_, nm in ((0.5, "v2-still-0.5s-room-clock"), (4.8, "v2-still-4.8s-pan-to-door"), (6.6, "v2-still-6.6s-door"),
               (9.0, "v2-still-9s-passage"), (13.5, "v2-still-13.5s-kitchen-doorway")):
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
    r.ffmpeg.constant_rate_factor = "HIGH"
    r.filepath = os.path.join(OUT, "1d-oner-camera-v2.mp4")
    bpy.ops.render.render(animation=True)
print("DONE", OUT)
