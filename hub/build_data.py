#!/usr/bin/env python3
"""Builds hub/data.json for the AAZHI Memory Hub from the repo and its git history.

Run from anywhere inside the repo:  python3 hub/build_data.py
The GitHub Action runs it on every push; the page reads the JSON it writes.
"""
import json, os, re, subprocess, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = "ananthuvj99/Aazhi-bible"
RAW = f"https://raw.githubusercontent.com/{REPO}/main/"
PEOPLE = ["Ananthu", "Ranjith", "Aswanth"]
ALIASES = {
    "ananthu": "Ananthu", "anandu": "Ananthu", "ananthuvj99": "Ananthu",
    "ranjith": "Ranjith", "renjith": "Ranjith", "ranjit": "Ranjith",
    "aswanth": "Aswanth", "ashwanth": "Aswanth", "ashwin": "Aswanth",
}
KINDS = ["asset", "lesson", "win", "shot", "continuity", "rule", "plan", "story", "undo"]


def git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True).stdout


def person(name):
    return ALIASES.get((name or "").strip().lower())


def credit(subject, author):
    """Who a commit belongs to: the 'Name:' prefix wins, then the git author.
    Early un-prefixed commits by 'Claude' were made in Ananthu's sessions."""
    m = re.match(r"\s*([A-Za-z]+)(?:\s*\([^)]*\))?\s*:", subject)
    if m and person(m.group(1)):
        return person(m.group(1))
    m = re.search(r"for (\w+)", author)
    if m and person(m.group(1)):
        return person(m.group(1))
    return person(author) or ("Ananthu" if author.startswith("Claude") else author)


def kind_of(subject):
    s = re.sub(r"^\s*[A-Za-z]+(?:\s*\([^)]*\))?\s*:\s*", "", subject).lower()
    for k in KINDS:
        if s.startswith(k):
            return k
    if re.search(r"\b[LW]\d+\b", subject):
        return "lesson" if re.search(r"\bL\d+\b", subject) else "win"
    if re.search(r"\bv\d|approved|prompt", s):
        return "shot"
    if re.search(r"checklist|rule|style|claude\.md", s):
        return "rule"
    if re.search(r"@\w|asset|sheet|plate|registry", s):
        return "asset"
    if "ledger" in s or "continuity" in s:
        return "continuity"
    return "other"


def commits():
    out = git("log", "--all", "--date-order", "--format=\x1e%H|%h|%at|%an|%P|%s", "--numstat")
    seen, items = set(), []
    for block in out.split("\x1e")[1:]:
        lines = block.strip("\n").split("\n")
        full, short, ts, author, parents, subject = lines[0].split("|", 5)
        if full in seen:
            continue
        seen.add(full)
        add = rem = files = 0
        for ln in lines[1:]:
            parts = ln.split("\t")
            if len(parts) == 3:
                files += 1
                add += int(parts[0]) if parts[0].isdigit() else 0
                rem += int(parts[1]) if parts[1].isdigit() else 0
        items.append({
            "sha": short, "t": int(ts), "who": credit(subject, author), "author": author,
            "msg": subject, "kind": kind_of(subject), "merge": len(parents.split()) > 1,
            "add": add, "del": rem, "files": files,
        })
    items.sort(key=lambda c: -c["t"])
    return items


def md_tables(text):
    """Yields (section heading, list of row dicts) for every pipe table."""
    section, header, rows = "", None, []
    for line in text.split("\n") + [""]:
        if line.startswith("#"):
            section = line.lstrip("#").strip()
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if header is None:
                header = cells
            elif not set("".join(cells)) <= set("-: "):
                rows.append(dict(zip(header, cells)))
        elif header is not None:
            yield section, rows
            header, rows = None, []


def strip_front(text):
    return re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S).strip()


def learnings():
    text = (ROOT / "learnings/INDEX.md").read_text()
    items = []
    for _, rows in md_tables(text):
        for r in rows:
            if not r.get("ID", "").strip():
                continue
            m = re.search(r"\(([^)]+\.md)\)", r.get("File", ""))
            body = ""
            if m and (ROOT / "learnings" / m.group(1)).exists():
                body = strip_front((ROOT / "learnings" / m.group(1)).read_text())
            items.append({
                "id": r["ID"], "type": r.get("Type", ""), "category": r.get("Category", ""),
                "title": r.get("Title", ""), "shot": r.get("Shot", ""),
                "who": person(r.get("Author", "")) or r.get("Author", ""),
                "date": r.get("Date", ""), "body": body,
            })
    return items


