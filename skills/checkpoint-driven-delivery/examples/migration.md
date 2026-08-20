# Example — Migration-Only Checkpoint

A checkpoint does not need frontend work when its outcome is independently operational.

## Goal
Backfill normalized customer identifiers and enforce a unique constraint without data loss.

## IN SCOPE
- pre-migration collision analysis;
- deterministic backfill;
- unique index/constraint;
- rollback or recovery plan;
- clean-database and representative-data verification.

## OUT OF SCOPE
- customer UI redesign;
- unrelated ORM refactor;
- new customer features.

The verification boundary is migration/data integrity, not browser behavior.
