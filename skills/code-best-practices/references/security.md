# Security design and review

Assess trust and privilege flows, not compliance with an arbitrary list. Review only authorized code and environments; distinguish evidenced weaknesses from hypotheses.

## Threat and control assessment

1. Identify valuable assets, sensitive data, actors, identities, privileges, entry points, dependencies, and trust boundaries.
2. Trace who can read, modify, execute, or delete across each boundary; identify plausible abuse, disclosure, integrity, availability, and supply-chain failure paths.
3. Assess exposure, impact, likelihood, existing controls, and the limits of available evidence. Do not claim exploitability without proof.
4. Recommend the smallest effective prevention, detection, and recovery controls; document residual risk and verify relevant behavior.

## Areas to inspect

- **Authentication:** identity assurance, credential management, session lifecycle, expiry, recovery and invalidation.
- **Authorization:** permission enforcement for each affected resource and side effect, separation of duties, least privilege, deny-by-default and isolation between actors.
- **Untrusted input and output:** validation and contextual encoding, injection risks, unsafe dynamic execution, parsing and deserialization, path and command boundaries, untrusted external responses.
- **Secrets:** source, build, logs, tests, diagnostics, artifacts, rotation, revocation and scoped storage. Never quote a discovered secret or credential.
- **Sensitive data and privacy:** minimization, access rules, encryption where required, retention, export, deletion, telemetry, logging and data lifecycle.
- **Dependencies and supply chain:** provenance, lock/integrity controls, vulnerability advisories, updates, maintenance risk, build artifacts and transitive trust.
- **Build, CI and release:** permissions, untrusted contributions, secret exposure, reproducibility and verification, deploy environments, configuration defaults, rollback.
- **Runtime resilience:** resource exhaustion, concurrency, retry storms, timeouts, availability degradation, abuse handling, safe failures and incident signals.
- **Cryptography:** established and correctly used primitives/libraries, appropriate key and secret lifecycle, no invented cryptographic protocols.

## Validation

Review source, configuration, effective authorization paths, relevant tests, dependencies, and available automation. Where appropriate and authorized, run security-oriented tests or scanning; assess scanner applicability and false positives. Prioritize negative authorization tests, trust-boundary validation, isolation, safe failures and redaction. Never attempt intrusive exploitation of external systems without explicit permission.

## Report

For each finding state the affected path/line or boundary, verified versus suspected status, plausible impact, confidence, minimal remediation, verification, and accepted residual risk. Do not reproduce sensitive data in the report.