def assets():
    text = (ROOT / "INDEX.md").read_text()
    items = []
    for section, rows in md_tables(text):
        for r in rows:
            rid = r.get("ID", "").replace("`", "").strip()
            files = re.findall(r"`([^`]+\.(?:png|jpe?g|webp))`", r.get("File", ""))
            path = files[0] if files else ""
            items.append({
                "group": section, "id": rid or "—", "shows": r.get("Shows", ""),
                "attach": r.get("Attach when", ""), "file": path,
                "img": RAW + path if path and (ROOT / path).exists() else "",
                "who": person(re.split(r"[ (]", r.get("Created by", "").strip())[0]) or r.get("Created by", ""),
                "date": r.get("Date", ""), "status": r.get("Status", ""),
            })
    return items


SCENES = [
    (r"^1", "Scene 1", "SB014", "Antony oversleeps; Amma from the kitchen"),
    (r"^2", "Scene 2", "SB015", "Ten days — Amma makes him eat"),
    (r"^(3-|scene3)", "Scene 3", "SB016–017", "Clara's classroom (yard version)"),
    (r"^s11", "Scene 11", "SB016", "Tuition — Antony at the door"),
    (r"^s13", "Scene 13", "SB019–020", "The harbour; reaching the uru"),
    (r"^SB023", "SB023", "SB023", "Aashaan's confidence"),
]


def classify(line):
    l = line.lower()
    tag = re.search(r"\[(approved|partial|failed)\]", l)
    if tag:
        return tag.group(1)
    if re.search(r"almost|partial|nearly", l):
        return "partial"
    if re.search(r"approv|came out (good|great|really well|well)|this is good|\bkept\b|worked", l):
        return "approved"
    if re.search(r"fail|wrong|broke|stiff|collapsed|error|robotic|didn.t|drift|retired", l):
        return "failed"
    return "partial"


def blame_lines(f):
    """Line text -> (time, person) of the commit that wrote it, so each logged take has a date."""
    out, info, cur = {}, {}, None
    for ln in git("blame", "--line-porcelain", "--", str(f.relative_to(ROOT))).split("\n"):
        m = re.match(r"^([0-9a-f]{40}) \d+ \d+", ln)
        if m:
            cur = info.setdefault(m.group(1), {})
        elif ln.startswith("author ") and cur is not None:
            cur["author"] = ln[7:]
        elif ln.startswith("author-time ") and cur is not None:
            cur["t"] = int(ln[12:])
        elif ln.startswith("summary ") and cur is not None:
            cur["summary"] = ln[8:]
        elif ln.startswith("\t") and cur is not None:
            out[ln[1:].strip()] = (cur.get("t", 0), credit(cur.get("summary", ""), cur.get("author", "")))
    return out


def storyboard_titles():
    text = (ROOT / "storyboard/aazhi-storyboard.md").read_text()
    return {m.group(1): m.group(2).strip() for m in re.finditer(r"^### (SB\d{3}) · [^—]*— ([^·\n]+)", text, re.M)}


def scene_of(msg, titles):
    """The storyboard panel or showreel scene a commit is about, or None."""
    m = re.search(r"\b(SB\d{3})\b", msg)
    if m:
        return {"sb": m.group(1), "label": f"{m.group(1)} · {titles.get(m.group(1), '')}".strip(" ·")}
    m = re.search(r"\b(s\d{2}-sh\d{2}|[123][A-D](?:-[a-z0-9]+)?|[23]-(?:\d|PART-[AB]|ALL|SINGLES))\b", msg)
    if m:
        # the shot file's title usually names its storyboard panel ("… SB021 part 3 …")
        f = ROOT / "scenes/showreel" / f"{m.group(1)}.md"
        if f.exists():
            sbm = re.search(r"\b(SB\d{3})\b", f.read_text().split("\n", 1)[0])
            if sbm:
                return {"sb": sbm.group(1), "label": f"{sbm.group(1)} · {titles.get(sbm.group(1), '')}".strip(" ·"), "shot": m.group(1)}
        for p, name, sb, desc in SCENES:
            if re.match(p, m.group(1)):
                return {"sb": sb, "label": f"{name} · {desc}", "shot": m.group(1)}
    return None


