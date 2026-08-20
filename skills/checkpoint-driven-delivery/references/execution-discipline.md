# Execution Discipline

These rules strengthen checkpoint execution without requiring any third-party skill package.

## Compact communication

Prefer terse, evidence-first engineering output.

Preserve exactly when material:
- commands;
- identifiers;
- error messages;
- acceptance criteria;
- test counts and exit codes;
- risks, blockers, and deviations.

Drop:
- filler and pleasantries;
- repeated context;
- tool-call narration;
- speculative progress commentary;
- long logs when a decisive excerpt or result is enough.

Compression must never remove technical meaning or verification evidence.

## Behavior changes: test first where practical

For features, bug fixes, refactors, or other behavior changes, prefer a red-green-refactor loop:

1. write or identify a test that demonstrates the required behavior;
2. run it and confirm the expected failure when the behavior is missing;
3. implement the smallest maintainable change that satisfies the checkpoint contract;
4. run the focused test and relevant regression gates;
5. refactor only while behavior stays verified.

If test-first is impractical, state why and define an equivalent verification path instead of silently skipping evidence.

## Bugs and failures: root cause before fix

When the checkpoint involves a bug, failed test, build failure, integration failure, or unexpected behavior:

1. reproduce or gather concrete evidence;
2. inspect errors, recent changes, data flow, configuration, and working analogues;
3. identify a root-cause hypothesis;
4. test the hypothesis with the smallest useful experiment;
5. fix the root cause, not only the symptom;
6. add regression evidence when practical.

Do not stack speculative fixes.

## Completion: fresh evidence before claims

Before saying a checkpoint is complete, fixed, passing, or ready:

1. identify which repository-native command or runtime action proves the claim;
2. run it fresh;
3. read the output and exit status;
4. state the actual result;
5. only then make the completion claim.

An agent report, previous run, partial gate, or confidence is not fresh evidence.

## Composition with other skills

If specialized skills are installed, they may strengthen execution technique, for example TDD, debugging, UI/UX, security, performance, repository navigation, or final verification.

They may not silently redefine:
- checkpoint scope;
- acceptance criteria;
- architecture constraints;
- verification boundary;
- stop boundary.
