---
name: analyze-performance
description: Investigate codebase performance with algorithmic analysis, empirical benchmarks, concurrency/correctness checks, and prioritized recommendations. Use for performance audits, benchmark plans, scaling analysis, or when the user invokes $analyze-performance.
---

Analyze the performance characteristics of the target application and return a findings report.

## Scope
- Benchmark artifacts stay in scratch space. Repository or production edits occur only when they are part of the task.
- Benchmarks use temporary storage, fixtures, or isolated test state instead of real user data.
- Keep benchmark scripts and generated data in a scratch directory.

## What to cover
1. Algorithmic complexity of representative operations, including hidden repeated I/O and redundant work.
2. Empirical measurements across realistic and stress-test dataset sizes.
3. Concurrency and correctness under load, including read-modify-write races, atomicity, locking, blocking I/O, and partial-write behavior when relevant.
4. Unbounded growth or retention patterns that make performance degrade over time.
5. Prioritized recommendations with estimated impact. Separate realistic-scale fixes from large-scale-only fixes.

## Measurement rules
- Record runtime and environment details needed to interpret results.
- Prefer repeatable benchmark inputs.
- Keep total benchmark runtime proportional to the task.
- Separate measured facts from inferred consequences.
- Production claims require evidence beyond a single microbenchmark.

## Output
Return a concise markdown report with:
- summary table of key findings;
- measurements table with actual observed numbers and environment details;
- detailed findings with `file:line` references;
- prioritized recommendations;
- explicit separation of measured facts and inferences.

For the original course example, read [references/original-subagent-prompt.md](references/original-subagent-prompt.md).
