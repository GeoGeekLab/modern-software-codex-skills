# Upstream maintenance policy

1. Locate the primary public source. Record its exact URL, the retrieval date, and whether it can be accessed independently.
2. Determine whether the material is an actual `SKILL.md` sample, an assignment, a lecture topic, or a runtime/system prompt. Do not merge these categories.
3. Keep the old `references/original-SKILL.md` snapshot unchanged until the source is verified. When it is verified, record its origin and permissible reuse terms.
4. Apply only the documented Codex adaptations to active `SKILL.md`; update [../SOURCE-MAP.md](../SOURCE-MAP.md) whenever the mapping changes.
5. Run `make validate`. Then test three expected activations, one near-miss, and an actual end-to-end execution in the target agent. Save the observed results; do not infer them from JSON fixtures.

The historical October 1 folder has not been independently checked in the November 1 audit. Course website and instructor assignments have been checked.
