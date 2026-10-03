# Activation cases

`cases.jsonl` is a small, model-agnostic set of discovery cases.

Each row contains:

```json
{"skill":"explore","expected":"trigger","prompt":"..."}
```

`trigger` means the named skill should be considered for the request.

`skip` means the named skill should not be the primary workflow for the request. Another bundled skill may be appropriate.

These cases are intentionally short. They test routing boundaries, not output quality.
