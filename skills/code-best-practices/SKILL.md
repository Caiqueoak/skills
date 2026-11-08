---
name: code-best-practices
description: Design and assess architecture, OOP code, security, and testing; implement or refactor software and validate repositories, commits, and pull requests using pragmatic, language-agnostic engineering principles.
allowed-tools: Bash(cat "$HOME/.claude/skill-overrides/code-best-practices.md" 2>/dev/null || true)
---

<!-- skill-source: Caiqueoak/skills -->

# Code best practices

Improve code by reasoning from **required behavior and constraints** toward the simplest understandable, testable implementation. Principles are decision aids, not unconditional laws. Do not select a paradigm, framework, architecture, or abstraction without a demonstrated need.

## Task selection

Use only the mode(s) implied by the request; each is independently usable. Accept requirements, designs, or code supplied by the user or project without assuming any other workflow or skill.

- **Architecture design or review:** evaluate quality attributes, responsibility and dependency boundaries, OOP models, alternatives, contracts, operations, security, and verification. Produce a reasoned design or findings, not a predetermined pattern.
- **Repository audit:** assess architecture, important flows, maintainability, security, dependency health, tests, CI, and operations. Identify inspected scope and uninspected areas.
- **Commit / pull-request review:** inspect the actual diff, base and callers, contracts, regression risk, security impact, test changes, and validation evidence; assess atomicity and relevance.
- **Test suite audit and improvement:** inspect tests and assertions, identify weak or missing protections, over-mocking, flaky or slow tests, and prioritise verifiable improvements.
- **Implementation and refactoring:** make the smallest scoped, tested change compatible with established contracts.
- **Focused code review:** return prioritized, substantiated findings rather than silently editing code.

See `references/architecture-oop.md`, `references/security.md`, `references/testing-validation.md`, and `references/review-audit.md` when their subjects are relevant.

## When invoked

- For **new implementation**, identify the required outcome, contract, invariants, boundaries, failure behavior, and existing conventions before writing code.
- For **refactoring**, preserve observable behavior and public contracts unless the user authorizes a change; identify the specific readability, cohesion, coupling, or change-cost problem to solve.
- For **review**, report concrete, prioritized findings with location, impact, evidence, and the smallest justified improvement. Distinguish correctness or safety defects from preferences; avoid cosmetic churn.
- For **questions**, explain the relevant tradeoffs directly. Recommend an approach only when constraints support it; ask for missing material context rather than assuming it.
- Do not initiate unrelated rewrites or introduce extra components, dependencies, or speculative extensibility.

## Priority order

1. **Correctness, safety, and explicit contracts:** preserve requirements, invariants, data integrity, security, and observable behavior.
2. **Readability and clear intent:** understand **what** behavior is required before **how** it is implemented; choose code that makes its purpose evident.
3. **Maintainability and testability:** optimize for safe, local, understandable future change and fast verification.
4. **Simplicity:** use the least complex solution meeting current, known requirements.
5. **Performance and scale:** optimize against measured constraints and relevant evidence, not guesses.

When priorities conflict, explain the tradeoff rather than pretending every principle can always be maximized.

## Principles to apply

Use `references/principles.md` for definitions, limitations, and decision tests. Apply only relevant principles:

- **KISS and YAGNI:** prefer direct designs; avoid hypothetical requirements, premature generalization, and optional infrastructure.
- **DRY and SSOT:** avoid duplicated *knowledge* or business rules, but tolerate harmless local repetition when abstraction would obscure intent or couple unrelated behavior.
- **SOLID with judgment:** cohesive responsibility, extension where change pressure exists, substitutable contracts, narrow interfaces, and dependency direction without gratuitous indirection.
- **Object-oriented programming (OOP):** encapsulation, abstraction, polymorphism, inheritance versus composition, identity/value, state lifecycle, behavioral invariants, and ownership; do not create classes by reflex.
- **High cohesion, low coupling, and locality:** keep closely related logic and data near their ownership; hide unrelated concerns behind small, meaningful boundaries.
- **SRP, clear intent, semantic naming:** use responsibility-oriented structure, obvious control flow, small understandable units, and names that communicate outcomes.
- **Functional/declarative thinking:** express **what** a computation does before its mechanism; favor pure functions, explicit inputs/outputs, immutability, and isolated side effects where they reduce uncertainty.
- **Composition over inheritance, delegation, Tell Don't Ask, Law of Demeter:** favor purposeful behavior ownership and direct dependencies over navigation chains or rigid hierarchies.
- **Explicit contracts and types:** define preconditions, postconditions, invariants, errors, and data ownership; avoid implicit states and invalid combinations.
- **Separation of concerns with vertical cohesion:** organize around changes and observable behavior rather than forcing fragmented layers or patterns.
- **Complexity return on investment:** adopt added indirection only if proven benefits in correctness, change isolation, testability, resilience, or measured performance outweigh maintenance and operational costs.
- **Test-first and behavior-focused verification:** default to a failing test, minimal passing code, and safe refactoring for behavior changes; exercise boundaries, meaningful failure modes, and regressions. Audit assertion strength, missing tests, false positives, flaky behavior, mutation resistance, and coverage meaning.
- **Reliable and secure behavior:** threat modeling, authentication, authorization, trust boundaries, injection defenses, secrets and sensitive data, dependency and build security, safe failure and recovery proportional to risk.
- **Sustainable engineering:** keep canonical documentation current, make reviewable changes, protect backwards compatibility when required, and verify rather than assume success.

