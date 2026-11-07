# {{PROJECT_NAME}} — Technical baseline

> Purpose: canonical cross-spec technical decisions. Spec-local mechanics belong in each spec's design.md.

## System overview

{{BRIEF_CONTEXT_AND_BOUNDARIES}}

## Architecture and components

- **Architecture:** {{ARCHITECTURE_OR_TBD}}
- **Major components and responsibilities:** {{COMPONENTS_OR_TBD}}
- **System context / integrations:** {{INTEGRATIONS_OR_TBD}}

## Technology and delivery

- **Language/runtime/framework:** {{STACK_OR_TBD}}
- **Storage and data ownership:** {{STORAGE_OR_TBD}}
- **Deployment / runtime environment:** {{DEPLOYMENT_OR_TBD}}

## Cross-cutting quality requirements

- **Security and privacy:** {{SECURITY_OR_TBD}}
- **Reliability, performance, accessibility:** {{QUALITY_ATTRIBUTES_OR_TBD}}
- **Observability and operations:** {{OPERATIONS_OR_TBD}}

## Engineering conventions

- Test-first development: red → green → refactor.
- One verified atomic commit per W###-T### task (tests, implementation, directly related documentation).
- Reuse project conventions and keep responsibilities explicit, cohesive, and simple.
- **Testing / CI:** {{TEST_COMMANDS_AND_QUALITY_GATES_OR_TBD}}

## Global technical decisions

| Decision | Reason | Status |
| --- | --- | --- |
| {{DECISION}} | {{RATIONALE}} | proposed / accepted / superseded |

## Open technical decisions

- {{QUESTION_AND_IMPACT_OR_NONE}}

## Related documents

- [Product baseline](prd.md)
- [Delivery progress](progress.md)
