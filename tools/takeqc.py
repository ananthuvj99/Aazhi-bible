"""Frame-by-frame QC sheet for a generated take (L147).

Pulls one frame every N seconds (default 1) from a video, stamps each with its time,
and tiles them into contact sheets, so every second of the take can be checked against
the prompt, the keyframe plates, the measured map and MEMORY.

Usage:  python tools/takeqc.py <video.mp4> <out_prefix> [every_seconds]
Writes: <out_prefix>-01.jpg, -02.jpg ... (16 frames per sheet). Needs ffmpeg on the PATH.
"""
import os, subprocess, sys, tempfile, glob
from PIL import Image, ImageDraw, ImageFont

def main(video, prefix, every=1.0):
    every = float(every)
    tmp = tempfile.mkdtemp()
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', video, '-vf', f'fps=1/{every},scale=640:-1',
                    os.path.join(tmp, 'f%04d.png')], check=True)
    frames = sorted(glob.glob(os.path.join(tmp, 'f*.png')))
    try:
        font = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 26)
    except OSError:
        font = ImageFont.load_default()
    per = 16
    for s in range(0, len(frames), per):
        chunk = frames[s:s + per]
        w, h = Image.open(chunk[0]).size
        sheet = Image.new('RGB', (w * 4, h * ((len(chunk) + 3) // 4)), 'black')
        for i, f in enumerate(chunk):
            im = Image.open(f).convert('RGB')
            d = ImageDraw.Draw(im)
            t = (s + i) * every
            d.rectangle([0, 0, 120, 36], fill='black')
            d.text((8, 3), f'{t:05.1f}s', font=font, fill='#ffd24a')
            sheet.paste(im, ((i % 4) * w, (i // 4) * h))
        out = f'{prefix}-{s // per + 1:02d}.jpg'
        sheet.save(out, quality=85)
        print(out)

if __name__ == '__main__':
    main(*sys.argv[1:])
