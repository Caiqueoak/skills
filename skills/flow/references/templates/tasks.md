# {{SPEC_ID}} — {{SPEC_TITLE}} — Tasks

## Quick navigation

- [At a glance](#at-a-glance)
- [Work order](#work-order)
- [Completion gate](#completion-gate)
- [Related documents](#related-documents)

## At a glance

- **Outcome:** {{SHORT_OUTCOME_OR_PURPOSE}}
- **Decisions:** {{DECISION_IDS_WITH_STATUS_AND_LINKS_OR_NONE}}
- **Pending review:** {{UNAPPROVED_ITEMS_OR_BLOCKERS_WITH_LINKS_OR_NONE}}
- **Next action:** {{ONE_ACTION_OR_LINK_TO_CANONICAL_OWNER_OR_NONE}}


> Task checkboxes are authoritative here; spec-level status is authoritative in ../../progress.md.

## Work order

- [ ] **{{SPEC_ID}}-T001 — {{SMALL_TESTABLE_DELIVERABLE}}**
  - **Acceptance:** {{SPEC_ID}}-AC01
  - **Execution steps (required for every task):**
    1. **Prepare:** {{REQUIREMENTS_DESIGN_DEPENDENCIES_AND_RELEVANT_CODE_TO_REVIEW}}
    2. **Red:** {{FAILING_AUTOMATED_TEST_TO_ADD_AND_CONFIRM}}
    3. **Green:** {{MINIMUM_BEHAVIOR_TO_MAKE_TEST_PASS}}
    4. **Refactor:** {{READABILITY_IMPROVEMENTS_WHILE_TESTS_STAY_GREEN}}
    5. **Validate:** {{REGRESSION_CHECKS_AND_ACCEPTANCE_CRITERIA_TO_VERIFY}}
    6. **Commit:** After successful validation, include tests, implementation, related docs, and this task's updated checkbox in one atomic commit: `feat({{SCOPE}}): {{SHORT_IMPERATIVE}} [{{SPEC_ID}}-T001]`
    7. **Confirm:** {{VERIFY_COMMIT_AND_TASK_COMPLETION_OR_LEAVE_UNCHECKED_IF_FAILED}}

## Completion gate

- Every task repeats all seven numbered steps; the shared gate cannot replace task-local TDD and commit instructions.
- A task is complete only when its failing test was confirmed, relevant tests pass, acceptance criteria are verified, and exactly one traceable atomic commit succeeds.
- Include the checkbox update in that same commit after validation; if the commit fails, restore the unchecked state and record the blocker in progress.md.
- Update global progress.md only for spec-level changes or the next action. Do not claim completion while blocked.

## Related documents

- [Requirements](requirements.md)
- [Design](design.md)
- [Project progress](../../progress.md)
