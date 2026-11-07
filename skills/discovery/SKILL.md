---
name: discovery
description: Interrogate a product, service, system, or feature idea before planning or implementation. Use to challenge assumptions, research viability, uncover stakeholders and personas, enumerate scenarios and edge cases, assess market and economics, explore engineering and infrastructure tradeoffs, examine privacy and compliance, and converge on an evidence-based scope.
allowed-tools: Bash(cat "$HOME/.claude/skill-overrides/discovery.md" 2>/dev/null || true)
---

<!-- skill-source: Caiqueoak/skills -->

# Discovery — rigorous scope interrogation

Use this skill when an idea is still ambiguous, assumptions have not been tested, or important product, business, technical, operational, or regulatory questions remain. Challenge the proposal until the consequential uncertainties have either been resolved, explicitly excluded, or assigned a validation path.

Discovery is **not** implementation, architecture-by-default, automatic PRD generation, or an obligation to build every conceivable feature. Enumerate the possibility space broadly; commit only what evidence and user decisions justify.

## Inputs and persistence

- Inspect existing project documents and decisions first. Do not overwrite, contradict, or repeat previously established facts without showing why the premise changed.
- Accept even a one-sentence idea; distinguish user-confirmed facts, sourced evidence, inferred hypotheses, unknowns, and recommendations.
- Keep a living record at `_flow/docs/discovery.md` in the target project, using `references/discovery-template.md`. This path is a neutral supporting-research location; **the Flow skill is not required**. Create its parent directories if absent. If filesystem write access is unavailable, provide the same structured findings in the conversation without pretending a file was saved.
- Update the existing document in place without dropping prior decisions, evidence, objections, or unresolved questions. Use references to canonical external artifacts, not copied sources of truth.
- Do not create or alter product specifications, implementation tasks, infrastructure, or code unless separately requested. When `_flow/prd.md` or `_flow/technical.md` exists, those files own adopted product or cross-cutting technical decisions; discovery records evidence, pending challenges, and links, not duplicate authoritative definitions.

## Discovery loop

1. **Frame:** State the core problem, intended outcome, actors, users, context, proposed boundaries, success signals, and explicit assumptions. Identify whose decision it is and the intended decision horizon. Do not select a stack or business model merely because one is familiar.
2. **Map breadth:** Scan every dimension in `references/coverage.md`. For each, record `unexamined`, `investigating`, `resolved`, `deferred`, or `not_applicable` with a reason. Add additional dimensions revealed by the idea; the checklist is a minimum, never a ceiling.
3. **Interrogate:** Attack the highest-risk assumptions and contradictions first. Ask targeted, non-leading questions in manageable waves (typically 3–5 independent high-leverage questions, fewer if one answer determines the others). For every answer, ask what would falsify it, who is affected, what breaks at boundaries, which alternatives exist, and what proof is needed. Continue across turns; never treat one wave as completion.
4. **Enumerate scenarios:** Map actors, journeys, state transitions, system boundaries, incentives, misuse, dependencies, and failures. Systematically apply the scenario lenses in `references/coverage.md`; add branches for invalid inputs, boundaries, concurrency, interruptions, external failures, recovery, abuse, accessibility, privacy, deletion, and lifecycle change wherever relevant. Capture expected outcome, detection, handling, test or validation, and severity. Record genuine exclusions instead of silently dropping categories.
5. **Investigate independently:** When the decision depends on current facts, research credible sources for market alternatives, user behavior, regulation, vendor constraints, prices, technology compatibility, operating costs, and risks. Cite source, date, geography, confidence, and applicability. Separate firsthand evidence, verified sources, estimates, and conjecture. If tools or data are unavailable, label `research_needed`; never invent competitors, statistics, legal conclusions, ROI, or user research.
6. **Stress-test options:** For material choices, compare doing nothing, a smaller scope, build/buy/integrate, delivery approaches, cost/risk tradeoffs, reversibility, and opportunity cost. Test optimistic, baseline, and adverse assumptions without fabricating numerical precision. Challenge desirability, viability, feasibility, usability, and responsible operation independently.
7. **Converge:** Distinguish `candidate`, `accepted`, `rejected`, `deferred`, and `unknown`. Propose explicit in-scope, later, and out-of-scope boundaries. Link each important decision to its supporting evidence, owner, rationale, and risks. Surface contradictions and dependencies for the user to resolve; never silently decide a consequential tradeoff.
8. **Repeat / hand off:** Revisit all dimensions and high-severity scenarios after decisions change. Summarize decisions, remaining blockers, highest risks, confidence, and the next questions or experiments. Ask the user to confirm the scoped baseline before declaring scope frozen. Hand only confirmed decisions and clearly labeled open issues to subsequent planning.

## How to challenge well

- Be rigorous but constructive: question weak premises, not the person proposing them. Ask what must be true, what would make the idea fail, who might be excluded or harmed, and what is genuinely necessary.
- Explore proactively beyond what the user names, including indirect actors and second-order consequences. Trace each important behavior through normal, unusual, adversarial, and recovery states.
- Prioritize `severity × uncertainty × irreversibility` and dependency impact over checklist order. Do not overwhelm the user with a dump of every conceivable question; maintain the full backlog in the discovery record.
- Expose tradeoffs instead of presenting every alternative as simultaneously viable. Separate legally required work from optional safeguards and avoid jurisdiction assumptions; request qualified review where needed.
- Keep answers atomic and resolve one decision per question when an issue is consequential. Consolidate redundant questions.
- No fixed number of rounds, scenarios, personas, or questions guarantees completeness. Continue when new material risks emerge; stop when remaining uncertainty is explicit, proportionate to the decision, and accepted.

## Completion gate

Do not declare discovery finished solely because every heading has text. A decision-ready baseline requires:

- An explicit problem, affected actors, intended outcome, and evidence/assumption distinction.
- Each relevant dimension assessed; exclusions and non-applicability justified.
- Core journeys, alternatives, critical edge cases, abuse/failure/recovery paths, and nonfunctional constraints investigated or assigned a validated follow-up.
- A scoped proposal with accepted/rejected/deferred boundaries, decision owners, dependencies, major risks, and measurable success or stop signals.
- Economic, operational, security, privacy, and regulatory feasibility assessed to an appropriate depth; unknown material facts acknowledged.
- High-impact unresolved issues surfaced, with owners and validation plans; no contradictory authoritative decisions.
- User confirmation before treating a baseline as frozen. `decision_ready` does not mean certainty or permanent completeness.

If any gate fails, report `in_discovery` or `blocked` with the specific gaps, rather than claiming the scope is closed.

## Coordination with other skills

This skill owns **discovery evidence, assumptions, challenges, questions, and option analysis**. Another planning/specification workflow may later own product scope, architecture, requirements, tasks, and implementation status. Handoff via references and explicit decisions; do not copy competing canonical text. No other skill is a runtime prerequisite.

## Public and private responsibilities

- **Public:** Only reusable, domain-, industry-, stack-, jurisdiction-, and organization-neutral process guidance, prompts, and templates belong here.
- **Private:** Local, personal, or workplace conventions belong only in `~/.claude/skill-overrides/discovery.md` on the relevant machine.
- For local customization, modify only that private file; do not modify this public skill, installed copies, or symlink targets.
- Create the private file only when customization is explicitly requested. Never commit, push, quote, or expose its contents. Resolve conflicts under applicable company and security policies.

## Private instructions (Claude Code only, loaded on invocation)

!`cat "$HOME/.claude/skill-overrides/discovery.md" 2>/dev/null || true`
