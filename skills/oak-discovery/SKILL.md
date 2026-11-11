---
name: oak-discovery
description: Interrogate a product, service, system, or feature idea before planning or implementation. Use to challenge assumptions, research viability, uncover stakeholders and personas, enumerate scenarios and edge cases, assess market and economics, explore engineering and infrastructure tradeoffs, examine privacy and compliance, and converge on an evidence-based scope.
allowed-tools: Bash(cat "$HOME/.claude/skill-overrides/oak-discovery.md" 2>/dev/null || true)
---

<!-- skill-source: Caiqueoak/skills -->

# Discovery — evidence-led scope decisions

Challenge an ambiguous product, service, system, or feature before committing scope. Explore relevant possibilities without treating discovery as implementation, default architecture, or automatic document generation.

## Inputs and persistence

- **Before proposing scope or asking questions, read existing code and documentation** when the project is accessible: architecture and decision records, current requirements, implementation, contracts, configuration, tests, and repository conventions. Trace relevant behavior; distinguish observed facts from intent and hypotheses. Reference paths and versions, reconcile contradictions, and do not repeat settled questions.
- If access is missing, disclose what could not be inspected and request only material evidence. Never imply a repository review occurred without it.
- Distinguish confirmed decisions, sourced facts, inferred hypotheses, unknowns, and recommendations. Respect authoritative project documents: discovery owns its evidence, open questions, options, and assumptions; link to adopted decisions instead of duplicating them.
- Track the discovery in conversation with `references/discovery-template.md`. When persistence is requested, use the **user-chosen or project-canonical location**; do not assume a repository layout. Preserve earlier findings and report any write limitation.
- Do not change implementation, tasks, or technical systems unless explicitly requested.

## Discovery loop

1. **Inspect the existing system first:** Ground the discussion in accessible code, tests, documents, decisions, and real behavior before proposing scope or questioning assumptions.
2. **Frame:** Identify the problem, actors, current baseline, outcome, constraints, decision owner, success signals, and assumptions. Do not presume a stack or business model.
3. **Calibrate:** Select focused, standard, or comprehensive depth using `references/coverage.md` based on uncertainty, impact, exposure, reversibility, and consequences; deepen individual high-risk dimensions even for small requests.
4. **Screen dimensions:** Mark each relevant axis essential, conditional, or not_applicable (with a reason); assign brief, targeted, or deep coverage and track readiness. Screen all axes internally without turning them all into questions.
5. **Build a dependency tree:** Map material decisions, prerequisites, risks, and owners. Address **blockers first** and resolve upstream dependencies before downstream choices. Detect cycles, record blocked questions, and avoid speculative answers while prerequisites are unknown.
6. **Ask ready questions:** Select a batch of up to **3–6 independently answerable** high-impact questions from the unblocked backlog (fewer if enough). Explain what each decision unlocks; offer meaningful options and a **provisional recommendation** with rationale only when evidence supports it. Always allow free-form answers.
7. **Incorporate and reorder:** Record partial answers, changes, contradictions, and confidence. Revisit dependency edges and generate follow-up questions only for newly unblocked or materially changed decisions; do not repeat answered questions.
8. **Expand scenarios:** Examine core journeys, states, users, permissions, boundaries, concurrency, failure, recovery, misuse, accessibility, retention, and evolution where applicable. Record expected outcome, severity, handling, and validation; include high-severity scenarios.
9. **Research material facts:** Verify current technical, market, cost, vendor, policy, or regulatory constraints when they affect decisions. Identify source, date, applicability, and confidence. Never invent evidence, statistics, user research, legal conclusions, or ROI; mark unsupported claims as research_needed.
10. **Stress-test:** Compare no-build, smaller scope, build/buy/integrate, delivery alternatives, opportunity costs, reversibility, adverse outcomes, and the assumptions that could invalidate the proposal.
11. **Converge:** Distinguish candidate, accepted, rejected, deferred, and unknown choices; link each decision to evidence, tradeoffs, owner, and unresolved risks.
12. **Re-audit and confirm:** Revisit applicable dimensions and serious failure paths after material decisions. Show scope, exclusions, remaining blockers, and risk acceptance; obtain explicit confirmation from the decision owner before claiming consensus.

## Question discipline

- Prioritize prerequisite blockers and dependency impact, then severity × uncertainty × irreversibility. Work on independent branches in parallel only when no unresolved shared prerequisite could invalidate them.
- Challenge premises constructively. Ask what must be true, how the proposal might fail, and who bears the cost or risk; do not manufacture low-value questions or falsely constrained options.
- Group compatible questions, not dependent ones; recommendations remain provisional until accepted. Explain missing evidence rather than guessing.
- Keep a concise user-facing batch and a complete internal backlog/record. No arbitrary question, round, scenario, or persona count proves completeness.

## Completion gate

A decision-ready outcome requires:

- Problem, affected actors, baseline, outcome, and evidence versus assumptions clearly stated.
- Existing code and docs inspected when accessible; inspected paths, conflicts, and access gaps recorded.
- Relevant dimensions screened proportionally, critical behaviors and high-severity scenarios assessed, irrelevant axes excluded with reasons.
- Dependency tree reviewed: **no unacknowledged material gaps** or silently assumed upstream prerequisites. Material blockers resolved or explicitly deferred with owner, impact, validation plan, and risk acceptance.
- Feasibility, nonfunctional constraints, costs, security, privacy, operations, and legal exposure assessed to the depth justified by actual risk.
- Proposed scope, exclusions, options, key decisions, success/stop signals, and remaining uncertainty reconciled.
- Iterative question batches and an **explicit confirmation** of the scope and residual risks by the decision owner.

Otherwise report `in_discovery` or `blocked` with the specific gaps. `decision_ready` does not mean certainty.

## Public and private responsibilities

- **Public:** This self-contained, domain-neutral workflow and its own references; never require or assume another skill.
- **Private:** Local and workplace conventions belong only in `~/.claude/skill-overrides/oak-discovery.md`; create the private extension only when requested. For local customization, edit only that file, never public source or installed copies. Never publish, quote, or expose private contents.

## Private instructions (Claude Code only, loaded on invocation)

!`cat "$HOME/.claude/skill-overrides/oak-discovery.md" 2>/dev/null || true`
