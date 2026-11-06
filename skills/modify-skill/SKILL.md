---
name: modify-skill
description: Modify existing Agent Skills. Route local changes to Caiqueoak/skills skills into private per-skill files while allowing authorized direct edits to company-owned skills.
allowed-tools: Bash(cat "$HOME/.claude/skill-overrides/modify-skill.md" 2>/dev/null || true)
---

<!-- skill-source: Caiqueoak/skills -->

# Modify a skill

Treat **ownership as the decision boundary**, not whether the skill is public or private.

## Classify before editing

1. Locate the target skill and inspect its `SKILL.md`, resolved symlink path, and repository origin where available. Do not classify a skill from its name alone.
2. `Caiqueoak/skills` ownership is confirmed by an installed source marker (`<!-- skill-source: Caiqueoak/skills -->`) together with its source path or repository provenance. This public repository's skills are **read-only targets** for ordinary customization.
3. Company-owned skills in company-controlled directories/repositories are **editable directly** when the user requests a change and company policy allows it. Never impose this repository's deny rules on company skills.
4. If provenance is uncertain, inspect further; ask which copy is intended before modifying anything. Do not infer that an unfamiliar skill belongs to this repository.

## Modify a skill from Caiqueoak/skills

1. Read the public skill as reference only.
2. Read and edit **only** `~/.claude/skill-overrides/<skill-name>.md` on this machine. Create the directory and file when first needed, without any separate setup step. Preserve unrelated private instructions.
3. Never modify installed copies, their symlink targets, or the public repository for a local adaptation. Never commit, push, or expose private override contents.
4. Verify that the public skill loads its matching private file through Claude Code dynamic context and has a narrow `allowed-tools` grant for that command. If it does not, report that the override cannot load automatically; don't alter the installed public skill to fix it.
5. For a truly reusable upstream improvement, have the user explicitly request public development as a separate task in a trusted development checkout. Keep any workplace information out of it.

## Modify a company-owned skill

1. Read that skill's instructions and the organization's repository rules.
2. Edit the **authorized company skill itself** at its canonical source; follow normal testing/review/version-control practices.
3. Do not redirect company skill edits into `~/.claude/skill-overrides/` by default; this mechanism is reserved for this repository's public skills.
4. Do not make an unrelated company skill read-only merely because it is installed in `~/.claude/skills` or `~/.agents/skills`.

## Finish

Summarize the target, the verified ownership, which file was changed, and how the behavior was checked. Do not print confidential instructions unnecessarily.

## Optional private instructions (Claude Code only, loaded on invocation)

!`cat "$HOME/.claude/skill-overrides/modify-skill.md" 2>/dev/null || true`
