---
name: implement
description: Implement an approved plan markdown file, keep changes inside its scope, and verify the result. Use when the user asks to execute a plan or invokes $implement.
---

Implement the plan described in the user-provided or current plan markdown file.

1. Read the plan fully before editing.
2. Inspect the current working tree and preserve unrelated user changes.
3. Treat the plan's scope, constraints, files, and verification steps as the implementation contract.
4. Reuse existing repository patterns named by the plan or evident in the target code.
5. If current code reality conflicts with the plan, preserve the user's intent with the smallest compatible adjustment and report the divergence.
6. Run the plan's verification steps and any directly relevant repository checks.
7. Report changed files, verification results, skipped checks, and unresolved issues.

Follow the approved design and scope. Report any required divergence explicitly.
