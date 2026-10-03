# Workflow architecture

The repository uses small stage-specific skills instead of one mega-prompt.

Each stage has one job and one exit condition.

```text
                  +--------------------+
                  | operating contract |
                  +----------+---------+
                             |
request ---> explore ---> research ---> proposals ---> plan ---> implement ---> review
               |            |              |           |           |           |
               |            |              |           |           |           +--> findings
               |            |              |           |           +--------------> working tree
               |            |              |           +--------------------------> plans/*.md
               |            |              +--------------------------------------> proposal set
               |            +-----------------------------------------------------> research/*.md
               +------------------------------------------------------------------> code map

Any long stage can emit a compact development handoff.
```

## Stage contracts

### `explore`

Input:
- an unfamiliar feature, subsystem, or code path.

Output:
- a concise map of entry points, dependencies, files, data flow, and state.

Stop when:
- the caller has enough orientation to ask a precise question or begin research.

Boundary:
- orientation stays read-only by default;
- redesign belongs to proposal work.

### `research-codebase`

Input:
- a specific question about how the repository works today.

Output:
- `research/<topic>.md` with concrete file and line references.

Stop when:
- the question is answered from current code and necessary history/docs.

Boundary:
- fixes belong to proposal or planning stages;
- root-cause hypotheses stay labeled as hypotheses.

### `make-proposals`

Input:
- one research document;
- one requested change or outcome.

Output:
- at most two distinct approaches;
- trade-offs, impacted systems, validation, open questions.

Stop when:
- the decision space is explicit enough for the user or planner to select an approach.

Boundary:
- implementation starts later;
- proposals use only constraints supported by research or the request.

### `plan`

Input:
- a sufficiently understood change;
- optionally a selected proposal.

Output:
- `plans/<topic>.md` following the bundled design template.

Stop when:
- the plan names scope, touched files, implementation steps, and meaningful verification.

Boundary:
- plan output is the artifact; product code remains unchanged during this stage.

### `plan-mode`

Use instead of plain `plan` when the code area is broad, uncertain, or high-impact.

It adds a strict read-only investigation phase before writing the plan.

### `implement`

Input:
- an approved plan.

Output:
- repository changes plus verification results.

Stop when:
- the plan is implemented or a concrete conflict blocks completion.

Boundary:
- plan changes are explicit;
- unrelated working-tree changes remain intact.

### `review`

Input:
- the current Git working tree and recent context.

Output:
- prioritized findings with file/line evidence.

Severity:

```text
P0  correctness, security, data loss, broken contract, release blocker
P1  likely bug, missing edge case, material performance/integration impact
P2  maintainability or lower-impact issue worth fixing
```

Boundary:
- every finding needs evidence;
- correctness outranks cosmetic style.

### `compact-development-context`

Input:
- a long development session.

Output:
- a resumable handoff containing requirements, decisions, files, tests, errors, constraints, and next work.

Boundary:
- the handoff stores concrete engineering state and user-visible rationale.

## Routing rules

Use the smallest path that fits the task.

```text
one-line fix        -> implement -> review
unknown subsystem   -> explore -> implement -> review
architecture change -> research -> proposals -> plan -> implement -> review
broad uncertain change -> plan-mode -> implement -> review
performance issue   -> analyze-performance -> plan -> implement -> review
```

Workflow length follows task complexity.
