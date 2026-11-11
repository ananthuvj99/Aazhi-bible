"""List platform IDs used in shot files that have no row in INDEX.md (L143).

Usage: python tools/unregistered-ids.py
"""
import io, os, re, glob

index = io.open('INDEX.md', encoding='utf-8').read()
registered = set(re.findall(r'^\| `(@[a-z0-9]+)`', index, re.M))
used = {}
for f in glob.glob('scenes/**/*.md', recursive=True):
    if os.sep + 'retired' + os.sep in f or '/retired/' in f:
        continue
    for i in set(re.findall(r'(?<![\w@])@([a-z][a-z0-9]{2,})\b', io.open(f, encoding='utf-8').read())):
        used.setdefault('@' + i, []).append(os.path.basename(f))
missing = {k: v for k, v in used.items() if k not in registered}
if not missing:
    print('Every ID used in the shot files is in INDEX.md.')
for k in sorted(missing):
    print(f'{k}  (in {len(missing[k])} files, e.g. {", ".join(sorted(missing[k])[:4])})')
