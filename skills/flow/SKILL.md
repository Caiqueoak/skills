---
name: flow
description: Plan and deliver a software product using a portable spec workflow. Use for new app ideas, feature decomposition, PRD and architecture baselines, numbered requirements/design/tasks specs, or tracking TDD implementation progress.
allowed-tools: Bash(cat "$HOME/.claude/skill-overrides/flow.md" 2>/dev/null || true)
---

<!-- skill-source: Caiqueoak/skills -->

# Flow — spec-driven product engineering

Use this skill to create or maintain a project's _flow/ documentation and, when asked, implement its tracked tasks. It is a portable workflow, not a dependency on a specific product, domain, or runtime.

## Directory contract

Create these files in the **target project's root**, not in the skill installation:

~~~text
_flow/
  prd.md
  technical.md
  progress.md
  specs/
    001-feature-slug/
      requirements.md
      design.md
      tasks.md
      docs/                  # optional; other spec-specific documents go here
    002-feature-slug/
      requirements.md
      design.md
      tasks.md
~~~

Keep spec directories numbered with stable, ascending three-digit prefixes: 001, 002, ... . A folder 001-* maps to spec/work-item W001. Every task ID is W001-T001, W001-T002, etc.; IDs never change when a spec or task is renamed. Do not create extra peer files next to the three canonical spec artifacts. Place any additional spec-specific document under that spec's docs/; do not create an empty docs/ directory unnecessarily.

## Start from an idea

1. Inspect the target repository, existing _flow/, and any project-provided source material first. Treat supplied claims according to their evidence and confirmation status. Preserve established choices, files, and IDs; never replace populated documents with blank templates. Do not assume other workflows, documents, or installed capabilities exist.
2. Capture the product goal, intended users, critical workflows, constraints, and explicit unknowns. Ask focused questions only for decisions that genuinely block a useful baseline; otherwise label reasonable assumptions as assumptions. Never turn an assumption into an asserted fact.
3. Bootstrap _flow/prd.md, _flow/technical.md, and _flow/progress.md using the templates in references/templates/. Fill them with project-specific information; omit irrelevant headings only with a clear reason. Use TBD / open decisions where architecture or requirements cannot yet be responsibly decided.
4. Decompose the product into a small, prioritized set of vertically sliced, user-valuable specs using references/granularity.md. Create all three required spec files for every proposed spec, not merely folders or a single giant spec. Draft concise requirements, a scoped design, and actionable tasks; flag unresolved choices instead of inventing them.
5. Register every spec in progress.md with status and link. Identify the next actionable spec/task and material blockers. Produce an overview of the created documents and the rationale for the spec boundaries.
6. If the user asked only for planning, stop before coding. If implementation is requested, follow the TDD execution rules below.

Templates shipped with the installed skill:

- references/templates/prd.md
- references/templates/technical.md
- references/templates/progress.md
- references/templates/requirements.md
- references/templates/design.md
- references/templates/tasks.md

Treat templates as **scaffolds**, not literal outputs. Replace placeholders; remove instructions that are not facts about the project. Keep the skill itself domain-neutral and free of worked product examples.

## Single source of truth

A fact has **one canonical home**. Link to that home elsewhere; do not copy tables, requirements, acceptance criteria, contracts, or status into several documents.

| Canonical file | Owns |
| --- | --- |
| _flow/prd.md | Product intent, users, outcomes, scope, exclusions, product-level constraints |
| _flow/technical.md | Cross-spec architecture, stack, system boundaries, standards, cross-cutting engineering decisions |
| _flow/progress.md | Project phase, spec-level status, blockers, next step, lightweight history |
| specs/NNN-*/requirements.md | This spec's behavior, rules, and numbered acceptance criteria |
| specs/NNN-*/design.md | This spec's implementation design and spec-local technical decisions |
| specs/NNN-*/tasks.md | Ordered, uniquely identified executable tasks and their completion checkboxes |
| specs/NNN-*/docs/* | Optional supporting research or deeper detail; always linked from its owning canonical file |

Global documents describe the whole project; spec documents describe only their slice. The progress summary must never maintain an independent copy of task checkboxes or acceptance criteria. Link by relative path. If a decision belongs in technical.md, don't re-decide it in every design.md. Keep unrelated application documentation outside _flow/ according to the target project's conventions.

## Spec boundaries and lifecycle

- Prefer complete capabilities or observable user outcomes, not generic layers such as "database", "API", and "UI". Each spec has one coherent outcome and can be accepted independently, with clear dependencies when unavoidable.
- Size specs so requirements and design remain readable and tasks are independently verifiable. Split an oversized spec; merge tiny, tightly coupled specs. See references/granularity.md for portable heuristics.
- Plan tasks as small, sequential, testable changes. Each task maps to explicit acceptance criteria, has a verifiable completion condition, and should fit **one atomic commit**. Use the smallest meaningful vertical slice, not arbitrary file-by-file work.
- Initial statuses in progress.md: planned, ready, in_progress, blocked, done. Only one canonical spec status exists there. Task completion exists only in tasks.md.
- Work in dependency order. A spec is done only when all required tasks, acceptance criteria, relevant validations, and documentation are complete.
- Changes to product scope go to prd.md; cross-cutting decisions to technical.md; new behavior to its spec requirements; implementation changes to its design; tracking to progress.md/tasks.md. Reconcile downstream artifacts and note changed assumptions without copying content.
- Never renumber existing specs/tasks or reuse removed IDs. New work gets new IDs. Respect user decisions and inspect the code before revising a baseline.

## Implementation: TDD and atomic commits

For each W###-T### task:

1. Read its requirements and design, inspect relevant existing code, and confirm the task's scope/dependencies.
2. **Red:** add or adjust a meaningful failing automated test for the intended behavior. Confirm failure is due to missing behavior, not a broken test environment.
3. **Green:** implement the simplest production change that passes the test.
4. **Refactor:** improve readability and structure while tests stay green; run relevant regression checks.
5. Check acceptance criteria and task completion conditions. Update its checkbox in tasks.md, then the high-level state in progress.md when appropriate.
6. Commit the coherent code, tests, and directly related documentation **once**, after validation, following `feat(<scope>): <action> [W###-T###]` (with the actual task ID). Do not combine unrelated task IDs or create separate red/green commits. Record validation and any blockers in the PR.

If validation is unavailable or failing, do not mark the task done or claim success; document the blocker and stop that task. Never rewrite unrelated user changes. Parallel agents may work only on genuinely independent specs/branches with explicit file ownership; do not have them concurrently edit global _flow documents.

## Quality checks

Before calling planning complete, confirm the exact directory structure, all six document templates used, no unreplaced placeholders, stable IDs and links, no duplicated authoritative facts, clear spec boundaries, and real next actions. Before calling implementation complete, verify TDD evidence, a passing relevant test suite, one traceable commit per completed task, and reconciled progress.

## Public and private responsibilities

- **Public:** This reusable workflow, file contract, and templates belong in this skill and may be improved upstream when explicitly requested.
- **Private:** Workstation-, personal-, or workplace-specific conventions belong only in ~/.claude/skill-overrides/flow.md on that machine, never in this public repository.
- For local customization, change only the matching private file. Do not modify this public skill, installed copies, or symlink targets.
- Create the private file only when customization is requested; never commit, push, quote, or publish its contents. If instructions conflict, report the conflict and follow applicable company/security policies.

## Private instructions (Claude Code only, loaded on invocation)

!`cat "$HOME/.claude/skill-overrides/flow.md" 2>/dev/null || true`
