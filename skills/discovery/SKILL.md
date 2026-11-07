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
- Maintain the discovery record in the conversation using `references/discovery-template.md`. When the user requests a persisted artifact or the existing project explicitly uses one, write to the **user-chosen or project-canonical location**; never assume a folder name, repository layout, or companion workflow. If no path is known and persistence is requested, use the existing documentation convention or ask for a destination only when necessary.
- If tools or write access are unavailable, provide the structured findings in the conversation and state what was not persisted. Update existing findings without dropping decisions, evidence, objections, or unresolved questions.
- Respect any existing authoritative project documents. Link to adopted decisions rather than maintaining competing definitions; discovery owns its evidence, assumptions, questions, and option analysis.
- Do not alter implementation, tasks, or technical systems unless explicitly requested. Never assume another capability will consume the result.

## Discovery loop

1. **Frame:** State the core problem, intended outcome, actors, users, context, proposed boundaries, success signals, and explicit assumptions. Identify whose decision it is and the intended decision horizon. Do not select a stack or business model merely because one is familiar.
2. **Map breadth:** Scan every dimension in `references/coverage.md`. For each, record `unexamined`, `investigating`, `resolved`, `deferred`, or `not_applicable` with a reason. Add additional dimensions revealed by the idea; the checklist is a minimum, never a ceiling.
3. **Interrogate in batches:** From the question backlog, ask a **batch of 3–6 independently answerable, high-leverage questions** at a time, grouped into a coherent topic where useful. Adjust size downward only for an answer that gates the rest. For each question, explain the decision briefly, offer realistic options **only when they clarify genuine choices**, and provide a **provisional recommendation with a concise rationale** when enough context supports one. Always allow an alternative or free-form answer; never force a false set of choices. Without sufficient evidence, explicitly say why a recommendation cannot yet be justified.
4. **Incorporate answers:** After each response, record the user's answers (including partial answers), update confidence, decisions and coverage, test for contradictions and second-order effects, then generate **the next batch** from newly exposed dependencies, scenarios and gaps. Do not repeat answered questions unless changed facts materially reopen them. Continue until the decision owner confirms consensus with no unacknowledged material gaps.
5. **Enumerate scenarios:** Map actors, journeys, state transitions, system boundaries, incentives, misuse, dependencies, and failures. Systematically apply the scenario lenses in `references/coverage.md`; add branches for invalid inputs, boundaries, concurrency, interruptions, external failures, recovery, abuse, accessibility, privacy, deletion, and lifecycle change wherever relevant. Capture expected outcome, detection, handling, test or validation, and severity. Record genuine exclusions instead of silently dropping categories.
6. **Investigate independently:** When the decision depends on current facts, research credible sources for market alternatives, user behavior, regulation, vendor constraints, prices, technology compatibility, operating costs, and risks. Cite source, date, geography, confidence, and applicability. Separate firsthand evidence, verified sources, estimates, and conjecture. If tools or data are unavailable, label `research_needed`; never invent competitors, statistics, legal conclusions, ROI, or user research.
7. **Stress-test options:** For material choices, compare doing nothing, a smaller scope, build/buy/integrate, delivery approaches, cost/risk tradeoffs, reversibility, and opportunity cost. Test optimistic, baseline, and adverse assumptions without fabricating numerical precision. Challenge desirability, viability, feasibility, usability, and responsible operation independently.
8. **Converge:** Distinguish `candidate`, `accepted`, `rejected`, `deferred`, and `unknown`. Propose explicit in-scope, later, and out-of-scope boundaries. Link each important decision to its supporting evidence, owner, rationale, and risks. Surface contradictions and dependencies for the user to resolve; never silently decide a consequential tradeoff.
9. **Re-audit and confirm:** Revisit all relevant dimensions and high-severity scenarios after each material decision. Summarize agreements, exclusions, unresolved blockers, validation plans, and remaining risks. Present the proposed consensus and ask the decision owner to confirm it before treating the scope as agreed. Do not presume any next-stage workflow.

## How to challenge well

- Be rigorous but constructive: question weak premises, not the person proposing them. Ask what must be true, what would make the idea fail, who might be excluded or harmed, and what is genuinely necessary.
- Explore proactively beyond what the user names, including indirect actors and second-order consequences. Trace each important behavior through normal, unusual, adversarial, and recovery states.
- Prioritize `severity × uncertainty × irreversibility` and dependency impact over checklist order. Do not overwhelm the user with a dump of every conceivable question; maintain the full backlog in the discovery record.
- Expose tradeoffs instead of presenting every alternative as simultaneously viable. Separate legally required work from optional safeguards and avoid jurisdiction assumptions; request qualified review where needed.
- Use **question batches, not serial one-question interviews**. Each question should target one decision. Group compatible questions; avoid dependent questions whose options are impossible to assess until an earlier answer.
- Where legitimate alternatives exist, present balanced tradeoffs and a **clearly labeled, context-dependent recommendation**; explain its rationale, evidence and major downside without anchoring the answer as a foregone conclusion. If alternatives are not meaningful (a factual unknown, open exploration, or free-form preference), ask directly without artificial options. A recommendation is never a substitute for the user's decision.
- After **each** answered batch, derive follow-up questions from the answers, stress-test each accepted choice, and check adjacent dimensions and edge cases. Reconcile conflicting answers before moving on.
- No fixed number of rounds, scenarios, personas, or questions guarantees completeness. Continue when new material risks emerge; stop when remaining uncertainty is explicit, proportionate to the decision, and accepted.

## Completion gate

Do not declare discovery finished solely because every heading has text. A decision-ready baseline requires:

- An explicit problem, affected actors, intended outcome, and evidence/assumption distinction.
- Each relevant dimension assessed; exclusions and non-applicability justified.
- Core journeys, alternatives, critical edge cases, abuse/failure/recovery paths, and nonfunctional constraints investigated or assigned a validated follow-up.
- A scoped proposal with accepted/rejected/deferred boundaries, decision owners, dependencies, major risks, and measurable success or stop signals.
- Economic, operational, security, privacy, and regulatory feasibility assessed to an appropriate depth; unknown material facts acknowledged.
- Every high-impact gap either resolved with evidence/decision or explicitly deferred with an owner, risk, validation plan, and user acceptance; no unacknowledged material gaps or contradictory decisions.
- Question batches iterated on prior answers until there are no decision-blocking unknowns and the scoped outcome is internally consistent.
- Explicit confirmation of the agreed scope, exclusions, and accepted residual uncertainty by the decision owner. `decision_ready` does not mean certainty or permanent completeness.

If any gate fails, report `in_discovery` or `blocked` with the specific gaps, rather than claiming the scope is closed.

## Public and private responsibilities

- **Public:** Only reusable, domain-, industry-, stack-, jurisdiction-, and organization-neutral process guidance, prompts, and templates belong here. This skill operates on its own without referring to or assuming any other skill.
- **Private:** Local, personal, or workplace conventions belong only in `~/.claude/skill-overrides/discovery.md` on the relevant machine.
- For local customization, modify only that private file; do not modify this public skill, installed copies, or symlink targets.
- Create the private file only when customization is explicitly requested. Never commit, push, quote, or expose its contents. Resolve conflicts under applicable company and security policies.

## Private instructions (Claude Code only, loaded on invocation)

!`cat "$HOME/.claude/skill-overrides/discovery.md" 2>/dev/null || true`