def shots():
    items = []
    for f in sorted((ROOT / "scenes/showreel").glob("*.md")):
        name = f.stem
        if name in ("plan", "1C-1D-edit-plan"):
            continue
        text = f.read_text()
        title = text.split("\n", 1)[0].lstrip("# ").strip()
        sm = re.search(r"^Status:\s*(.+)$", text, re.M)
        status_text = re.sub(r"[*`]", "", sm.group(1)).strip() if sm else ""
        s = status_text.lower()
        status = ("approved" if "approved" in s else "proposal" if "proposal" in s else
                  "ready" if "ready" in s else "draft" if "draft" in s else
                  "spare" if "not needed" in s else "script" if not s else "other")
        qa = re.search(r"QA (\d{2,3})", status_text)
        gens = []
        res = re.search(r"## Generation results\n(.*?)(?:\n## |\Z)", text, re.S)
        if res:
            blame = blame_lines(f)
            for ln in res.group(1).split("\n"):
                ln = ln.strip()
                if ln.startswith("- ") and "none yet" not in ln and not ln.startswith("- 20"):
                    t, who = blame.get(ln, (0, ""))
                    gens.append({"text": ln[2:], "result": classify(ln), "t": t, "who": who})
        add_log = git("log", "--diff-filter=A", "--format=%s|%an", "--", str(f.relative_to(ROOT))).strip().split("\n")
        owner = credit(*add_log[-1].split("|", 1)) if add_log and "|" in add_log[-1] else "Ananthu"
        last = git("log", "-1", "--format=%at", "--", str(f.relative_to(ROOT))).strip()
        scene = next(((n, sb, d) for p, n, sb, d in SCENES if re.match(p, name)), ("Other", "", ""))
        items.append({
            "id": name, "title": title, "status": status, "statusText": status_text,
            "qa": int(qa.group(1)) if qa else None, "gens": gens, "owner": owner,
            "updated": int(last) if last else 0, "scene": scene[0], "sb": scene[1], "sceneDesc": scene[2],
        })
    return items


def plan_scenes():
    """Rows of the scene table in scenes/showreel/plan.md. A scene counts as completed
    when its Status cell says complete, completed, done or final."""
    text = (ROOT / "scenes/showreel/plan.md").read_text()
    for _, rows in md_tables(text):
        if rows and "Scene" in rows[0] and "Status" in rows[0]:
            return [{
                "scene": r["Scene"], "beat": r.get("Beat", ""), "sb": r.get("Storyboard", ""),
                "status": r["Status"],
                "done": bool(re.search(r"\b(complete|completed|done|final)\b", r["Status"], re.I)),
            } for r in rows]
    return []


def now_working(all_commits):
    """team/now.md lines like '- Ranjith: s13-sh02 — the approach to the uru' win;
    otherwise each person's latest shot commit."""
    out = {}
    nf = ROOT / "team/now.md"
    if nf.exists():
        for m in re.finditer(r"^[-*]\s*(\w+)\s*[:—-]\s*(.+)$", nf.read_text(), re.M):
            if person(m.group(1)):
                out[person(m.group(1))] = {"text": m.group(2).strip(), "source": "now.md"}
    titles = storyboard_titles()
    for p in PEOPLE:
        mine = [c for c in all_commits if c["who"] == p and not c["merge"]]
        if p not in out:
            c = next((c for c in mine if c["kind"] == "shot"), None) or (mine[0] if mine else None)
            if c:
                text = re.sub(r"^\s*[A-Za-z]+:\s*(shot:\s*)?", "", c["msg"])
                out[p] = {"text": text, "source": "last commit", "t": c["t"]}
        # the scene: from now.md text first, else the latest commit that names one
        sc = scene_of(out[p]["text"], titles) if p in out else None
        if not sc:
            sc = next((s for s in (scene_of(c["msg"], titles) for c in mine) if s), None)
        if p in out and sc:
            out[p]["scene"] = sc
    return out


DOCS = [
    ("CLAUDE.md", "How every session works"),
    ("rules/workflow.md", "Team workflow"),
    ("rules/prompt-rules.md", "Prompt rules"),
    ("rules/pre-delivery-checklist.md", "Pre-delivery checklist"),
    ("rules/style-cinema-camera.md", "Camera & style block"),
    ("continuity/showreel.md", "Continuity ledger"),
    ("scenes/showreel/plan.md", "Showreel plan"),
    ("ONBOARDING.md", "Onboarding"),
]


def main():
    cs = commits()
    data = {
        "repo": REPO, "built": int(time.time()), "head": git("rev-parse", "--short", "HEAD").strip(),
        "people": PEOPLE, "commits": cs, "learnings": learnings(), "assets": assets(), "shots": shots(),
        "now": now_working(cs), "scenes": plan_scenes(),
        "docs": [{"path": p, "title": t, "text": (ROOT / p).read_text()} for p, t in DOCS if (ROOT / p).exists()],
        "storyboardPanels": len(re.findall(r"^### SB\d+", (ROOT / "storyboard/aazhi-storyboard.md").read_text(), re.M)),
    }
    out = ROOT / "hub/data.json"
    out.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")))
    print(f"hub/data.json: {len(cs)} commits, {len(data['learnings'])} learnings, "
          f"{len(data['assets'])} assets, {len(data['shots'])} shots, {out.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