## Architecture, security, and test-quality decisions

- **Architecture:** start with required behavior, quality attributes and constraints, then compare simpler and more complex options. Identify module/component responsibility, dependency direction, data ownership, contracts, state and lifecycle, operational boundaries, and fitness tests. Record decisions in the project's established authoritative location without creating competing documentation.
- **OOP:** prefer encapsulated invariants and cohesive responsibilities; require real substitutability for polymorphism or inheritance. Composition, straightforward functions, or functional transformations may be better than extra objects.
- **Security:** map assets, entry points, identity, permission and data flows; examine untrusted inputs, safe defaults, secrets, dependencies, build/release permissions, and failure exposure. Mark suspected weaknesses separately from verified vulnerabilities and never reproduce credentials.
- **Testing:** evaluate what behaviors each test would detect if broken. Inspect unit, integration, contract and end-to-end evidence as appropriate; improve assertions, reliability, isolation and meaningful edge cases. No green build or coverage percentage alone proves quality.
- **Audit/review:** inspect source and diff context, rank observed risks by severity and confidence, and recommend the smallest justified fix with a way to verify it. A repository-wide conclusion requires sufficiently broad evidence.

## Working method

1. **Read before changing:** establish request mode and scope; inspect relevant code, repository and commit context, tests, contracts, constraints, and established style. Understand the behavior and the reason behind the existing design.
2. **State the intended result:** describe input/output behavior and constraints; identify the simplest viable approach. Assess the cost of change and avoid speculative capabilities.
3. **Choose boundaries deliberately:** optimize locality and cohesion, explicit dependency direction, minimal interfaces, and a clear owner for each rule/state.
4. **Implement and verify:** use the project's conventions. For a behavior change, prefer red → green → refactor; validate observable behavior and important edge cases. Refactor only while behavior remains verifiable.
5. **Review complexity ROI:** inspect every new abstraction, dependency, configuration layer, branch, and shared state for a concrete benefit. Prefer removal or simplification when the benefit is uncertain.
6. **Finish with evidence:** run applicable checks (tests, lint, typing, build, relevant security/performance checks when available), inspect the diff, and report what passed, failed, or could not run. Assess whether tests actually protect relevant behavior. Do not claim unexecuted validation or a complete audit of unseen code.

## Decision rules

- Do **not** force a pattern, paradigm, abstraction, or architectural style because it appears on a checklist.
- Keep a small local duplication when the alternative creates an unnecessary shared dependency. Extract only stable, genuinely shared behavior or knowledge.
- Do not fragment code solely to minimize function length or file size. Split when responsibilities, reasoning, testability, or change ownership improve.
- Prefer one coherent path over layers of wrappers; expose failure and state rather than relying on implicit magic.
- When two reasonable designs remain, articulate the least-complex viable default and when a more complex alternative would be justified.
- Respect existing interfaces, repository policies, and authorized scope; do not reformat or restructure unrelated code.

## Review output

For findings, give **priority, location, evidence, impact, confidence, recommended change, and verification**. State the audit baseline, inspected and omitted areas, tests and checks actually performed, and residual uncertainty. Separate required corrections from optional improvements. If no meaningful problems are evidenced, say so for the inspected scope without inventing concerns. Read references/review-audit.md for commit, PR, repository, and architecture-review procedure.

## Public and private responsibilities

- **Public:** This self-contained, reusable, language-, industry-, and platform-agnostic workflow and its references.
- **Private:** Any local, personal, or workplace conventions belong only in `~/.claude/skill-overrides/code-best-practices.md`.
- For local customization, edit only the matching private file; do not modify the public source, installed copies, or symlink targets.
- Create the optional private file only upon request. Never commit, push, quote, or expose its contents. If instructions conflict, follow applicable security and organizational policies and surface the conflict.

## Private instructions (Claude Code only, loaded on invocation)

!`cat "$HOME/.claude/skill-overrides/code-best-practices.md" 2>/dev/null || true`
