---
name: compact-development-context
description: Create a detailed continuation summary for a long software-development session so work can resume after compaction or handoff. Use when context is long, before a fresh session, or when the user invokes $compact-development-context.
---

Create a detailed continuation summary of the software-development session.

Summarize observed facts, decisions, user-visible rationale, tool results, code changes, errors, tests, constraints, and pending work.

## Required sections
1. Primary Request and Intent.
2. Key Technical Concepts.
3. Files and Code Sections.
4. Errors and Fixes.
5. Problem Solving and Decisions.
6. User Requirements and Feedback.
7. Pending Tasks.
8. Current Work.
9. Next Step, only when it follows directly from the current task.

## Preservation rules
- Preserve explicit user constraints and security restrictions accurately.
- Preserve important file paths, symbols, commands, test results, and architectural decisions.
- Distinguish facts from inferences.
- Attribute user requirements only to actual user messages.
- Include enough detail to resume work without re-reading the full session.
- Prefer concrete state over narrative chronology when the two compete.

The source prompt is kept at [references/original-compaction-prompt.md](references/original-compaction-prompt.md) for provenance. The Codex adapter uses the engineering handoff structure while leaving runtime-specific formatting in the source snapshot.
