# Test design, audits, validation, and improvement

Treat tests as evidence of protected behavior, not as a count or coverage percentage. Evaluate whether a relevant regression would make the test fail for the correct reason.

## Appropriate test layers

- **Unit and property-based tests:** local behavior, invariants, transformations, boundaries and generative properties.
- **Integration and contract tests:** interaction and agreement between real components or independently evolving interfaces; avoid mock-only confidence.
- **System and end-to-end tests:** critical externally observable workflows and deployment confidence, used proportionately to cost.
- **Security, concurrency, performance, resilience and recovery tests:** use when exposure and risk justify them.
- **Static checks, types, lint, build and package checks:** important complementary evidence, never substitutes for behavioral verification.

## Test-first implementation

Prefer red → green → refactor for behavior changes: demonstrate a relevant failing assertion for the expected behavior, implement the minimal passing change, then refactor while regression tests remain green. If a test cannot be run, document why and do not claim the cycle was verified.

## Test-suite audit

1. Inventory test runner(s), commands, project conventions, existing suites, skipped/ignored tests, CI gates and environment assumptions.
2. Map contracts, critical flows, state invariants, permissions, and failure paths to actual assertions. Locate unprotected behavior, false positives, and duplicate tests without extra confidence.
3. Inspect assertion strength: vacuous assertions, unexecuted cases, missing negative outcomes, mock interactions that do not prove behavior, broad snapshots and brittle implementation coupling.
4. Look for flaky tests caused by time, concurrency, shared state, ordering, environment, uncontrolled external services, fragile waits, or non-deterministic data.
5. Consider coverage gaps, branch reachability, mutation testing and defect-seeding **as diagnostic evidence** when safe and feasible. No universal coverage or mutation percentage proves quality.
6. Audit maintainability and feedback: fixtures, test data, setup cost, speed, isolation, naming, diagnostics, and unnecessary test abstractions.
7. Prioritize improvements by risk: consequential untested behavior and misleading tests first, then flakiness and costly maintenance, then optional efficiency.

## Improve tests

- For every proposed test, state the behavior or invariant, input/trigger, expected observable outcome, regression it should catch, chosen layer, and why that layer is sufficient.
- Favor meaningful assertions and high-value boundary and negative paths over merely increasing coverage. Use deterministic seams for time and side effects when appropriate.
- Reduce over-mocking, improve contract alignment and make test failure diagnosis actionable. Keep fixtures local and small unless shared abstraction offers clear maintenance ROI.
- Fix the root cause of flakiness instead of blindly adding retries, sleeps, or skipping tests; quarantine only with explicit risk and follow-up.
- For a changed assertion, verify that it fails for an intentionally missing or incorrect behavior where safely feasible; restore code and rerun relevant regression checks.
- Avoid changing production interfaces solely to satisfy test internals unless the resulting design improvement is independently justified.

## Validation and reporting

Record **what was examined**, **commands and environments actually executed**, **pass/fail/skipped/not-run results**, **behavioral risks covered**, **test-quality weaknesses**, **prioritized improvements**, and **unknowns**. Distinguish local execution from reported CI results. A green test suite, code coverage, or scanner badge never proves the full repository correct or secure.
