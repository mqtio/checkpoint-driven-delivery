# Contributing

Contributions are welcome.

## Principles

Changes should keep the skill:
- focused;
- model- and session-agnostic;
- repository-first;
- contract-centric;
- composable with other skills.

Do not add vendor-specific workflow requirements to `SKILL.md` unless the capability genuinely depends on that vendor.

## Skill changes follow pressure-test discipline

When changing behavior:

1. Add or update a scenario in `tests/pressure-scenarios.md`.
2. Explain the undesired baseline behavior or loophole.
3. Make the smallest skill/reference change that addresses it.
4. Re-run `python scripts/validate_skill.py`.
5. Test activation/behavior in at least one supported agent when practical.

## Pull requests

Please include:
- problem being solved;
- affected pressure scenarios;
- why the change belongs in the core skill instead of a project-specific instruction;
- compatibility impact;
- validation evidence.

Keep heavy detail in `references/` rather than bloating `SKILL.md`.
