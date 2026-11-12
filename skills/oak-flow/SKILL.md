---
name: oak-flow
description: Plan and deliver a software product using a portable spec workflow. Use for new app ideas, feature decomposition, PRD and architecture baselines, numbered requirements/design/tasks specs, or tracking TDD implementation progress.
---

<!-- skill-source: Caiqueoak/skills -->

# Flow — spec-driven product engineering

Plan, document, and optionally implement a project's work with a portable `_flow/` baseline. **Do not assume other workflows** or installed capabilities. Inspect relevant project code and documents first; preserve established decisions and user changes.

## Canonical directory and ownership

Create files at the target project's root, never in this installed skill:

```text
_flow/
  discovery.md
  prd.md
  technical.md
  progress.md
  specs/
    001-feature-slug/
      requirements.md
      design.md
      tasks.md
      docs/                 # optional supporting documents
```

- `_flow/discovery.md`: provisional questions, hypotheses, options, decision history, links to promoted facts.
- `_flow/prd.md`: product intent, users, outcomes, scope, exclusions, product constraints.
- `_flow/technical.md`: cross-spec architecture, system boundaries, standards, technical decisions.
- `_flow/progress.md`: phase, spec status, blockers, next action, lightweight history.
- `specs/NNN-*/requirements.md`: this spec's behavior, business rules, and acceptance criteria.
- `specs/NNN-*/design.md`: this spec's local implementation decisions.
- `specs/NNN-*/tasks.md`: ordered executable tasks and their checkboxes.
- `specs/NNN-*/docs/*`: optional detail linked from the owning spec; do not create empty directories or extra spec peer documents.

Use stable, ascending three-digit spec prefixes, mapped to IDs `W001`, `W002`, and task IDs `W001-T001`, `W001-T002`. Never renumber IDs, even after a rename or removal. Each fact has one canonical owner; link elsewhere instead of copying requirements, task statuses, or decisions.

## Plan from the existing project

1. Read code, existing `_flow/`, relevant docs, and user inputs. Do not overwrite populated documents or mistake proposals for decisions.
2. Start/resume `_flow/discovery.md` using `references/templates/discovery.md`. Track confirmed, proposed, assumed, open, and superseded choices with evidence, rationale, and history. Preserve old decisions and unresolved questions. If only discovery was requested, stop here.
3. Ask only questions that materially affect the baseline. Promote settled product facts to `prd.md`, cross-cutting engineering choices to `technical.md`, and spec-specific rules to their owning spec. Keep discovery history with links; avoid competing definitions.
4. Create/update `prd.md`, `technical.md`, and `progress.md` from their installed templates. Record unknowns as TBD, not invented requirements or approvals.
5. Decompose into small, vertically sliced, user-observable specs with `references/granularity.md`. Create each spec's requirements, design, and tasks templates; link acceptance criteria to tasks and identify prerequisites.
6. Register specs and statuses (`planned`, `ready`, `in_progress`, `blocked`, `done`) in `progress.md`. Task checkboxes live only in `tasks.md`; identify blockers and the next ready task. Stop before coding unless implementation was requested.

Installed scaffolds: `references/templates/discovery.md`, `references/templates/prd.md`, `references/templates/technical.md`, `references/templates/progress.md`, `references/templates/requirements.md`, `references/templates/design.md`, `references/templates/tasks.md`. Replace placeholders, omit irrelevant sections with a reason, and never treat template prose as project facts.

## Readable artifacts and revisions

- Start every artifact with **Quick navigation** and **At a glance**, containing exactly four concise fields in order: **Outcome**, **Decisions**, **Pending review**, **Next action**. Use `None` where appropriate; link canonical details rather than duplicating them.
- Use outcome-first headings, short grouped sections, stable IDs, explicit approval status, and relevant links. Do not pad with empty headings or duplicate supporting material.
- After an artifact's first version, reconcile changes in its owning file before summarizing them. In chat, give **one short line per changed item**, grouped by file and tagged exactly `[NEW]`, `[MODIFIED]`, or `[REMOVED]`; include stable IDs and propagated changes. Do not paste whole requirement/design text unless asked. Include the same change markers in changed index entries until reviewed. No changed items means no invented log.
- Do not interpret silence, draft wording, or the change log as user approval. Preserve approval state and prior rationale separately from revision tags.

## Requirements and spec boundaries

- Write normative behavior in `specs/NNN-*/requirements.md` with **EARS (Easy Approach to Requirements Syntax)**: one atomic, observable, testable requirement per `W###-R##` ID. Use `shall` and the simplest applicable ubiquitous, event-driven, state-driven, optional-feature, or unwanted-behavior pattern. Avoid vague qualitative language, unexplained implementation choices, and conflated requirements.
- Add traceable acceptance criteria for normal, boundary, and failure behavior. Given/When/Then may clarify tests but does not replace EARS.
- Split by independent, user-valuable outcomes rather than UI/API/data layers; merge tiny coupled specs and split oversized ones. Prefer the smallest meaningful vertical slice, not arbitrary per-file tasks.
- Each task must map to requirements/acceptance criteria, have an observable completion check, and fit **one atomic commit**. Schedule in dependency order; finish a spec only when all tasks, validation, and docs meet acceptance.
- Reconcile later scope changes with their canonical owner and affected downstream artifacts. Never mark unresolved choices as implementation-ready requirements.

## TDD task execution and atomic commits

**Every `W###-T###` task entry** must explicitly reproduce seven task-specific numbered steps, in this order; a shared checklist alone is insufficient:

1. **Prepare:** inspect the task's requirements, design, existing code, and dependencies.
2. **Red:** write a meaningful failing automated test and confirm it fails for the intended missing behavior, not environment failure.
3. **Green:** make the smallest production change to pass.
4. **Refactor:** improve readability/cohesion with tests green.
5. **Validate:** run relevant regressions, acceptance and failure-path checks. If failed or unavailable, stop and record the blocker, without completing the task.
6. **Commit:** include code, test, relevant docs, and task checkbox in **one atomic commit** with `feat(<scope>): <action> [W###-T###]`. No separate red/green commits or unrelated tasks.
7. **Confirm:** verify that the commit exists and covers the completed task; otherwise leave or restore the task as incomplete.

Preserve unrelated changes. Parallel workers need separate file ownership and independent branches/specs; never let them concurrently edit global `_flow/` files. Put validation evidence and blockers in the PR.

## Completion checks

For planning, verify paths, seven installed templates as applicable, stable links/IDs, no placeholders or duplicated authorities, EARS requirements, acceptance traceability, focused spec boundaries, readable four-field summaries, explicit task steps, and a real next action. For implementation, verify failed-first tests where applicable, relevant green checks, the traceable commit for every completed task, and reconciled progress. Report checks not executed rather than inventing success.

## Public and private responsibilities

- **Public:** This independent, domain-neutral workflow, its file contract, and installed templates; public upstream changes require explicit authorization.
- **Private:** Personal, machine, or organization conventions belong only in `~/.claude/skill-overrides/oak-flow.md`. Create it only upon request; customize it rather than canonical or installed files. Never publish, quote, or commit private content.

## Optional private override (on invocation)

When invoked, resolve `~` to the active user's home directory and attempt to read `~/.claude/skill-overrides/oak-flow.md` using an available native file-reading tool or API. Do not require Bash, `cat`, or any specific shell. Apply only this skill's matching private instructions. If the file is absent or inaccessible, continue with the public workflow; report the access limitation only if it affects the requested customization. Do not read unrelated overrides or disclose private contents.
