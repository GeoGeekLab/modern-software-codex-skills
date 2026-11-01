# modern-software-codex-skills

Six focused software-development skills for Codex: explore a codebase, document existing behavior, compare approaches, plan changes, implement a plan, and review code.

[简体中文](README.zh-CN.md) · [CS146S course](https://themodernsoftware.dev/) · [Source map](SOURCE-MAP.md)

## Skills

| Skill | Purpose |
| --- | --- |
| `explore` | Map entry points, dependencies, file structure, and data flow. |
| `research-codebase` | Document current behavior with file and line references. |
| `make-proposals` | Compare implementation approaches based on codebase research. |
| `plan` | Write a design and implementation plan using the supplied template. |
| `implement` | Implement a specified plan Markdown file. |
| `review` | Review staged and unstaged changes and prioritize action items. |

## Install

```bash
git clone https://github.com/GeoGeekLab/modern-software-codex-skills.git
cd modern-software-codex-skills
./scripts/install.sh all
```

Install selected skills:

```bash
./scripts/install.sh explore research-codebase plan implement review
```

Skills install to `${CODEX_HOME:-$HOME/.codex}/skills`. Use `--force` to replace an existing installation.

## Use

Invoke a skill in Codex with `$skill-name`:

```text
$explore Map the authentication module and its data flow.
$research-codebase Document how session expiration currently works.
$make-proposals Compare approaches using research/sessions.md.
$plan Draft an implementation plan for session expiration.
$implement Implement plans/session-expiration.md.
$review Review the staged and unstaged changes.
```

Each skill lives in `skills/<name>/SKILL.md`. Supporting files and source text are in the skill's `references/` directory.

## Development

```bash
make validate   # Validate skill files, source mappings, and evaluation fixtures
make list       # List available skills
make dist       # Build ZIP packages
```

Evaluation prompts and run-report templates are in [`evals/`](evals/README.md).

## References

- [Stanford CS146S · The Modern Software Developer](https://themodernsoftware.dev/)
- [CS146S assignments](https://github.com/mihail911/modern-software-dev-assignments)
- [Skill source map](SOURCE-MAP.md)
- [Source and licensing notice](NOTICE.md)
