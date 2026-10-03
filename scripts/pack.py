#!/usr/bin/env python3
from __future__ import annotations

import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
SKILLS = ROOT / "skills"

if DIST.exists():
    shutil.rmtree(DIST)
DIST.mkdir(parents=True)


def zip_tree(source: Path, target: Path, arc_prefix: str) -> None:
    with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(source.rglob("*")):
            if not path.is_file():
                continue
            if any(part in {"dist", ".git", "__pycache__"} for part in path.parts):
                continue
            rel = path.relative_to(source)
            zf.write(path, Path(arc_prefix) / rel)


for skill_dir in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
    zip_tree(skill_dir, DIST / f"{skill_dir.name}.zip", skill_dir.name)

repo_zip = DIST / "modern-software-codex-skills.zip"
with zipfile.ZipFile(repo_zip, "w", compression=zipfile.ZIP_DEFLATED) as zf:
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT)
        if rel.parts and rel.parts[0] in {"dist", ".git"}:
            continue
        if "__pycache__" in rel.parts:
            continue
        zf.write(path, Path(ROOT.name) / rel)

print(f"wrote {len(list(DIST.glob('*.zip')))} archives to {DIST}")
