# Repository contract

This repository ports public CS146S software-engineering prompts and skills to Codex.

## Invariants

- Preserve upstream intent.
- Keep Codex-specific changes narrow and explicit.
- Keep `SKILL.md` procedural and lean. Put long source material in `references/`.
- Use model-specific tool names only when the workflow depends on them.
- Extend an existing skill when it already expresses the user goal.
- Keep factual investigation separate from proposals and implementation.
- Keep implementation inside the approved plan.
- Treat `references/original-*` as source snapshots; update them only during a source sync.

## Required checks

Run:

```bash
make validate
```

before completing a repository change.

A source-derived skill change updates `SOURCE-MAP.md` and `CHANGELOG.md` in the same change.

## Style

- Prefer terse technical prose.
- Prefer ASCII diagrams over decorative diagrams.
- Use plain engineering language.
- Badges report real automated signals.
- Repository text contains no generated-by notices or model signatures.
