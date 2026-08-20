# Quality Gates

Discover canonical commands from the repository first: project files, package manifests, task runners, README, CI workflows, and project instructions are the source of truth.

## Logical gate order

Run applicable gates in a repository-appropriate order:

1. build / compile
2. format check
3. lint
4. type / static analysis
5. focused unit tests
6. integration / contract tests
7. migration or real-provider verification
8. runtime / API verification
9. browser / E2E verification for user-facing flows
10. self-review
11. git diff review
12. handoff

A green generated-code report is not evidence unless the commands actually ran.

## Review dimensions

Check both:

### Missing scope
- Which IN SCOPE item is absent?
- Which acceptance criterion is not proven?
- Which failure or authorization path is untested?

### Extra scope
- What changed that the checkpoint never requested?
- Was future-feature scaffolding added?
- Was unrelated code refactored?
- Was architecture broadened without a current need?
- Did implementation start the next checkpoint?

Unexpected extra code is a finding, not automatically a bonus.

## Engineering concerns

When relevant, inspect:
- business invariants;
- auth/authz and tenant/data boundaries;
- input validation;
- persistence and migration correctness;
- transaction/concurrency behavior;
- external failure handling;
- async cancellation/timeouts/backpressure;
- performance regressions;
- frontend loading/empty/error/forbidden/conflict/success states;
- localization and accessibility;
- secrets and sensitive logging;
- backward compatibility.

## Independent verification

An implementation agent may self-review and prepare evidence. It must not claim a human or independent review passed unless that review actually occurred.
