"""Public skills must be self-contained and support optional private companions."""

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
MARKER = "<!-- skill-source: Caiqueoak/skills -->"


class SkillContractTests(unittest.TestCase):
    def test_every_public_skill_has_a_scoped_private_loader(self):
        skills = sorted(SKILLS_DIR.glob("*/SKILL.md"))
        self.assertTrue(skills, "Expected at least one installable skill")

        for skill in skills:
            with self.subTest(skill=skill.parent.name):
                name = skill.parent.name
                content = skill.read_text(encoding="utf-8")
                frontmatter_match = re.match(r"\A---\n(.*?)\n---\n", content, re.DOTALL)
                self.assertIsNotNone(frontmatter_match)
                frontmatter = frontmatter_match.group(1)
                command = (
                    f'cat "$HOME/.claude/skill-overrides/{name}.md" '
                    "2>/dev/null || true"
                )
                self.assertIn(f"name: {name}", frontmatter)
                self.assertRegex(frontmatter, r"(?m)^description: \S")
                self.assertIn(f"allowed-tools: Bash({command})", frontmatter)
                self.assertIn(MARKER, content)
                self.assertIn(f"!\x60{command}\x60", content)
                self.assertNotIn("{{SKILL_NAME}}", frontmatter)
                self.assertNotIn("{{DESCRIPTION}}", frontmatter)

    def test_creation_template_is_repository_only(self):
        template_file = ROOT / "templates/skill/SKILL.md"
        self.assertTrue(template_file.is_file())
        template = template_file.read_text(encoding="utf-8")
        self.assertIn(MARKER, template)
        self.assertIn("## Public and private responsibilities", template)
        self.assertIn("allowed-tools: Bash(cat", template)
        self.assertIn('!\x60cat "$HOME/.claude/skill-overrides/{{SKILL_NAME}}.md"', template)
        self.assertFalse((SKILLS_DIR / "create-skill/SKILL.md").exists())

    def test_company_skill_edits_are_not_redirected(self):
        modifier = (SKILLS_DIR / "modify-skill/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Edit the **authorized company skill itself**", modifier)

    def test_all_public_skills_must_be_domain_agnostic(self):
        instructions = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("Keep every public skill domain-agnostic", instructions)
        self.assertIn("Do not embed worked product ideas", instructions)

    def test_private_files_are_never_committed_as_skills(self):
        self.assertFalse(list(SKILLS_DIR.rglob("skill-overrides/*.md")))


if __name__ == "__main__":
    unittest.main()
