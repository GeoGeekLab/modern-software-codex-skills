# modern-software-codex-skills

A **source-constrained** Codex adaptation of six sample `SKILL.md` files previously collected from materials linked in Stanford CS146S: The Modern Software Developer (Fall 2026).

**Not an official Stanford repository or an official CS146S skill pack.** The course's [Week 3 assignment](https://github.com/mihail911/modern-software-dev-assignments/blob/master/week3/assignment.md) asks students to **author and test their own skill**. It does not prescribe this six-skill collection.

These six files are retained because this repository already held corresponding source snapshots attributed to a course-linked October 1 resource folder. **The source folder's contents were not independently accessible during the November 1, 2026 audit.** Therefore their attribution is recorded as a historical repository claim, not as newly verified course authorship. See [SOURCE-MAP.md](SOURCE-MAP.md).

## Included samples

| Name | Original sample's purpose |
| --- | --- |
| `explore` | Orient in a code area without executing code unless asked. |
| `research-codebase` | Record existing behavior, with paths and line references; no improvement proposals. |
| `make-proposals` | Form solutions from a `research-codebase` document. |
| `plan` | Write a plan using the included original design document template; do not implement. |
| `implement` | Implement a specified plan markdown file. |
| `review` | Review staged and unstaged changes with the original red/yellow/green action levels. |

**There is no required course-defined sequence connecting these samples.** Invoke the skill relevant to your request. The repository's former workflow-router and prompt-derived skills were removed because they were local inventions, not identified sample skills.

## Install in Codex

```bash
make validate
./scripts/install.sh all
```

To install individual samples:

```bash
./scripts/install.sh explore research-codebase plan
```

The destination is `${CODEX_HOME:-$HOME/.codex}/skills`. Existing skill directories are not overwritten without `--force`.

Each skill has a minimal standard `SKILL.md`. The `agents/openai.yaml` file is **local Codex UI metadata**, not a course artifact. `plugin.json`, installer, packager and static checks are also local packaging utilities.

## Source fidelity

The `references/original-SKILL.md` files preserve the pre-existing source snapshots. The active `SKILL.md` files differ only where necessary for the runtime or to resolve one identified source inconsistency:

- Remove the Claude-specific `disable-model-invocation` frontmatter. **This changes automatic activation behavior**, which cannot be represented by this repository's minimal Agent Skills metadata.
- Render the original `/name` invocation examples as Codex `$name` examples.
- Replace the `implement` sample's literal placeholder `/path/to/plan_md` with the provided plan file.
- Resolve the `make-proposals` sample's contradictory “two or three” line to its stated “up to two” maximum.
- Put `plan/design_doc_template.md` where the original plan sample expects it.
- Keep the original `context7` reference in `research-codebase`. It is **not bundled**: third-party API research requires the tool to be available.

Run `make validate` to check **static** format, expected source-to-adapter transformations, and evaluation fixtures. This does **not** prove model activation or skill execution.

## Course-aligned evaluation (not yet executed)

Per the official Week 3 rubric, every sample has **three expected-to-trigger prompts and one near-miss** in [evals/cases.jsonl](evals/cases.jsonl). These are test **fixtures**, not recorded test results. For each skill, perform the workflow manually once, check the four activation prompts against an actual Codex session, run one end-to-end case in a real repository, and record evidence using [the report template](evals/RUN-REPORT-TEMPLATE.md). No real-run pass rate is claimed.

## Primary course references

- [CS146S Fall 2026 course site](https://themodernsoftware.dev/)
- [CS146S Fall 2026 official assignments](https://github.com/mihail911/modern-software-dev-assignments)
- [Week 3: Author a Skill](https://github.com/mihail911/modern-software-dev-assignments/blob/master/week3/assignment.md)
- [Agent Skills specification](https://agentskills.io/specification)

For source scope, verification status, and attribution, read [SOURCE-MAP.md](SOURCE-MAP.md), [docs/SCOPE.md](docs/SCOPE.md), and [NOTICE.md](NOTICE.md).

## License

Original repository-authored packaging and documentation are MIT-licensed. The historical sample snapshots are **not** relicensed by this repository. See [NOTICE.md](NOTICE.md).
