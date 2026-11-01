#!/usr/bin/env python3
"""Static integrity checks for the six source-constrained CS146S sample adapters.

This does NOT run an agent or prove that activation prompts trigger.
"""
from __future__ import annotations

from collections import Counter
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
EXPECTED = {
    "explore",
    "research-codebase",
    "make-proposals",
    "plan",
    "implement",
    "review",
}
NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LOCAL_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def normalized(text: str) -> str:
    return text.rstrip("\n") + "\n"


def frontmatter(path: Path) -> dict[str, str]:
    lines = read(path).splitlines()
    if not lines or lines[0] != "---":
        fail(f"{path.relative_to(ROOT)}: missing YAML frontmatter")
        return {}
    try:
        end = lines.index("---", 1)
    except ValueError:
        fail(f"{path.relative_to(ROOT)}: unterminated frontmatter")
        return {}
    metadata: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip():
            continue
        if ":" not in line:
            fail(f"{path.relative_to(ROOT)}: invalid frontmatter: {line}")
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip("\"'")
    return metadata


def check_links(path: Path) -> None:
    for link in LOCAL_LINK.findall(read(path)):
        if link.startswith(("https://", "http://", "#", "mailto:")):
            continue
        relative = link.split("#", 1)[0]
        if relative and not (path.parent / relative).resolve().exists():
            fail(f"{path.relative_to(ROOT)}: broken local link {relative}")


def expected_adapter(name: str, source: str) -> str:
    # The only allowed changes are documented in SOURCE-MAP.md.
    adapted = source.replace("disable-model-invocation: true\n", "")
    adapted = adapted.replace(f"invokes /{name}", f"invokes ${name}")
    if name == "make-proposals":
        adapted = adapted.replace(
            "Keep the list to two or three distinct proposals",
            "Keep the list to at most two distinct proposals",
        )
    if name == "implement":
        adapted = adapted.replace(
            "Implement the plan described in /path/to/plan_md.",
            "Implement the plan described in the plan markdown file provided for this invocation.",
        )
    return normalized(adapted)


if not SKILLS.is_dir():
    fail("skills/: missing")
    actual: set[str] = set()
else:
    actual = {path.name for path in SKILLS.iterdir() if path.is_dir()}
if actual != EXPECTED:
    fail(f"skills/: expected {sorted(EXPECTED)}, found {sorted(actual)}")

for name in sorted(EXPECTED & actual):
    directory = SKILLS / name
    active = directory / "SKILL.md"
    source = directory / "references" / "original-SKILL.md"
    ui = directory / "agents" / "openai.yaml"
    if not active.is_file() or not source.is_file():
        fail(f"skills/{name}: missing active SKILL.md or historical source snapshot")
        continue
    metadata = frontmatter(active)
    if set(metadata) != {"name", "description"}:
        fail(f"skills/{name}: frontmatter must have name and description only")
    if metadata.get("name") != name or not NAME.fullmatch(name):
        fail(f"skills/{name}: invalid name")
    if not metadata.get("description"):
        fail(f"skills/{name}: missing trigger description")
    if normalized(read(active)) != expected_adapter(name, read(source)):
        fail(f"skills/{name}: adapter drift from the documented source transformations")
    check_links(active)
    if not ui.is_file():
        fail(f"skills/{name}: missing optional Codex UI metadata")
    else:
        for field in ("display_name:", "short_description:", "default_prompt:"):
            if field not in read(ui):
                fail(f"skills/{name}: UI metadata missing {field}")

plan_template = SKILLS / "plan" / "design_doc_template.md"
if not plan_template.is_file():
    fail("skills/plan/design_doc_template.md: missing source template")

plugin = ROOT / "plugin.json"
if not plugin.is_file():
    fail("plugin.json: missing")
else:
    try:
        data = json.loads(read(plugin))
        if data.get("name") != "modern-software-codex-skills":
            fail("plugin.json: unexpected name")
        if data.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
            fail("plugin.json: unexpected schema")
        if data.get("version") != "0.2.0":
            fail("plugin.json: version must match 0.2.0")
    except json.JSONDecodeError as exc:
        fail(f"plugin.json: invalid JSON: {exc}")

fixtures = ROOT / "evals" / "cases.jsonl"
counts: Counter[tuple[str, str]] = Counter()
if not fixtures.is_file():
    fail("evals/cases.jsonl: missing")
else:
    for line_number, line in enumerate(read(fixtures).splitlines(), 1):
        if not line.strip():
            continue
        try:
            case = json.loads(line)
        except json.JSONDecodeError as exc:
            fail(f"evals/cases.jsonl:{line_number}: {exc}")
            continue
        skill, expectation = case.get("skill"), case.get("expected")
        if skill not in EXPECTED or expectation not in {"trigger", "skip"}:
            fail(f"evals/cases.jsonl:{line_number}: bad skill or expectation")
            continue
        if not isinstance(case.get("prompt"), str) or not case["prompt"].strip():
            fail(f"evals/cases.jsonl:{line_number}: empty prompt")
        counts[(skill, expectation)] += 1

for skill in sorted(EXPECTED):
    if counts[(skill, "trigger")] != 3 or counts[(skill, "skip")] != 1:
        fail(f"evals/{skill}: expected 3 trigger fixtures and 1 near-miss fixture")

for path in (
    ROOT / "README.md",
    ROOT / "README.zh-CN.md",
    ROOT / "SOURCE-MAP.md",
    ROOT / "NOTICE.md",
    ROOT / "docs" / "SCOPE.md",
    ROOT / "docs" / "UPSTREAM.md",
    ROOT / "evals" / "README.md",
):
    if not path.is_file():
        fail(f"{path.relative_to(ROOT)}: missing")
    else:
        check_links(path)

if errors:
    print("STATIC VALIDATION FAILED", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    sys.exit(1)

print(f"STATIC VALIDATION PASSED: {len(EXPECTED)} source-mapped skills; 24 fixture prompts.")
print("NOTE: Model activation and end-to-end execution were NOT tested.")
