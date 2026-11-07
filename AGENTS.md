# Skill authoring and maintenance standards

These rules apply to public skills maintained in this repository, independent of the tool used to author them.

## Creating skills

- Use `skills/<kebab-case-name>/SKILL.md`, with valid `name` and a trigger-oriented `description`.
- Base public skills on the canonical `templates/skill/SKILL.md`. The template is maintained in this repository and is not installed as an executable skill.
- Define a narrow responsibility. Keep steps, necessary inputs, constraints, and completion checks concise. Prefer readable and maintainable instructions.
- Place only required resources inside `skills/<name>/references/` or `skills/<name>/scripts/`, and use paths that work from the installed skill directory.
- Do not require global configuration or unrelated local repository files for basic skill use.
- **Keep every public skill domain-agnostic and reusable.** Do not embed worked product ideas, real-world use cases, named application examples, personas, companies, industry-specific requirements, or assumed technologies, countries, markets, or user preferences in skill instructions, bundled references, or templates. Use abstract decision criteria, generic scenario categories, and clearly marked placeholders instead.
- Scope platform-specific instructions only where intrinsic to the repository's installation or private-extension contract; never treat an illustrative project or environment as a default.
- Review all new or modified skill resources for concrete examples and leaked contextual assumptions before publishing.

## Required public/private pattern

Every skill originating from this repository must:

1. Preserve `<!-- skill-source: Caiqueoak/skills -->`.
2. Include the canonical template's public/private responsibilities section and explain what belongs in the public workflow versus a private extension.
3. Include an optional Claude Code loader for `~/.claude/skill-overrides/<skill-name>.md` and matching narrowly scoped `allowed-tools` permission, using the same skill name.
4. Load only its matching private extension when invoked; never import unrelated private context globally.
5. Keep private overrides outside this repository. Never commit, push, quote, or reproduce private contents in public files, issues, PRs, or logs.

The private file is created only when a local customization is requested. A missing private extension must not prevent the public skill from working. Never add internal or confidential context to the public template.

## Modifying existing skills

- Identify ownership from source path and provenance, not from name alone.
- For skills from this repository, environment-specific changes go to the matching local private file. Do not modify public source or installed copies for those changes.
- Public-source improvements must be generally reusable, explicitly intended for publication, and free of private or proprietary details.
- For organization-owned skills, follow the owner's rules and edit the canonical source directly when authorized. Do not impose this repository's edit denies on unrelated skills.
- Preserve the skill name, owner marker, loader, and private-path contract when changing a public skill.

## Review and publishing

- Verify the skill triggers for intended tasks and avoids unrelated triggers.
- Verify frontmatter, naming, bundled references, source markers, matching loader and private paths.
- Run `python -m unittest discover -s tests -v`; check GitHub Actions and inspect changes before merging.
- Use a reviewable branch/PR with purpose, decisions, validation, and any known limitations.
- Never include internal code, proprietary examples, credentials, internal URLs, or other private information in this public repository.

## Installation and safeguards

- Public skills must work after `npx skills add Caiqueoak/skills -g`; do not require a separate clone for their references.
- The Skills CLI does not apply global Claude Code permission denies or run a post-install setup script.
- Optional `scripts/protect-installed-skills.py` adds scoped deny rules only for verified copies owned by this repository.
- Never use broad `Edit(~/.claude/skills/**)` or `Edit(~/.agents/skills/**)` denies, which could block unrelated skills.
- Treat `allowed-tools` and dynamic injection as Claude Code-specific capabilities subject to managed policies.
