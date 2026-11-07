# Discovery coverage and scenario lenses

This is an **interrogation map**, not a list of mandatory features or assumed facts. Examine applicability for every axis; mark `not_applicable` only with a reason. Ask follow-up questions and extend the map when the idea reveals new actors, risks, or incentives. No domain, platform, geography, vendor, or technology is assumed.

## Dimensions to interrogate

| Axis | Explore and challenge |
| --- | --- |
| Problem and opportunity | Root cause, current alternatives, severity, frequency, consequence of inaction, necessity of a software solution |
| Outcomes and measurement | Who benefits, desired change, success/failure metrics, leading signals, counter-metrics, instrumentation |
| Users, actors, and stakeholders | Distinct needs, authority, incentives, skill levels, access, underserved groups, indirect or conflicting stakeholders |
| Personas and research | Behavioral differences, context, evidence quality, recruitment bias, proxy users, validation gaps |
| Jobs, journeys, and scope | Entry/exit conditions, goals, dependencies, role permissions, critical paths, exclusions, life cycle, feature interactions |
| Experience and accessibility | Discoverability, comprehension, error prevention, assistive access, language and localization, trust and transparency |
| Market and positioning | Alternatives, substitutes, competitive differentiation, urgency, demand evidence, distribution, defensibility |
| Business model and adoption | Pricing hypotheses, willingness to pay, onboarding, conversion, retention, switching, channel viability |
| Economics and ROI | Build/buy cost, recurring costs, operating burden, support, cost of acquisition, value realized, break-even, sensitivities, opportunity cost |
| Data and information | Sources, quality, lineage, classification, ownership, correctness, import/export, retention, portability, deletion |
| Security and trust | Threats, trust boundaries, identity, authorization, misuse, fraud, secrets, auditing, incident handling |
| Privacy, legal, and ethics | Applicable jurisdiction and contracts, lawful basis, notices/consent as applicable, sensitive handling, rights, accountability, fairness, harm |
| Technical feasibility | Architectural options, integration contracts, data models, constraints, interoperability, maintenance, testability, reversibility |
| Infrastructure and operations | Environment, deployment, capacity, cost, availability, observability, recovery, support ownership, vendor dependencies |
| Reliability and performance | Latency, throughput, limits, degradation, resilience, consistency, retry behavior, backup and restoration |
| Delivery and governance | Skills, team capacity, dependencies, procurement, milestones, rollout, approvals, decision rights, change control |
| Measurement and learning | Experiment design, monitoring of assumptions, feedback, quality gates, stop/pivot/scale criteria |
| Long-term lifecycle | Updates, migrations, compatibility, ownership transfer, deprecation, end-of-life, data exit and vendor lock-in |

## Scenario expansion

For every important user journey, system interface, and state transition, deliberately ask:

- **Nominal and alternate:** What is the intended path? Which valid sequence variations or actor differences change it?
- **Input and state:** Missing, malformed, contradictory, stale, duplicate, out-of-order, boundary, or forbidden states?
- **Time and concurrency:** Race conditions, repeated requests, ordering, timeouts, clock differences, partial progress, idempotency?
- **Dependencies and connectivity:** Unavailability, degraded service, intermittent access, third-party changes, incompatible versions?
- **Trust and misuse:** Incorrect permissions, unintended disclosure, abuse, fraud, manipulation, hostile inputs, escalated privileges?
- **Human factors:** Misunderstanding, accidental action, interruption, accessibility barriers, wrong assumptions, recovery and undo?
- **Data lifecycle:** Provenance, corruption, updates, synchronization, retention, export, removal, access revocation?
- **Operations and scale:** Bursts, saturation, cost spikes, loss of observability, rollback, incident response, disaster recovery?
- **Change over time:** New segments, new rules, migrations, changed objectives, expansion and withdrawal?

For each applicable scenario, capture: actor/context, trigger or precondition, expected/acceptable outcome, failure or harm, recovery/detection, severity, and validation. **Do not** manufacture low-value cases just to hit a count. Prioritize high-impact, likely, difficult-to-reverse, and poorly evidenced cases.

## Deeper probes

- What assumption would invalidate the entire proposal?
- What does the user do now, and why is it insufficient?
- Who benefits, who pays, who bears risk, and who may resist?
- What could make adoption fail even if the implementation works?
- Which failure would be hardest to discover, reverse, or explain?
- What would a lower-cost or no-build alternative accomplish?
- What new dependency, cost, liability, or operational obligation does this introduce?
- What can be safely postponed without undermining the smallest useful outcome?
- Which decision must be researched rather than answered through intuition?
- What would cause us to stop, pivot, reduce scope, or retire the solution?

Maintain explicit `unknown` and `not_applicable` outcomes. Discovery is complete only to the depth required for a decision; absence of additional questions is never proof of exhaustive certainty.
