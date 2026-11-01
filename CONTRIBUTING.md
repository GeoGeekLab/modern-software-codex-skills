# Contributing

This package prioritizes **source fidelity over features**.

1. Verify whether the proposed content is an actual public source `SKILL.md`. Lecture subjects, exercises, runtime prompts and your own workflows are not source skills.
2. Provide an inspectable upstream URL and retrieval date. Record whether attribution and reuse rights are confirmed.
3. Preserve the source snapshot and list each exact compatibility difference in `SOURCE-MAP.md`.
4. If an existing active skill changes, update `scripts/validate.py`'s comparison only for the documented difference.
5. Run `make validate` and, where practical, perform the manual and end-to-end tests required by the Fall 2026 Week 3 assignment. Put observations in the run report. Do not record invented results.

No unsourced skill is included in the six-sample default distribution. Local extensions belong in a clearly separate project or category.

References: [Week 3 assignment](https://github.com/mihail911/modern-software-dev-assignments/blob/master/week3/assignment.md) and [SOURCE-MAP.md](SOURCE-MAP.md).
