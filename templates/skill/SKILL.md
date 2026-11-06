---
name: {{SKILL_NAME}}
description: {{DESCRIPTION}}
---

<!-- skill-source: Caiqueoak/skills -->

# {{SKILL_NAME}}

<!-- Replace placeholders before publishing. This is a template, not an installed skill. -->

## Public workflow

Write the concise, reusable workflow here. Include task inputs, key steps, safeguards, and a completion check.

## Local customization policy

- This skill comes from `Caiqueoak/skills`. For a personal or workplace adaptation, update **only** `~/.claude/skill-overrides/{{SKILL_NAME}}.md` locally.
- Do not edit this public skill, its installed copy, or its symlink targets to implement local changes.
- A public, reusable improvement requires a separate explicit request and must not contain proprietary context.
- Apply private instructions as additional constraints when present. Explain conflicts rather than silently discarding instructions; follow applicable company policy.

## Optional private instructions (Claude Code only)

!`cat "$HOME/.claude/skill-overrides/{{SKILL_NAME}}.md" 2>/dev/null || true`
