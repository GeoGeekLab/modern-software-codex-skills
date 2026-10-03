---
name: review
description: Review all uncommitted changes, staged and unstaged, and return prioritized findings with file and line references. Use for diff review, pre-commit review, or when the user invokes $review.
---

Perform a comprehensive review of all uncommitted changes and produce prioritized action items.

## Collect context

Inspect:

```bash
git status --porcelain
git diff
git diff --cached
git diff HEAD
git log --oneline -n 5
```

Use equivalent commands when the repository state makes one of these inappropriate.

## Review for

- correctness and regressions;
- security and data-loss impact;
- missing edge cases;
- integration and dependency impact;
- performance problems caused by the change;
- repository-specific style or contract violations;
- missing verification where it materially affects confidence.

## Severity

- `[P0]` must fix: release blocker, security flaw, data loss, broken contract, or deterministic correctness failure.
- `[P1]` should fix: likely bug, missing edge case, or material integration/performance impact.
- `[P2]` consider: lower-impact maintainability issue with concrete engineering value.

Report only evidence-backed findings. Correctness outranks cosmetic preferences.

## Output

```markdown
## Code Review

Summary: <1-2 sentences>

Findings:
1. [P0] <actionable finding> in `path:line`
2. [P1] <actionable finding> in `path:start-end`
```

When there are no material findings, report that result and list any unperformed verification.
