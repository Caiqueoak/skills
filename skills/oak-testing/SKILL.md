---
name: oak-testing
description: Design, create, maintain, and execute meaningful automated tests with minimal feedback latency. Use for TDD, test changes, regression selection, or optimizing test execution in any framework.
---

<!-- skill-source: Caiqueoak/skills -->

# Testing — meaningful coverage, fast feedback

Protect canonical behavior with the smallest sufficient tests and validation scope. Do not equate test count, coverage, or suite size with confidence. Adapt to the target repository's actual language, runner, configuration, and policies.

## Select the relevant workflow

- **Create, change, review, or remove tests:** read `references/creation.md`.
- **Run tests, choose a validation scope, or improve feedback time:** read `references/execution.md`.
- **TDD or test maintenance involving both:** read both, and apply creation rules before selecting execution.
- Read only the needed reference(s); do not load unrelated guidance by default.

## Shared rules

1. **Inspect before acting:** identify requested scope, canonical requirements/accepted behavior, existing tests, affected code and dependencies, runner capabilities, and CI gates. Do not invent requirements or commands.
2. **Test a contract, not an accident:** each test must identify an intended behavior or invariant and a plausible regression it detects. A previous implementation mistake is not a new requirement.
3. **Use risk-proportionate coverage:** choose the cheapest test layer that actually verifies the contract; preserve real boundary checks when mocks alone cannot prove integration.
4. **Optimize the whole feedback loop:** minimize test creation, fixture/setup, discovery, compilation, process/browser startup, and execution cost without weakening assertions or hiding failures.
5. **Keep scope narrow:** avoid unrelated test creation, unrelated feature edits, and routine full-suite execution in local TDD loops. Broaden verification for changes that materially affect shared behavior or safety.
6. **Be transparent:** record what ran, what failed or was skipped, relevant duration if available, and risks not validated. Never claim unexecuted checks passed.

## Completion checks

- Every added or retained test has a canonical behavioral reason and meaningful assertion.
- Removed or changed behavior has its obsolete tests reconciled; no reflexive tests asserting that accidental features are absent.
- The relevant changed behavior was validated with the smallest sufficient runner selection, and broader gates were respected when required.
- Test commands, results, unrun checks, and blockers are reported without inventing evidence.

## Public and private responsibilities

- **Public:** Reusable, company-independent instructions belong in this `SKILL.md` and its own references, and may be improved upstream when explicitly requested.
- **Private:** Workstation, personal, and workplace-specific instructions belong only in `~/.claude/skill-overrides/oak-testing.md` on the machine where they are needed.
- For local customization of this skill, update only the matching private file. Do not modify this public file, installed copies, or symlink targets.
- Create the private file only when customization is requested; it is never stored in this repository, committed, pushed, or included in public PRs.
- If private and public instructions conflict, surface the conflict and comply with applicable company and security policies. Do not silently overwrite the public workflow.

## Optional private override (on invocation)

When invoked, resolve `~` to the active user's home directory and attempt to read `~/.claude/skill-overrides/oak-testing.md` using an available native file-reading tool or API. Do not require Bash, `cat`, or any specific shell. Apply only this skill's matching private instructions. If the file is absent or inaccessible, continue with the public workflow; report the access limitation only if it affects the requested customization. Do not read unrelated overrides or disclose private contents.
