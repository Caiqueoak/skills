---
name: oak-create-skills
description: Create, validate, and publish new reusable Agent Skills in a public skills repository. Use when asked to author a new skill, package reusable agent instructions, or publish a skill through Git and a pull request, following the destination repository's authoring standards.
---

<!-- skill-source: Caiqueoak/skills -->

# Create and publish Agent Skills

Author a narrow, independently usable Agent Skill in the authorized canonical source repository. Do not assume other skills, project-specific tooling, or a particular runtime.

## Authority and inputs

- For this collection, the public destination is `Caiqueoak/skills`. Read `AGENTS.md`, `templates/skill/SKILL.md`, existing skills, tests, and CI from the **current repository state**. The destination's **canonical template** and policy, not copied instructions, define the contract.
- Locate an authorized source checkout or authenticated connector. Never edit installed copies, **symlink targets**, or private extensions.
- When another repository is selected, use that owner's rules. A draft request authorizes no publication; an explicit publish/push request authorizes a **reviewable branch and PR**, not bypassing review.
- **If repository access or authorization is unavailable**, provide the draft and precise blocker. Never pretend that code, a PR, checks, or merge exist.

## Creation and publishing workflow

1. **Specify purpose:** identify trigger, expected output, safety boundaries, non-goals, and required evidence. Choose a clear kebab-case name; use the `oak-` prefix exactly once only for this repository.
2. **Check existing work:** inspect names/descriptions to prevent duplicate responsibilities; expand an existing skill rather than overwriting it as new.
3. **Start from source:** use the current `templates/skill/SKILL.md` and create `skills/<skill-name>/SKILL.md`. Preserve marker, metadata, public/private division, matching shell-independent optional private-override lookup.
4. **Keep instructions reusable:** public content must be **domain-neutral**, self-contained, and portable. **Never mention or assume other installed skills.** Avoid concrete use cases, private context, default technology, duplicated rules, and **unnecessary configuration**; bundle only needed relative references/scripts.
5. **Audit content:** treat every staged file as **publicly readable**. Remove credentials, private overrides, workplace details, internal URLs, accidental artifacts, or confidential information before any external write. **No private material** may appear in source, reviews, logs, or tests.
6. **Validate:** inspect metadata, trigger specificity and **false triggers**, templates, linked files, portability, source provenance, security, and **least privilege**. Run relevant tests and public-file guard, review the diff, and disclose what could not run.
7. **Publish when authorized:** create a topic branch from the **latest default branch**, change only intended files, commit coherently, push, and **open a PR**. Put purpose, decisions, validation evidence, affected scope, public-content audit, and limitations **in the PR itself**. Do not push straight to the default branch.
8. **Verify outcome:** inspect CI and reviews. Merge only if explicitly requested, authorized, and required **checks/reviews pass**. **After merge, verify** the skill exists on the default branch. Report the exact branch, commit, PR, checks, and merge state.

## Safeguards

- **Do not infer authorization to bypass reviews**, force-push, rewrite history, or cross repository ownership boundaries.
- Prefer narrowly scoped edits, existing credentials and permissions, and immutable records of what actually happened.
- **A pushed branch, open PR, and merged skill are distinct outcomes.** Never claim publication or installation from an unmerged branch.
- Keep local customization separate from canonical upstream development. Respect applicable owner and organization rules.

## Public and private responsibilities

- **Public:** Reusable, independent guidance and any references belonging to this skill, without domain or organization assumptions.
- **Private:** Local and workplace conventions belong only in `~/.claude/skill-overrides/oak-create-skills.md`. Create this file only when requested; for customization edit it, not public source, installed copies, or symlink targets. Never quote, commit, or publish private instructions.

## Optional private override (on invocation)

When invoked, resolve `~` to the active user's home directory and attempt to read `~/.claude/skill-overrides/oak-create-skills.md` using an available native file-reading tool or API. Do not require Bash, `cat`, or any specific shell. Apply only this skill's matching private instructions. If the file is absent or inaccessible, continue with the public workflow; report the access limitation only if it affects the requested customization. Do not read unrelated overrides or disclose private contents.
