# Source map

This repository reorganizes selected public material linked by [CS146S: The Modern Software Developer](https://themodernsoftware.dev/) into Codex-compatible skills.

The mapping makes each source-to-adapter change directly inspectable.

## 2026-09-24 — coding-agent prompt internals

Course folder:

https://drive.google.com/drive/folders/1c6_atVW0RrqEBWsNIscG2KNwCiuPxWQG?usp=drive_link

| Upstream item | Source snapshot | Codex adapter | Adapter notes |
| --- | --- | --- | --- |
| `system_prompt.md` | `skills/coding-agent-operating-contract/references/original-system-prompt.md` | `coding-agent-operating-contract` | Keeps portable engineering rules; drops Claude runtime/model assumptions. |
| `config_files.md` | `skills/coding-agent-operating-contract/references/original-config-files.md` | `coding-agent-operating-contract` | Maps project-level `CLAUDE.md` ideas to provider-neutral repository guidance such as `AGENTS.md`. |
| `tool_list.md` | `skills/coding-agent-operating-contract/references/original-tool-list.md` | `coding-agent-operating-contract` | Keeps the tool list as provenance while Codex capabilities come from the active runtime. |
| `plan_mode.md` | `skills/plan-mode/references/original-plan-mode.md` | `plan-mode` | Preserves read-only planning intent; removes hard dependencies on Claude-only tool names and exit semantics. |
| `subagent_prompt.md` | `skills/analyze-performance/references/original-subagent-prompt.md` | `analyze-performance` | Generalizes the repository-specific performance task into a reusable measurement-first skill. |
| `compaction_prompt.md` | `skills/compact-development-context/references/original-compaction-prompt.md` | `compact-development-context` | Preserves handoff structure; removes runtime-specific output requirements and any request for hidden reasoning. |

Direct source files:

- `system_prompt.md`: https://drive.google.com/file/d/1iABC8ZEqDrazIBxOuZkQeDXjWWhyXuw9/view
- `config_files.md`: https://drive.google.com/file/d/1o_mswpLvqwOvIg1oafFi01xx2NU4WkM0/view
- `tool_list.md`: https://drive.google.com/file/d/1hWpX0oyNa_APSatFZH4-Re3MXpRNv8xb/view
- `plan_mode.md`: https://drive.google.com/file/d/1ben7eiAjEre_6lNl_QrIVyJZF9X3hPKZ/view
- `subagent_prompt.md`: https://drive.google.com/file/d/17HypCtg5px_B_RwoqOWJ27OhoQGQKZdK/view
- `compaction_prompt.md`: https://drive.google.com/file/d/1RU5Gi9olltNQV-qs2_MEwzmYfRiY2_FC/view

## 2026-10-01 — reusable skills

Course folder:

https://drive.google.com/drive/folders/1aEHCXzZKkokuA4AYjD_2i6OrcM5iQosW?usp=drive_link

| Upstream skill | Snapshot | Codex adapter | Intentional difference |
| --- | --- | --- | --- |
| `explore` | `skills/explore/references/original-SKILL.md` | `skills/explore/SKILL.md` | Invocation wording only; core procedure remains close to upstream. |
| `research-codebase` | `skills/research-codebase/references/original-SKILL.md` | `skills/research-codebase/SKILL.md` | Replaces the named third-party docs tool with current authoritative documentation. |
| `make-proposals` | `skills/make-proposals/references/original-SKILL.md` | `skills/make-proposals/SKILL.md` | Resolves the source's “up to two” vs “two or three” ambiguity to **at most two**. |
| `plan` | `skills/plan/references/original-SKILL.md` | `skills/plan/SKILL.md` | Keeps template-driven planning; tightens the handoff/verification contract. |
| `design_doc_template.md` | `skills/plan/references/design_doc_template.md` | same | Preserved as the plan template reference. |
| `implement` | `skills/implement/references/original-SKILL.md` | `skills/implement/SKILL.md` | Expands the one-line upstream command into a Codex execution contract. |
| `review` | `skills/review/references/original-SKILL.md` | `skills/review/SKILL.md` | Replaces decorative severity markers with `P0/P1/P2`; findings require concrete evidence. |

## Local additions

These are not course source files:

- `software-engineering-workflow`: orchestration/router skill for the adapted set.
- `skills/*/agents/openai.yaml`: Codex UI metadata.
- `plugin.json`: portable Agent Plugins manifest.
- `scripts/`: validation, installation, and packaging helpers.
- `docs/`: architecture and upstream-maintenance notes.

## Compatibility policy

Codex-specific changes stay narrow.

1. `SKILL.md` frontmatter contains only `name` and `description`.
2. User-invoked examples use `$skill-name` where explicit invocation helps.
3. Adapted skills use Codex-available capabilities instead of Claude-only tool names.
4. Long source text stays in `references/` rather than being injected on every invocation.
5. Output contracts contain task state and user-visible rationale.
6. Source snapshots preserve upstream wording for provenance and diffing.

Last source audit: 2026-10-03.
