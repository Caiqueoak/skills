# Principles, limits, and tradeoffs

This reference is a **judgment guide**, not a list of transformations to apply indiscriminately. Start with correctness, real requirements, and demonstrated costs. Prefer the simplest local solution that protects important invariants.

## Understand what before how

- Establish the observable outcome, ownership, input/output contract, invariants, and failure conditions before choosing an algorithm, abstraction, or library.
- Prefer intention-revealing expressions, names, and interfaces over clever control flow. A reader should first understand the purpose, then inspect the mechanism only when needed.
- Prefer explicit, predictable data flow. Avoid hidden mutations, surprise effects, and implicit dependencies.
- Make common behavior easy to follow; expose exceptional paths without burying them in unnecessary indirection.

## Simplicity, duplication, and complexity economics

| Principle | Prefer | Avoid / qualify |
| --- | --- | --- |
| KISS | The smallest design satisfying current constraints | Complexity motivated only by theoretical elegance |
| YAGNI | Implement demonstrated needs and preserve reasonable evolvability | Speculative extension points, compatibility layers, general-purpose frameworks |
| DRY | One authoritative definition of a shared rule or invariant | Extracting superficially similar code with different reasons to change |
| SSOT | One owner of each rule, state, decision, or contract | Independent copies requiring synchronization |
| Complexity ROI | Compare benefit to implementation, cognitive, testing, migration, runtime, and operational costs | Abstraction justified solely by fewer lines or imagined reuse |
| Locality | Keep related data and behavior close to their owner and typical change path | Distant navigation, scattered configuration, global coupling, or premature shared utilities |

**Complexity test:** What concrete requirement does the extra layer serve? What simpler alternative exists? What failure or change cost does it reduce? What ongoing cost does it introduce? Is there evidence the benefit exceeds the cost? If not, defer the complexity.

**Tradeoff:** DRY can conflict with locality; SRP can conflict with needless fragmentation; flexibility can conflict with comprehensibility. Prefer explicit ownership and independent reasons to change over mechanical rules.

## Responsibility and dependency design

- **Single Responsibility:** one cohesive reason to change; responsibilities should reflect domain or behavior ownership rather than arbitrary file-size limits.
- **Open/Closed:** enable extension when a real family of change requires it; direct changes can be simpler than premature plugin points.
- **Liskov Substitution:** substitutes preserve observable promises, invariants, error behavior, and expectations.
- **Interface Segregation:** dependencies expose only capabilities consumers need; avoid bloated public interfaces.
- **Dependency Inversion:** keep important policy insulated from volatile detail where that boundary pays for itself; do not create interfaces without a useful seam.
- **High cohesion / low coupling:** keep logically related behavior together and minimize cross-boundary knowledge and synchronized modifications.
- **Composition over inheritance:** prefer assembled behavior and delegation when inheritance creates rigid coupling; inheritance remains valid when substitutability is real.
- **Tell Don't Ask / Law of Demeter:** place operations with the data and knowledge that own them; avoid exposing internal object navigation and orchestration unnecessarily.
- **Separation of concerns:** distinguish policies, mechanisms, and side effects when it improves reasoning or testing. Preserve vertical, end-to-end cohesion rather than mandatory horizontal layering.
- **Sensible abstraction:** extract around stable concepts and genuine variation; avoid wrappers, indirection, circular dependencies, and generic base types that only move code.

## Functional and declarative thinking

- Start with the *meaning* of the transformation before its *mechanism*. Prefer code that communicates outcomes and constraints rather than operational ceremony.
- Prefer **pure functions** for deterministic transformations when practical: explicit input, explicit output, and no externally observable side effects.
- Favor **immutability** and controlled state transitions when they improve correctness, concurrent reasoning, and testability; permit mutation where it is clearer or necessary.
- Push unavoidable **side effects to explicit boundaries** and keep them visible and independently testable; do not hide network, disk, time, randomness, or shared-state access.
- Use transformations and composition when they improve clarity, but avoid nested chains, opaque callbacks, and excessive point-free or clever expressions.
- Prefer explicit error outcomes and well-defined state transitions over ambiguous sentinel states or broad exception suppression.
- Do not mandate functional programming when a different idiom is clearer in the actual language and codebase.

## Contracts, state, and failure handling

- Preserve public contracts and backward compatibility unless authorized to change them.
- Favor strong types, small meaningful value representations, and validation at the point where trust changes.
- Make illegal states difficult to represent where cost is justified; document invariants and ownership.
- Make concurrency and resource lifecycles explicit when relevant. Protect against unintended repeated work, stale state, partial failure, and ordering assumptions.
- Bound and justify timeouts, retries, backoff, cancellation, and idempotency. These are context-dependent reliability tools, not automatic additions.
- Fail visibly with useful context; recover only where a clear policy and safe path exist. Do not suppress or silently reinterpret failures.
- Use least privilege, careful data handling, safe defaults, and clear trust boundaries. Security requirements override preferences for fewer lines.

## Verification and delivery

- Test **observable behavior, invariants, and meaningful boundaries**, not incidental implementation details.
- Prefer a test that fails for the right reason before implementing a behavioral change; implement the minimum and refactor without changing the contract.
- Balance unit, integration, contract, and end-to-end evidence according to risk and system boundaries. Tests should be reliable, isolated, deterministic where possible, and quick enough to support feedback.
- Include boundary, invalid-state, error, and recovery tests when they protect meaningful risk; do not manufacture exhaustive tests that add no confidence.
- Preserve established project tooling. Run the checks that can actually validate the change, and report unavailable checks as such.
- Prefer reviewable, cohesive diffs and atomic commits; avoid mixing formatting churn with behavior changes.
- Keep comments focused on non-obvious *why*, constraints, and decisions rather than repeating code. Keep documentation canonical and aligned with behavior.
- Address measured performance bottlenecks and resource use; avoid premature optimization and unjustified caching or concurrency.

## Practical review lens

1. **Behavior:** Does the change satisfy the correct contract? Could it violate an invariant, safety condition, or recovery path?
2. **Clarity:** Is the purpose evident without following unnecessary indirection? Are names, interfaces, and flow understandable?
3. **Ownership:** Does one cohesive unit own each rule and state transition? Is coupling proportionate?
4. **Complexity:** Which abstraction, layer, or dependency could be removed without losing an actual requirement?
5. **Verification:** Which evidence proves important behavior and edge conditions? Were the checks actually executed?
6. **Change impact:** Are compatibility, operational costs, failure visibility, documentation, and rollback risks handled at the appropriate level?

Recommend changes only where they measurably improve correctness, clarity, testability, change cost, or essential quality attributes.
