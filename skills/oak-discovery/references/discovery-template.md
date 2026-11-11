# {{INITIATIVE}} — Discovery record

> Canonical record for discovery evidence, hypotheses, question history, scenarios, and unresolved issues. Link to any separately maintained accepted decisions rather than duplicating them.
> Status: {{in_discovery|blocked|decision_ready|confirmed}} | Last reviewed: {{DATE_OR_TBD}} | Decision owner: {{OWNER_OR_UNKNOWN}}

## Problem framing

- **Problem statement:** {{KNOWN_OR_HYPOTHESIS}}
- **Desired outcome:** {{OUTCOME}}
- **Affected actors and stakeholders:** {{ACTORS}}
- **Current alternatives / baseline:** {{BASELINE_OR_UNKNOWN}}
- **Constraints and intended decision horizon:** {{CONSTRAINTS}}

## Existing system and source review

- **Inspected code, tests, configuration, and documents (paths/versions):** {{SOURCES_OR_ACCESS_GAPS}}
- **Observed behavior and established decisions:** {{REFERENCES_AND_SUMMARY}}
- **Documentation/code contradictions and proposed reconciliation:** {{CONFLICTS_OR_NONE}}
- **Affected integration boundaries and dependencies:** {{EVIDENCE_OR_UNKNOWN}}

## Facts, hypotheses, and evidence

| ID | Claim | Classification | Source / date / applicability | Confidence | Validation needed |
| --- | --- | --- | --- | --- | --- |
| H-001 | {{CLAIM}} | confirmed / sourced / hypothesis / unknown | {{REFERENCE_OR_NONE}} | high / medium / low / unassessed | {{METHOD_OR_NONE}} |

Use research URLs or existing canonical document links where available. Never promote hypotheses to confirmed facts without evidence or user confirmation.

## Discovery depth and dimension coverage

- **Overall depth:** {{FOCUSED_STANDARD_COMPREHENSIVE_AND_WHY}}
- **Escalation triggers:** {{EXPOSURE_DATA_SAFETY_COMPLEXITY_DEPENDENCIES_OR_NONE}}
- **Principle:** Screen all axes internally; investigate and question only those that materially affect this decision. Escalate individual dimensions independently of overall depth.

| Dimension | Applicability | Depth | Readiness | Evidence / exclusion rationale / remaining decision | Priority |
| --- | --- | --- | --- | --- | --- |
| {{AXIS_FROM_COVERAGE}} | essential / conditional / not_applicable | brief / targeted / deep / none | unexamined / investigating / resolved / deferred / not_applicable | {{JUSTIFICATION_AND_NEXT_STEP}} | high / medium / low / none |

Screen all axes in references/coverage.md or link to an existing authoritative coverage inventory. `not_applicable` must have a concise reason; `deferred` on material axes requires ownership, risk acceptance, and a validation path. Avoid turning every axis into a user-facing question or a mandatory requirement.

## Stakeholder needs and user journeys

- **Distinct actors, motivations, and constraints:** {{FINDINGS_OR_OPEN_QUESTIONS}}
- **Key journeys and lifecycle transitions:** {{JOURNEYS_OR_OPEN_QUESTIONS}}
- **Accessibility, trust, and usability concerns:** {{FINDINGS_OR_OPEN_QUESTIONS}}

## Scenario and edge-case register

| ID | Actor / precondition | Trigger / deviation | Expected behavior or open choice | Risk / severity | Validation |
| --- | --- | --- | --- | --- | --- |
| S-001 | {{ACTOR_AND_STATE}} | {{TRIGGER}} | {{HANDLING_OR_QUESTION}} | {{IMPACT}} | {{TEST_RESEARCH_OR_REVIEW}} |

Include nominal, alternate, failure, misuse, recovery, and change scenarios according to relevance. Never label an unverified expectation as settled.

## Opportunity, market, and economics

