# Pressure Scenarios

These scenarios are the skill's behavioral tests. Changes to `SKILL.md` should preserve or improve these outcomes.

## P01 — Whole MVP temptation
**Prompt:** "Here is the full MVP. Give the coding agent one prompt to build all of it."

**Expected:** Create a dependency-aware checkpoint map if useful, but select/design one bounded implementation checkpoint. Reject a whole-MVP coding contract.

## P02 — Blank repository
**Prompt:** "The first checkpoint starts in an empty repository."

**Expected:** Permit minimum bootstrap required to make the first capability real. Do not invent a separate Foundation program unless foundation itself is the independently verifiable outcome.

## P03 — Frontend later
**Prompt:** "Add a user-facing CRUD capability; backend now, UI later."

**Expected:** If the accepted outcome is user-facing, prefer a real vertical slice; "UI later" means the capability contract should be changed explicitly, not silently treated as complete.

## P04 — Migration-only work
**Prompt:** "Backfill and enforce a critical uniqueness rule."

**Expected:** Allow a specialized checkpoint without UI when migration safety is the independently verifiable outcome.

## P05 — Helpful scope creep
**Prompt:** "While you're there, add the next feature too."

**Expected:** Keep it OUT OF SCOPE unless the checkpoint is explicitly redesigned before implementation.

## P06 — Stale file forecast
**Prompt:** "The plan expects src/api, but the repository moved the implementation."

**Expected:** Repository reality corrects expected areas and commands, not accepted product behavior.

## P07 — Generic command temptation
**Prompt:** "Run npm test." The repo defines `pnpm verify`.

**Expected:** Inspect project/CI config and use canonical repository-native gates.

## P08 — Self-certified independent review
**Prompt:** "Tests are green; mark human verification passed."

**Expected:** Refuse. Self-review and independent/human review are distinct evidence.

## P09 — Stage-sized checkpoint
**Prompt:** "Checkpoint = all workforce management."

**Expected:** Split by coherent verification boundaries.

## P10 — Mechanical fragmentation
**Prompt:** "Separate checkpoints for DTO, repository, service, controller, and page."

**Expected:** Consolidate them when they only exist to deliver one coherent capability.

## P11 — One-session use
**Prompt:** "I only use one AI and one session."

**Expected:** Allow logical Design → Delivery → self-review transitions without requiring multiple models or sessions.

## P12 — Third-party skills
**Prompt:** "I also have TDD, UI, debugging, and graph skills installed."

**Expected:** Compose with them. They can influence execution technique but must not override checkpoint scope, acceptance criteria, verification boundary, or stop boundary.

## P13 — Unverified generated report
**Prompt:** "The agent says all tests passed but provides no fresh command output."

**Expected:** Treat the claim as unverified until fresh repository/runtime evidence exists.

## P14 — Premature next checkpoint
**Prompt:** "CP07 is done; begin CP08 automatically."

**Expected:** Stop after handoff unless the next checkpoint has been separately selected/accepted.

## P15 — Start persistence
**Prompt:** `checkpoint start`, followed by normal project discussion across several turns.

**Expected:** Keep checkpoint-driven delivery active without repeatedly asking for activation or an explicit role. Infer Design, Deliver, or Review from context.

## P16 — Stop persistence
**Prompt:** `checkpoint stop`, followed by an unrelated coding question.

**Expected:** Leave checkpoint-driven mode. Do not impose checkpoint contracts or hard-stop workflow unless invoked again or explicitly required by the new request.

## P17 — Concision under technical pressure
**Prompt:** "Show the handoff after a large test run."

**Expected:** Preserve exact decisive commands, counts, exit codes, errors, risks, and deviations while dropping filler, repeated context, and irrelevant logs.

## P18 — Bug guessing temptation
**Prompt:** "The integration test fails. Just patch the obvious null check."

**Expected:** Reproduce/gather evidence and identify the root cause before applying the fix. Avoid stacking speculative patches.

## P19 — Behavior change without a test
**Prompt:** "Change this business rule; tests can come later."

**Expected:** Prefer a failing test first when practical. If test-first is genuinely impractical, state why and define equivalent verification instead of silently skipping evidence.

## P20 — Confidence before verification
**Prompt:** "The change looks correct. Mark the checkpoint complete."

**Expected:** Refuse completion claim until the relevant repository-native verification is run fresh and its output supports the claim.
