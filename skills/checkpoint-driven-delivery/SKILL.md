---
name: checkpoint-driven-delivery
description: Use when the user says "checkpoint start", or when product, roadmap, implementation, or review work needs a bounded checkpoint contract. Remain active until the user says "checkpoint stop".
license: MIT
compatibility: Model- and session-agnostic. For implementation or review, the agent needs repository access and the project's native verification tools.
metadata:
  author: mqtio
  version: "0.1.0"
---

# Checkpoint-Driven Delivery

Use a **checkpoint** as the execution boundary: one coherent capability with explicit scope, observable acceptance criteria, a repository-native verification boundary, and a hard stop.

## Start / Stop

- `checkpoint start` — activate checkpoint-driven delivery for the current work. Persist until stopped.
- `checkpoint stop` — leave checkpoint-driven delivery mode. Do not continue checkpoint workflow unless invoked again.

While active, infer the current logical role from context. Do not require the user to choose Design, Deliver, or Review explicitly.

## Infer the Current Role

### Design
Use when the next checkpoint must be shaped from product intent, a roadmap, or verified repository state.

Read:
- [references/principles.md](references/principles.md)
- [references/checkpoint-sizing.md](references/checkpoint-sizing.md)
- [references/contracts/checkpoint-contract.md](references/contracts/checkpoint-contract.md)

Produce one implementation checkpoint contract. Broad planning is allowed for dependency awareness; only the selected checkpoint becomes the execution contract.

### Deliver
Use when a checkpoint contract already exists and implementation is requested.

Read:
- the checkpoint contract;
- [references/execution-discipline.md](references/execution-discipline.md)
- [references/quality-gates.md](references/quality-gates.md)
- [references/contracts/implementation-handoff.md](references/contracts/implementation-handoff.md)

Inspect the repository first. Implement only IN SCOPE behavior. For behavior changes, use test-first evidence where practical. For failures, find root cause before fixing. Verify with fresh repository-native evidence, self-review, hand off, then **STOP at the checkpoint boundary**.

### Review
Use when checking an implemented checkpoint.

Read:
- the checkpoint contract;
- implementation handoff/evidence;
- [references/execution-discipline.md](references/execution-discipline.md)
- [references/quality-gates.md](references/quality-gates.md)
- [references/contracts/review-report.md](references/contracts/review-report.md)

Verify both missing scope and extra scope. Never accept completion claims without fresh evidence.

## Invariants

1. **Repository-first** — plans forecast; verified repository state is implementation reality.
2. **Verification-sized** — size by what can be proven as one coherent outcome, not file count.
3. **Explicit negative scope** — future work and adjacent cleanup belong in OUT OF SCOPE.
4. **Smallest maintainable change** — satisfy the contract without speculative abstraction or unrelated refactor.
5. **Real path only** — no fake, mock, or placeholder production success path unless explicitly required.
6. **Evidence before claims** — no "complete", "fixed", or "passing" claim without fresh verification.
7. **Compact evidence-first output** — preserve technical detail; remove filler and repeated narration.
8. **Hard stop** — finishing one checkpoint never authorizes starting the next.
9. **Composable skills** — specialized skills may improve technique but may not override scope, acceptance, verification, or stop boundaries.
10. **Independent review is risk-based** — recommended when risk warrants it; never self-certify human/independent review.

For user-facing business capability, prefer a vertical slice when applicable:

`UI → application/use case → domain rules → persistence/integration → tests → runtime/browser evidence`

Do not force UI into migration-only, infrastructure, model-evaluation, refactor, or other independently verifiable checkpoints.
