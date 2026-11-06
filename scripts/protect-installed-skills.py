#!/usr/bin/env python3
"""Configure Claude Code edit denies for skills installed from Caiqueoak/skills only."""

import argparse
import json
import os
import stat
from pathlib import Path

SOURCE_MARKER = "<!-- skill-source: Caiqueoak/skills -->"
INSTALL_DIRS = (".claude/skills", ".agents/skills")
BROAD_DENIES = {
    "Edit(~/.claude/skills/**)",
    "Edit(~/.agents/skills/**)",
}


def read_json(path: Path) -> dict:
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"Expected a JSON object: {path}")
    return data


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    mode = stat.S_IMODE(path.stat().st_mode) if path.exists() else 0o600
    os.chmod(temporary, mode)
    temporary.replace(path)


def collect_rules(repository: Path, home: Path) -> tuple[list[str], list[str]]:
    rules = [f"Edit(//{(repository / 'skills').resolve().as_posix().lstrip('/')}/**)"]
    skipped = []
    for source in sorted((repository / "skills").glob("*/SKILL.md")):
        name = source.parent.name
        if SOURCE_MARKER not in source.read_text(encoding="utf-8"):
            raise ValueError(f"Missing source marker in public skill: {source}")
        for directory in INSTALL_DIRS:
            installed = home / directory / name / "SKILL.md"
            if not installed.is_file():
                continue
            if SOURCE_MARKER in installed.read_text(encoding="utf-8"):
                rules.append(f"Edit(~/{directory}/{name}/**)")
            else:
                skipped.append(str(installed))
    return sorted(set(rules)), skipped


def apply_rules(home: Path, required: list[str]) -> tuple[list[str], list[str]]:
    settings_file = home / ".claude/settings.json"
    managed_file = home / ".claude/skill-overrides/.managed-edit-denies.json"

    settings = read_json(settings_file)
    permissions = settings.setdefault("permissions", {})
    if not isinstance(permissions, dict):
        raise ValueError("permissions must be a JSON object")
    denies = permissions.setdefault("deny", [])
    if not isinstance(denies, list) or any(not isinstance(rule, str) for rule in denies):
        raise ValueError("permissions.deny must be a list of strings")

    broad = BROAD_DENIES.intersection(denies)
    if broad:
        raise ValueError(
            "Remove broad Edit denies manually; they would block company skills: "
            + ", ".join(sorted(broad))
        )

    managed = read_json(managed_file).get("rules", [])
    if not isinstance(managed, list) or any(not isinstance(rule, str) for rule in managed):
        raise ValueError("Managed protection metadata is invalid")

    retained = [rule for rule in denies if rule not in managed]
    added = [rule for rule in required if rule not in retained]
    permissions["deny"] = retained + added

    write_json(settings_file, settings)
    write_json(managed_file, {"rules": added})
    return added, [rule for rule in managed if rule not in required]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Update your Claude Code user settings (without changing other rules)",
    )
    args = parser.parse_args()

    repository = Path(__file__).resolve().parent.parent
    home = Path.home()
    rules, skipped = collect_rules(repository, home)

    print("Scoped edit-deny rules for Caiqueoak/skills:")
    for rule in rules:
        print("  " + rule)
    for path in skipped:
        print("Not protected (no matching ownership marker): " + path)
    if len(rules) == 1:
        print("No owned installed skills found; install the skills and run this again.")

    if args.apply:
        added, removed = apply_rules(home, rules)
        print(f"Updated ~/.claude/settings.json ({len(added)} managed rules).")
        if removed:
            print(f"Removed {len(removed)} stale managed rules.")


if __name__ == "__main__":
    main()
