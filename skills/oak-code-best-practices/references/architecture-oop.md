# Architecture and object-oriented programming

Start from observable requirements and evidence; do not assume a platform, domain, framework, or favored architecture. A diagram alone does not establish a viable design.

## Architecture decision procedure

1. Identify users/actors, capabilities, quality attributes, constraints, failure costs, change pressure, and assumptions.
2. Trace key operations through interfaces, data ownership, state transitions, side effects, trust boundaries, and recovery.
3. Define cohesive components and module boundaries, dependency direction, contracts, and permitted communication. Avoid cross-boundary knowledge, cycles, global shared state, and unnecessary layers.
4. Compare viable alternatives including the simpler design; evaluate reliability, evolvability, performance, cognitive/operational cost, testability, scalability when justified, and reversibility.
5. Address consistency and concurrency, resource lifecycles, migration, backward compatibility, deployment, configuration, observability, security, and cost where applicable.
6. Document decision, alternatives, constraints, tradeoffs, open risks, and validation strategy using existing project conventions. Do not create a competing source of truth.
7. Verify architecture with relevant dependency checks, contract/integration tests, operability checks, or other practical fitness functions when warranted.

## OOP design lenses

- **Encapsulation:** object state and invariants have an owner; callers cannot easily violate constraints through exposed internals.
- **Abstraction:** a type or interface represents meaningful behavior. Do not create wrappers and interfaces for unproven hypothetical use.
- **Polymorphism:** alternative implementations preserve the same observable contract, error semantics, preconditions, and postconditions.
- **Inheritance:** require genuine substitutability; avoid fragile base classes, deep hierarchies, and surprising overrides. Prefer composition when behavior is assembled.
- **Identity vs value:** decide equality, mutation, persistence, and lifecycle semantics intentionally. Prefer values and pure transformations when stateful identity is unnecessary.
- **Responsibility and cohesion:** operations that enforce an invariant belong near its owner when that simplifies reasoning; avoid both state-only objects with scattered rules and overly broad objects.
- **Collaboration:** favor intention-revealing APIs, small contracts, explicit required dependencies, and predictable construction and cleanup.
- **SOLID:** SRP, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion are tradeoff heuristics, not mandates for classes, interfaces, or patterns.
- **Patterns and architecture styles:** use only when they resolve demonstrated variability, lifecycle, complexity, or dependency problems. Compare against direct code, composition, and functional alternatives.

## OOP and functional programming

These approaches can coexist. Prefer deterministic pure functions for stateless transformations; objects can own lifecycle, state transitions, collaborators, and invariants. Expose side effects deliberately. Never force a computation into a class or a functional pipeline when the other form is clearer.

## Architecture assessment output

Provide **drivers and assumptions**, **proposed structure and responsibility boundaries**, **interfaces and data ownership**, **alternatives and complexity ROI**, **OOP/state decisions**, **quality and security risks**, **test/operational validation**, and **remaining questions**. Mark unresolved material assumptions rather than inventing constraints.
