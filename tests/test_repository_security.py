"""Check public-repository file safeguards and least-privilege CI."""

import importlib.util
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECKER_PATH = ROOT / "scripts/check-public-files.py"
SPEC = importlib.util.spec_from_file_location("check_public_files", CHECKER_PATH)
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


class PublicRepositorySecurityTests(unittest.TestCase):
    def test_private_paths_are_blocked_without_blocking_templates(self):
        blocked_paths = [
            ".env",
            "config/.env.production",
            "local/id_ed25519",
            "local/credentials.json",
            "tests/private.pem",
            "bundle/secret.p12",
            "state/infra.tfstate.backup",
            ".claude/skill-overrides/local.md",
            ".claude/settings.json",
            "workspace/.aws/config",
            "src/__pycache__/module.pyc",
        ]
        allowed_paths = [
            "skills/independent/SKILL.md",
            "templates/skill/SKILL.md",
            "README.md",
            "config/.env.example",
            "config/.env.sample",
            ".github/workflows/validate.yml",
            "scripts/check-public-files.py",
        ]
        for path in blocked_paths:
            with self.subTest(path=path):
                self.assertTrue(checker.is_private_path(path))
        for path in allowed_paths:
            with self.subTest(path=path):
                self.assertFalse(checker.is_private_path(path))

    def test_path_results_are_unique_and_stable(self):
        self.assertEqual(
            checker.find_private_paths([".env", "README.md", ".env"]),
            [".env"],
        )

    def test_actions_are_immutable_and_token_permissions_read_only(self):
        workflow = (ROOT / ".github/workflows/validate.yml").read_text(
            encoding="utf-8"
        )
        self.assertRegex(workflow, r"(?m)^permissions:\n  contents: read$")
        self.assertNotIn("pull_request_target:", workflow)
        self.assertNotIn("workflow_run:", workflow)
        for action in ("checkout", "setup-python"):
            with self.subTest(action=action):
                self.assertRegex(
                    workflow,
                    rf"actions/{action}@[0-9a-f]{{40}}\s+# v\d+\.\d+\.\d+",
                )
        self.assertIn("persist-credentials: false", workflow)
        self.assertIn("python scripts/check-public-files.py", workflow)
        self.assertIn("python -m unittest discover -s tests -v", workflow)

    def test_dependency_updates_and_public_reporting_policy_exist(self):
        dependabot = (ROOT / ".github/dependabot.yml").read_text(
            encoding="utf-8"
        )
        self.assertIn("package-ecosystem: github-actions", dependabot)
        self.assertIn("interval: weekly", dependabot)
        policy = (ROOT / ".github/SECURITY.md").read_text(encoding="utf-8")
        self.assertIn("privately", policy)
        self.assertIn("Do not", policy)


if __name__ == "__main__":
    unittest.main()
