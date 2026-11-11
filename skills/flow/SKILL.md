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
  discovery.md             # living discovery draft; provisional until reconciled
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
2. Start or resume `_flow/discovery.md` as a living draft **before** committing to the formal baseline. Record the goal, intended users, workflows, constraints, alternatives, evidence, assumptions, open questions, and decisions as discovery unfolds. Preserve prior entries across sessions and update them after each meaningful decision; never overwrite the draft with a fresh template or silently treat proposals as agreements. Use `references/templates/discovery.md` as the scaffold.
3. **Infer by default.** Derive missing noncritical details from the request, inspected repository, existing conventions, evidence, and least-complex compatible choices. Record inferred choices as `[ASSUMED]` with a concise rationale and a clear validation path. Draft usable artifacts without waiting for every detail to be confirmed. Ask only when a missing decision would block a coherent baseline, create significant security/privacy/compliance risk, conflict with an explicit requirement, or incur costly/irreversible consequences. Preserve user decisions over inferences. Never present an inference as confirmed or invent evidence, stakeholder approval, metrics, or validation.
4. Bootstrap _flow/prd.md, _flow/technical.md, and _flow/progress.md using the templates in references/templates/. Fill them with project-specific information; omit irrelevant headings only with a clear reason. Prefer a clearly marked, reversible assumption over TBD for low-risk decisions; reserve TBD/open for genuine blockers.
5. Decompose the product into a small, prioritized set of vertically sliced, user-valuable specs using references/granularity.md. Create all three required spec files for every proposed spec, not merely folders or a single giant spec. Draft concise requirements, a scoped design, and actionable tasks; mark defensible inferred choices `[ASSUMED]` and isolate genuinely blocking unknowns.
6. Register every spec in progress.md with status and link. Identify the next actionable spec/task and material blockers. Produce an overview of the created documents and the rationale for the spec boundaries.
7. If the user asked only for planning, stop before coding. If implementation is requested, follow the TDD execution rules below.

Templates shipped with the installed skill:

- references/templates/discovery.md
- references/templates/prd.md
- references/templates/technical.md
- references/templates/progress.md
- references/templates/requirements.md
- references/templates/design.md
- references/templates/tasks.md

Treat templates as **scaffolds**, not literal outputs. Replace placeholders; remove instructions that are not facts about the project. Keep the skill itself domain-neutral and free of worked product examples.

## Cognitive-load and scanability contract

- Optimize for **developer comprehension and expectation alignment**, not exhaustive questioning or document length. Make defensible assumptions first, then invite correction through artifacts.
- Distinguish `[CONFIRMED]` from `[ASSUMED]` and `[OPEN]` at the owning item; `[ASSUMED]` is **not** an approval. Give each assumption a short reason, confidence when material, and what would validate or overturn it. Do not tag every trivial sentence.
- Prefer existing code, interfaces, constraints, and conventions over inventing alternatives. Select the simplest reversible, consistent option when evidence is incomplete. Do not invent specific facts, external data, authorization, user choices, or passing checks.
- Ask a focused question only for consequential ambiguity: incompatible intent, irreversible external action, substantial cost, or safety/security/privacy/compliance exposure. When blocked, still produce the unaffected parts and identify the exact decision needed.
- Each artifact starts with a concise **Quick navigation** index linking to its major sections, and a brief **At a glance** summary of its purpose, key decisions/outcome, and review-needed assumptions or blockers. Include only relevant sections; do not pad with empty headings.
- Organize related items under short, descriptive **outcome-first headings** that explain what the section accomplishes. Prefer one coherent idea per bullet, stable identifiers, short paragraphs, and linked details over prose walls or generic labels. Use subheadings for logical groups, not arbitrary depth.
- Keep detailed reasoning and implementation nuance inside the owning section or linked supporting docs. The overview/index is navigation, not a second source of truth. In subsequent revisions keep the existing `[NEW]`/`[MODIFIED]`/`[REMOVED]` change markers and add them to index entries for changed items until reviewed; preserve approval status separately from change type.
- Show concise change summaries in chat so the developer can review exceptions rather than reread all artifacts. Do not treat silence as confirmation.

## Discovery draft lifecycle

- Discovery may span multiple sessions. On every continuation, read the existing draft first and record newly confirmed or revised decisions with a date or sequence, rationale, and relevant trade-offs; retain superseded choices with a brief explanation so decisions are not lost.
- Explicitly distinguish **confirmed**, **proposed**, **assumed**, **open**, and **superseded**. Mark reviewable inferences `[ASSUMED]`, separating them from approval and from truly blocking questions. Cite project-supplied evidence or links when available. Do not invent stakeholder agreement, validation, dates, or requirements.
- The draft is a **temporary staging area**, not a competing permanent source of truth. During active discovery, it owns tentative options and decision history. As decisions stabilize, promote current authoritative product facts to `prd.md`, cross-cutting technical facts to `technical.md`, and spec-local rules/designs to their owning spec. Link to those destinations from the draft; do not maintain two independent copies of finalized requirements.
- Keep the draft for traceability after promotion, marking each resolved item with its canonical destination. Reopen a decision explicitly when new information changes it and reconcile affected baselines/specs before execution. Do not treat an unresolved question as an implementation-ready requirement.
- If discovery is the only requested stage, update the draft and summarize confirmed decisions, inferred decisions requiring review, genuine blockers, and next steps; do not bootstrap specs or implement code unless requested.

## Single source of truth

A fact has **one canonical home**. Link to that home elsewhere; do not copy tables, requirements, acceptance criteria, contracts, or status into several documents.

