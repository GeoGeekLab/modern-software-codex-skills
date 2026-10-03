---
name: plan
description: Draft an implementation plan as a markdown file under plans/ using the bundled design document template. Use for design-only work, implementation planning, or when the user invokes $plan.
---

The design document template is [references/design_doc_template.md](references/design_doc_template.md).

1. Resolve only the scope, constraints, and timeline questions that materially affect the plan.
2. Open the template and mirror its structure in a `.md` file under `plans/`.
3. Populate current context, requirements, design decisions, affected files, and implementation steps with concise, actionable content.
4. Include testing, observability, rollout, and security only when they materially affect the change.
5. Produce the plan as the stage output; product-code changes belong to implementation.
6. Keep the solution inside the requested scope. Prefer existing project patterns over new abstractions.
7. End with concrete verification steps that another session can execute without hidden context.
