---
name: checkpoint-driven-delivery
description: Use when a product, roadmap item, or repository change needs to be shaped into a bounded implementation checkpoint, or when implementing or reviewing work under an existing checkpoint contract.
license: MIT
compatibility: Model- and session-agnostic. For implementation or review, the agent needs repository access and the project's native verification tools.
metadata:
  author: tuanmaiquoc
  version: "0.1.0"
---

# Checkpoint-Driven Delivery

Use a **checkpoint** as the execution boundary: one coherent capability with explicit scope, observable acceptance criteria, a repository-native verification boundary, and a hard stop.

Logical roles do **not** require separate models or sessions. The same AI, different AIs, humans, or any combination may perform them.

## Choose the Current Role

Do not silently mix roles.

### Design
Use when defining the next checkpoint from product intent, a roadmap, or verified repository state.

Read:
- [references/principles.md](references/principles.md)
- [references/contracts/checkpoint-contract.md](references/contracts/checkpoint-contract.md)

Produce one checkpoint contract. A broad roadmap may be sketched for dependency awareness, but only the selected checkpoint becomes the implementation contract.

### Deliver
Use when a checkpoint contract already exists and the task is to implement it.

Read:
- the checkpoint contract;
- [references/quality-gates.md](references/quality-gates.md)
- [references/contracts/implementation-handoff.md](references/contracts/implementation-handoff.md)

Inspect the repository first. Implement only IN SCOPE behavior. Use repository-native commands. Verify, self-review, write handoff evidence, then **STOP**.

### Review
Use when independently checking an implemented checkpoint.

Read:
- the checkpoint contract;
- implementation handoff/evidence;
- [references/quality-gates.md](references/quality-gates.md)
- [references/contracts/review-report.md](references/contracts/review-report.md)

Verify both missing scope and extra scope. Do not accept claims that lack repository/runtime evidence.

## Invariants

1. **Repository-first** — plans forecast; the verified repository is implementation reality.
2. **Verification-sized** — size checkpoints by what can be proven as one coherent outcome, not by file count.
3. **Explicit negative scope** — future work and adjacent cleanup belong in OUT OF SCOPE.
4. **Real path only** — no fake, mock, or placeholder production success path unless the contract explicitly requires a prototype.
5. **Native gates** — inspect project/CI configuration before choosing build, lint, type, test, migration, runtime, or browser commands.
6. **Hard stop** — implementation correctness includes not starting the next checkpoint.
7. **Independent review is risk-based** — recommended when risk warrants it; do not self-certify a human/independent review.

## Shape Guidance

For user-facing business capability, prefer a vertical slice when applicable:

`UI → application/use case → domain rules → persistence/integration → tests → runtime/browser evidence`

Do not force UI into migration-only, infrastructure, model-evaluation, refactor, or other checkpoints that have an independently verifiable outcome.

If checkpoint boundaries are unclear, read [references/checkpoint-sizing.md](references/checkpoint-sizing.md).
