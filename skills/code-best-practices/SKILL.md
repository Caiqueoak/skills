---
name: code-best-practices
description: Apply or review pragmatic, language-agnostic coding best practices when implementing, refactoring, testing, debugging, or reviewing code. Prioritize correctness, intent, readability, maintainability, simplicity, cohesion, testability, and proportionate complexity.
allowed-tools: Bash(cat "$HOME/.claude/skill-overrides/code-best-practices.md" 2>/dev/null || true)
---

<!-- skill-source: Caiqueoak/skills -->

# Code best practices

Improve code by reasoning from **required behavior and constraints** toward the simplest understandable, testable implementation. Principles are decision aids, not unconditional laws. Do not select a paradigm, framework, architecture, or abstraction without a demonstrated need.

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
- **High cohesion, low coupling, and locality:** keep closely related logic and data near their ownership; hide unrelated concerns behind small, meaningful boundaries.
- **SRP, clear intent, semantic naming:** use responsibility-oriented structure, obvious control flow, small understandable units, and names that communicate outcomes.
- **Functional/declarative thinking:** express **what** a computation does before its mechanism; favor pure functions, explicit inputs/outputs, immutability, and isolated side effects where they reduce uncertainty.
- **Composition over inheritance, delegation, Tell Don't Ask, Law of Demeter:** favor purposeful behavior ownership and direct dependencies over navigation chains or rigid hierarchies.
- **Explicit contracts and types:** define preconditions, postconditions, invariants, errors, and data ownership; avoid implicit states and invalid combinations.
- **Separation of concerns with vertical cohesion:** organize around changes and observable behavior rather than forcing fragmented layers or patterns.
- **Complexity return on investment:** adopt added indirection only if proven benefits in correctness, change isolation, testability, resilience, or measured performance outweigh maintenance and operational costs.
- **Test-first and behavior-focused verification:** default to a failing test, minimal passing code, and safe refactoring for behavior changes; exercise boundaries, meaningful failure modes, and regressions.
- **Reliable and secure behavior:** validate trust boundaries, minimize permissions, handle errors deliberately, make side effects observable, and design recovery proportional to risk.
- **Sustainable engineering:** keep canonical documentation current, make reviewable changes, protect backwards compatibility when required, and verify rather than assume success.

## Working method

1. **Read before changing:** inspect relevant existing code, tests, contracts, constraints, and established style. Understand the problem and the reason behind the existing design.
2. **State the intended result:** describe input/output behavior and constraints; identify the simplest viable approach. Assess the cost of change and avoid speculative capabilities.
3. **Choose boundaries deliberately:** optimize locality and cohesion, explicit dependency direction, minimal interfaces, and a clear owner for each rule/state.
4. **Implement and verify:** use the project's conventions. For a behavior change, prefer red → green → refactor; validate observable behavior and important edge cases. Refactor only while behavior remains verifiable.
5. **Review complexity ROI:** inspect every new abstraction, dependency, configuration layer, branch, and shared state for a concrete benefit. Prefer removal or simplification when the benefit is uncertain.
6. **Finish with evidence:** run applicable checks (tests, lint, typing, build, relevant security/performance checks when available), inspect the diff, and report what passed, failed, or could not run. Do not claim unexecuted validation.

## Decision rules

- Do **not** force a pattern, paradigm, abstraction, or architectural style because it appears on a checklist.
- Keep a small local duplication when the alternative creates an unnecessary shared dependency. Extract only stable, genuinely shared behavior or knowledge.
- Do not fragment code solely to minimize function length or file size. Split when responsibilities, reasoning, testability, or change ownership improve.
- Prefer one coherent path over layers of wrappers; expose failure and state rather than relying on implicit magic.
- When two reasonable designs remain, articulate the least-complex viable default and when a more complex alternative would be justified.
- Respect existing interfaces, repository policies, and authorized scope; do not reformat or restructure unrelated code.

## Review output

For findings, give **priority, location, violated constraint or risk, recommended change, and verification**. Limit recommendations to substantive, actionable items. Separate required corrections from optional improvements. If no meaningful problems are evidenced, say so without inventing concerns.

## Public and private responsibilities

- **Public:** This self-contained, reusable, language-, industry-, and platform-agnostic workflow and its references.
- **Private:** Any local, personal, or workplace conventions belong only in `~/.claude/skill-overrides/code-best-practices.md`.
- For local customization, edit only the matching private file; do not modify the public source, installed copies, or symlink targets.
- Create the optional private file only upon request. Never commit, push, quote, or expose its contents. If instructions conflict, follow applicable security and organizational policies and surface the conflict.

## Private instructions (Claude Code only, loaded on invocation)

!`cat "$HOME/.claude/skill-overrides/code-best-practices.md" 2>/dev/null || true`
