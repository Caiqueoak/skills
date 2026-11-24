"""Protect the installed Flow skill's spec and template contract."""

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FLOW = ROOT / "skills" / "oak-flow"
TEMPLATES = FLOW / "references" / "templates"
REQUIRED = {
    "discovery.md": ("## Intent and context", "## Decision log", "## Session handoff"),
    "prd.md": ("## Problem and intended users", "## Scope", "## Desired outcomes"),
    "technical.md": ("## Architecture and components", "## Engineering conventions"),
    "progress.md": ("## Spec tracker", "## Blockers / open dependencies"),
    "requirements.md": ("## Functional requirements", "## Acceptance criteria"),
    "design.md": ("## Implementation map", "## Contracts and state", "## Failures and verification", "## Decisions and risks"),
    "tasks.md": ("## Work order", "Steps (repeat for every task)"),
}


class FlowSkillTests(unittest.TestCase):
    def test_templates_are_installed_with_skill(self):
        self.assertEqual({file.name for file in TEMPLATES.glob("*.md")}, set(REQUIRED))
        for filename, sections in REQUIRED.items():
            with self.subTest(filename=filename):
                content = (TEMPLATES / filename).read_text(encoding="utf-8")
                for section in sections:
                    self.assertIn(section, content)

    def test_standard_at_a_glance_in_every_template(self):
        fields = ("Outcome", "Decisions", "Pending review", "Next action")
        for filename in REQUIRED:
            with self.subTest(filename=filename):
                content = (TEMPLATES / filename).read_text(encoding="utf-8")
                positions = []
                for field in fields:
                    label = f"- **{field}:**"
                    self.assertEqual(content.count(label), 1)
                    positions.append(content.index(label))
                self.assertEqual(positions, sorted(positions))

    def test_design_has_predictable_compact_sections(self):
        content = (TEMPLATES / "design.md").read_text(encoding="utf-8")
        headings = [line for line in content.splitlines() if line.startswith("## ")]
        self.assertEqual(
            headings,
            [
                "## Quick navigation",
                "## At a glance",
                "## Implementation map",
                "## Contracts and state",
                "## Failures and verification",
                "## Decisions and risks",
            ],
        )
        self.assertIn("{{VERIFIED_COMPONENT_OR_PATH}}", content)
        self.assertIn("{{ERROR_OR_EDGE_CASE_AND_AC_ID}}", content)

    def test_every_task_scaffold_repeats_tdd_and_commit_steps(self):
        content = (TEMPLATES / "tasks.md").read_text(encoding="utf-8")
        steps = ("Prepare", "Red", "Green", "Refactor", "Validate", "Commit", "Confirm")
        for index, step in enumerate(steps, start=1):
            self.assertIn(f"    {index}. **{step}:**", content)
        self.assertIn("one atomic commit", content)
        self.assertIn("{{SPEC_ID}}-T001", content)

    def test_flow_contract_and_stable_ids(self):
        content = (FLOW / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("name: oak-flow", content)
        self.assertIn("_flow/", content)
        self.assertIn("W001-T001", content)
        self.assertIn("red", content.lower())
        self.assertIn("green", content.lower())
        self.assertIn("refactor", content.lower())
        self.assertIn("one atomic commit", content)
        self.assertIn("specs/NNN-*/docs/*", content)
        self.assertIn("references/granularity.md", content)
        self.assertNotIn("_flow/docs/discovery.md", content)
        self.assertNotIn("discovery skill", content.lower())
        self.assertIn("Do not assume other workflows", content)

    def test_spec_templates_link_to_canonical_global_artifacts(self):
        requirements = (TEMPLATES / "requirements.md").read_text(encoding="utf-8")
        design = (TEMPLATES / "design.md").read_text(encoding="utf-8")
        tasks = (TEMPLATES / "tasks.md").read_text(encoding="utf-8")
        self.assertIn("../../prd.md", requirements)
        self.assertIn("../../technical.md", design)
        self.assertIn("../../progress.md", tasks)
        self.assertIn("{{SPEC_ID}}-T001", tasks)
        self.assertIn("{{SPEC_ID}}-AC01", requirements)

    def test_progress_is_static_and_delivery_state_is_spec_local(self):
        progress = (TEMPLATES / "progress.md").read_text(encoding="utf-8")
        tasks = (TEMPLATES / "tasks.md").read_text(encoding="utf-8")
        skill = (FLOW / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("[specs directory](specs/)", progress)
        self.assertNotIn("{{", progress)
        self.assertNotIn("| Spec |", progress)
        self.assertNotIn("## Recent meaningful changes", progress)
        self.assertNotIn("**Status:**", progress)
        self.assertIn("## Delivery state", tasks)
        for field in ("Status", "Dependencies", "Blockers"):
            self.assertIn(f"- **{field}:**", tasks)
        self.assertIn("one writer per spec", skill)
        self.assertIn("No worker may edit `progress.md`", skill)
        self.assertIn("same atomic task commit", skill)
        self.assertIn("Migrate older trackers once", skill)

    def test_granularity_rules_are_vertical_and_domain_neutral(self):
        content = (FLOW / "references" / "granularity.md").read_text(encoding="utf-8")
        self.assertIn("## Decomposition procedure", content)
        self.assertIn("not a mandatory task count", content.lower())
        self.assertIn("user-observable capability", content)
        for forbidden in ("diet", "nutrition", "food-log", "tracking app"):
            self.assertNotIn(forbidden, content.lower())


if __name__ == "__main__":
    unittest.main()
