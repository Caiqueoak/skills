---
name: oak-modify-skill
description: Customize existing Agent Skills through external per-skill overrides without editing their canonical definitions, installed copies, or symlink targets.
allowed-tools: Bash(cat "$HOME/.claude/skill-overrides/oak-modify-skill.md" 2>/dev/null || true)
---

<!-- skill-source: Caiqueoak/skills -->

# Modify a skill

**Invariant: never edit a skill definition to customize it.** The owning source repository is the single source of truth (SSOT) for a skill's canonical instructions. Installed skills, copied `SKILL.md` files, bundles, and symlink targets are derived artifacts, not customization surfaces. Apply local or environment-specific changes **only through an external, per-skill override**.

## Identify the skill and override contract

1. Locate the target skill, inspect its `SKILL.md`, resolved path, and provenance. Identify its canonical repository rather than inferring ownership from its name.
2. Determine the skill's supported override mechanism and exact path. Follow the owner's policy and organizational security constraints; do not assume every runtime supports Claude Code's dynamic loading.
3. For skills originating from `Caiqueoak/skills`, use only `~/.claude/skill-overrides/<skill-name>.md` (with the **current full skill name**) for local customization. Verify the skill already loads this file and permits its narrowly scoped read command.
4. For skills from another owner, use only an external override that the skill/runtime explicitly supports and that the owner permits. Do not impose this repository's path convention on unrelated skills.
5. If an external override cannot be loaded, **stop and report the limitation**. Do not patch the skill, its loader, an installed copy, a symlink target, or the upstream repository as a workaround.

## Customize through the override

1. Read the canonical skill only as reference. Leave its contents, metadata, references, and installed files unchanged, whether publicly or organization owned.
2. Create or update **only** the matching external override file. Preserve unrelated existing instructions. Do not share one override across multiple skills or load unrelated context.
3. Keep personal, organizational, and confidential instructions in their authorized private location. Never commit, push, copy into public artifacts, or disclose private override contents.
4. Confirm the override path is correct, its loader is available in the target runtime, and the resulting instructions are effective where verification is possible. If not verifiable, say so rather than claiming success.
5. Verify the canonical source, installed copy, and symlink target were **not modified**.

## Separate canonical maintenance from customization

An explicitly requested reusable improvement to the base skill is a **separate upstream development task**, performed in an authorized source-repository checkout through its normal review, test, and publication process. It is **not** a local skill customization or permission to patch an installed copy. For all ordinary modification requests, use an override only. Never silently turn a customization request into a source-repository edit.

## Finish

Report the skill and provenance, the override path updated (not its private contents), and what was verified or blocked. Never claim the canonical skill was updated when only an override changed.

## Optional private instructions (Claude Code only, loaded on invocation)

!`cat "$HOME/.claude/skill-overrides/oak-modify-skill.md" 2>/dev/null || true`
