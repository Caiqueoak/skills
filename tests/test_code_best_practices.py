"""Validate the standalone, domain-neutral code best practices skill."""

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "oak-code-best-practices"
SKILL = SKILL_DIR / "SKILL.md"
REFERENCE = SKILL_DIR / "references" / "principles.md"
ARCHITECTURE = SKILL_DIR / "references" / "architecture-oop.md"
SECURITY = SKILL_DIR / "references" / "security.md"
TESTING = SKILL_DIR / "references" / "testing-validation.md"
REVIEW = SKILL_DIR / "references" / "review-audit.md"


class CodeBestPracticesTests(unittest.TestCase):
    def test_installable_and_self_contained(self):
        skill = SKILL.read_text(encoding="utf-8")
        self.assertIn("name: oak-code-best-practices", skill)
        self.assertIn("references/principles.md", skill)
        self.assertTrue(REFERENCE.is_file())
        self.assertIn("<!-- skill-source: Caiqueoak/skills -->", skill)
        self.assertIn(
            'cat "$HOME/.claude/skill-overrides/oak-code-best-practices.md" 2>/dev/null || true',
            skill,
        )

    def test_principles_are_explicit_and_not_absolutist(self):
        skill = SKILL.read_text(encoding="utf-8")
        reference = REFERENCE.read_text(encoding="utf-8")
        for expected in (
            "SOLID", "KISS", "YAGNI", "DRY", "SSOT", "SRP",
            "High cohesion", "low coupling", "locality",
            "Composition over inheritance", "Tell Don't Ask",
            "Law of Demeter", "Complexity ROI", "pure functions",
            "immutability", "explicit contracts", "red", "green", "refactor",
        ):
            with self.subTest(principle=expected):
                self.assertIn(expected.lower(), (skill + reference).lower())
        self.assertIn("not unconditional laws", skill)
        self.assertIn("What simpler alternative exists?", reference)
        self.assertIn("Understand what before how", reference)

    def test_scope_and_review_criteria(self):
        skill = SKILL.read_text(encoding="utf-8")
        self.assertIn("Do not initiate unrelated rewrites", skill)
        self.assertIn("report what passed, failed, or could not run", skill)
        self.assertIn("Distinguish correctness or safety defects from preferences", skill)
        self.assertIn("For **review**", skill)
        self.assertIn("For **refactoring**", skill)

    def test_expanded_modes_and_installable_references(self):
        skill = SKILL.read_text(encoding="utf-8")
        for mode in (
            "Architecture design or review", "Repository audit",
            "Commit / pull-request review", "Test suite audit and improvement",
            "Focused code review",
        ):
            self.assertIn(mode.lower(), skill.lower())
        for file in (ARCHITECTURE, SECURITY, TESTING, REVIEW):
            self.assertTrue(file.is_file())
            self.assertIn("references/" + file.name, skill)

    def test_oop_security_and_test_quality_are_covered(self):
        a = ARCHITECTURE.read_text(encoding="utf-8").lower()
        s = SECURITY.read_text(encoding="utf-8").lower()
        t = TESTING.read_text(encoding="utf-8").lower()
        r = REVIEW.read_text(encoding="utf-8").lower()
        for topic in ("encapsulation", "abstraction", "polymorphism", "inheritance", "composition", "substitutability", "invariants", "architecture", "dependency direction"):
            self.assertIn(topic, a)
        for topic in ("authentication", "authorization", "least privilege", "untrusted input", "secrets", "dependencies", "supply-chain", "ci", "threat"):
            self.assertIn(topic, s)
        for topic in ("red → green → refactor", "unit", "integration", "contract", "end-to-end", "assertion", "flaky", "mutation", "coverage", "regression", "negative"):
            self.assertIn(topic, t)
        for topic in ("repository audit", "commit review", "pull-request review", "architecture review", "path and line", "confidence", "not run"):
            self.assertIn(topic, r)

    def test_no_cross_skill_references_or_concrete_examples(self):
        joined = "\\n".join(
            file.read_text(encoding="utf-8")
            for file in (SKILL, REFERENCE, ARCHITECTURE, SECURITY, TESTING, REVIEW)
        ).lower()
        for disallowed in (
            "skills/flow", "skills/discovery", "flow skill", "discovery skill",
            "diet app", "nutrition", "food log", "_flow/", "e.g.",
        ):
            with self.subTest(text=disallowed):
                self.assertNotIn(disallowed, joined)


if __name__ == "__main__":
    unittest.main()
