# Checkpoint-Driven Delivery

A lightweight, model- and session-agnostic Agent Skill for turning product intent into bounded, verifiable implementation checkpoints.

The core idea is simple:

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

The logical roles may be performed by one AI in one session, one AI across multiple sessions, different AIs, humans, or any combination.

## Why

Large coding prompts tend to mix product decomposition, architecture, implementation, testing, and future planning. This skill makes the execution boundary explicit:

- repository-first;
- one coherent capability;
- IN SCOPE / OUT OF SCOPE;
- verification-sized checkpoints;
- real implementation paths;
- repository-native quality gates;
- hard stop before the next checkpoint.

It is intentionally composable with TDD, debugging, UI/UX, security, repository-graph, performance, and review skills.

## Install

This repository follows the open [Agent Skills specification](https://agentskills.io/specification).

### Recommended — Skills CLI

```bash
npx skills add tuanmaiquoc/checkpoint-driven-delivery --skill checkpoint-driven-delivery
```

Install globally:

```bash
npx skills add tuanmaiquoc/checkpoint-driven-delivery --skill checkpoint-driven-delivery -g
```

Examples for specific supported agents:

```bash
npx skills add tuanmaiquoc/checkpoint-driven-delivery -a qoder
npx skills add tuanmaiquoc/checkpoint-driven-delivery -a kiro-cli
npx skills add tuanmaiquoc/checkpoint-driven-delivery -a windsurf
npx skills add tuanmaiquoc/checkpoint-driven-delivery -a gemini-cli
npx skills add tuanmaiquoc/checkpoint-driven-delivery -a codex
npx skills add tuanmaiquoc/checkpoint-driven-delivery -a cursor
npx skills add tuanmaiquoc/checkpoint-driven-delivery -a claude-code
npx skills add tuanmaiquoc/checkpoint-driven-delivery -a github-copilot
```

The `skills` CLI supports many additional agents and installs to their native skill directories.

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

### ChatGPT and other hosted assistants

If the host does not expose a filesystem skill installer, attach or import the skill folder/files through that product's supported project/custom-instructions mechanism. The skill itself does not require a specific model vendor.

## Repository layout

```text
skills/checkpoint-driven-delivery/
├── SKILL.md
├── references/
│   ├── principles.md
│   ├── checkpoint-sizing.md
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

## Usage

Ask naturally, for example:

- "Turn this MVP into capability checkpoints and design the next one."
- "Implement this checkpoint only and stop after verification."
- "Review this checkpoint against its contract and repository evidence."
- "This task is too large; find a verification-sized checkpoint boundary."

The skill selects the logical role: **Design**, **Deliver**, or **Review**.

## Design principles

The skill is deliberately:
- **model-agnostic** — ChatGPT, Gemini, Claude, Codex, Qoder, Kiro, Windsurf, or another agent can participate;
- **session-agnostic** — one session or many;
- **stack-agnostic** — full-stack, backend, migration, infrastructure, ML, mobile, etc.;
- **contract-centric** — handoffs are explicit artifacts, not hidden conversation state;
- **composable** — specialized engineering skills remain useful and do not need to be bundled here.

## Validation

```bash
python scripts/validate_skill.py
```

Pull requests run the same validator in GitHub Actions.

Behavioral pressure scenarios live in `tests/pressure-scenarios.md`. Changes to the skill should be tested against those scenarios.

## Status

`v0.1.0` — public preview.

The first goal is to validate the protocol across multiple agents, stacks, and project sizes before expanding the framework.

## References

- [Agent Skills specification](https://agentskills.io/specification)
- [Agent Skills repository](https://github.com/agentskills/agentskills)
- [skills CLI](https://github.com/vercel-labs/skills)
- [Kiro Agent Skills](https://kiro.dev/docs/skills/)
- [Qoder Skills](https://docs.qoder.com/cli/Skills)

## License

MIT
