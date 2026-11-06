---
name: {{SKILL_NAME}}
description: {{DESCRIPTION}}
---

# {{SKILL_NAME}}

<!-- Replace placeholders before publishing a skill. This template is not an installed skill. -->

## Public workflow

Write the reusable, platform-independent workflow here.

## Customization policy

- The public skill is the upstream source of reusable behavior.
- If asked to tailor this skill for a workplace, organization, machine, or personal preference, change **only** `~/.claude/skill-overrides/{{SKILL_NAME}}.md` on that machine. Create the private file if needed.
- Do **not** change this public `SKILL.md`, installed copies, or upstream repositories for local customization, even if a public file is writable.
- Only modify the public skill when the user explicitly asks for a public, reusable change. Do not include confidential context in public changes.
- Apply the private file as additional constraints when it exists. Surface conflicting instructions rather than silently dropping either set. Follow applicable safety and organizational policies.

## Optional private instructions (Claude Code only)

!`cat "$HOME/.claude/skill-overrides/{{SKILL_NAME}}.md" 2>/dev/null || true`
