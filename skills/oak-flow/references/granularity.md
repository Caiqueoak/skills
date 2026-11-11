# Spec decomposition and sizing

Choose a **user-observable capability** as the default spec boundary. Each spec should have one clear outcome, explicit acceptance criteria, and a workable implementation path. Spec boundaries are driven by cohesion, not a mandatory task count.

## Boundaries

- **Keep together:** requirements that form one cohesive, testable user workflow; a thin vertical slice across multiple technical layers that only becomes useful together.
- **Split:** independent user goals, materially different business rules, distinct release gates, or work too large to understand, review, and verify without ambiguity.
- **Avoid over-splitting:** never make a spec for every screen, endpoint, class, framework layer, test file, or data entity by default.
- **Avoid under-splitting:** never place an entire product in a single feature spec or combine unrelated journeys because they touch a shared component.
- Prefer a small, understandable initial set of specs. A working heuristic is **2–7 trackable tasks per spec**, revisited as uncertainty falls; this is not an enforced limit. One verified test-driven change and atomic commit define task size better than an hour or point estimate.
- Make dependencies explicit. Prioritize the smallest coherent, independently verifiable product outcome and avoid unnecessary serial dependencies.
- For broad ideas, propose a thin initial scope and defer optional functionality explicitly. Keep genuine unresolved questions in the relevant canonical document.

## Decomposition procedure

1. Identify distinct actors, desired outcomes, and key behavior from the product baseline or available discovery evidence.
2. Group closely related behavior and acceptance conditions by cohesive user-visible outcome rather than by implementation technology.
3. Draw dependency edges; test whether any group can be split to reduce coupling or a group must be merged because neither part is independently meaningful.
4. For each candidate spec, articulate one acceptance statement and its in-scope/out-of-scope boundary.
5. Outline small verifiable tasks that fit a single test-first implementation and one atomic commit. If a candidate needs too many unrelated task outcomes, split the spec.
6. Assign stable sequential spec IDs and task IDs after boundaries are chosen. Do not renumber IDs after publication.

## Planning review

For every candidate spec, ask:

- What outcome can a person verify, and which assumptions must hold?
- Are the rules cohesive and the dependencies transparent?
- Can this outcome be accepted without implementing an unrelated capability?
- Is its design readable without repeating global architecture?
- Can each task be implemented test-first and validated as a single commit?
- Can a reader discover the authoritative requirement, design, task state, and project status without reconciling copies?

Adjust boundaries when these answers are weak. Keep existing IDs stable after publication. Do not embed domain-specific sample projects, personas, implementations, or technology assumptions into this guidance.
