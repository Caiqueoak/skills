---
name: create-skill
description: Create a new reusable Agent Skill with concise instructions, valid SKILL.md frontmatter, and skill-scoped customization support. Use when designing or publishing a new skill.
---

<!-- skill-source: Caiqueoak/skills -->

# Create a skill

1. Identify the skill's purpose, name, scope, and **destination**: this public repository, an authorized company repository, or a private local directory. Do not assume every skill should be public.
2. For public skills owned by `Caiqueoak/skills`, create `skills/<kebab-case-name>/SKILL.md` from `templates/skill/SKILL.md`. Replace placeholders and keep the source marker, public/private routing policy, and optional private loader.
3. For company-owned skills, follow the company's skill structure and permissions. Do **not** add this repository's ownership marker, private loader, or protection rules unless explicitly authorized.
4. Give each skill a clear name and a short, trigger-oriented `description`. Keep the body concise and task-focused: purpose, inputs, workflow, safeguards, completion checks. Use references or scripts only when they materially improve the workflow.
5. Never put company secrets, proprietary examples, internal URLs, or private overrides into a public skill. Do not copy private context into public PRs or logs.
6. Validate that YAML frontmatter parses, name matches the directory, no placeholders remain, supporting paths exist, and the skill can be invoked by its name. Test its intended use and a non-matching scenario where possible.
7. When asked to **modify an existing skill**, use `/modify-skill` instead. Do not rewrite an installed public skill as a shortcut.

## Optional private instructions (Claude Code only)

!`cat "$HOME/.claude/skill-overrides/create-skill.md" 2>/dev/null || true`
