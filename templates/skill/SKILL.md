---
name: {{SKILL_NAME}}
description: {{DESCRIPTION}}
---

<!-- skill-source: Caiqueoak/skills -->

# {{SKILL_NAME}}

## Public workflow

<!-- Replace with a focused workflow: when to use it, inputs, steps, boundaries, and completion checks. -->

## Public and private responsibilities

- **Public:** Reusable, company-independent instructions belong in this `SKILL.md` and may be improved upstream when explicitly requested.
- **Private:** Workstation, personal, and workplace-specific instructions belong only in `~/.claude/skill-overrides/{{SKILL_NAME}}.md` on the machine where they are needed.
- For local customization of this skill, update only the matching private file. Do not modify this public file, any installed copies, or their symlink targets.
- Create the private file only when customization is requested; it is never stored in this repository, committed, pushed, or included in public PRs.
- If private and public instructions conflict, surface the conflict and comply with applicable company and security policies. Do not silently overwrite the public workflow.

## Optional private override (on invocation)

When invoked, resolve `~` to the active user's home directory and attempt to read `~/.claude/skill-overrides/{{SKILL_NAME}}.md` using an available native file-reading tool or API. Do not require Bash, `cat`, or any specific shell. Apply only this skill's matching private instructions. If the file is absent or inaccessible, continue with the public workflow; report the access limitation only if it affects the requested customization. Do not read unrelated overrides or disclose private contents.
