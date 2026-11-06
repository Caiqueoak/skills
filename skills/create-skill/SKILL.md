---
name: create-skill
description: Create a reusable Agent Skill, including a public workflow and an optional skill-scoped private extension. Use when designing, scaffolding, or publishing a skill.
allowed-tools: Bash(cat "$HOME/.claude/skill-overrides/create-skill.md" 2>/dev/null || true)
---

<!-- skill-source: Caiqueoak/skills -->

# Create a skill

## 1. Choose ownership and scope

- Confirm the intended destination: `Caiqueoak/skills` (public), an authorized company repository, or a private local skill.
- Never assume a company skill belongs in a personal public repository.
- Separate **portable behavior** (what other users can reuse) from **environment-specific behavior** (personal/work/company conventions and data).

## 2. Author a public skill from Caiqueoak/skills

- Read the **bundled** template at `${CLAUDE_SKILL_DIR}/references/public-skill-template.md`. It ships with this installed skill: **do not depend on files in a separate Git clone**.
- Create `skills/<kebab-case-name>/SKILL.md` within an authorized checkout of `Caiqueoak/skills`.
- Replace `{{SKILL_NAME}}` and `{{DESCRIPTION}}`. Keep the ownership marker, private instructions section, exact per-skill `allowed-tools` grant, and matching dynamic loader.
- Write focused public guidance: trigger, purpose, inputs, actions, boundaries, and verification. Use additional references only when genuinely useful.
- Every public skill must **explicitly mention** its optional private companion at `~/.claude/skill-overrides/<skill-name>.md` and that it is loaded only when the skill runs.
- Do **not** create or commit the private file as part of publishing the skill. Create it on a work machine only if work-specific customization is actually requested.
- **Default for modifying a public skill to fit a workplace:** edit only its private companion. Reserve edits to public `SKILL.md` for explicitly requested, reusable upstream changes.

## 3. Author company-owned or private skills

- Follow the owning organization's skill format, permissions, and repository rules. Company skills may be edited directly when authorized.
- Do not copy this repository's ownership marker, protections, or private loader to a company skill unless the company explicitly chooses that mechanism.
- Never include confidential company examples, URLs, identifiers, secrets, or private override contents in a public skill.

## 4. Validate

- YAML frontmatter contains a matching `name` and trigger-oriented `description`; no template placeholders remain.
- For public skills owned by `Caiqueoak/skills`, the matching private loader, narrow `allowed-tools` grant, and ownership marker remain intact.
- Private materials are outside Git and never leak into commits, PRs, documentation, or logs.
- Skill references are resolvable **from its installed directory** (not only from the source checkout).
- Test invocation and a non-matching scenario where possible.
- When the task is to change an **existing** skill, use `/modify-skill` and respect its ownership routing.

## Optional private instructions (Claude Code only)

!`cat "$HOME/.claude/skill-overrides/create-skill.md" 2>/dev/null || true`
