---
name: plan-mode
description: Plan a non-trivial coding task through read-only exploration and design before implementation. Use when the user asks to plan first, requests no edits yet, the change is broad or uncertain, or the user invokes $plan-mode.
---

Use this skill for read-only investigation followed by an implementation plan.

## Planning rules
- Repository inspection stays read-only during planning; the plan file is the only write artifact when requested.
- Prefer read-only repository inspection and authoritative documentation.
- Run tests only when they are non-destructive and useful to understand current behavior.
- If parallel workers are available, use them only when independent exploration areas justify the overhead.
- Translate Claude-specific tool names into the closest available Codex capability.
- Put the final plan under the user-specified path, or `plans/` by default.

## Workflow
1. Initial understanding: inspect the request and relevant code. Search for existing functions, utilities, and patterns to reuse.
2. Design: produce a concrete implementation approach grounded in the exploration.
3. Review: re-read critical files and verify that the design matches the original request.
4. Final plan: record the recommended approach, critical files, reusable functions, trade-offs, and end-to-end verification steps.
5. Stop after the plan. Implementation begins when the user requests it.

For the source wording, read [references/original-plan-mode.md](references/original-plan-mode.md) only when provenance or migration details matter.
