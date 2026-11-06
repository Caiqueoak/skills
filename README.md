# Reusable Agent Skills

Public, company-independent skills for compatible coding agents. The canonical source is this repository. **Workplace-specific customizations belong in private, skill-scoped files on the work machine**, never in this repository or an installed public skill.

## Layout

```text
skills/
  customize-skill/SKILL.md    # Private customization workflow
templates/
  skill/SKILL.md              # Starting point for any new public skill
AGENTS.md                     # Rules for agents maintaining this repository
```

## Install

```sh
npx skills add Caiqueoak/skills -g
```

To create another public skill, copy `templates/skill/SKILL.md` to `skills/<skill-name>/SKILL.md`, replace `{{SKILL_NAME}}` and `{{DESCRIPTION}}`, then write its reusable workflow. Use kebab-case for names.

## How per-skill private customizations work

Every published skill uses this convention (replace `<skill-name>` with the skill's name):

```text
Public:  skills/<skill-name>/SKILL.md
Private: ~/.claude/skill-overrides/<skill-name>.md
```

The public skill includes an optional Claude Code dynamic-context command:

```markdown
## Optional private instructions

!`cat "$HOME/.claude/skill-overrides/<skill-name>.md" 2>/dev/null || true`
```

Claude Code expands the private file **only when that skill is invoked**. A missing file adds no context. Each skill loads only its own private file; no global `CLAUDE.md` or global rules are needed. The public workflow remains reusable on machines where no private file exists.

**Important:** The injection syntax is a Claude Code extension, not a portable Agent Skills feature. It requires shell execution to be enabled and permitted by local/company policy, and the example expects a Bash-compatible shell. Some managed Claude Code setups can disable it. Do not bypass your employer's restrictions. Other agents can use the public skill but may ignore the private injection.

## Customize privately at work

Run `/customize-skill <skill-name>` and describe the change, or invoke the target skill and request a local-only customization. The agent must edit only `~/.claude/skill-overrides/<skill-name>.md`, not the installed/public skill. Keep this directory outside every public repository.

Example private file, **created on your work machine, not committed here**:

```markdown
# Local additions for flow-core

- Follow internal documentation conventions.
- Use the organization's approved tooling.
- Do not publish internal code or details.
```

The public skill and private file are separate, so updating the public skill cannot overwrite the private customization or cause a Git merge conflict. However, conflicting *instructions* may need to be reconciled.

## Prevent accidental edits to public skills

On the work machine, consider adding these rules to **your existing** `~/.claude/settings.json` (merge with existing settings; do not overwrite them):

```json
{
  "permissions": {
    "deny": [
      "Edit(~/.claude/skills/**)",
      "Edit(~/.agents/skills/**)",
      "Edit(~/skills-public/**)"
    ]
  }
}
```

The `.agents/skills` rule covers installations that use that shared skills directory. Here `~/skills-public` is the optional local checkout of this public repository. If you use a different checkout path, change that rule. `Edit` rules also cover Claude Code's Write tool. They substantially reduce accidental modifications to public skill files, including symlink targets, but do **not** prevent all arbitrary shell scripts, external tools, or manual edits. For strict isolation use file-system access controls or a separate work environment.

Do not add deny rules for `~/.claude/skill-overrides/**`; that is where workplace changes belong.

## Publishing and security

- Only reusable, non-confidential instructions may enter this repository.
- The explicit request must be to improve the public behavior before a public skill is changed.
- Work-only changes are private by default; do not add private content to commits, PRs, logs, or public issues.
- Follow your employer's policies before storing internal rules locally or sending them to an external model.
- Review public skill updates before installation, as with any executable skill content.
