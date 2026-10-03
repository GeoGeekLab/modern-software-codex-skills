---
name: explore
description: Explore an unfamiliar area of a codebase and brief the user on purpose, entry points, call graph, file layout, and data flow. Use for codebase orientation, feature-area exploration, or when the user invokes $explore. Run code only when the task calls for execution.
---

Explore the unfamiliar area of this codebase and brief me. Focus on clarity and concision.

What to produce:
- Short overview of the feature/area and its purpose.
- Key entry points/functions, with file paths and what each does.
- Call graph/dependencies: how major functions/modules interact; note external libs/services.
- File and directory structure: where related code lives and how it is organized.
- Data flow and state: important models, inputs/outputs, side effects.

How to explore:
- Start by reading the primary entry file, then follow imports to map dependencies.
- Skim tests, fixtures, or example scripts to see intended behavior.
- Note setup steps required to run or reproduce behavior. Execute only when the task calls for it.
