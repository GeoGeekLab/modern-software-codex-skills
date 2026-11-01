# Week 3-inspired activation fixtures

The [CS146S 2026 Week 3 assignment](https://github.com/mihail911/modern-software-dev-assignments/blob/master/week3/assignment.md) requires:
- Three prompts that **should** trigger a Skill.
- One near-miss prompt that **should not** trigger it.
- An actual run of the Skill in a real repository.
- A manual execution of the workflow before encoding it.

`cases.jsonl` records **expected** activation behavior only. It has three `trigger` and one `skip` prompt per sample. `make validate` checks the data structure, but **does not launch Codex or test behavior**.

For an actual evaluation, run the workflow manually; then submit each prompt to the target agent in an appropriate repository, record whether the skill activated, and capture evidence. Execute the skill end-to-end and complete [RUN-REPORT-TEMPLATE.md](RUN-REPORT-TEMPLATE.md). If you have not run it, leave the outcome as `NOT RUN`. Do not present predicted trigger behavior as evidence.
