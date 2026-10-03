# modern-software-codex-skills



<p align="center">
  <img width="513" height="379" alt="image" src="https://github.com/user-attachments/assets/3f5f7748-5295-48a8-b55e-df97769315e4" />
</p>

`CS146S -> Codex`
A Codex-oriented port of selected prompt and skill material from  
[CS146S: The Modern Software Developer](https://themodernsoftware.dev/).

The repository preserves the engineering workflows, removes runtime-specific coupling, and packages them as normal Codex skills.

```text
request
   |
   v
explore ---------> fast code map
   |
   v
research --------> factual baseline
   |
   v
proposals -------> explicit trade-offs
   |
   v
plan ------------> executable design
   |
   v
implement -------> scoped change
   |
   v
review ----------> independent diff check
   |
   +-------------> compact when context gets expensive
```

## What is here

| Skill | Job |
| --- | --- |
| `explore` | Map an unfamiliar code area without changing it. |
| `research-codebase` | Document current behavior with file and line references. |
| `make-proposals` | Compare grounded implementation approaches. |
| `plan` | Write a design/implementation plan. |
| `plan-mode` | Run read-only investigation before a non-trivial change. |
| `implement` | Execute an approved plan. |
| `review` | Review staged and unstaged changes by severity. |
| `analyze-performance` | Run a measurement-first performance investigation. |
| `compact-development-context` | Produce a resumable engineering handoff. |
| `coding-agent-operating-contract` | Port the reusable parts of the course's agent operating rules. |
| `software-engineering-workflow` | Route a task through only the stages it needs. |

The reusable course skills stay close to the original wording. Codex-specific changes live in the adapter layer. Source snapshots and provenance live next to the adapted skills and in [`SOURCE-MAP.md`](SOURCE-MAP.md).

## Install

Ask Codex:

```text
Install the Codex skills from https://github.com/GeoGeekLab/modern-software-codex-skills.
Use the repository's plugin and skills structure, then validate the installation.
```

Already inside the repository:

```text
Install the skills in this repository into my Codex setup and validate them.
```

### Manual

Validate the repository:

```bash
make validate
```

Install every skill:

```bash
./scripts/install.sh all
```

Install a subset:

```bash
./scripts/install.sh explore research-codebase plan implement review
```

Default target:

```text
${CODEX_HOME:-$HOME/.codex}/skills
```

Existing skill directories stay unchanged. Pass `--force` to replace them.

### Contributor commands

List bundled skills:

```bash
make list
```

Build one ZIP per skill plus a repository ZIP:

```bash
make dist
```

## Portable plugin layout

The repository root contains [`plugin.json`](plugin.json). Codex-compatible plugin hosts can discover the root `skills/` directory.

```text
modern-software-codex-skills/
├── plugin.json
├── skills/
│   ├── explore/
│   │   ├── SKILL.md
│   │   ├── agents/openai.yaml
│   │   └── references/
│   └── ...
├── docs/
├── scripts/
└── SOURCE-MAP.md
```

Each `SKILL.md` keeps frontmatter small:

```yaml
---
name: explore
description: ...
---
```

Codex uses `name` and `description` for discovery. The body loads after skill selection.

## Design rules

```text
facts != proposals
proposals != plan
plan != implementation
implementation != review
```

- Investigation produces facts.
- Proposal work compares options.
- Planning defines the implementation contract.
- Implementation follows the selected plan.
- Review evaluates the actual diff.
- Source semantics stay intact except where Codex compatibility needs a translation.
- Long source material lives in `references/`.
- Codex-native capabilities replace Claude-specific tool names.
- Small tasks use small workflows.

See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) for the stage contract.

## Source

The source material is linked from:

- [The Modern Software Developer](https://themodernsoftware.dev/)
- the 2026-09-24 coding-agent prompt materials
- the 2026-10-01 reusable skill materials

[`SOURCE-MAP.md`](SOURCE-MAP.md) records source-to-skill mappings and intentional compatibility changes.

## License

Repository-authored adapters, scripts, and documentation use the MIT license.

Course prompt snapshots under `references/original-*` retain their source attribution and sit outside that MIT grant. See [`NOTICE.md`](NOTICE.md).

## References

Codex skill/plugin packaging:

- https://developers.openai.com/plugins/build/skills
- https://developers.openai.com/plugins/build/plugins

`evals/cases.jsonl` contains lightweight activation cases for routing boundaries.

## Maintenance

Before a commit that changes a skill:

```bash
make validate
```

Changes to source-derived behavior also update `SOURCE-MAP.md`.

No magic prompt. Just explicit state transitions.
