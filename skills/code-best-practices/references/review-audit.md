# Repository, commit, code review, and architecture audits

Default to read-only assessment unless the user requests edits. Findings require evidence, not just an aesthetic preference. Match breadth to the requested target; avoid declaring a repository healthy after sampling only a small part.

## Establish evidence and scope

- **Repository audit:** inspect structure, high-risk code paths and owners, modules/dependencies and cycles, test/CI/build configuration, security, operational configuration, and representative entry points. Disclose uninspected regions.
- **Commit review:** inspect parent/base, the changed diff, affected callers and behavior, regression tests, compatibility, commit cohesion and traceability.
- **Pull-request review:** inspect base/head and all relevant changes; review new and existing tests, interfaces, migrations, security and operational impact, check outcomes and unanswered review comments.
- **Code review:** analyze relevant local flows, control paths, error handling, contracts, OOP responsibilities, complexity, side effects, and tests. Do not expand into unrelated changes.
- **Architecture review:** reconstruct actual boundaries and data flow before recommending restructuring; compare alternatives and show their complexity ROI.

If necessary files, branches, CI results, deployment details or runtime data are unavailable, explicitly mark the limit. Do not infer an implementation detail that the source does not show.

## Review priorities

1. Verified correctness, authorization/security, data integrity, and compatibility risks.
2. Material failure recovery and operational risks, unverified behavior and weak or missing tests.
3. Change amplification, responsibility mistakes, coupling, object invariants, ambiguity, and complexity cost.
4. Performance problems only with defensible evidence, and optional style changes last.

## Findings contract

For each substantive finding include **priority**, **path and line/diff scope**, **observed evidence**, **behavioral/security/maintainability impact**, **confidence**, **minimal recommended change**, and **how to validate**. State separately what is verified, suspected, or untested. Do not reveal secrets or invent results.

## Verification

- Select unit, integration, contract, end-to-end, security, static, build, and operational checks according to changed behavior and risk.
- Execute available authorized checks and report their exact outcomes. When a check is not available, distinguish **not run** from **passed** and explain why.
- Inspect assertions and coverage meaning rather than trusting a green pipeline. A review may conclude incomplete evidence despite passing CI.
- For fixes, preserve existing behavior unless authorized, prefer a failing regression test, apply the minimal correction, rerun tests, then inspect the diff.
- Record decisions, validation, risks, and remaining action directly in the review or pull-request artifact where possible.

## Output

Present scope/baseline, findings ordered by priority, verification, remediation order, residual risks, and a conclusion limited to observed evidence. If no major issue is found, report **no substantive findings in inspected scope** rather than claiming comprehensive correctness.
