# Agent guidelines — Caiqueoak/skills

The public `skills/` tree contains reusable workflows. Private work instructions belong outside this repository and load only when the matching skill is invoked.

## Create public skills

- Use `/create-skill` and its **installed** template at `skills/create-skill/references/public-skill-template.md`. Never assume a repository-root template exists on a work machine.
- New public skills belong in `skills/<kebab-case-name>/SKILL.md`. Use concise `name`, trigger-oriented `description`, and a focused workflow.
- **Mandatory public/private contract for each skill owned by Caiqueoak/skills:**
  - Include `<!-- skill-source: Caiqueoak/skills -->` and a "Public and private responsibilities" section.
  - Tell the user that private additions go to `~/.claude/skill-overrides/<name>.md`, and explicitly forbid editing public or installed skill files for workplace customization.
  - Include the exact matching optional Claude Code injection `!\`cat "$HOME/.claude/skill-overrides/<name>.md" 2>/dev/null || true\`` and narrow `allowed-tools: Bash(cat "$HOME/.claude/skill-overrides/<name>.md" 2>/dev/null || true)` frontmatter to permit it under normal Claude Code permissions.
  - Do not create or commit private override files when publishing a public skill. Create a private file **only** when a local change is requested.
- Never include internal company data, secrets, proprietary examples, URLs, or private override contents in public source, commits, or PRs.
- Keep referenced templates and helper resources inside an installed skill directory so `npx skills add Caiqueoak/skills -g` is sufficient for skill functionality.
- Validate metadata, matching private paths, loaders, source markers, resource paths, and non-matching triggers before publishing.

## Modify existing skills

- Prefer `/modify-skill`; determine ownership from trusted provenance and source marker, **not** from name alone.
- Skills owned by `Caiqueoak/skills`: local/work modifications belong exclusively in `~/.claude/skill-overrides/<name>.md`. Never modify installed copies or symlink targets for local adaptations.
- Company-owned skills: authorized direct modifications of the company's canonical `SKILL.md` are allowed; do not apply this repo's private routing or read-only rules to them.
- Public reusable improvements require an explicit request and an appropriate upstream change, without private context.

## Installation and optional protection

- The expected installation is **one** command: `npx skills add Caiqueoak/skills -g`. Skills must not depend on external repository files or private directory initialization.
- The skills CLI does **not** execute post-install scripts or install Claude Code settings; don't claim automatic permission-level protection.
- `scripts/protect-installed-skills.py --apply` is an **optional** manual hardening step, and must only target verified installations of this repository.
- Never apply `Edit(~/.claude/skills/**)` or `Edit(~/.agents/skills/**)`: broad denies could block company skills.
- Follow organization policies; managed Claude settings may disable skill shell injection or ignore per-skill `allowed-tools`. Do not bypass those restrictions.

## Context

- Do not add global `CLAUDE.md` or `~/.claude/rules/` to implement skill-specific customization.
- A public skill's `SKILL.md` and its optional private companion must be the only sources of its skill-specific instructions.
- Avoid duplicated templates and source definitions. The bundled create-skill reference is the single source of truth for the authoring template.
