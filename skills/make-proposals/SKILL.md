---
name: make-proposals
description: Generate up to two solution proposals grounded in a research-codebase document and a feature or project request. Use when architecture choices or trade-offs need comparison, or when the user invokes $make-proposals. Requires a research document.
---

Generate up to two solution proposals grounded in an existing research document and a new feature or project request.

## Behavior
- Treat the provided research document as the factual baseline.
- Require a research document produced by `$research-codebase` or an equivalent evidence document.
- Produce at most two distinct solution approaches tailored to the request.
- Tie each approach back to research findings.
- Highlight trade-offs, impacted systems, validation steps, and open questions.

## Steps
1. Intake.
   - Capture the request and research document path.
2. Parse research.
   - Read the research document fully.
   - Extract constraints, relevant modules, dependencies, data flows, and prior decisions.
3. Synthesize solution space.
   - Derive up to two candidate approaches grounded in the research.
   - For each approach, note primary changes, affected code paths, required migrations/config updates, and rollout considerations.
4. Plan validation.
   - Identify tests, experiments, or observability needed to prove each approach.
   - Surface critical unknowns or prerequisite research.
5. Deliver the result using the template below.

## Output template
```markdown
## Solution Proposals

Context:
- Request: <short restatement>
- Research Source: <filename and key sections>

### Proposal 1 — <title>
- Overview: <2-3 sentences>
- Key Changes: <components/modules>
- Trade-offs: <risks vs benefits>
- Validation: <tests/experiments/metrics>
- Open Questions: <gaps or follow-ups>

### Proposal 2 — <title>
- Overview: <2-3 sentences>
- Key Changes: <components/modules>
- Trade-offs: <risks vs benefits>
- Validation: <tests/experiments/metrics>
- Open Questions: <gaps or follow-ups>
```

## Notes
- Reference code using `path/to/file.py:lines` when citing specifics from research.
- If research does not cover the request, state the gap and stop for additional research instead of inventing a proposal.
- Stay concise; favor actionable differences over exhaustive prose.
