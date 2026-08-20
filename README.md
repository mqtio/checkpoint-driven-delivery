# Checkpoint-Driven Delivery

A lightweight, model- and session-agnostic Agent Skill for turning software product intent into bounded, verifiable implementation checkpoints.

> **Scope:** this skill is for software engineering and coding delivery. It is not a general-purpose workflow for research, writing, slide creation, business analysis, or other non-coding work.

```text
Product intent
    ↓
Checkpoint Contract
    ↓
Implementation
    ↓
Evidence
    ↓
Review
    ↓
Verified repository state
    ↓
Next checkpoint
```

One AI in one session, one AI across sessions, multiple AIs, humans, or any combination can use the same workflow.

## Why

Large coding prompts often mix product decomposition, architecture, implementation, testing, and future planning. This skill makes the execution boundary explicit:

- repository-first;
- one coherent capability;
- explicit IN SCOPE / OUT OF SCOPE;
- verification-sized checkpoints;
- smallest maintainable change;
- root-cause-first debugging;
- test-first behavior changes where practical;
- fresh evidence before completion claims;
- compact, evidence-first handoff;
- hard stop before the next checkpoint.

The skill is intentionally composable with TDD, debugging, UI/UX, security, repository-graph, performance, and review skills. It does not vendor or require them.

## Install

This repository follows the open [Agent Skills specification](https://agentskills.io/specification).

### Recommended — Skills CLI

```bash
npx skills add mqtio/checkpoint-driven-delivery --skill checkpoint-driven-delivery
```

Install globally:

```bash
npx skills add mqtio/checkpoint-driven-delivery --skill checkpoint-driven-delivery -g
```

Specific agents:

```bash
npx skills add mqtio/checkpoint-driven-delivery -a qoder
npx skills add mqtio/checkpoint-driven-delivery -a kiro-cli
npx skills add mqtio/checkpoint-driven-delivery -a windsurf
npx skills add mqtio/checkpoint-driven-delivery -a gemini-cli
npx skills add mqtio/checkpoint-driven-delivery -a codex
npx skills add mqtio/checkpoint-driven-delivery -a cursor
npx skills add mqtio/checkpoint-driven-delivery -a claude-code
npx skills add mqtio/checkpoint-driven-delivery -a github-copilot
```

### Manual examples

Qoder:

```text
~/.qoder/skills/checkpoint-driven-delivery/
```

Kiro:

```text
~/.kiro/skills/checkpoint-driven-delivery/
```

Windsurf:

```text
~/.codeium/windsurf/skills/checkpoint-driven-delivery/
```

For project-scoped installation, use the agent's project skill directory instead.

### Hosted assistants

If the host does not expose a filesystem skill installer, attach/import the skill folder through that product's supported project or custom-instructions mechanism.

## Use

After installation, the user-facing control is intentionally small:

```text
checkpoint start
```

The skill stays active for the current software engineering work and infers whether it should **Design**, **Deliver**, or **Review** from context.

When you want to leave the workflow:

```text
checkpoint stop
```

You do not need to select a model, role, or session topology. Logical roles may happen in one session or be handed across agents through the included contracts.

## What the skill absorbs

The core includes several proven engineering disciplines without depending on third-party skill packages:

- concise communication while preserving commands, identifiers, errors, and evidence;
- red-green-refactor behavior for changes where test-first is practical;
- root-cause investigation before bug fixes;
- fresh verification before any success/completion claim;
- scope and stop boundaries that specialized skills cannot override.

Installed specialized skills can still strengthen execution technique.

## Repository layout

```text
skills/checkpoint-driven-delivery/
├── SKILL.md
├── references/
│   ├── principles.md
│   ├── checkpoint-sizing.md
│   ├── execution-discipline.md
│   ├── quality-gates.md
│   └── contracts/
│       ├── checkpoint-contract.md
│       ├── implementation-handoff.md
│       └── review-report.md
└── examples/
    ├── single-session.md
    ├── multi-agent.md
    ├── fullstack.md
    └── migration.md

tests/
└── pressure-scenarios.md

scripts/
└── validate_skill.py
```

## Design principles

- **software-delivery focused** — implementation, bug fixes, refactors, migrations, infrastructure, ML/mobile/backend/frontend/full-stack engineering, and implementation review;
- **model-agnostic** — ChatGPT, Gemini, Claude, Codex, Qoder, Kiro, Windsurf, or another agent can participate;
- **session-agnostic** — one session or many;
- **stack-agnostic** — full-stack, backend, migration, infrastructure, ML, mobile, etc.;
- **contract-centric** — handoffs are explicit artifacts, not hidden conversation state;
- **composable** — specialized engineering skills remain useful without becoming dependencies.

## Validation

```bash
python scripts/validate_skill.py
```

Pull requests run the same validator in GitHub Actions. Behavioral pressure scenarios live in `tests/pressure-scenarios.md`.

## Status

`v0.1.0` — public preview.

The goal is to validate the protocol across multiple agents, stacks, and project sizes before expanding it.

## References

- [Agent Skills specification](https://agentskills.io/specification)
- [Agent Skills repository](https://github.com/agentskills/agentskills)
- [skills CLI](https://github.com/vercel-labs/skills)
- [Kiro Agent Skills](https://kiro.dev/docs/skills/)
- [Qoder Skills](https://docs.qoder.com/cli/Skills)

## License

MIT
