# {{SPEC_ID}} — {{SPEC_TITLE}} — Tasks

> Task checkboxes are authoritative here; spec-level status is authoritative in ../../progress.md.

## Work order

- [ ] **{{SPEC_ID}}-T001 — {{SMALL_TESTABLE_DELIVERABLE}}**
  - **Acceptance:** {{SPEC_ID}}-AC01
  - **Red:** {{FAILING_TEST_TO_ADD}}
  - **Green:** {{MINIMUM_BEHAVIOR_TO_IMPLEMENT}}
  - **Refactor / verify:** {{RELEVANT_CHECKS_AND_REGRESSIONS}}
  - **Commit:** feat({{SCOPE}}): {{SHORT_IMPERATIVE}} [{{SPEC_ID}}-T001]

## Completion gate

- Each task has a meaningful failing test first, passing implementation, and cleanup.
- Relevant tests pass; verify listed acceptance criteria and any migration or integration behavior.
- Commit exactly once per completed task with its stable ID (unless a repo policy requires a stricter compatible convention).
- Mark a checkbox only after successful validation and commit. Update global progress.md only for spec-level changes or the next action.
- If blocked, leave unchecked and record the blocker in progress.md; do not claim completion.

## Related documents

- [Requirements](requirements.md)
- [Design](design.md)
- [Project progress](../../progress.md)
