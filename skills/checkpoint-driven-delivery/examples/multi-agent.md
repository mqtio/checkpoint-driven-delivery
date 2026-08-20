# Example — Multiple Agents

Tool/model choice is not part of the protocol.

Example:

`Planner AI → Checkpoint Contract → Coding AI → Handoff Evidence → Reviewer AI/Human`

The planner might be ChatGPT, the implementer Gemini/Qoder/Kiro/Codex/Windsurf, and the reviewer another model or a human. Those are deployment choices.

The portable artifacts are:
1. checkpoint contract;
2. implementation handoff;
3. review report.

Do not embed model-specific assumptions into the checkpoint itself unless the product/runtime genuinely depends on them.
