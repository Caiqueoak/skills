# Reusable Agent Skills

A public collection of reusable Agent Skills. Each skill keeps its general workflow separate from optional, environment-specific instructions.

## Installation

```sh
npx skills add Caiqueoak/skills -g
```

The installer provides the public skills. Private instructions are optional and do not need to exist at installation time.

## Repository structure

```text
skills/
  flow/
    SKILL.md
    references/
      granularity.md
      templates/
        prd.md, technical.md, progress.md
        requirements.md, design.md, tasks.md
  modify-skill/
    SKILL.md
templates/
  skill/
    SKILL.md
AGENTS.md
.github/workflows/validate.yml
```

## Flow: spec-driven project planning

The installed /flow skill turns a product idea into a project-local _flow/ baseline with a PRD, technical architecture, progress tracker, and numbered specs containing requirements.md, design.md, and tasks.md. Extra spec documents belong in that spec's docs/ subdirectory. Each W###-T### task is implemented with TDD and one verified, traceable commit. The skill ships templates and an abstract spec-decomposition guide; it does not add a _flow/ directory to this skills repository. It is independent of other installed skills and accepts only project-provided inputs.

## Creating a skill

Follow [AGENTS.md](AGENTS.md) for repository authoring conventions, and start from the [canonical skill template](templates/skill/SKILL.md).

1. Define one clear responsibility, a kebab-case skill name, and a description explaining when it should be used.
2. Create `skills/<skill-name>/SKILL.md`. Keep the template's source marker, public/private split, and matching optional private loader.
3. Put all required references and scripts inside that skill's directory so it works after global installation.
4. Validate before publishing with `python -m unittest discover -s tests -v`. Use a PR for changes and record the validation results.

Skill creation is maintained through the repository's authoring standards; only runtime-useful skills are installed.

## Public/private extension contract

For a skill named `example`:

```text
skills/example/SKILL.md                   # Public source
~/.claude/skill-overrides/example.md      # Optional local extension
```

The public skill provides the reusable workflow; the private file contains local or environment-specific additions. Each public skill includes an optional loader for **only its matching private file**, loaded when that skill is invoked.

```markdown
## Private instructions (Claude Code only)

!`cat "$HOME/.claude/skill-overrides/example.md" 2>/dev/null || true`
```

The canonical template also includes the corresponding narrowly scoped `allowed-tools` permission. This mechanism uses Claude Code features, so behavior may vary across agents or managed environments.

Private files must never be committed to this repository, copied into public examples, or included in pull requests. Updating public skills leaves independent private files unchanged; conflicting instructions may still require review.

## Modifying skills

| Origin | Local modification behavior |
| --- | --- |
| This repository | Change the matching private extension; do not edit installed/public files for local customization |
| Other repositories | Verify ownership and applicable rules before editing |
| Organization-owned | Edit the authorized original when permitted by the organization |

The `/modify-skill` skill implements these routing rules.

## Optional edit protection

Skill instructions help avoid accidental edits to the public source. Strict Claude Code edit-deny settings are separate from the Skills CLI and cannot be installed automatically by `npx skills add`.

An optional script, `scripts/protect-installed-skills.py`, generates scoped denies for verified installations from this repository. It deliberately does not block all `~/.claude/skills/**`, because unrelated skills may be editable. Permission rules are not a full filesystem security boundary.

## Independent skill selection

Skills are independent and do not reference or require each other. The developer or calling workflow selects combinations explicitly; an agent may independently select a relevant skill from the user's request and the skill's trigger description. Skills contain no worked product examples or domain-specific default choices.

## Discovery: interrogate ideas before committing scope

The installable `discovery` skill systematically challenges assumptions across users, product, market, business viability, engineering, infrastructure, security, privacy, compliance, operations, and edge cases. It uses batches of focused questions, offers meaningful options and qualified recommendations, and iterates on answers until a decision-ready consensus is reached without unacknowledged material gaps. Its record can be kept in the conversation or in a project-selected document. It does not silently decide scope, select technology, or implement features.
