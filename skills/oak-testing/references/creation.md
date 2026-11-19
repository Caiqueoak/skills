# Test creation and maintenance

Use for new behavior, TDD, bug fixes, refactors, and removal of obsolete tests. Test design must justify both regression value and total feedback cost.

## 1. Find an authoritative contract

Consult the request, accepted requirements, supported behavior, public contracts, invariants, and existing tests. Distinguish intended behavior from incidental implementation. Do not infer a new product rule solely because code once existed.

A candidate test is eligible only when all are answerable:

- **Contract:** What authorized, in-scope behavior or invariant does it protect?
- **Trigger and outcome:** Which realistic input/state produces which observable result?
- **Regression:** What plausible defect would make it fail for the right reason?
- **Marginal value:** Does an existing test already provide adequate confidence?
- **Cost:** Is this the lowest-cost reliable test layer and setup for that risk?

Reject or simplify tests without a meaningful contract or distinct value. Do not create tests solely to increase counts, satisfy a test-per-change quota, mirror source files, or record an implementation decision.

## 2. Handle change types deliberately

- **New or changed behavior:** test canonical success, consequential boundary/failure cases, and explicit invariants proportional to risk.
- **Bug fix:** verify the intended contract with a regression test when it exposes an otherwise unprotected defect; avoid preserving incidental buggy behavior.
- **Refactor without contract change:** prefer existing behavioral tests; add a test only for a real uncovered risk.
- **Removed accidental/out-of-scope behavior:** remove obsolete tests and implementation; do not automatically test that the accident is absent.
- **Explicit absence or prohibition requirement:** a negative assertion is appropriate when absence itself is part of the contract, including access restrictions or forbidden state transitions.
- **Deletion-only or mechanically verified change:** do not fabricate a failing test. Use the existing relevant checks and explain when a new red-phase test has no meaningful target.

Avoid speculative scenarios, impossible states under documented preconditions, implementation-only branches, and unrelated features.

## 3. Choose the lowest sufficient layer

- Prefer local unit or property checks for pure behavior and invariants.
- Use component tests when rendered or interactive behavior is itself contractual.
- Use integration or contract tests for real boundaries and independently changing interfaces; do not pretend mock-only tests establish integration.
- Reserve system/end-to-end, performance, concurrency, security, and recovery tests for relevant critical risks.

One concise scenario may cover related assertions when it remains diagnostic; split independent behaviors only when doing so improves clarity or regression localization. Do not test every combination without a credible distinct risk.

## 4. Keep tests isolated and inexpensive

- Arrange focused, deterministic setup and test data; keep fixtures near their owner unless sharing has clear value.
- Mock uncontrollable external boundaries, not the behavior under test. Prefer simple fakes over elaborate mock graphs.
- Avoid starting real services, full applications, expensive dependency containers, or browsers for a contract provable at a cheaper layer.
- Avoid global mutable state, order dependence, real sleeps, retries that hide flakiness, fragile snapshots, and private-method assertions.
- Name tests for observable behavior; assert results and public effects rather than irrelevant calls or internal structure.
- Keep test modules cohesive with the owning feature. Reuse harnesses only when they reduce actual maintenance and setup cost.
- Consider setup, compilation, discovery, runtime, teardown, and future debugging time when evaluating test design.

## 5. Apply TDD when the change supports it

1. Pick the smallest eligible contract and the lowest sufficient test layer.
2. **Red:** make one meaningful test fail for the intended missing behavior; distinguish this from setup/environment failures.
3. **Green:** implement the smallest in-scope change and rerun the targeted test.
4. **Refactor:** simplify code and tests without changing the contract; rerun impacted checks.
5. Reconcile obsolete tests, then follow the scoped validation process in the execution reference.

If the behavior is already protected, do not duplicate tests solely to manufacture a red phase. If a test cannot run, document the limitation rather than claiming TDD evidence.

## Review gate

Before keeping a test, verify: canonical scope, observable assertion, distinct regression value, realistic inputs, deterministic isolation, cheapest sufficient layer, and justified lifecycle cost. If any fails, improve, remove, or decline the test.