| Canonical file | Owns |
| --- | --- |
| _flow/discovery.md | Provisional discovery notes, decision rationale and history, unresolved options, and links to promoted canonical decisions |
| _flow/prd.md | Product intent, users, outcomes, scope, exclusions, product-level constraints |
| _flow/technical.md | Cross-spec architecture, stack, system boundaries, standards, cross-cutting engineering decisions |
| _flow/progress.md | Project phase, spec-level status, blockers, next step, lightweight history |
| specs/NNN-*/requirements.md | This spec's behavior, rules, and numbered acceptance criteria |
| specs/NNN-*/design.md | This spec's implementation design and spec-local technical decisions |
| specs/NNN-*/tasks.md | Ordered, uniquely identified executable tasks and their completion checkboxes |
| specs/NNN-*/docs/* | Optional supporting research or deeper detail; always linked from its owning canonical file |

Global documents describe the whole project; spec documents describe only their slice. The progress summary must never maintain an independent copy of task checkboxes or acceptance criteria. Link by relative path. If a decision belongs in technical.md, don't re-decide it in every design.md. Keep unrelated application documentation outside _flow/ according to the target project's conventions.

## Requirements: EARS

- Write every normative behavioral requirement in `specs/NNN-*/requirements.md` using **EARS (Easy Approach to Requirements Syntax)**. Keep one observable, verifiable behavior per requirement, with stable `W###-R##` IDs and explicit system/actor terminology.
- Choose the **simplest applicable** EARS pattern: ubiquitous (`The <system> shall <response>.`), event-driven (`When <trigger>, the <system> shall <response>.`), state-driven (`While <state>, the <system> shall <response>.`), optional feature (`Where <feature is enabled>, the <system> shall <response>.`), or unwanted behavior (`If <undesired condition>, then the <system> shall <response>.`). Combine clauses only when essential to express the same atomic requirement.
- Specify measurable conditions, boundaries, failures, and observable results without implying unwarranted implementations. Avoid ambiguous language such as "fast", "appropriate", "user-friendly", or "should"; use `shall` for normative requirements.
- Use Given/When/Then for acceptance tests **when useful**, not as a substitute for EARS requirements. Link each acceptance criterion to its owning requirement ID; ensure normal, edge, and failure paths are covered where applicable.
- Discovery notes, scope statements, and open questions need not be forced into EARS, but must not be treated as implementation-ready requirements.

## Spec boundaries and lifecycle

- Prefer complete capabilities or observable user outcomes, not generic layers such as "database", "API", and "UI". Each spec has one coherent outcome and can be accepted independently, with clear dependencies when unavoidable.
- Size specs so requirements and design remain readable and tasks are independently verifiable. Split an oversized spec; merge tiny, tightly coupled specs. See references/granularity.md for portable heuristics.
- Plan tasks as small, sequential, testable changes. Each task maps to explicit acceptance criteria, has a verifiable completion condition, and should fit **one atomic commit**. Use the smallest meaningful vertical slice, not arbitrary file-by-file work.
- Initial statuses in progress.md: planned, ready, in_progress, blocked, done. Only one canonical spec status exists there. Task completion exists only in tasks.md.
- Work in dependency order. A spec is done only when all required tasks, acceptance criteria, relevant validations, and documentation are complete.
- Changes to product scope go to prd.md; cross-cutting decisions to technical.md; new behavior to its spec requirements; implementation changes to its design; tracking to progress.md/tasks.md. Reconcile downstream artifacts and note changed assumptions without copying content.
- Never renumber existing specs/tasks or reuse removed IDs. New work gets new IDs. Respect user decisions and inspect the code before revising a baseline.

## Chat change summaries after the first artifact version

- For the first version of an artifact, write its complete Markdown content and follow the initial overview rules above. For **every subsequent revision**, first reconcile the full details in the owning `_flow/` Markdown files, then summarize **each individual item actually changed** in chat.
- Group the chat summary by affected artifact path. Give **one short line per changed item**, not one line per file or per user request. Include changes propagated to related artifacts; omit untouched items and artifacts.
- Prefix **every item** with exactly one explicit tag: `[NEW]` for added content, `[MODIFIED]` for revised content, or `[REMOVED]` for deleted content. Retain the item's stable ID where one exists; never reuse removed IDs.
- Each line identifies the item and briefly states the change. Do not paste complete requirements, EARS clauses, acceptance criteria, design explanations, before/after text, or task detail unless requested; those belong in the Markdown files.
- Show only changes from **the current revision**, not unchanged or previously reported items. A short total by tag may follow the grouped lines. If no items changed, say so without inventing a change log.
- Preserve the item's actual decision/approval status in the canonical artifact. A chat summary is a navigational change log, **not** a second source of truth or evidence of approval.

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

Before calling planning complete, confirm the exact directory structure, the discovery draft and all six baseline/spec templates used where relevant, no unreplaced placeholders, stable IDs and links, no duplicated authoritative facts, EARS-formatted atomic requirements with traceable acceptance criteria, clear spec boundaries, readable outcome-first headings, navigable indexes, at-a-glance summaries, visible reviewable assumptions, and real next actions. Before calling implementation complete, verify TDD evidence, a passing relevant test suite, one traceable commit per completed task, and reconciled progress.

## Public and private responsibilities

- **Public:** This reusable workflow, file contract, and templates belong in this skill and may be improved upstream when explicitly requested.
- **Private:** Workstation-, personal-, or workplace-specific conventions belong only in ~/.claude/skill-overrides/flow.md on that machine, never in this public repository.
- For local customization, change only the matching private file. Do not modify this public skill, installed copies, or symlink targets.
- Create the private file only when customization is requested; never commit, push, quote, or publish its contents. If instructions conflict, report the conflict and follow applicable company/security policies.

## Private instructions (Claude Code only, loaded on invocation)

!`cat "$HOME/.claude/skill-overrides/flow.md" 2>/dev/null || true`
