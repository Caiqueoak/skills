# Test selection and low-latency execution

Use the repository's real tools and supported filtering capabilities. Aim for the shortest trustworthy feedback loop, not the fewest tests at any cost.

## 1. Discover once, then reuse

Inspect available test scripts, runner configuration, test locations, workspace/project graph, CI requirements, browser or service dependencies, and supported selectors. Determine the exact command from the project; never assume a framework, shell, CLI flag, or test runner.

Reuse this knowledge during the task unless the configuration changes. Do not repeatedly scan the repository, reinstall dependencies, or rebuild unrelated targets.

## 2. Compute the impacted test set

Start from the diff, modified public contracts, feature ownership, imports/callers, shared dependencies, and changed test configuration.

1. **Direct:** tests for the changed behavior, component, function, or package.
2. **Dependent:** affected consumers, interfaces, integration seams, and relevant regressions.
3. **Broader:** only when changes touch shared contracts, infrastructure, cross-cutting behavior, critical risks, or a mandated gate.
4. **Full suite:** at a CI/release boundary or when risk/policy specifically requires it; do not rerun it after every local edit.

A narrow diff is not always low impact: widen selection when dependency evidence warrants it. Do not exclude security- or data-critical checks merely to save time.

## 3. Run the smallest trustworthy command

- Use the runner's supported selection by exact test, file, directory, workspace, tag, changed target, or affected dependency graph.
- Prefer fast deterministic checks first, then necessary integration/component tests; use expensive end-to-end checks only for relevant behavior.
- Turn off optional coverage, reporting, rebuilds, and unrelated targets for local iterations when safe; preserve required CI gates.
- Prefer warm watch/incremental mode for interactive TDD where supported, and explicit one-shot/non-watch mode for unattended runs.
- Reuse dependencies, compiled output, and caches where safe. Do not invalidate caches or repeat startup without evidence.
- Keep concurrency within machine and resource limits; excessive parallelism can increase wall time and flakiness.
- Measure cold-start versus warm-run time where useful. Optimize disproportionate discovery, build, fixture, environment, browser, and teardown overhead before sacrificing regression confidence.

## 4. Account for runner and environment latency

A runner configured not to **auto-launch a browser** may still require an already connected browser; this does not mean tests can run browserlessly. Verify the runner's execution model. For unattended browser tests, use a supported headless launcher and a terminating run mode when available; do not leave a runner waiting indefinitely for a browser or file changes.

For any required external dependency, use the cheapest faithful test environment, explicit readiness/termination behavior, and bounded waits. Avoid arbitrary sleeps, blanket retries, and timeouts so short that they introduce flakiness. Never invent unsupported CLI flags.

## 5. Respond to failure without scope drift

- During red phase, confirm the failing assertion matches the expected missing behavior.
- After a change, investigate targeted failures before widening the suite.
- If an unrelated test fails, record the evidence and isolate its cause; do not alter an unrelated feature merely to make the suite green.
- A flaky or unavailable runner is not a passing result. Diagnose or report the limitation; do not silently skip it.
- Expand scope when an interface change or observed failure shows previously unrecognized impact.

## 6. Report evidence, not assumed coverage

Summarize the selected scope and why, commands actually executed, pass/fail/skipped outcomes, duration when measured, environment limitations, broader checks not run, and any risk requiring CI or follow-up. Distinguish local targeted validation from full-suite CI. Never claim a suite was validated when only a filtered subset ran.
