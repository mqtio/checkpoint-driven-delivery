# Example — User-Facing Full-Stack Capability

## Goal
Create and manage Legal Entities within the authenticated tenant.

## Likely checkpoint shape
`PostgreSQL → backend/domain/application → API → frontend → auth/tenant → tests → runtime/browser`

This is one checkpoint because the meaningful outcome is not "an API exists"; it is "a user can manage legal entities safely through the real application."

OUT OF SCOPE might include:
- organization units;
- positions;
- future workflow engines;
- speculative caching.

Acceptance evidence should prove persistence, tenant isolation, validation, real API wiring, frontend states, and runtime/browser behavior.
