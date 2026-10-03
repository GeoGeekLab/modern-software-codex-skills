---
name: research-codebase
description: Research and document the existing codebase exactly as it works today, with file paths and line references, and write the result under research/. Use for implementation archaeology, current-state documentation, or when the user invokes $research-codebase. Keep the output factual and current-state only.
---

Research and document the existing codebase exactly as it is today.

## Behavior contract
- Scope the document to current behavior, current structure, and evidence from the repository.
- Provide concrete file paths and line references in findings.
- Read any user-mentioned files fully before decomposing work.

## Steps after receiving the research query
1. Read directly mentioned files fully.
2. Decompose the query into focused research areas and create an internal checklist.
3. Explore relevant directories and files in parallel when areas are independent. If necessary, inspect `git` history for answers. If a third-party API matters, use current authoritative documentation.
4. Synthesize after exploration completes; prioritize live code findings over historical docs.
5. Produce a structured research document with:
   - Summary of findings answering the question.
   - Detailed sections per component/area with code references.
   - Cross-component connections and data flows.
   - Place the document in the top-level `research/` directory.

## Output format
- High-level summary (3-6 sentences).
- Detailed findings grouped by component/area.
- Code references in the form `path/to/file.py:123-145`.
