---
name: customize-skill
description: Customize a reusable agent skill locally for one machine or workplace without editing its public source. Use when asked to adapt, change, or add organization-specific instructions to an existing skill.
---

# Customize a skill privately

This workflow changes **only** the private addendum for a named skill.

1. Identify the target skill name (directory/name used to invoke it). Ask if the target is ambiguous; do not guess a filename.
2. Read the target public `SKILL.md` and the existing private file if it exists. The public content is reference material, not an editing target.
3. Apply the requested changes to `~/.claude/skill-overrides/<skill-name>.md` on this machine. Create its parent directory if needed. Keep edits minimal and specific; preserve unrelated local instructions.
4. Do not write to `~/.claude/skills/`, the public Git clone, or any tracked project file, even if they are writable. Do not commit or push the private file or quote private content in public PRs/issues/logs.
5. Check that the target skill supports optional local loading. If it does not, **report that it will not load automatically**; do not silently alter third-party/public skill files. A user may explicitly request a separate public enhancement.
6. Report the private path changed and describe the result without exposing confidential contents unnecessarily.

For a genuinely **public** skill improvement, use a separate, explicit task to edit its upstream repository and keep that work company-independent.

## Optional private instructions (Claude Code only)

!`cat "$HOME/.claude/skill-overrides/customize-skill.md" 2>/dev/null || true`
