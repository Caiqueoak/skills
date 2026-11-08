# Discovery coverage and scenario lenses

This is an **interrogation map**, not a list of mandatory features or assumed facts. Examine applicability for every axis; mark `not_applicable` only with a reason. Ask follow-up questions and extend the map when the idea reveals new actors, risks, or incentives. No domain, platform, geography, vendor, or technology is assumed.

## Adaptive depth selection

Screen every axis, but **do not ask every question**. Select depth based on user intent, uncertainty, exposure, impact, reversibility, dependencies, and existing evidence—not request length or arbitrary feature counts.

| Mode | Typical signals | Expected work |
| --- | --- | --- |
| Focused | Localized, reversible change; known users and behavior; little new data or external exposure | Confirm outcome, boundaries, relevant behaviors, acceptance signals, and one or two consequential risks; mark unrelated axes not applicable |
| Standard | Multiple workflows or actors, integrations, meaningful data, nontrivial adoption or operational decisions | Probe applicable product, user, data, technical, cost, quality, and delivery axes; examine key alternatives and failures |
| Comprehensive | Unclear product strategy, novel business model, multi-party system, sensitive or regulated data, high exposure, scale, difficult rollback, material financial or safety consequences | Deeply assess all applicable axes, dependencies, evidence, threats, lifecycle, governance, and adverse scenarios; validate material unknowns |

Escalate individual axes independently: a small-scope request with sensitive data may need deep privacy/security work while market analysis remains not applicable. De-escalate when facts already establish decisions. Never assume an axis applies just because it exists in the map.

For each axis record:
- **Applicability:** `essential` (can change the decision), `conditional` (check trigger or dependency), or `not_applicable` (explain why).
- **Depth:** `brief`, `targeted`, or `deep` for applicable axes.
- **Readiness:** `unexamined`, `investigating`, `resolved`, or `deferred`; for an excluded axis, use `not_applicable`.
- **Evidence and next step:** What is known, what would change the decision, and the owner/validation plan for material uncertainty.

Only surface a concise prioritized subset to the user. Keep the complete coverage map in the record when persistence is appropriate. Increase depth if new users, dependencies, risks, or contradictions emerge.

## Dimensions to interrogate

These are **candidate decision areas**, not mandatory product requirements. Screen each cluster; activate and deepen its dimensions only when the initiative warrants them.

| Cluster | Dimension | Decision probes |
| --- | --- | --- |
| Framing | Problem and root cause | Pain, baseline, frequency, severity, urgency, constraints, why intervention is needed |
| Framing | Desired outcomes and success | Beneficiaries, observable changes, success and stop signals, trade-offs, unintended impacts |
| Framing | Scope and boundaries | Minimal useful outcome, non-goals, dependencies, exclusions, reversible sequencing |
| People | Users, buyers, operators, stakeholders | Roles, authority, payer vs beneficiary, incentives, conflicts, underserved actors |
| People | Context and research | Behavior, environments, access, evidence strength, sampling bias, validation needs |
| People | Adoption and change management | Motivation, onboarding, migration, training, communications, switching and resistance |
| Experience | Journeys and business rules | Entry/exit states, permissions, exceptional paths, approval rules, interactions |
| Experience | UX and interaction | Comprehension, discoverability, error prevention, trust, feedback, undo, support |
| Experience | Accessibility and inclusion | Assistive technology, cognitive and physical constraints, language, localization, device constraints |
| Product | Prioritization and differentiation | Alternatives, must-have vs optional, distribution of value, feature dependencies |
| Product | Market and competitors | Substitutes, demand evidence, positioning, segments, advantage, market evolution—only if relevant |
| Business | Model and viability | Funding, pricing, buyer willingness, value capture, distribution, retention—only where applicable |
| Business | Costs and returns | Build/buy, operating and support costs, expected benefit, sensitivities, opportunity cost, budgets |
| Business | Contracts and procurement | Commercial obligations, approval processes, vendors, terms, licensing, exit costs |
| Information | Data sources and semantics | Inputs, quality, correctness, provenance, vocabulary, ownership, lineage, transformations |
| Information | Data lifecycle and governance | Storage, classification, integrity, retention, deletion, export, portability, migration |
| Information | Reporting and analytics | Decisions supported, metrics, collection method, bias, quality, privacy, auditability |
| Engineering | Technical alternatives | Build/buy/integrate, feasibility, existing constraints, complexity, maintenance, reversibility |
| Engineering | Architecture and boundaries | Components, interfaces, coupling, contracts, integration ownership, versioning |
| Engineering | External dependencies | APIs, quotas, vendor changes, availability, licensing, fallback, interoperability |
| Engineering | Quality and testing | Functional/nonfunctional acceptance, testability, automation, compatibility, regression evidence |
| Engineering | AI or automated decisions | Applicability, data provenance, model fitness, evaluation, hallucinations, bias, human oversight, cost, drift—only if relevant |
| Infrastructure | Hosting and environments | Deployment targets, environments, configuration, secrets, provisioning, sovereignty, capacity |
| Infrastructure | Performance and scalability | Latency, throughput, growth, resource budgets, hotspots, caching, cost under load |
| Infrastructure | Reliability and recovery | SLOs where needed, failure modes, consistency, queues, idempotency, backups, recovery objectives |
| Infrastructure | Observability and support | Logging, tracing, alerts, diagnostics, on-call ownership, maintenance, incident response |
| Trust | Security and abuse | Threat actors, authentication, authorization, boundaries, secret management, abuse/fraud, audit trails |
| Trust | Privacy and sensitive data | Data minimization, access, sharing, retention, rights, user expectations, consent where applicable |
| Trust | Safety, harm, and ethics | Consequential errors, manipulation, vulnerable groups, fairness, explainability, escalation |
| Trust | Legal, regulatory, and policy | Jurisdiction, sector-specific obligations, intellectual property, contractual restrictions, required reviews |
| Delivery | Team and ownership | Skills, responsibility, decision rights, maintenance ownership, capacity, dependencies |
| Delivery | Schedule and rollout | Phases, milestones, release strategy, experiments, migration, rollback, approvals |
| Delivery | Validation and learning | Evidence gaps, prototypes, usability studies, experiments, instrumentation, go/no-go criteria |
| Lifecycle | Evolution and retirement | Updates, compatibility, technical debt, handoff, deprecation, vendor exit, data disposition |
| Ecosystem | Cross-system and societal effects | Secondary stakeholders, incentives, interoperability, environmental or community effects where material |

**Trigger rules:** Public or third-party users make adoption, accessibility, support, and trust more likely relevant. New persistent data activates information lifecycle, privacy, backup, and ownership checks. External systems activate integration reliability, contracts, and vendor exits. Automated or consequential decisions activate evaluation, monitoring, safety, and override checks. Commercialization activates demand, pricing, economics, and acquisition. Shared production infrastructure activates operability, access controls, capacity, and recovery. A change confined to an established, well-understood internal workflow may need only its affected dimensions.

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

Turn new gaps into prioritized, independently answerable question batches. Offer alternative choices only if the problem genuinely admits meaningful options; qualify recommendations by evidence, tradeoffs, and assumptions. Incorporate answers, uncover their consequences, and create follow-up batches until no material gaps remain unacknowledged. Maintain explicit `unknown` and `not_applicable` outcomes; absence of additional questions is never proof of exhaustive certainty.
