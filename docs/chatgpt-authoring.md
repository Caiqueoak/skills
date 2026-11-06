# Create and maintain skills using ChatGPT

**Authoring environment:** ChatGPT (using the connected GitHub repository).
**Execution environment:** Claude Code on personal or work machines.
**Private customization:** Local to the work machine; never stored in this public GitHub repository.

You do **not** need to run `/create-skill` in Claude Code to create a public skill. That installed skill is an optional alternative for users authoring directly from Claude Code. ChatGPT can read this repository's authoring contract and write to GitHub using its GitHub integration.

## ChatGPT workflow: new public skill

When asked to create a new skill in `Caiqueoak/skills`:

1. Read this repository's `AGENTS.md` and the **canonical** template at `skills/create-skill/references/public-skill-template.md` on the current default branch.
2. Define one clear responsibility, a kebab-case name, and a trigger-oriented description. Confirm that all contents can safely be published.
3. Create `skills/<skill-name>/SKILL.md` and any *necessary* references/scripts on a new GitHub branch. Preserve the exact template's `<!-- skill-source: Caiqueoak/skills -->` marker, public/private responsibilities section, matching optional private loader, and its narrow `allowed-tools` command.
4. Do not create `~/.claude/skill-overrides/<skill-name>.md`, change Claude settings, or publish workplace details. Those are local work-machine concerns.
5. Validate the skill metadata, loader/name alignment, file paths, and scope; run/review the repository's checks. Open a pull request recording context, decisions, changes, and test evidence. Never claim a Claude Code runtime test happened unless it actually did.
6. Merge only when appropriate and authorized. Explain the installation or update command. When the repo is updated, `npx skills add Caiqueoak/skills -g` (or the user's CLI update workflow) can install the public changes.

## ChatGPT workflow: update a public skill

- Read the existing public skill and relevant repo conventions before changing it.
- Publish **only reusable improvements**. Never move private workplace instructions from a local file or chat into the public skill.
- Preserve the public/private loader contract and do not overwrite the private addendum.
- Use a PR with validation evidence.

If the request is to customize public behavior **for work**, explain that the change belongs in the work machine's `~/.claude/skill-overrides/<skill-name>.md`. ChatGPT cannot access that local file through the public GitHub connection. The user can apply the change locally with Claude Code's `/modify-skill`.

For **company-owned skills**, their own organization controls authoring and modifications. Do not add `Caiqueoak/skills` ownership markers or protection rules to them.

## Real example

Ask ChatGPT:

> Create a public `flow` skill in `Caiqueoak/skills` for specification-driven development. Use this repository's `AGENTS.md` and bundled template. Keep it generic, include optional private instructions, validate it, and open a PR.

After merging, install on a Claude Code machine:

```sh
npx skills add Caiqueoak/skills -g
```

At work, ask Claude Code:

> /modify-skill flow — use the company-approved architecture patterns and commit conventions.

Claude should place those work-specific additions in `~/.claude/skill-overrides/flow.md`, not in the installed public `flow/SKILL.md`. When `/flow` is invoked, only its matching private file is loaded alongside the public skill, subject to company-managed tool permissions.

## Constraints

- A single `npx skills add` installs **public skill content**, not local private configuration or strict edit-deny settings.
- The private loader uses Claude Code's dynamic shell injection and may be restricted by company policy.
- Private overrides stay outside GitHub; their separation avoids file merge conflicts but not all possible instruction conflicts.
