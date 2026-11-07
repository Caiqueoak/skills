"""Discovery must remain installable, generic, and separable from implementation."""

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/discovery/SKILL.md"
COVERAGE = ROOT / "skills/discovery/references/coverage.md"
TEMPLATE = ROOT / "skills/discovery/references/discovery-template.md"


class DiscoverySkillTests(unittest.TestCase):
    def test_installable_and_independent(self):
        content = SKILL.read_text(encoding="utf-8")
        self.assertIn("name: discovery", content)
        self.assertIn("_flow/docs/discovery.md", content)
        self.assertIn("the Flow skill is not required", content)
        self.assertIn("references/coverage.md", content)
        self.assertIn("references/discovery-template.md", content)
        self.assertIn("No other skill is a runtime prerequisite", content)

    def test_covers_challenge_risks_and_scope_handoff(self):
        content = SKILL.read_text(encoding="utf-8")
        for required in (
            "## Discovery loop",
            "## Completion gate",
            "user confirmation",
            "high-severity scenarios",
            "never invent",
            "sources of truth",
        ):
            self.assertIn(required.lower(), content.lower())
        self.assertIn("discovery records evidence", content.lower())

    def test_comprehensive_domain_neutral_coverage(self):
        content = COVERAGE.read_text(encoding="utf-8")
        for required in (
            "Personas and research",
            "Market and positioning",
            "Economics and ROI",
            "Technical feasibility",
            "Infrastructure and operations",
            "Privacy, legal, and ethics",
            "Time and concurrency",
            "Data lifecycle",
            "Deeper probes",
        ):
            self.assertIn(required, content)

    def test_template_preserves_uncertainty_and_scenarios(self):
        content = TEMPLATE.read_text(encoding="utf-8")
        for section in (
            "## Facts, hypotheses, and evidence",
            "## Dimension coverage",
            "## Scenario and edge-case register",
            "## Opportunity, market, and economics",
            "## Options and decisions",
            "## Proposed scope boundaries",
            "## Risks, contradictions, and open questions",
            "## Readiness and next discovery wave",
        ):
            self.assertIn(section, content)
        self.assertIn("not_applicable", content)
        self.assertIn("candidate / accepted / rejected / deferred / unknown", content)

    def test_no_concrete_product_example(self):
        joined = "\n".join(
            file.read_text(encoding="utf-8")
            for file in (SKILL, COVERAGE, TEMPLATE)
        ).lower()
        for forbidden in ("diet app", "diet tracker", "food log", "nutrition goals"):
            self.assertNotIn(forbidden, joined)


if __name__ == "__main__":
    unittest.main()
