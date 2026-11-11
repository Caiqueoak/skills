---
name: oak-create-skills
description: Create, validate, and publish new reusable Agent Skills in a public skills repository. Use when asked to author a new skill, package reusable agent instructions, or publish a skill through Git and a pull request, following the destination repository's authoring standards.
allowed-tools: Bash(cat "$HOME/.claude/skill-overrides/oak-create-skills.md" 2>/dev/null || true)
---

<!-- skill-source: Caiqueoak/skills -->

# Create and publish Agent Skills

Create a narrow, useful Agent Skill from a requested capability, validate it against its **canonical source repository**, and publish it through a reviewable Git change when authorized. Work independently: do not assume, load, or depend on any other skill or a particular agent runtime.

## Destination and authority

- The default public source and publishing destination is `Caiqueoak/skills`. Determine its current default branch and read `AGENTS.md`, `templates/skill/SKILL.md`, relevant tests, and CI configuration **from the current repository state** before authoring. These files, not a copied template in this skill, own the publishing contract.
- The skill may run from any working directory. Locate an authorized development checkout or use an authenticated repository connector; **never edit installed skill copies, symlink targets, or user private extensions**.
- If the user explicitly selects another destination, inspect that repository's standards and permissions rather than imposing this repository's conventions on it. Do not silently publish to a different owner or repository.
- Public publication requires a user-authorized destination and write operation. A request to create **and publish/push** authorizes a reviewable branch and PR; a request for a draft only does not. Do not infer authorization to bypass reviews, force-push, delete history, or merge protected branches.
- If repository access or authorization is unavailable, provide the complete draft and the specific blocker; never claim a push, PR, check, or merge happened when it did not.

## Creation workflow

1. **Define the contract.** Extract the requested behavior, when the skill should trigger, expected output, boundaries, evidence requirements, and non-goals. Choose an unambiguous kebab-case name and a trigger-oriented description. When publishing to `Caiqueoak/skills`, prefix each public skill name with `oak-` exactly once; elsewhere follow the destination's conventions. Ask for a missing decision only if it materially changes the skill's purpose or safety; avoid speculative questions and invented project requirements.
2. **Check ownership and duplicates.** Inspect the destination's existing names, skill descriptions, canonical template, authoring policy, and tests. If a skill with equivalent responsibility already exists, report the overlap and recommend a scoped addition or improvement. Do not overwrite it as a new skill.
3. **Build from the canonical template.** Create `skills/<skill-name>/SKILL.md` at the destination's canonical source, replacing template placeholders. Preserve the repository's source marker, required frontmatter, public/private responsibility rules, and its **matching optional private-extension loader**, including correctly scoped tool permissions. Load only that skill's optional extension when invoked; a missing extension must be harmless.
4. **Keep the public skill abstract.** Use clear, domain-neutral procedures, criteria, constraints, and completion gates; avoid worked product examples, concrete personas, stack preferences, vendor choices, organization internals, and model-biasing defaults. Never mention or assume other installed skills. Prefer concise instructions over long catalogs or unnecessary abstractions.
5. **Bundle only necessary assets.** Put genuinely required references/scripts inside the new skill directory using stable relative paths. Keep source documents and rules single-source-of-truth; reference the canonical repository template rather than duplicating it. Do not add unnecessary configuration, dependencies, installers, or auto-executing scripts.
6. **Review safety before any external write.** Inspect **all staged content** for credentials, personal or workplace details, private overrides, internal URLs, confidential procedures, unsafe instructions, accidental generated artifacts, and dependency on machine-local paths. Exclude sensitive material entirely, even if the request originated from a private conversation. Treat the target as publicly readable.
7. **Validate behavior and contract.** Check the name/trigger specificity and false triggers, metadata, marker, loader/path match, resource paths, skill independence, portability, permissions, and completeness. Add focused tests when useful, run available repository tests and the public-file guard, and review the actual diff. Document checks that could not run; never invent a passing result.
8. **Publish when authorized.** Start a topic branch from the latest default branch, change only the intended skill and directly related tests/docs, make a coherent commit, push through authenticated Git or the repository connector, and open a PR. Explain purpose, design choices, affected files, validation **with evidence**, public-content audit, and limitations **in the PR itself**. Avoid direct pushes to the default branch.
9. **Verify and report.** Check required CI and review status. Merge only when the user has requested publication **to the default branch**, permissions and branch rules allow it, and required checks/reviews pass. Otherwise leave a reviewable PR and state its status. After merge, verify that `skills/<skill-name>/SKILL.md` exists on the destination default branch. Report the precise repository, branch, PR, commit, checks and actual merge status.

## Publishing safeguards

- **Explicit scope:** Create a new public skill only when requested; do not silently modify other skills or bundle unrelated edits. A public-source improvement is distinct from a local/private customization.
- **No private material:** Never read out, copy, commit, push, quote, or expose private-extension contents or unrelated user/workplace data in a public artifact, branch, PR, log, or test fixture.
- **Least privilege:** Use existing authenticated tooling; never request or place credentials in prompts, code, configs, commits, or command arguments. Do not create broad tool permission grants solely to ease publishing.
- **Reviewable changes:** Re-read the latest base before writing; do not overwrite concurrent work, rewrite default-branch history, bypass branch protections, or merge failing checks.
- **Provenance and neutrality:** Follow the selected repository's current conventions; every published skill should be independent, free of concrete use cases and unjustified assumptions, and safe to install without optional local configuration.
- **Truthful completion:** A pushed branch, open PR, and merged skill are distinct outcomes. State which was achieved; no public installation claim until the source exists on the canonical default branch.

## Public and private responsibilities

- **Public:** This portable skill-authoring and publishing process, using the destination repository's canonical policies at execution time.
- **Private:** Workstation-, personal-, and workplace-specific instructions belong only in `~/.claude/skill-overrides/oak-create-skills.md` on the machine where they are needed.
- For local customization, edit only the matching private file; do not change this public source, an installed copy, or a symlink target.
- Create the private file only when requested. Never commit, push, quote, or reproduce its contents in public source, reviews, or logs. If instructions conflict, surface the conflict and follow applicable organization and security policies.

## Private instructions (Claude Code only, loaded on invocation)

!`cat "$HOME/.claude/skill-overrides/oak-create-skills.md" 2>/dev/null || true`