- **Demand and alternatives:** {{EVIDENCE_OR_RESEARCH_NEEDED}}
- **Differentiation / distribution / adoption:** {{HYPOTHESES_OR_EVIDENCE}}
- **Economics / ROI model and assumptions:** {{COSTS_BENEFITS_SENSITIVITIES_OR_UNKNOWN}}
- **Disconfirming evidence and stop signals:** {{RISKS_AND_THRESHOLD_OR_TBD}}

## Engineering, infrastructure, and operating feasibility

- **Candidate approaches and tradeoffs:** {{OPTIONS_NOT_PREMATURE_DECISIONS}}
- **System and data constraints:** {{FACTS_AND_UNKNOWNS}}
- **Resilience / support / ongoing operations:** {{RESPONSIBILITIES_AND_RISKS}}
- **Security and privacy obligations:** {{APPLICABLE_REQUIREMENTS_OR_REVIEW_NEEDED}}
- **Relevant regulatory / contractual applicability:** {{JURISDICTION_BASED_ASSESSMENT_OR_UNKNOWN}}

## Options and decisions

| ID | Decision / option | State | Evidence and rationale | Owner | Canonical destination / link |
| --- | --- | --- | --- | --- | --- |
| D-001 | {{DECISION}} | candidate / accepted / rejected / deferred / unknown | {{RATIONALE}} | {{OWNER}} | {{LINK_IF_ADOPTED}} |

When a decision becomes canonical in another document, link to it rather than maintaining a competing definition here.

## Proposed scope boundaries

- **Candidate initial scope:** {{OUTCOMES_UNDER_CONSIDERATION}}
- **Candidate later scope:** {{DEFERRED_OPTIONS}}
- **Proposed exclusions:** {{EXCLUSIONS_AND_RATIONALE}}
- **Not yet approved:** {{MATERIAL_CHOICES_PENDING_CONFIRMATION}}

## Risks, contradictions, and open questions

| ID | Decision question / risk | Impact and uncertainty | Meaningful options, if any | Provisional recommendation and rationale, if justified | Answer / evidence | Owner and validation path | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Q-001 | {{SINGLE_DECISION_OR_UNCERTAINTY}} | {{RISK_AND_UNCERTAINTY}} | {{OPTIONS_OR_OPEN_ENDED}} | {{RECOMMENDATION_RATIONALE_OR_NOT_YET_JUSTIFIED}} | {{RESPONSE_OR_UNANSWERED}} | {{OWNER_AND_NEXT_STEP}} | open / investigating / resolved / deferred |

## Decision dependencies and blockers

| Decision ID | Depends on | Blocker / impact | Status | Owner or validation action |
| --- | --- | --- | --- | --- |
| Q-001 | {{PREREQUISITE_IDS_OR_NONE}} | {{WHY_THIS_GATES_A_DECISION_OR_NONE}} | blocked / ready / resolved / deferred | {{OWNER_AND_NEXT_STEP}} |

Resolve upstream blockers before asking downstream questions. Identify cycles and uncertain prerequisites; ask together only questions with no unresolved shared prerequisite.

## Current question batch and readiness

- **Decision-readiness status:** {{STATUS_WITH_REASON}}
- **Most consequential unresolved issues:** {{BLOCKERS}}
- **Current batch (up to 3–6 unblocked, independently answerable question IDs; fewer when sufficient):** {{QUESTION_IDS_FROM_REGISTER}}
- **Answers incorporated and new questions derived from:** {{LAST_USER_RESPONSE_OR_UNANSWERED}}
- **Next validation or experiments:** {{VALIDATION_ACTIONS}}
- **Gap audit:** {{ALL_AXES_SCREENED_APPLICABLE_HIGH_IMPACT_GAPS_RESOLVED_OR_ACCEPTED_AND_EXCLUSIONS_JUSTIFIED}}
- **Consensus proposal and outstanding objections:** {{SCOPE_BOUNDARIES_AND_CONTRADICTIONS}}
- **Explicitly confirmed by decision owner:** {{YES_NO_AND_DATE}}

Discovery is not a guarantee of full knowledge. Keep uncertainty explicit and reopen assessments when evidence or scope changes.
