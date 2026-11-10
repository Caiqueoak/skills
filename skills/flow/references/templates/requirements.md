# {{SPEC_ID}} — {{SPEC_TITLE}} — Requirements

> Spec: {{SPEC_ID}} | Folder: {{NUMBER}}-{{SLUG}} | Canonical spec status: [progress](../../progress.md). Each NEW badge means review is pending.

## Index

> 🆕 **NEW** = awaits explicit approval of the current item.

- [User outcome](#user-outcome) — 🆕 **NEW**
  - [User outcome](#o001) — 🆕 **NEW**
- [Scope and boundaries](#scope-and-boundaries) — 🆕 **NEW**
  - [In scope](#s001) — 🆕 **NEW**
  - [Out of scope](#s002) — 🆕 **NEW**
- [Functional requirements (EARS)](#functional-requirements-ears) — 🆕 **NEW**
  - [{{SPEC_ID}}-R01 — Requirement](#r01) — 🆕 **NEW**
- [Acceptance criteria](#acceptance-criteria) — 🆕 **NEW**
  - [{{SPEC_ID}}-AC01 — Acceptance](#ac01) — 🆕 **NEW**
- [Dependencies and constraints](#dependencies-and-constraints) — 🆕 **NEW**
  - [Dependencies / constraints](#dep01) — 🆕 **NEW**
- [Open questions](#open-questions) — 🆕 **NEW**
  - [Open question](#q001) — 🆕 **NEW**
- [Related documents](#related-documents)

## User outcome

- <a id="o001"></a>**O001 — Independently verifiable outcome** 🆕 **NEW**: {{ONE_INDEPENDENTLY_VERIFIABLE_OUTCOME}}

## Scope and boundaries

### In scope

- <a id="s001"></a>**S001 — Included behavior / rule** 🆕 **NEW**: {{BEHAVIOR_OR_RULE}}

### Out of scope

- <a id="s002"></a>**S002 — Excluded behavior** 🆕 **NEW**: {{BOUNDARY_AND_LINK_IF_OTHER_SPEC}}

## Functional requirements (EARS)

Write every normative behavior as **one atomic, observable EARS requirement**, choosing the simplest applicable pattern:

- Ubiquitous: The {{SYSTEM}} shall {{OBSERVABLE_RESPONSE}}.
- Event-driven: When {{TRIGGER}}, the {{SYSTEM}} shall {{OBSERVABLE_RESPONSE}}.
- State-driven: While {{STATE}}, the {{SYSTEM}} shall {{OBSERVABLE_RESPONSE}}.
- Optional feature: Where {{FEATURE_IS_ENABLED}}, the {{SYSTEM}} shall {{OBSERVABLE_RESPONSE}}.
- Unwanted behavior: If {{UNDESIRED_CONDITION}}, then the {{SYSTEM}} shall {{OBSERVABLE_RESPONSE}}.

Use only applicable patterns in the completed document; remove this drafting guidance.

- <a id="r01"></a>**{{SPEC_ID}}-R01** 🆕 **NEW**: {{ONE_ATOMIC_EARS_REQUIREMENT}}

## Acceptance criteria

Reference the owning requirement; use Given/When/Then where it clarifies an observable normal, edge, or failure scenario. Do not duplicate the requirement.

- <a id="ac01"></a>**{{SPEC_ID}}-AC01 ({{SPEC_ID}}-R01)** 🆕 **NEW**: Given {{CONTEXT}}, when {{ACTION}}, then {{OBSERVABLE_RESULT}}.

## Dependencies and constraints

- <a id="dep01"></a>**DEP01 — Dependencies / constraints / assumptions** 🆕 **NEW**: {{SPEC_IDS_AND_LOCAL_CONSTRAINTS_OR_NONE}}

## Open questions

- <a id="q001"></a>**Q001 — Question requiring decision** 🆕 **NEW**: {{OPEN_QUESTION_OR_NONE}}

## Related documents

- [Spec design](design.md)
- [Executable tasks](tasks.md)
- [Product scope](../../prd.md)
