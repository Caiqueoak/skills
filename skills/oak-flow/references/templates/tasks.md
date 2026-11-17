# {{SPEC_ID}} — {{SPEC_TITLE}} — Tasks

## Quick navigation

- [At a glance](#at-a-glance)
- [Work order](#work-order)

## At a glance

- **Outcome:** {{ONE_DELIVERABLE}}
- **Decisions:** {{DECISION_IDS_WITH_STATUS_OR_NONE}}
- **Pending review:** {{OPEN_BLOCKERS_OR_NONE}}
- **Next action:** {{FIRST_READY_TASK_ID_OR_BLOCKER}}

> Checkboxes live here; spec status lives in [progress](../../progress.md). [Requirements](requirements.md) · [Design](design.md).

## Work order

- [ ] **{{SPEC_ID}}-T001 — {{ONE_ATOMIC_TESTABLE_CHANGE}}**
  - **Acceptance:** {{SPEC_ID}}-AC01
  - **Steps (repeat for every task):**
    1. **Prepare:** {{CODE_REQUIREMENTS_DESIGN_AND_DEPENDENCIES_TO_CHECK}}.
    2. **Red:** {{TEST_TO_ADD}}; confirm failure for the intended behavior.
    3. **Green:** {{MINIMUM_IMPLEMENTATION}}.
    4. **Refactor:** {{READABILITY_OR_COHESION_IMPROVEMENT}} with tests green.
    5. **Validate:** {{RELEVANT_TESTS_AND_FAILURE_CASES}}; stop if failed or unavailable.
    6. **Commit:** Make one atomic commit containing code, test, relevant docs, and the checked task: `feat({{SCOPE}}): {{ACTION}} [{{SPEC_ID}}-T001]`, only after validation passes.
    7. **Confirm:** Verify commit and evidence; otherwise leave task unchecked and record blocker.
