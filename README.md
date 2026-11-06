# Caiqueoak/skills

Reusable, company-independent Agent Skills. **Public workflows stay upstream; workplace customizations stay private and are loaded only with their matching skill.**

## Skills in this repository

| Skill | Purpose |
| --- | --- |
| `/create-skill` | Create a new, well-scoped Agent Skill in its appropriate repository or directory |
| `/modify-skill` | Change existing skills according to verified ownership; route this repository's local adaptations to private files |

Read [AGENTS.md](AGENTS.md) for authoring and maintenance rules and [templates/skill/SKILL.md](templates/skill/SKILL.md) when creating a public skill.

## Ownership-based modifications

| Origin | Where to edit | Protection |
| --- | --- | --- |
| `Caiqueoak/skills` | `~/.claude/skill-overrides/<skill-name>.md` for local/workplace changes | Explicit edit denies for verified installed skills |
| Company-owned | Company's canonical `SKILL.md` (subject to authorization) | **Not blocked** by this repo's rules |
| Other/unknown | Check provenance and applicable rules first | No assumptions by name alone |

The public skill contains the optional Claude Code dynamic injection:

```markdown
## Optional private instructions (Claude Code only)

!`cat "$HOME/.claude/skill-overrides/<skill-name>.md" 2>/dev/null || true`
```

This loads only the matching private file when the skill runs. The file is not a global rule, and isn't part of GitHub or installed skill content. Missing private files contribute no additional text.

> Dynamic injection is a **Claude Code-specific** extension that depends on permitted shell execution. It is not guaranteed by the portable Agent Skills standard. Check employer policies before including internal information in any model context.

## Work-machine setup

Install the public skills:

```sh
npx skills add Caiqueoak/skills -g
mkdir -p ~/.claude/skill-overrides
```

Optionally set up ownership-scoped file edit protection:

```sh
git clone https://github.com/Caiqueoak/skills.git ~/caiqueoak-skills
python3 ~/caiqueoak-skills/scripts/protect-installed-skills.py
python3 ~/caiqueoak-skills/scripts/protect-installed-skills.py --apply
```

- First command previews rules; `--apply` updates `~/.claude/settings.json` while retaining existing unrelated settings.
- The script inspects installed skills under `~/.claude/skills/` and `~/.agents/skills/`. It protects only installed skills carrying this repository's source marker and the public checkout's `skills/` directory. **Company skills without that ownership marker remain editable**, even when they share a name.
- It tracks its own generated rules in `~/.claude/skill-overrides/.managed-edit-denies.json`, so re-running it after skill updates can remove stale managed rules.
- If you previously installed broad denies such as `Edit(~/.claude/skills/**)`, remove them manually first. The installer refuses to proceed while they exist.
- Re-run `npx skills add ...` / your update command and then the protection script after adding or updating public skills. Verify installed paths and rules in Claude Code's `/permissions` dialog.
- `Edit` deny rules cover Claude Code's built-in file-editing tools and some recognized shell operations. They **do not block every indirect write by arbitrary programs**. For strong isolation use filesystem permissions or a sandbox.

Do not install company-owned skills on top of identically named public skills. Name collisions should be resolved explicitly instead of relying on path matching.

## Create a public skill

Run `/create-skill`, or copy `templates/skill/SKILL.md` to `skills/<skill-name>/SKILL.md` and fill in the template. Keep the source marker and per-skill private loader. Use a short description that says when the skill should be invoked. Never publish internal examples or instructions.

## Customize a skill at work

Use `/modify-skill flow` (replace `flow` with the target skill). For a skill owned by this repository, the agent updates only `~/.claude/skill-overrides/flow.md`; for an authorized company-owned skill, it can edit the company skill directly.

Public and private files do not have Git merge conflicts, but their instructions can still contradict one another. Resolve contradictions deliberately.
