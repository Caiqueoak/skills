# Spec decomposition and sizing

Choose a **user-observable capability** as the default spec boundary. Each spec should have one clear outcome, explicit acceptance criteria, and a workable implementation path. Spec boundaries are driven by cohesion, not a mandatory task count.

## Decisions

- **Keep together:** requirements that form one cohesive, testable user workflow; a thin UI/API/data slice that only becomes useful together.
- **Split:** unrelated user goals, materially different business rules, distinct release gates, or work too large to design and review without ambiguity.
- **Avoid over-splitting:** don't create a spec for each screen, endpoint, class, framework layer, test file, or database table.
- **Avoid under-splitting:** don't place a whole product into one feature spec or mix independent workflows merely because they share the same model.
- Prefer a handful of understandable initial specs. A working heuristic is **2–7 trackable tasks per spec**, revisited as uncertainty falls. Task size is validated by having one coherent test-driven change and one commit, not by hours or story points.
- Dependencies should be explicit; independent specs can be implemented separately. Sequence the smallest useful product experience first.
- For broad ideas, propose a thin MVP and clearly defer optional functionality. Record genuine unresolved questions in the relevant canonical document.

## Worked decomposition: "Build a diet tracking app"

These are **illustrative assumptions**, not default user requirements:

| Folder / ID | User-visible outcome | Dependency |
| --- | --- | --- |
| 001-nutrition-goals / W001 | Set a daily calorie/macronutrient goal | None |
| 002-food-lookup / W002 | Find foods and inspect nutrition values | None |
| 003-daily-food-log / W003 | Log consumed food and see daily totals | W002 |
| 004-log-history / W004 | Review and correct previously logged meals | W003 |

Global _flow/prd.md owns the target audience, problem, MVP scope, success indicators, and exclusions. Global _flow/technical.md owns the architecture/stack only once. Global _flow/progress.md links the four specs and tracks what is ready, active, or blocked.

Inside 003-daily-food-log/:
- requirements.md owns "given a food and amount, record consumption and update daily totals" and its measurable acceptance criteria.
- design.md owns only the meal-logging data flow, validation, persistence interactions, and test strategy, referencing global architecture.
- tasks.md breaks delivery into traceable test-driven changes, such as W003-T001 (record a food quantity) and W003-T002 (calculate and show daily totals). Each gets a separate verified commit.
- docs/ exists only if additional spec-local research or documentation is genuinely necessary.

## Planning review

For every candidate spec, ask: What outcome can a person verify? Are its rules cohesive? Could the work be accepted without implementing an unrelated feature? Are its tasks small enough for test-first implementation and a single commit each? Can a reader discover the authoritative description without searching multiple documents?

Adjust boundaries when these answers are weak. Keep existing IDs stable after publication.
