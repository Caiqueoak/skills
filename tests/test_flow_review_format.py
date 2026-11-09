"""Contract checks for Flow's review-first Markdown artifact templates."""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "skills" / "flow" / "references" / "templates"
NEW = "🆕 **NEW**"
FILES = (
    "discovery.md",
    "prd.md",
    "technical.md",
    "progress.md",
    "requirements.md",
    "design.md",
    "tasks.md",
)
ANCHOR_PATTERN = re.compile(r'<a id="([a-z0-9-]+)"></a>')
INDEX_LINK_PATTERN = re.compile(r"\[[^\]]+\]\(#([a-z0-9-]+)\)")


def heading_slug(heading: str) -> str:
    """Match the simple GitHub heading slugs used by these templates."""
    return re.sub(r"\s+", "-", re.sub(r"[^a-z0-9 -]", "", heading.lower()).strip())


def pending_near_anchor(body: str, anchor: re.Match[str]) -> bool:
    """The marker must belong to this item, not to another item below it."""
    snippet = body[anchor.start() : anchor.start() + 260]
    return NEW in "\n".join(snippet.splitlines()[:2])


class FlowReviewFormatTests(unittest.TestCase):
    def test_review_contract_is_referenced_by_skill(self) -> None:
        skill = (ROOT / "skills" / "flow" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("references/review-layout.md", skill)
        self.assertIn(NEW, skill)
        self.assertTrue((ROOT / "skills" / "flow" / "references" / "review-layout.md").is_file())

    def test_templates_have_accurate_index_and_item_markers(self) -> None:
        for filename in FILES:
            with self.subTest(file=filename):
                text = (TEMPLATES / filename).read_text(encoding="utf-8")
                self.assertEqual(text.count("\n## Index\n"), 1)
                index_start = text.index("\n## Index\n")
                body_start = text.index("\n## ", index_start + len("\n## Index\n"))
                index = text[index_start:body_start]
                body = text[body_start:]

                headings = re.findall(r"^## (.+)$", body, flags=re.MULTILINE)
                self.assertTrue(headings)
                anchors = list(ANCHOR_PATTERN.finditer(body))
                ids = [anchor.group(1) for anchor in anchors]
                self.assertTrue(ids, "Each template needs at least one reviewable item")
                self.assertEqual(len(ids), len(set(ids)), "Item anchors must be unique")

                links = INDEX_LINK_PATTERN.findall(index)
                expected = [heading_slug(heading) for heading in headings] + ids
                self.assertCountEqual(links, expected)

                # The index must mirror the NEW badge for every individual item.
                for anchor in anchors:
                    anchor_id = anchor.group(1)
                    link_line = next(
                        line for line in index.splitlines() if f"(#{anchor_id})" in line
                    )
                    self.assertEqual(
                        NEW in link_line,
                        pending_near_anchor(body, anchor),
                        f"Review marker drift for {anchor_id}",
                    )

                # Section badges are derived from their contained pending items.
                section_ranges = list(re.finditer(r"^## (.+)$", body, re.MULTILINE))
                for i, section in enumerate(section_ranges):
                    end = (
                        section_ranges[i + 1].start()
                        if i + 1 < len(section_ranges)
                        else len(body)
                    )
                    section_body = body[section.start() : end]
                    section_pending = any(
                        pending_near_anchor(section_body, match)
                        for match in ANCHOR_PATTERN.finditer(section_body)
                    )
                    section_link = f"(#{heading_slug(section.group(1))})"
                    index_line = next(
                        line for line in index.splitlines() if section_link in line
                    )
                    self.assertEqual(
                        NEW in index_line,
                        section_pending,
                        f"Section badge drift: {section.group(1)}",
                    )


if __name__ == "__main__":
    unittest.main()
