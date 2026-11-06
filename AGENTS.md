# Agent guidelines — Caiqueoak/skills

This repository is the **public source** of reusable skills. Keep all public content free of workplace-only or confidential details.

## Create skills

- Prefer using `/create-skill` when authoring a new skill. Follow `templates/skill/SKILL.md` and the official Agent Skills format.
- New public skills belong at `skills/<kebab-case-name>/SKILL.md`.
- Each public skill needs valid `name` and trigger-oriented `description`, a concise single-purpose workflow, this repository's source marker, and an optional Claude Code private loader.
- Use extra reference files or scripts only if needed. Test the skill's intended trigger and scope before publishing.
- Company-owned skills belong in authorized company locations, **not** this repository. Do not add this repository's ownership marker to company skills.

## Review before publishing

- Confirm that the skill triggers for its intended task and does not unnecessarily match unrelated tasks.
- Confirm that every required file lives inside the installable skill directory, with no dependency on a local working copy.
- Confirm that public instructions, per-skill private paths, ownership marker, and loader all use the same skill name.
- Keep generic public instructions separate from private workplace or machine-specific additions.

## Modify existing skills

- Prefer using `/modify-skill` for existing skills. **Determine origin before editing; never infer ownership from name alone.**
- Skills originating from `Caiqueoak/skills`: for local/workplace customization, write only to `~/.claude/skill-overrides/<skill-name>.md`. Do not change the published skill or installed copies.
- Company-owned skills: direct edits to the company's canonical skill are **allowed when authorized**. Never block them just because they live under `~/.claude/skills/` or `~/.agents/skills/`.
- Other/unknown skills: inspect ownership and applicable policy before editing.
- Only edit a public skill in this repository if the user explicitly requests a **reusable upstream improvement**. Never publish company-specific content in that change.
- Preserve the per-skill optional loader and source marker when editing public skills.

## Protect only this repository's installations

- Do not deny `Edit(~/.claude/skills/**)` or `Edit(~/.agents/skills/**)`: these broad rules block company-owned skills.
- `scripts/protect-installed-skills.py --apply`, when run on the user's machine, applies scoped deny rules only for verified installations of this repository's skills plus that checkout's public `skills/` directory.
- The installer never adds a deny for an unmarked same-named company skill. Re-run after installing/updating public skills.
- Permission denies are a guard for Claude Code file tools and recognized shell operations, **not** a full filesystem security boundary.

## Privacy and scope

- Private overrides are neither source files nor artifacts to commit. Never quote them in public issues, PRs, logs, commits, or README examples.
- Do not add global `CLAUDE.md` or `~/.claude/rules/` instructions for per-skill customization. Private additions should load only with the matching skill.
- Follow company policy for use of local instructions and external AI tools.
