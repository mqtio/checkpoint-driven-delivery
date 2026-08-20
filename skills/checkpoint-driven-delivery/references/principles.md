# Principles

## Source-of-truth model

Use three layers:

1. **Product / MVP spec** — durable intent, accepted behavior, architecture constraints.
2. **Checkpoint contract** — current implementation scope.
3. **Verified repository state** — implementation reality, current patterns, migrations, tests, commands, and working behavior.

Repository evidence may correct stale forecasts about files, layout, or canonical commands. It does not authorize dropping accepted behavior or expanding scope.

## Four boundaries

Every checkpoint must make these visible:

- **Spec boundary** — which product/architecture constraints matter now.
- **Scope boundary** — explicit IN SCOPE and OUT OF SCOPE.
- **Verification boundary** — evidence proving the capability works.
- **Stop boundary** — handoff, then stop before future work.

## Role model

Roles are logical, not physical:

`Design → Checkpoint Contract → Deliver → Implementation Evidence → Review → Verified State`

Valid execution modes include:

- one AI in one session;
- one AI across separate sessions;
- multiple AIs;
- humans plus AI.

When one session performs multiple roles, explicitly transition roles and preserve the checkpoint contract instead of rewriting scope opportunistically during implementation.

## Architecture discipline

Prefer existing project boundaries and patterns. Architecture guidance in a checkpoint should contain only constraints that materially affect the current capability.

Do not introduce:
- speculative frameworks;
- future services;
- generic abstraction layers without a current change point;
- unrelated dependency upgrades;
- broad refactors merely because they seem cleaner.

## Composability

This skill is a workflow boundary, not an all-in-one engineering handbook. It should compose with specialized skills for:
- TDD;
- debugging;
- repository graph/navigation;
- UI/UX;
- security;
- performance;
- migration safety;
- final verification.

Specialized skills may change *how* a checkpoint is executed. They must not silently change its scope.
