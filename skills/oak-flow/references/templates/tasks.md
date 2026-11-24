# {{SPEC_ID}} — {{SPEC_TITLE}} — Tasks

## Quick navigation

- [At a glance](#at-a-glance)
- [Delivery state](#delivery-state)
- [Work order](#work-order)

## At a glance

- **Outcome:** {{ONE_DELIVERABLE}}
- **Decisions:** {{DECISION_IDS_WITH_STATUS_OR_NONE}}
- **Pending review:** {{OPEN_BLOCKERS_OR_NONE}}
- **Next action:** {{FIRST_READY_TASK_ID_OR_BLOCKER}}

> This file owns the spec's delivery state and task checkboxes. [Progress guide](../../progress.md) · [Requirements](requirements.md) · [Design](design.md).

## Delivery state

- **Status:** {{PLANNED_READY_IN_PROGRESS_BLOCKED_OR_DONE}}
- **Dependencies:** {{SPEC_OR_TASK_IDS_OR_NONE}}
- **Blockers:** {{OWNER_AND_UNBLOCK_CONDITION_OR_NONE}}

Use the At a glance Next action field as the resume point; Pending review links to blockers here when needed. Do not duplicate the state in global documents. Only the assigned spec writer or integrating lead may update this file.

## Work order

- [ ] **{{SPEC_ID}}-T001 — {{ONE_ATOMIC_TESTABLE_CHANGE}}**
  - **Acceptance:** {{SPEC_ID}}-AC01
  - **Steps (repeat for every task):**
    1. **Prepare:** {{CODE_REQUIREMENTS_DESIGN_AND_DEPENDENCIES_TO_CHECK}}.
    2. **Red:** {{TEST_TO_ADD}}; confirm failure for the intended behavior.
    3. **Green:** {{MINIMUM_IMPLEMENTATION}}.
    4. **Refactor:** {{READABILITY_OR_COHESION_IMPROVEMENT}} with tests green.
    5. **Validate:** {{RELEVANT_TESTS_AND_FAILURE_CASES}}; fix recoverable failures and retry; if still blocked, leave unchecked, record the blocker, and continue independent authorized work.
    6. **Commit:** Make one atomic commit containing code, test, relevant docs, and the checked task: `feat({{SCOPE}}): {{ACTION}} [{{SPEC_ID}}-T001]`, only after validation passes.
    7. **Confirm:** Verify commit and evidence; otherwise leave task unchecked and record blocker.
