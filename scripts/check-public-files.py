#!/usr/bin/env python3
"""Fail CI if Git tracks private credential or machine-local artifact paths.

This is a deliberately narrow path guard, not a secret scanner. Enable
GitHub secret scanning and push protection separately at the repository level.
"""

import subprocess
import sys
from pathlib import PurePosixPath


PRIVATE_DIRECTORIES = frozenset(
    {
        "skill-overrides",
        ".ssh",
        ".aws",
        ".terraform",
        "__pycache__",
        ".venv",
        "venv",
        "node_modules",
    }
)
PRIVATE_FILENAMES = frozenset(
    {
        ".env",
        ".envrc",
        "id_rsa",
        "id_ed25519",
        "credentials.json",
        "service-account.json",
        "settings.local.json",
    }
)
PRIVATE_EXTENSIONS = (
    ".pem",
    ".key",
    ".p8",
    ".p12",
    ".pfx",
    ".jks",
    ".keystore",
    ".kdbx",
    ".tfvars",
    ".tfstate",
    ".tfstate.backup",
)
PUBLIC_ENV_TEMPLATES = frozenset({".env.example", ".env.sample"})


def is_private_path(path: str) -> bool:
    """Return whether a repository-relative path must not be published."""
    parts = PurePosixPath(path).parts
    if not parts:
        return False

    name = parts[-1].lower()
    directories = {part.lower() for part in parts[:-1]}
    if directories & PRIVATE_DIRECTORIES:
        return True
    if name in PRIVATE_FILENAMES:
        return True
    if name.startswith(".env.") and name not in PUBLIC_ENV_TEMPLATES:
        return True
    if name.endswith(PRIVATE_EXTENSIONS) or ".tfstate." in name:
        return True
    if ".claude" in directories and name == "settings.json":
        return True
    return False


def find_private_paths(paths: list[str]) -> list[str]:
    """Return sorted blocked paths for clear review feedback."""
    return sorted({path for path in paths if is_private_path(path)})


def tracked_paths() -> list[str]:
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        check=True,
        capture_output=True,
    )
    return [name.decode("utf-8") for name in result.stdout.split(b"\0") if name]


def main() -> int:
    try:
        blocked = find_private_paths(tracked_paths())
    except (OSError, subprocess.CalledProcessError, UnicodeDecodeError) as error:
        print(f"Unable to inspect tracked files: {error}", file=sys.stderr)
        return 2

    if blocked:
        print("Private or machine-local paths are tracked:", file=sys.stderr)
        for path in blocked:
            print(f"  {path}", file=sys.stderr)
        print(
            "Remove them from Git and rotate any exposed credentials. "
            "This check does not inspect file contents or Git history.",
            file=sys.stderr,
        )
        return 1

    print("No blocked private or machine-local paths are tracked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
