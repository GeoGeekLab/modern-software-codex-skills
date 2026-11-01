# Repository agent instructions

This is a third-party Codex compatibility package for **six historical sample skills**. It is not an official CS146S distribution.

## Repository-specific rules

- Use `SOURCE-MAP.md` to identify which files come from historical snapshots and which are local packaging.
- Keep `skills/*/references/original-SKILL.md` unchanged unless a primary-source verification justifies synchronization.
- Do not add new “course skills” from lectures, assignment topic suggestions, Claude system prompts, or generic best practices.
- Preserve the source-to-adapter comparison in `scripts/validate.py`.
- Keep the original `plan/design_doc_template.md` content unchanged.
- Add or change human-written evaluation fixtures only with a clear distinction between expected and observed behavior.
- Do not claim that validation of files proves a model ran a skill.

## Commands

- Static validation: `make validate`
- List packaged skills: `make list`
- Build ZIP packages: `make dist`

## Change boundaries

- `skills/*/SKILL.md`: only source-backed content and documented runtime changes.
- `agents/openai.yaml`, `scripts/`, `docs/`, and `evals/`: local compatibility and maintenance files.
- `references/original-SKILL.md`: historical source snapshots; do not silently edit or relicense.
