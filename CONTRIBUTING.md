# Contributing

Keep changes small enough to audit.

## Skill changes

For an upstream-derived skill:

1. identify the source in `SOURCE-MAP.md`;
2. preserve original behavior; record Codex compatibility changes explicitly;
3. document semantic changes;
4. update source snapshots only during a verified source sync;
5. run `make validate`.

For a new local skill:

1. target one recognizable user goal;
2. use only `name` and `description` in `SKILL.md` frontmatter;
3. put trigger conditions in the description;
4. define input, steps, output, and stop conditions in the body;
5. add `agents/openai.yaml` for Codex UI metadata;
6. add the skill to the README table and validation cases.

## Commit shape

A source-derived skill change normally touches:

```text
skills/<name>/SKILL.md
skills/<name>/agents/openai.yaml
SOURCE-MAP.md
CHANGELOG.md
```

Keep unrelated skill rewrites in separate commits.
