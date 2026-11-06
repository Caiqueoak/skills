"""Tests for repository-scoped Claude Code edit protection."""

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/protect-installed-skills.py"
SPEC = importlib.util.spec_from_file_location("protect_installed_skills", SCRIPT)
protection = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(protection)


class ProtectionTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.repository = self.root / "public-repo"
        self.home = self.root / "home"

    def tearDown(self):
        self.temporary.cleanup()

    def make_skill(self, base: Path, name: str, owned: bool):
        skill = base / name / "SKILL.md"
        skill.parent.mkdir(parents=True, exist_ok=True)
        marker = protection.SOURCE_MARKER if owned else "<!-- company-owned -->"
        skill.write_text(f"---\nname: {name}\n---\n{marker}\n", encoding="utf-8")

    def test_protects_only_skills_with_own_marker(self):
        self.make_skill(self.repository / "skills", "create-skill", owned=True)
        self.make_skill(self.repository / "skills", "modify-skill", owned=True)
        self.make_skill(self.home / ".claude/skills", "create-skill", owned=True)
        self.make_skill(self.home / ".claude/skills", "modify-skill", owned=False)
        self.make_skill(self.home / ".claude/skills", "company-review", owned=False)

        rules, skipped = protection.collect_rules(self.repository, self.home)

        self.assertIn("Edit(~/.claude/skills/create-skill/**)", rules)
        self.assertNotIn("Edit(~/.claude/skills/modify-skill/**)", rules)
        self.assertFalse(any("company-review" in rule for rule in rules))
        self.assertEqual(len(skipped), 1)

    def test_apply_preserves_unrelated_rules_and_removes_stale_ones(self):
        settings_path = self.home / ".claude/settings.json"
        protection.write_json(
            settings_path,
            {"model": "sonnet", "permissions": {"deny": ["Read(./.env)"]}},
        )

        first = ["Edit(~/.claude/skills/create-skill/**)"]
        protection.apply_rules(self.home, first)

        settings = protection.read_json(settings_path)
        self.assertEqual(settings["model"], "sonnet")
        self.assertEqual(settings["permissions"]["deny"], ["Read(./.env)"] + first)

        second = ["Edit(~/.claude/skills/modify-skill/**)"]
        protection.apply_rules(self.home, second)
        protection.apply_rules(self.home, second)

        settings = protection.read_json(settings_path)
        self.assertEqual(settings["permissions"]["deny"], ["Read(./.env)"] + second)

    def test_broad_denies_are_rejected(self):
        protection.write_json(
            self.home / ".claude/settings.json",
            {"permissions": {"deny": ["Edit(~/.claude/skills/**)"]}},
        )
        with self.assertRaisesRegex(ValueError, "Remove broad Edit denies"):
            protection.apply_rules(self.home, ["Edit(~/.claude/skills/create-skill/**)"])


if __name__ == "__main__":
    unittest.main()
