#!/usr/bin/env python3
"""Contract tests for the public checkpoint-driven-delivery skill.

These tests intentionally verify durable behavioral invariants in the skill text.
They do not call an LLM. Pressure scenarios remain the higher-level behavioral
conformance suite.
"""

from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "checkpoint-driven-delivery" / "SKILL.md"
PRESSURE = ROOT / "tests" / "pressure-scenarios.md"


class SkillContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = SKILL.read_text(encoding="utf-8")
        cls.pressure = PRESSURE.read_text(encoding="utf-8")
        cls.normalized = cls.skill.lower()

    def test_version_remains_v010(self):
        self.assertRegex(self.skill, r'version:\s*["\']0\.1\.0["\']')

    def test_scope_is_software_delivery(self):
        self.assertTrue(
            any(term in self.normalized for term in ("software", "coding", "repository")),
            "Skill must explicitly remain scoped to software/coding delivery.",
        )

    def test_start_and_stop_controls_exist(self):
        self.assertIn("checkpoint start", self.normalized)
        self.assertIn("checkpoint stop", self.normalized)

    def test_explicit_negative_scope_is_an_invariant(self):
        self.assertIn("out of scope", self.normalized)
        self.assertIn("explicit negative scope", self.normalized)

    def test_repository_first_is_an_invariant(self):
        self.assertIn("repository-first", self.normalized)
        self.assertIn("inspect the repository first", self.normalized)

    def test_hard_stop_is_an_invariant(self):
        self.assertIn("hard stop", self.normalized)
        self.assertRegex(self.normalized, r"stop at the checkpoint boundary|finishing one checkpoint never authorizes starting the next")

    def test_fresh_verification_precedes_completion_claims(self):
        self.assertIn("evidence before claims", self.normalized)
        self.assertRegex(self.normalized, r"fresh verification|fresh repository-native evidence")

    def test_smallest_maintainable_change_is_required(self):
        self.assertIn("smallest maintainable change", self.normalized)

    def test_root_cause_first_debugging_is_required(self):
        self.assertRegex(self.normalized, r"root cause before fixing|root-cause")

    def test_test_first_behavior_is_preserved(self):
        self.assertRegex(self.normalized, r"test-first|failing test first")

    def test_compact_evidence_first_output_is_preserved(self):
        self.assertIn("compact evidence-first output", self.normalized)

    def test_specialized_skills_cannot_override_checkpoint_contract(self):
        self.assertIn("composable skills", self.normalized)
        for term in ("scope", "acceptance", "verification", "stop"):
            self.assertIn(term, self.normalized)

    def test_pressure_suite_covers_core_execution_failure_modes(self):
        for marker in range(1, 21):
            self.assertIn(f"## P{marker:02d}", self.pressure)


if __name__ == "__main__":
    unittest.main(verbosity=2)
