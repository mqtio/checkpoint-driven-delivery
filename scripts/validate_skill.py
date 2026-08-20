#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "checkpoint-driven-delivery"
SKILL = SKILL_DIR / "SKILL.md"

errors = []

if not SKILL.exists():
    errors.append("Missing skills/checkpoint-driven-delivery/SKILL.md")
else:
    text = SKILL.read_text(encoding="utf-8")
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append("SKILL.md must start with YAML frontmatter.")
    else:
        front = m.group(1)

        def field(name):
            mm = re.search(rf"^{re.escape(name)}:\s*(.+)$", front, re.M)
            return mm.group(1).strip() if mm else None

        name = field("name")
        desc = field("description")
        license_ = field("license")
        compatibility = field("compatibility")

        if name != "checkpoint-driven-delivery":
            errors.append("Frontmatter name must match directory name.")
        if not name or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            errors.append("name must use lowercase letters/numbers/hyphens only.")
        if name and len(name) > 64:
            errors.append("name exceeds 64 characters.")
        if not desc:
            errors.append("description is required.")
        elif len(desc) > 1024:
            errors.append("description exceeds 1024 characters.")
        if desc and not desc.startswith("Use when"):
            errors.append('description should start with "Use when" for discovery.')
        if compatibility and len(compatibility) > 500:
            errors.append("compatibility exceeds 500 characters.")
        if license_ != "MIT":
            errors.append("Expected license: MIT")

        body = text[m.end():]
        for link in re.findall(r"\[[^\]]+\]\(([^)]+)\)", body):
            if "://" in link or link.startswith("#"):
                continue
            target = (SKILL_DIR / link).resolve()
            try:
                target.relative_to(SKILL_DIR.resolve())
            except ValueError:
                errors.append(f"Link escapes skill directory: {link}")
                continue
            if not target.exists():
                errors.append(f"Broken SKILL.md relative link: {link}")

if (SKILL_DIR / "README.md").exists():
    errors.append("Keep human README at repository root, not inside the skill folder.")

required = [
    "references/principles.md",
    "references/checkpoint-sizing.md",
    "references/execution-discipline.md",
    "references/quality-gates.md",
    "references/contracts/checkpoint-contract.md",
    "references/contracts/implementation-handoff.md",
    "references/contracts/review-report.md",
]
for rel in required:
    if not (SKILL_DIR / rel).exists():
        errors.append(f"Missing required reference: {rel}")

pressure = ROOT / "tests" / "pressure-scenarios.md"
if not pressure.exists():
    errors.append("Missing pressure scenarios.")
else:
    pressure_text = pressure.read_text(encoding="utf-8")
    for marker in ["P15", "P16", "P17", "P18", "P19", "P20"]:
        if f"## {marker}" not in pressure_text:
            errors.append(f"Missing execution-discipline pressure scenario: {marker}")

if errors:
    print("Skill validation FAILED:")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)

print("Skill validation PASSED.")
print(f"- Skill: {SKILL}")
print("- Frontmatter/discovery constraints checked")
print("- Progressive-disclosure references checked")
print("- Start/stop and execution-discipline pressure scenarios present")
