#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        fail(f"{path.relative_to(ROOT)}: missing YAML frontmatter")
        return {}
    try:
        end = lines.index("---", 1)
    except ValueError:
        fail(f"{path.relative_to(ROOT)}: unterminated YAML frontmatter")
        return {}

    data: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip():
            continue
        if ":" not in line:
            fail(f"{path.relative_to(ROOT)}: invalid frontmatter line: {line!r}")
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def check_local_links(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    for target in LINK_RE.findall(text):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        target = target.split("#", 1)[0]
        if not target:
            continue
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            fail(f"{path.relative_to(ROOT)}: broken local link -> {target}")


if not SKILLS.is_dir():
    fail("skills/: missing")
else:
    for skill_dir in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        skill = skill_dir.name
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.is_file():
            fail(f"skills/{skill}: missing SKILL.md")
            continue

        meta = parse_frontmatter(skill_md)
        if set(meta) != {"name", "description"}:
            fail(f"skills/{skill}/SKILL.md: frontmatter must contain only name + description")
        if meta.get("name") != skill:
            fail(f"skills/{skill}/SKILL.md: name must match directory")
        if not NAME_RE.match(skill):
            fail(f"skills/{skill}: invalid kebab-case skill name")
        if not meta.get("description", "").strip():
            fail(f"skills/{skill}/SKILL.md: empty description")

        check_local_links(skill_md)

        ui = skill_dir / "agents" / "openai.yaml"
        if not ui.is_file():
            fail(f"skills/{skill}: missing agents/openai.yaml")
        else:
            ui_text = ui.read_text(encoding="utf-8")
            for required in ("display_name:", "short_description:", "default_prompt:"):
                if required not in ui_text:
                    fail(f"skills/{skill}/agents/openai.yaml: missing {required[:-1]}")

        adapted = skill_md.read_text(encoding="utf-8")
        banned = {
            "disable-model-invocation:": "Claude-only frontmatter",
            "EnterPlanMode": "Claude-only tool name",
            "ExitPlanMode": "Claude-only tool name",
            "AskUserQuestion": "Claude-only tool name",
        }
        for token, reason in banned.items():
            if token in adapted:
                fail(f"skills/{skill}/SKILL.md: contains {reason}: {token}")

plugin = ROOT / "plugin.json"
if not plugin.is_file():
    fail("plugin.json: missing")
else:
    try:
        payload = json.loads(plugin.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"plugin.json: invalid JSON: {exc}")
    else:
        if payload.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
            fail("plugin.json: unexpected schema")
        if payload.get("name") != "modern-software-codex-skills":
            fail("plugin.json: unexpected plugin name")
        if not payload.get("version"):
            fail("plugin.json: missing version")


# Validate activation cases.
evals = ROOT / "evals" / "cases.jsonl"
if not evals.is_file():
    fail("evals/cases.jsonl: missing")
else:
    known = {p.name for p in SKILLS.iterdir() if p.is_dir()}
    for lineno, line in enumerate(evals.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            case = json.loads(line)
        except json.JSONDecodeError as exc:
            fail(f"evals/cases.jsonl:{lineno}: invalid JSON: {exc}")
            continue
        if case.get("skill") not in known:
            fail(f"evals/cases.jsonl:{lineno}: unknown skill {case.get('skill')!r}")
        if case.get("expected") not in {"trigger", "skip"}:
            fail(f"evals/cases.jsonl:{lineno}: expected must be trigger or skip")
        if not isinstance(case.get("prompt"), str) or not case["prompt"].strip():
            fail(f"evals/cases.jsonl:{lineno}: prompt must be non-empty")

for doc in (ROOT / "README.md", ROOT / "SOURCE-MAP.md", ROOT / "NOTICE.md"):
    if doc.is_file():
        check_local_links(doc)
    else:
        fail(f"{doc.name}: missing")

if errors:
    print("validation failed", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    sys.exit(1)

count = len([p for p in SKILLS.iterdir() if p.is_dir()])
print(f"ok: {count} skills, plugin manifest, local links, UI metadata")
