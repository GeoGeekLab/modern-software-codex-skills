---
name: software-engineering-workflow
description: Route a non-trivial software task through the bundled explore, research, proposal, planning, implementation, review, performance, and compaction skills. Use for multi-step feature work, refactors, bug investigations, or engineering tasks that need an explicit state machine.
---

Use the smallest workflow that fits the task.

## Default route
1. Use `$explore` when the relevant code area is unfamiliar.
2. Use `$research-codebase` when a decision needs a precise factual baseline.
3. Use `$make-proposals` when multiple approaches are plausible and trade-offs matter.
4. Use `$plan` when the solution is understood, or `$plan-mode` when broad read-only investigation must come first.
5. Use `$implement` to execute the approved plan.
6. Use `$review` on the resulting diff before declaring completion.
7. Use `$compact-development-context` when the session needs a handoff or fresh context.

## Specialist route
Use `$analyze-performance` for performance investigations before proposing an optimization.

## Skip unnecessary stages
- Trivial localized change: implement, then review.
- Pure orientation: stop after explore.
- Current-state documentation: stop after research.
- Design-only request: stop after proposals or plan.
- Planning-only request: stop after proposals or plan.

## Invariants
- Evidence before claims.
- Facts before proposals.
- Design before non-trivial implementation.
- Actual diff before review conclusions.
- User scope over workflow ceremony.

For stage inputs, outputs, and stop conditions, read [references/workflow-contract.md](references/workflow-contract.md).
