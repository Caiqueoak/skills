"""Create-skills must follow the canonical repository contract and safe publish rules."""

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_FILE = ROOT / "skills" / "oak-create-skills" / "SKILL.md"


class CreateSkillsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = SKILL_FILE.read_text(encoding="utf-8")

    def test_trigger_metadata_and_private_extension(self):
        self.assertTrue(self.content.startswith("---\n"))
        self.assertIn("name: oak-create-skills", self.content)
        self.assertIn("description: Create, validate, and publish", self.content)
        self.assertIn("<!-- skill-source: Caiqueoak/skills -->", self.content)
        loader = 'cat "$HOME/.claude/skill-overrides/oak-create-skills.md" 2>/dev/null || true'
        self.assertIn(f"allowed-tools: Bash({loader})", self.content)
        self.assertIn(f"!\x60{loader}\x60", self.content)
        self.assertIn("## Public and private responsibilities", self.content)

    def test_uses_canonical_policy_and_template_instead_of_bundling_copies(self):
        for required in (
            "AGENTS.md",
            "templates/skill/SKILL.md",
            "current repository state",
            "canonical template",
            "skills/<skill-name>/SKILL.md",
        ):
            with self.subTest(text=required):
                self.assertIn(required, self.content)
        self.assertFalse((SKILL_FILE.parent / "references" / "template.md").exists())

    def test_preserves_separation_of_public_and_private_material(self):
        for required in (
            "domain-neutral",
            "Never mention or assume other installed skills",
            "No private material",
            "publicly readable",
            "symlink targets",
            "unnecessary configuration",
            "false triggers",
            "least privilege",
        ):
            with self.subTest(text=required):
                self.assertIn(required.lower(), self.content.lower())

    def test_safe_push_and_truthful_publication(self):
        for required in (
            "reviewable branch and PR",
            "latest default branch",
            "open a PR",
            "checks/reviews pass",
            "After merge, verify",
            "A pushed branch, open PR, and merged skill are distinct outcomes",
            "If repository access or authorization is unavailable",
            "in the PR itself",
        ):
            with self.subTest(text=required):
                self.assertIn(required, self.content)
        self.assertIn("Do not infer authorization to bypass reviews", self.content)

    def test_does_not_reference_other_named_skills_or_concrete_examples(self):
        text = self.content.lower()
        for forbidden in (
            "skills/oak-discovery/",
            "skills/oak-flow/",
            "skills/oak-modify-skill/",
            "skills/oak-code-best-practices/",
            "diet app",
            "food log",
            "for example:",
            "e.g.",
        ):
            with self.subTest(text=forbidden):
                self.assertNotIn(forbidden, text)


if __name__ == "__main__":
    unittest.main()
