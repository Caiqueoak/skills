# Reusable Agent Skills

A public collection of reusable Agent Skills. Each skill keeps its general workflow separate from optional, environment-specific instructions.

## Installation

```sh
npx skills add Caiqueoak/skills -g
```

The installer provides the public skills. Private instructions are optional and do not need to exist at installation time.

## Migrating existing installations

Renaming changes a skill's installed identity; an ordinary update may leave old names installed. Replace only skills installed from this repository:

```sh
npx skills ls -g
npx skills remove Caiqueoak/skills -g -y
npx skills add Caiqueoak/skills -g -y
npx skills ls -g
```

If you have optional Claude Code private extensions, first copy them to their matching new names without overwriting an existing destination:

```sh
for name in code-best-practices create-skills discovery flow modify-skill; do
  old="$HOME/.claude/skill-overrides/$name.md"
  new="$HOME/.claude/skill-overrides/oak-$name.md"
  if [ -f "$old" ] && [ ! -e "$new" ]; then
    cp "$old" "$new"
  fi
done
```

Review the new private files before removing the old copies. Keep their contents local. For project-scoped installs, repeat remove/add without `-g` from that project. After reinstalling, rerun the optional edit-protection script to update scoped rules.

## Repository structure

```text
skills/
  oak-create-skills/
    SKILL.md
  oak-code-best-practices/
    SKILL.md
    references/
      principles.md, architecture-oop.md
      security.md, testing-validation.md, review-audit.md
  oak-discovery/
    SKILL.md
    references/
      coverage.md, discovery-template.md
  oak-flow/
    SKILL.md
    references/
      granularity.md
      templates/
        prd.md, technical.md, progress.md
        requirements.md, design.md, tasks.md
  oak-modify-skill/
    SKILL.md
templates/
  skill/
    SKILL.md
AGENTS.md
.github/workflows/validate.yml
```

## Flow: spec-driven project planning

The installed /oak-flow skill turns a product idea into a project-local _flow/ baseline with a PRD, technical architecture, progress tracker, and numbered specs containing requirements.md, design.md, and tasks.md. Extra spec documents belong in that spec's docs/ subdirectory. Each W###-T### task is implemented with TDD and one verified, traceable commit. The skill ships templates and an abstract spec-decomposition guide; it does not add a _flow/ directory to this skills repository. It is independent of other installed skills and accepts only project-provided inputs.

## Code Best Practices

The installable `oak-code-best-practices` skill independently supports architecture design, OOP and functional design, security reviews, repository and commit/PR audits, test-quality assessment, and evidence-based validation. It applies principles pragmatically rather than enforcing a fixed stack or architecture.

## Create Skills

The installable `oak-create-skills` skill authors **new, reusable skills** against this repository's current authoring standards, validates the resulting public content, and—when explicitly authorized—pushes a topic branch and opens a reviewable PR. Publication to the default branch is verified separately after successful checks and any required review. It does not depend on other installed skills.

## Creating a skill

Follow [AGENTS.md](AGENTS.md) for repository authoring conventions, and start from the [canonical skill template](templates/skill/SKILL.md).

1. Define one clear responsibility, an `oak-`-prefixed kebab-case skill name, and a description explaining when it should be used.
2. Create `skills/<skill-name>/SKILL.md`. Keep the template's source marker, public/private split, and matching optional private loader.
3. Put all required references and scripts inside that skill's directory so it works after global installation.
4. Validate before publishing with `python -m unittest discover -s tests -v`. Use a PR for changes and record the validation results.

Skill creation is maintained through the repository's authoring standards; only runtime-useful skills are installed.

## Public/private extension contract

For a skill named `oak-example`:

```text
skills/oak-example/SKILL.md                   # Public source
~/.claude/skill-overrides/oak-example.md      # Optional local extension
```

The public skill provides the reusable workflow; the private file contains local or environment-specific additions. Each public skill includes an optional loader for **only its matching private file**, loaded when that skill is invoked.

```markdown
## Private instructions (Claude Code only)

!`cat "$HOME/.claude/skill-overrides/oak-example.md" 2>/dev/null || true`
```

The canonical template also includes the corresponding narrowly scoped `allowed-tools` permission. This mechanism uses Claude Code features, so behavior may vary across agents or managed environments.

Private files must never be committed to this repository, copied into public examples, or included in pull requests. Updating public skills leaves independent private files unchanged; conflicting instructions may still require review.

## Modifying skills

The canonical repository is the **single source of truth** for each skill. `/oak-modify-skill` never edits a skill's source, installed copy, or symlink target to customize it; local changes go **only into a supported external per-skill override**.

- Skills from this repository: use `~/.claude/skill-overrides/<skill-name>.md` with the current skill name.
- Other or organization-owned skills: use their approved external override mechanism, if supported. Otherwise report the limitation; do not patch the original or its loader.
- Intentionally improving a canonical skill is a separate upstream source-development task, requiring authorization, review, and validation. Never substitute it for an override-only customization.


## Optional edit protection

Skill instructions help avoid accidental edits to the public source. Strict Claude Code edit-deny settings are separate from the Skills CLI and cannot be installed automatically by `npx skills add`.

An optional script, `scripts/protect-installed-skills.py`, generates scoped denies for verified installations from this repository. It deliberately does not block all `~/.claude/skills/**`, because unrelated skills may be editable. Permission rules are not a full filesystem security boundary.

## Independent skill selection

Skills are independent and do not reference or require each other. The developer or calling workflow selects combinations explicitly; an agent may independently select a relevant skill from the user's request and the skill's trigger description. Skills contain no worked product examples or domain-specific default choices.

## Discovery: interrogate ideas before committing scope

The installable `oak-discovery` skill reads accessible project code and documentation before questioning scope, then resolves decision dependency trees starting with blockers. It challenges material product, engineering, economic, operational, and trust assumptions with focused batches, evidence, alternatives, and qualified recommendations. Its record can be kept in the conversation or in a project-selected document. It does not silently decide scope, select technology, or implement features.
