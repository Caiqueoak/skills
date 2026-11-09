# {{SPEC_ID}} — {{SPEC_TITLE}} — Tasks

> Task checkboxes are authoritative here; spec status is in [progress](../../progress.md). NEW marks pending task-plan approval, not unfinished implementation.

## Index

> 🆕 **NEW** = awaits explicit approval of the current item.

- [Work order](#work-order) — 🆕 **NEW**
  - [{{SPEC_ID}}-T001 — Deliverable](#t001) — 🆕 **NEW**
- [Completion gate](#completion-gate)
- [Related documents](#related-documents)

## Work order

<a id="t001"></a>
### {{SPEC_ID}}-T001 — {{SMALL_TESTABLE_DELIVERABLE}} 🆕 **NEW**

- [ ] **Implementation complete** (mark only after successful validation and commit)
- **Acceptance:** {{SPEC_ID}}-AC01
- **Red:** {{FAILING_TEST_TO_ADD}}
- **Green:** {{MINIMUM_BEHAVIOR_TO_IMPLEMENT}}
- **Refactor / verify:** {{RELEVANT_CHECKS_AND_REGRESSIONS}}
- **Commit:** feat({{SCOPE}}): {{SHORT_IMPERATIVE}} [{{SPEC_ID}}-T001]

Keep each task small, vertical, independently verifiable, and mapped to explicit acceptance criteria. The NEW badge is removed when the plan is explicitly approved; the checkbox is completed after implementation, testing, and commit. Neither implies the other.

## Completion gate

- Start with a meaningful failing test, implement, refactor, and run relevant regressions.
- Verify acceptance conditions, migration/integration behavior, and relevant documentation.
- Commit exactly once per completed task with its stable ID (unless repository policy requires a stricter compatible convention).
- Check off a task only after successful validation and commit; update global progress.md only when the spec-level state or next step changes.
- If blocked, leave the task unchecked and document the blocker in progress.md.

## Related documents

- [Requirements](requirements.md)
- [Design](design.md)
- [Project progress](../../progress.md)
