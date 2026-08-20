# Checkpoint Sizing

A checkpoint should be the smallest coherent capability for which a reviewer can say:

> This outcome now works and can be verified as one unit.

## Prefer capability boundaries

Good full-stack examples:
- legal entity management;
- upload + persistence;
- employee assignment;
- search + export.

Good specialized examples:
- safe schema backfill + unique constraint;
- production deployment readiness;
- model export contract + evaluation;
- cache invalidation correctness;
- focused architectural refactor with preserved behavior.

## Avoid stage-sized checkpoints

Too broad:
- "Build HR module"
- "Implement the entire MVP"
- "Complete authentication, organization, work management, and reporting"

Split by independently verifiable outcomes and dependencies.

## Avoid mechanical fragmentation

Usually too small:
- DTO
- repository
- service
- controller
- page

If those pieces exist only to deliver one user-visible capability, keep them inside one checkpoint.

## Use risk to justify narrow checkpoints

A migration, security boundary, data correction, or infrastructure change may deserve its own checkpoint even without UI when:
- failure impact is high;
- rollback must be verified independently;
- the change has a distinct operational outcome;
- it should be reviewed before dependent feature work starts.

## Rolling planning

Plan broadly enough to understand dependencies, but re-plan later checkpoints from verified repository state.

Do not freeze a detailed whole-product implementation plan and force future work to follow assumptions invalidated by real implementation evidence.
