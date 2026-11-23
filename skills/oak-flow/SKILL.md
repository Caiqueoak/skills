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

1. **Scope the change:** for a targeted request, find its existing canonical owner before creating files; update only that owner and directly affected links/status. For a new project, establish the smallest useful baseline; do not generate every spec in advance.
2. **Inspect once:** read relevant existing code, tests, `_flow/` artifacts, and project docs before writing. Follow imports/dependencies only where needed to resolve a concrete decision. Reuse confirmed context rather than rescanning unchanged files.
3. **Discover if necessary:** maintain `_flow/discovery.md` using `references/templates/discovery.md` when questions or provisional decisions exist. Ask only questions that block an important decision. If discovery alone was requested, stop there.
4. **Place facts once:** put agreed product facts in `prd.md`, cross-spec engineering choices in `technical.md`, spec behavior in `requirements.md`, and local implementation choices in `design.md`. Preserve pending decisions as TBD, never invented approvals.
5. **Route, then decompose ready work:** first reuse or extend an existing spec when the request belongs to its outcome; create a new spec only when the boundary test in `references/granularity.md` justifies one. Add executable tasks only for ready work, with direct dependencies and acceptance links.
6. **Track and stop:** update `progress.md` with spec statuses (`planned`, `ready`, `in_progress`, `blocked`, `done`), blockers, and one next action. Task checkboxes stay in `tasks.md`. Stop before coding unless implementation was requested.

Load only the needed files from `references/templates/`. Replace placeholders; never present template instructions as project facts.

## Existing-spec-first routing

Whenever a task, change, or feature is requested, **decide its canonical spec before allocating a new spec ID**:

1. Inspect `_flow/progress.md` and the titles, scopes, requirement IDs, and task lists of potentially relevant `_flow/specs/*`; follow links and read detail only for candidates. Consider completed specs too. If no `_flow/` baseline exists, create only what the request needs.
2. **Reuse** the best-matching spec if the change refines, fixes, or extends the same cohesive user-observable outcome and shares its acceptance boundary. Add or revise the owning requirements, local design, acceptance criteria, and tasks in place as needed; never create a spec merely because a new task was requested.
3. **Create** a new spec only for a distinct independently verifiable outcome, materially different rules or release boundary, or scope that would make the existing spec incoherent. Explain the specific boundary reason. Never split solely by file, layer, endpoint, or invocation.
4. For changes spanning multiple specs, choose one canonical behavior owner; update shared decisions in `prd.md` or `technical.md` when applicable and link affected specs instead of duplicating requirements. Split or reconcile existing scopes only when ownership is genuinely unclear, retaining stable identifiers and traceability.
5. Append task IDs using the next unused number **within the owning spec**. Do not renumber, recycle, overwrite completed tasks, erase implementation history, or silently change approved behavior. A completed spec may receive a new scoped task and an updated status when further work is justified; record any changed approvals explicitly.

Record the routing outcome concisely in the response (reused `W###`, or new `W###` with its boundary reason). Do not create a separate routing document or regenerate unrelated artifacts.

## Fast, predictable artifacts

- **One pass, smallest scope:** inspect relevant owners, decide boundaries, then write concise artifacts. Do not repeatedly regenerate the full `_flow/` tree or expand a requested spec into unrelated work.
- **Fixed layout:** every artifact keeps Quick navigation and At a glance (Outcome, Decisions, Pending review, Next action, in that order). In `design.md`, use exactly the template's four body sections in the given order; write `None` for inapplicable entries instead of inventing content.
- **Design for implementation:** identify verified touchpoints/responsibilities, execution sequence, changed contracts or state, failure behavior and tests, plus spec-local tradeoffs. Prefer short bullets/tables over prose; do not re-explain requirements, global architecture, or task checklists. Aim for roughly 30–45 lines for a simple spec, expanding only for implementation-critical complexity.
- **No speculative detail:** inspect code before naming paths or APIs. If unresolved, write a specific TBD with its impact. Put substantial diagrams or rare edge-case analysis in `docs/` only when indispensable, and link them.
- **Efficient revisions:** edit the owning sections and affected references in place. Read or validate changed material and essential links, not the entire unchanged document set; preserve stable IDs and approvals.

## Readable artifacts and revisions

- Start every artifact with **Quick navigation** and **At a glance**, containing exactly four concise fields in order: **Outcome**, **Decisions**, **Pending review**, **Next action**. Use `None` where appropriate; link canonical details rather than duplicating them.
- Use outcome-first headings, short grouped sections, stable IDs, explicit approval status, and relevant links. Outside the fixed design layout, omit irrelevant sections; never duplicate supporting material.
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

For planning, verify existing-spec reuse was evaluated before any new spec, paths, seven installed templates as applicable, stable links/IDs, no placeholders or duplicated authorities, EARS requirements, acceptance traceability, focused spec boundaries, readable four-field summaries, explicit task steps, and a real next action. For implementation, verify failed-first tests where applicable, relevant green checks, the traceable commit for every completed task, and reconciled progress. Report checks not executed rather than inventing success.

## Public and private responsibilities

- **Public:** This independent, domain-neutral workflow, its file contract, and installed templates; public upstream changes require explicit authorization.
- **Private:** Personal, machine, or organization conventions belong only in `~/.claude/skill-overrides/oak-flow.md`. Create it only upon request; customize it rather than canonical or installed files. Never publish, quote, or commit private content.

## Optional private override (on invocation)

When invoked, resolve `~` to the active user's home directory and attempt to read `~/.claude/skill-overrides/oak-flow.md` using an available native file-reading tool or API. Do not require Bash, `cat`, or any specific shell. Apply only this skill's matching private instructions. If the file is absent or inaccessible, continue with the public workflow; report the access limitation only if it affects the requested customization. Do not read unrelated overrides or disclose private contents.
