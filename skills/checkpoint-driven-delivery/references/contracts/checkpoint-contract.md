# Checkpoint Contract

Use this template for the artifact handed from Design to Delivery.

## Checkpoint
`CPxx — <Capability Name>`

## Goal
One coherent product or operational outcome.

## Repository-first instruction
Continue from the current repository. Inspect relevant project instructions, code, tests, contracts, migrations, configuration, and canonical verification commands before changing anything. Do not re-scaffold unless the repository is actually blank or this checkpoint explicitly requires bootstrap.

## IN SCOPE
List concrete behavior required for this outcome.

Include applicable:
- domain/application behavior;
- persistence/integration;
- API/contracts;
- frontend/user flow;
- authorization/tenant/audit;
- localization/accessibility;
- tests and runtime evidence.

## OUT OF SCOPE
Explicitly name likely scope-drift temptations:
- next checkpoint;
- adjacent features;
- unrelated refactor/cleanup;
- speculative infrastructure;
- framework/dependency replacement;
- placeholder production paths.

## Dependencies
Only already-verified checkpoints, accepted contracts, providers, migrations, or external prerequisites.

## Architecture constraints
Only constraints that materially affect this checkpoint.

## Expected areas
Forecast likely modules/files to inspect. This is orientation, not permission for broad refactoring.

## Acceptance criteria
Observable behavior. Include applicable happy path, validation, failure, authorization, persistence/history, conflict/concurrency, UI states, localization, and compatibility.

## Verification boundary
State evidence required. Prefer repository-native commands discovered during inspection rather than invented generic commands.

## Completion boundary
After implementation, verification, self-review, and handoff:

**STOP. Do not start the next checkpoint.**

## Effort / risk
`Small | Medium | Large`

Explain the main complexity/risk drivers, not token estimates.
