# Caiqueoak/skills

Globally reusable Agent Skills, with optional **private instructions per skill**. The public workflows can be updated independently of workplace customizations.

## Install — one command

```sh
npx skills add Caiqueoak/skills -g
```

Choose **Claude Code** and the skills when the CLI prompts. Both installed skills are self-contained: **no extra clone, template download, settings edit, or directory initialization is needed for normal use.** The CLI's `-g` flag makes skills available across projects.

Skills included:

| Skill | When to use |
| --- | --- |
| `/create-skill` | Create a new public, company-owned, or private skill; includes the public/private instructions convention |
| `/modify-skill` | Adapt an existing skill using ownership-aware routing; public skills from this repo receive private overrides |

## Public and private parts of every new skill

Public skills published to this repository have two logical parts:

```text
Caiqueoak/skills/
  skills/
    example/
      SKILL.md                    # Public, updatable upstream

~/.claude/
  skill-overrides/
    example.md                    # Private to this machine, optional
```

Each public `SKILL.md` explicitly documents the private companion and includes its own narrow shell permission and optional Claude Code loader:

```yaml
---
name: example
description: Describe when this skill should be used
allowed-tools: Bash(cat "$HOME/.claude/skill-overrides/example.md" 2>/dev/null || true)
---
```

```markdown
## Private instructions (Claude Code, loaded only when invoked)

!`cat "$HOME/.claude/skill-overrides/example.md" 2>/dev/null || true`
```

- **Installation:** Only the public skill is installed. There is nothing private to create during setup.
- **First workplace customization:** `/modify-skill example` creates `~/.claude/skill-overrides/example.md` if absent and writes the new rules there.
- **Later usage:** `/example` loads its public workflow plus `example.md` (if present); unrelated private files remain unloaded.
- **Upstream update:** The private companion stays outside the installed skill and is not replaced or merged with public content.
- **Privacy:** Never commit, push, paste into issues, or include private companion contents in public PRs.

The command injection and `allowed-tools` field are Claude Code features. A managed policy that disallows skill shell execution or disallows user-skill tool grants can prevent private loading; this repository cannot bypass organizational security settings. Claude Code skills loaded from cloud-synced accounts may have different execution rules. A skill's description is available for discovery, but the body and private instructions load only when invoked.

## Creating skills from anywhere

The public template is **bundled with the installed `/create-skill`** at:

```text
skills/create-skill/references/public-skill-template.md
```

It can be read from that skill's installed directory using `${CLAUDE_SKILL_DIR}`. You do not need a local clone of `Caiqueoak/skills` to read the template or follow the creation workflow. When actually publishing a new public skill, you still need the normal permission/access to change its GitHub repository.

The template requires a per-skill public/private section, optional private loader, narrow permission grant, and `<!-- skill-source: Caiqueoak/skills -->` source marker. **Company-owned skills are not required to use this convention**: they follow their employer's format and remain directly editable when authorized.

Read [AGENTS.md](AGENTS.md) for the repository maintenance policy.

## Ownership-aware modification

| Ownership | Editing behavior |
| --- | --- |
| `Caiqueoak/skills` | Local/work customization changes only `~/.claude/skill-overrides/<name>.md` |
| Company-owned | Edit the authorized original company skill directly |
| Other or uncertain | Verify source and policy first; do not identify ownership by skill name alone |

`/modify-skill` contains these rules **inside its own installed `SKILL.md`**, rather than relying on a global `CLAUDE.md` or `AGENTS.md` that might not be loaded from the source repository.

## Optional strict edit protection

The `npx skills add` CLI installs skill files. It **does not automatically change** `~/.claude/settings.json`, install global edit-deny permissions, or run scripts from this repository. Thus the normal single-command setup provides agent **instructions**, not an OS-enforced read-only guarantee.

If you additionally want Claude Code permission-level edit denies for this repository's installed skills, the optional `scripts/protect-installed-skills.py` can configure them from a separate clone:

```sh
git clone https://github.com/Caiqueoak/skills.git ~/caiqueoak-skills
python3 ~/caiqueoak-skills/scripts/protect-installed-skills.py --apply
```

This is **not required for normal skill behavior**. The script scopes denies to identified `Caiqueoak/skills` installations and checkout, not all `~/.claude/skills/**`; company skills remain editable. Manually remove broad deny rules if you previously configured them. Permission rules are not a complete filesystem isolation boundary.

## Maintenance

- Public improvements require an explicit upstream request; workplace-specific adaptations are private by default.
- `npx skills update -g` updates installed public skills; it does not edit the independent private companions.
- Don't install company-owned and public skills under the same name at the same agent path; resolve name collisions explicitly.
- Respect company policies on storing or sending internal instructions to AI tools.
