# {{SPEC_ID}} — {{SPEC_TITLE}} — Requirements

> Spec: {{SPEC_ID}} | Folder: {{NUMBER}}-{{SLUG}} | Status is tracked in ../../progress.md.

## User outcome

{{ONE_INDEPENDENTLY_VERIFIABLE_OUTCOME}}

## In scope

- {{BEHAVIOR_OR_RULE}}

## Out of scope

- {{BOUNDARY_AND_LINK_IF_OTHER_SPEC}}

## Functional requirements (EARS)

Write each normative behavioral requirement using the simplest applicable EARS pattern. Replace placeholders with unambiguous, observable conditions and responses; preserve stable requirement IDs. Use only the patterns applicable to this spec:

- **Ubiquitous:** The {{SYSTEM}} shall {{OBSERVABLE_RESPONSE}}.
- **Event-driven:** When {{TRIGGER}}, the {{SYSTEM}} shall {{OBSERVABLE_RESPONSE}}.
- **State-driven:** While {{STATE}}, the {{SYSTEM}} shall {{OBSERVABLE_RESPONSE}}.
- **Optional feature:** Where {{FEATURE_IS_ENABLED}}, the {{SYSTEM}} shall {{OBSERVABLE_RESPONSE}}.
- **Unwanted behavior:** If {{UNDESIRED_CONDITION}}, then the {{SYSTEM}} shall {{OBSERVABLE_RESPONSE}}.

- **{{SPEC_ID}}-R01:** {{ONE_ATOMIC_EARS_REQUIREMENT}}

## Acceptance criteria

Reference the corresponding requirement ID. Use Given/When/Then when it makes an observable test scenario clearer; cover relevant normal, boundary, and failure conditions without duplicating normative requirements.

- **{{SPEC_ID}}-AC01 ({{SPEC_ID}}-R01):** Given {{CONTEXT}}, when {{ACTION}}, then {{OBSERVABLE_RESULT}}.

## Dependencies and constraints

- **Depends on:** {{SPEC_IDS_OR_NONE}}
- **Constraints / assumptions:** {{LOCAL_CONSTRAINTS_OR_NONE}}

## Open questions

- {{OPEN_QUESTION_OR_NONE}}

## Related documents

- [Spec design](design.md)
- [Executable tasks](tasks.md)
- [Product scope](../../prd.md)
