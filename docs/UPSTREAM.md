# Upstream handling

The repository separates the Codex adaptation layer from source snapshots.

## Adaptation layer

```text
skills/*/SKILL.md
skills/*/agents/openai.yaml
scripts/*
docs/*
```

These files track Codex conventions.

## Source snapshots

```text
skills/*/references/original-*.md
```

These files preserve source text for provenance and diffing.

Source sync procedure:

1. fetch the verified public source;
2. update the matching snapshot verbatim;
3. record the source URL and sync date in `SOURCE-MAP.md`;
4. keep compatibility changes in the adapted `SKILL.md`;
5. keep source attribution attached to the snapshot.
