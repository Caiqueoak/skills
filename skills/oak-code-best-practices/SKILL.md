---
name: oak-code-best-practices
description: Design and assess architecture, OOP code, security, and testing; implement or refactor software and validate repositories, commits, and pull requests using pragmatic, language-agnostic engineering principles.
---

<!-- skill-source: Caiqueoak/skills -->

# Code best practices

Reason from required behavior toward the simplest safe, readable, maintainable, and testable solution. Principles are **not unconditional laws**; optimize for clear intent and demonstrated constraints rather than patterns or speculative extensibility.

## Select only the requested mode

- **Architecture design or review:** evaluate alternatives, quality attributes, contracts, boundaries, dependency direction, ownership, operations, and verification.
- **Repository audit:** assess important code paths, architecture, dependencies, tests, CI, security, and maintainability; disclose uninspected areas.
- **Commit / pull-request review:** inspect actual diff, base, callers, contracts, test changes, security risk, and evidence.
- **Test suite audit and improvement:** evaluate assertions, regression detection, isolation, flaky tests, missing cases, and maintainability.
- **Implementation and refactoring:** deliver the smallest scoped change with verified behavior.
- **Focused code review:** provide prioritized evidence-backed findings rather than editing without permission.

Read only relevant references: `references/principles.md`, `references/architecture-oop.md`, `references/security.md`, `references/testing-validation.md`, `references/review-audit.md`.

## Priorities and principles

1. Correctness, safety, data integrity, contracts, and observable behavior.
2. Readability, explicit intent, semantic naming, high cohesion, low coupling, and locality.
3. Maintainability, testability, clear responsibility, and a single source of truth.
4. KISS and YAGNI: smallest current solution, not speculative infrastructure.
5. Evidence-based performance and scale; avoid guesswork.

Apply SOLID, SRP, DRY, SSOT, explicit contracts and types, OOP encapsulation and substitutability, Composition over inheritance, Tell Don't Ask, Law of Demeter, and functional design only when they improve outcomes. Prefer pure functions, immutability, and isolated side effects when useful; tolerate local duplication when abstraction increases coupling. Evaluate **Complexity ROI** for every layer, dependency, or shared state: measurable benefit must outweigh cognitive and operating cost.

## Working method

1. **Inspect first:** read relevant source, tests, docs, existing conventions, public interfaces, and affected callers. For refactoring, identify the actual cohesion or change-cost problem and preserve behavior.
2. **Define the contract:** state inputs, outputs, invariants, failure modes, constraints, and acceptance evidence; identify the least complex viable approach.
3. **Choose clear ownership:** organize around cohesive behavior or vertical slices; use explicit dependencies and narrow interfaces only when needed.
4. **Implement and test:** prefer red → green → refactor for behavior changes. Test meaningful nominal, boundary, failure, and regression cases; validate relevant security and operational risks.
5. **Review complexity:** challenge new indirection, configuration, classes, shared state, or layers; avoid accidental unrelated changes.
6. **Validate and finish:** run appropriate tests, build, lint, typing, or security checks when possible, inspect the diff, and **report what passed, failed, or could not run**. Do not claim coverage of unseen source or checks not executed.

## Mode-specific constraints

- For **refactoring**: preserve observable behavior and public contracts unless change is explicitly authorized.
- For **review**: **Distinguish correctness or safety defects from preferences**; rank findings by severity and confidence, cite path/location and observed evidence, explain impact, smallest justified fix, and how to verify it.
- **For architecture:** compare simple and complex options from actual requirements, state, data ownership, operational exposure, and reversibility; do not impose a paradigm.
- **For security:** trace assets, trust boundaries, authentication, authorization, untrusted inputs, secrets, dependencies, supply chain, and failure exposure; label suspected versus verified issues.
- **For tests:** judge whether checks would detect a meaningful regression; green CI and coverage percentages do not establish test quality.
- **Do not initiate unrelated rewrites** or changes outside authorized scope. Explain unresolved tradeoffs and uncertainty instead of fabricating results.

## Review output

Include priority, location, evidence, impact, confidence, recommended change, and verification; state scope examined, baselines, tests actually run, omitted areas, and residual risks. Prefer concrete findings over style-only churn.

## Public and private responsibilities

- **Public:** Reusable, independent guidance and any references belonging to this skill, without domain or organization assumptions.
- **Private:** Local and workplace conventions belong only in `~/.claude/skill-overrides/oak-code-best-practices.md`. Create this file only when requested; for customization edit it, not public source, installed copies, or symlink targets. Never quote, commit, or publish private instructions.

## Optional private override (on invocation)

When invoked, resolve `~` to the active user's home directory and attempt to read `~/.claude/skill-overrides/oak-code-best-practices.md` using an available native file-reading tool or API. Do not require Bash, `cat`, or any specific shell. Apply only this skill's matching private instructions. If the file is absent or inaccessible, continue with the public workflow; report the access limitation only if it affects the requested customization. Do not read unrelated overrides or disclose private contents.
