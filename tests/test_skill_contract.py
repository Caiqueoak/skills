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
                self.assertTrue(name.startswith("oak-"), name)
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

    def test_skill_customization_is_override_only(self):
        modifier = (SKILLS_DIR / "oak-modify-skill/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("single source of truth (SSOT)", modifier)
        self.assertIn("never edit a skill definition to customize it", modifier)
        self.assertIn("only through an external, per-skill override", modifier)
        self.assertIn("Leave its contents, metadata, references, and installed files unchanged", modifier)
        self.assertIn("whether publicly or organization owned", modifier)
        self.assertIn("stop and report the limitation", modifier)
        self.assertIn("separate upstream development task", modifier)
        self.assertNotIn("Edit the **authorized company skill itself**", modifier)

    def test_all_public_skills_must_be_domain_agnostic(self):
        instructions = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("Keep every public skill domain-agnostic", instructions)
        self.assertIn("Do not embed worked product ideas", instructions)

    def test_skill_resources_do_not_reference_neighbor_skills(self):
        skill_names = {path.parent.name for path in SKILLS_DIR.glob("*/SKILL.md")}
        for skill_file in SKILLS_DIR.glob("*/SKILL.md"):
            own_name = skill_file.parent.name
            resources = [skill_file, *skill_file.parent.rglob("*.md")]
            for resource in set(resources):
                content = resource.read_text(encoding="utf-8").lower()
                for other_name in skill_names - {own_name}:
                    with self.subTest(resource=resource, other=other_name):
                        self.assertNotIn(f"skills/{other_name}/", content)
                        self.assertNotIn(f"/{other_name} skill", content)
                        self.assertNotIn(f"{other_name} skill", content)

    def test_composition_is_owned_by_caller(self):
        instructions = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("Every skill is self-contained and independent", instructions)
        self.assertIn("Composition belongs to the caller/developer", instructions)

    def test_private_files_are_never_committed_as_skills(self):
        self.assertFalse(list(SKILLS_DIR.rglob("skill-overrides/*.md")))


if __name__ == "__main__":
    unittest.main()
