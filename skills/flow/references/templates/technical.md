# {{PROJECT_NAME}} — Technical baseline

> Purpose: canonical cross-spec architecture and standards; spec-local details belong in each design document.

## Index

> 🆕 **NEW** = awaiting explicit review and approval of the current item.

- [System overview](#system-overview) — 🆕 **NEW**
  - [A001 — System context / boundaries](#a001) — 🆕 **NEW**
- [Architecture and components](#architecture-and-components) — 🆕 **NEW**
  - [A002 — Architecture](#a002) — 🆕 **NEW**
  - [A003 — Components / responsibilities](#a003) — 🆕 **NEW**
  - [A004 — Integrations](#a004) — 🆕 **NEW**
- [Technology and delivery](#technology-and-delivery) — 🆕 **NEW**
  - [A005 — Language / runtime / framework](#a005) — 🆕 **NEW**
  - [A006 — Data ownership / storage](#a006) — 🆕 **NEW**
  - [A007 — Deployment](#a007) — 🆕 **NEW**
- [Cross-cutting quality attributes](#cross-cutting-quality-attributes) — 🆕 **NEW**
  - [A008 — Security / privacy](#a008) — 🆕 **NEW**
  - [A009 — Quality attributes](#a009) — 🆕 **NEW**
  - [A010 — Operations / observability](#a010) — 🆕 **NEW**
- [Engineering conventions](#engineering-conventions) — 🆕 **NEW**
  - [A011 — Testing / CI gates](#a011) — 🆕 **NEW**
- [Global technical decisions](#global-technical-decisions) — 🆕 **NEW**
  - [A012 — Technical decision](#a012) — 🆕 **NEW**
- [Open technical decisions](#open-technical-decisions) — 🆕 **NEW**
  - [A013 — Open decision](#a013) — 🆕 **NEW**
- [Related documents](#related-documents)
## System overview

- <a id="a001"></a>**A001 — System context / boundaries** 🆕 **NEW**: {{BRIEF_CONTEXT_AND_BOUNDARIES}}

## Architecture and components

- <a id="a002"></a>**A002 — Architecture** 🆕 **NEW**: {{ARCHITECTURE_OR_TBD}}
- <a id="a003"></a>**A003 — Components / responsibilities** 🆕 **NEW**: {{COMPONENTS_OR_TBD}}
- <a id="a004"></a>**A004 — Integrations** 🆕 **NEW**: {{INTEGRATIONS_OR_TBD}}

## Technology and delivery

- <a id="a005"></a>**A005 — Language / runtime / framework** 🆕 **NEW**: {{STACK_OR_TBD}}
- <a id="a006"></a>**A006 — Data ownership / storage** 🆕 **NEW**: {{STORAGE_OR_TBD}}
- <a id="a007"></a>**A007 — Deployment** 🆕 **NEW**: {{DEPLOYMENT_OR_TBD}}

## Cross-cutting quality attributes

- <a id="a008"></a>**A008 — Security / privacy** 🆕 **NEW**: {{SECURITY_OR_TBD}}
- <a id="a009"></a>**A009 — Reliability / performance / accessibility** 🆕 **NEW**: {{QUALITY_ATTRIBUTES_OR_TBD}}
- <a id="a010"></a>**A010 — Operations / observability** 🆕 **NEW**: {{OPERATIONS_OR_TBD}}

## Engineering conventions

- Test first: red → green → refactor.
- One verified atomic commit per W###-T### task, including tests and directly related documentation.
- Reuse established project patterns; keep responsibilities simple, cohesive, and explicit.
- <a id="a011"></a>**A011 — Testing / CI gates** 🆕 **NEW**: {{TEST_COMMANDS_AND_QUALITY_GATES_OR_TBD}}

## Global technical decisions

| ID | Decision | Rationale | State |
| --- | --- | --- | --- |
| <a id="a012"></a>A012 | 🆕 **NEW** {{DECISION}} | {{RATIONALE}} | proposed |

State values: proposed, accepted, superseded. Approval markers are independently maintained.

## Open technical decisions

- <a id="a013"></a>**A013 — Decision needed** 🆕 **NEW**: {{QUESTION_AND_IMPACT_OR_NONE}}

## Related documents

- [Product baseline](prd.md)
- [Delivery progress](progress.md)
