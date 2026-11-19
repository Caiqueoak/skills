"""Validate the independent, framework-agnostic testing skill and its references."""

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "oak-testing"
SKILL = SKILL_DIR / "SKILL.md"
CREATION = SKILL_DIR / "references" / "creation.md"
EXECUTION = SKILL_DIR / "references" / "execution.md"


class TestingSkillTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.orchestrator = SKILL.read_text(encoding="utf-8")
        cls.creation = CREATION.read_text(encoding="utf-8")
        cls.execution = EXECUTION.read_text(encoding="utf-8")

    def test_orchestrator_routes_both_cases_without_eager_loading(self):
        self.assertIn("name: oak-testing", self.orchestrator)
        self.assertIn("references/creation.md", self.orchestrator)
        self.assertIn("references/execution.md", self.orchestrator)
        self.assertIn("Read only the needed reference", self.orchestrator)

    def test_creation_rejects_noncanonical_and_redundant_tests(self):
        for phrase in (
            "authorized, in-scope behavior",
            "plausible defect",
            "existing test",
            "Removed accidental/out-of-scope behavior",
            "do not automatically test",
            "Explicit absence or prohibition requirement",
            "lowest sufficient layer",
            "Red:",
            "Green:",
            "Refactor:",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase.lower(), self.creation.lower())

    def test_execution_prioritizes_impacted_tests_and_latency(self):
        for phrase in (
            "supported selection",
            "Direct:",
            "Dependent:",
            "Full suite:",
            "unrelated targets",
            "cold-start versus warm-run",
            "already connected browser",
            "headless launcher",
            "unrelated feature",
            "commands actually executed",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase.lower(), self.execution.lower())

    def test_sources_are_self_contained_and_framework_agnostic(self):
        content = "\n".join((self.orchestrator, self.creation, self.execution)).lower()
        self.assertIn("<!-- skill-source: caiqueoak/skills -->", content)
        self.assertIn("## public and private responsibilities", content)
        self.assertIn("~/.claude/skill-overrides/oak-testing.md", content)
        self.assertIn("native file-reading tool or api", content)
        for forbidden in (
            "skills/oak-flow/",
            "skills/oak-discovery/",
            "karma",
            "vitest",
            "jest",
            "pytest",
            "maven",
            "npm test",
            "browser: []",
        ):
            with self.subTest(forbidden=forbidden):
                self.assertNotIn(forbidden, content)


if __name__ == "__main__":
    unittest.main()
