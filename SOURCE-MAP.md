# Source map and verification status

**Audit date:** 2026-11-01. This repository is a third-party Codex adaptation; it is not affiliated with Stanford.

## Independently verified course sources

1. [CS146S Fall 2026 course website](https://themodernsoftware.dev/) — course scope includes MCP, agent skills, spec-driven development, loop engineering, and software factory.
2. [Instructor's official Fall 2026 assignment repository](https://github.com/mihail911/modern-software-dev-assignments).
3. [Week 3: Author a Skill](https://github.com/mihail911/modern-software-dev-assignments/blob/master/week3/assignment.md) — requires a real repeatable workflow, judgment, manual run, three trigger tests, one non-trigger test, and an end-to-end run.
4. [Week 4: Make a Messy Repo Agent-Ready](https://github.com/mihail911/modern-software-dev-assignments/blob/master/week4/assignment.md) — evaluates a *repository-specific* AGENTS.md or CLAUDE.md, **not** a published Skill.
5. [Week 5: Agent-Readiness Report](https://github.com/mihail911/modern-software-dev-assignments/blob/master/week5/assignment.md) — compares three reports, **not** a published Skill.
6. [Agent Skills specification](https://agentskills.io/specification) — documents `SKILL.md` format.

The Week 3 assignment recommends [mattpocock/skills](https://github.com/mattpocock/skills) as a **third-party sample collection**. It does not identify it as a Stanford-authored set.

## Six historical sample snapshots (not independently upstream-verified)

The previous version of this repository associated these six snapshots with a [course-linked October 1 Drive folder](https://drive.google.com/drive/folders/1aEHCXzZKkokuA4AYjD_2i6OrcM5iQosW?usp=drive_link). During this audit the folder could not be independently read. We preserve the snapshots and historical attribution for comparison; **do not treat the linkage or authorship as independently proven**.

| Historical snapshot | Active Codex adapter | Documented changes |
| --- | --- | --- |
| [explore original](skills/explore/references/original-SKILL.md) | [explore](skills/explore/SKILL.md) | Remove Claude-only invocation flag; `/explore` -> `$explore` in description |
| [research-codebase original](skills/research-codebase/references/original-SKILL.md) | [research-codebase](skills/research-codebase/SKILL.md) | Remove invocation flag; `/research-codebase` -> `$research-codebase` in description; retain Context7 dependence |
| [make-proposals original](skills/make-proposals/references/original-SKILL.md) | [make-proposals](skills/make-proposals/SKILL.md) | Remove flag; `/make-proposals` -> `$make-proposals` in description; make “two or three” consistent with the original “up to two” bound |
| [plan original](skills/plan/references/original-SKILL.md) | [plan](skills/plan/SKILL.md) | Remove flag; `/plan` -> `$plan` in description; use original [template](skills/plan/design_doc_template.md) at its source-expected location |
| [implement original](skills/implement/references/original-SKILL.md) | [implement](skills/implement/SKILL.md) | Remove flag; `/implement` -> `$implement` in description; replace hard-coded example path with the supplied plan file |
| [review original](skills/review/references/original-SKILL.md) | [review](skills/review/SKILL.md) | Remove flag; `/review` -> `$review` in description; restore original emoji severity markers |

**Original source ambiguity:** The `make-proposals` snapshot says “up to two” and “two distinct” but later says “two or three.” The adapter changes only the contradictory line; the untouched snapshot remains available.

**Runtime limitation:** Removing `disable-model-invocation: true` is a behavior change, not a semantics-preserving no-op. This metadata is not part of the minimal Agent Skills specification. Whether a skill activates automatically depends on the Codex host. All six should be explicitly invoked if the original manual-selection behavior matters.

**Tool limitation:** The `research-codebase` snapshot names `context7`. This package does not provide that tool. Without it, that particular third-party documentation step cannot run as originally written.

## Removed third-party derivations

The earlier repository treated course-linked **agent prompt examples** and an invented multi-skill workflow as installable course skills. The following directories were removed from `skills/` (their previous contents remain in Git history):

- `coding-agent-operating-contract`: derived from system/config/tool prompts, not a sourced Skill.
- `plan-mode`: derived from a plan-mode prompt, not a sourced Skill.
- `compact-development-context`: derived from a compaction prompt, not a sourced Skill.
- `analyze-performance`: generalized from a subagent prompt, not a sourced Skill.
- `software-engineering-workflow`: repository-authored orchestration/router, not a course Skill.

There is **no promise of full CS146S coverage**. Course topics, exercise ideas, and vendor tools must not be converted into new “course skills” without an explicitly verified Skill source and the correct attribution.

## Adapter provenance policy

- `references/original-SKILL.md`: unchanged historical snapshot; no claim that the course owns copyright.
- `SKILL.md`: mechanically derived adapter, checked by `scripts/validate.py` against the snapshot.
- `agents/openai.yaml`, `plugin.json`, `scripts/`, `evals/`: local engineering utilities, not course materials.
- `evals/cases.jsonl`: unexecuted hypotheses for triggering; the validator does not run a model.

Do not update a snapshot from secondary summaries. Confirm a public primary source, capture its URL and retrieval date, and document any ownership or licensing restriction before changing the corresponding adapter.
