---
name: oak-modify-skill
description: Customize existing Agent Skills through external per-skill overrides without editing their canonical definitions, installed copies, or symlink targets.
allowed-tools: Bash(cat "$HOME/.claude/skill-overrides/oak-modify-skill.md" 2>/dev/null || true)
---

<!-- skill-source: Caiqueoak/skills -->

# Modify a skill

**Invariant: never edit a skill definition to customize it.** The canonical source repository is the **single source of truth (SSOT)**. Installed copies, bundles, and symlink targets are derived artifacts. Make local changes **only through an external, per-skill override**.

## Procedure

1. Identify the target skill, its resolved path, owner, canonical source, and documented override mechanism. Do not infer ownership or permission from a name.
2. For skills owned by `Caiqueoak/skills`, use `~/.claude/skill-overrides/<skill-name>.md` with the full current name, and verify that the matching loader is supported. For other owners, follow only their approved external mechanism; do not impose this path on them.
3. If no usable, authorized external override exists, **stop and report the limitation**. Never patch a public skill, its loader, an installed copy, or a symlink target as a workaround.
4. Read the skill for reference. **Leave its contents, metadata, references, and installed files unchanged**, whether publicly or organization owned. Create or edit only the corresponding private override; preserve unrelated instructions.
5. Keep all personal, internal, and confidential instructions private. Do not commit, publish, paste, or log override contents. Do not share one extension across different skills.
6. Check the override path and loader, verify effective behavior when possible, and confirm no canonical or installed files changed. Report what was verified and what remains untested.

## Upstream changes are different

An explicitly authorized, reusable change to a canonical skill is a **separate upstream development task** with source-repository review, tests, and publication. Never silently substitute an upstream edit for a local customization.

## Finish

State the skill's provenance, which override path was edited, and the actual validation or blocker. Updating an override is not updating the canonical skill.

## Public and private responsibilities

- **Public:** This portable modification policy and override decision procedure.
- **Private:** Local conventions belong only in `~/.claude/skill-overrides/oak-modify-skill.md`; do not disclose or commit private instructions.

## Optional private instructions (Claude Code only, loaded on invocation)

!`cat "$HOME/.claude/skill-overrides/oak-modify-skill.md" 2>/dev/null || true`
