# Stage contract

This file is the compact routing contract for the bundled workflow.

| Stage | Input | Output | Stop condition |
| --- | --- | --- | --- |
| explore | unfamiliar area | code map | area is understood enough to ask a precise question |
| research | precise current-state question | `research/*.md` | facts are documented with evidence |
| proposals | research + requested outcome | <= 2 approaches | trade-offs are explicit |
| plan | understood change | `plans/*.md` | another session can execute it |
| plan-mode | broad or uncertain change | researched plan | read-only investigation is complete |
| implement | approved plan | working tree changes | plan is complete or a concrete blocker is identified |
| review | actual diff | prioritized findings | material findings are exhausted |
| compact | long session | handoff summary | another session can resume without hidden state |

Prefer the shortest path that fits the task.
