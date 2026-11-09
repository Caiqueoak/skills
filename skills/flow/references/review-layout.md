# Review-first Markdown artifacts

This contract applies to all generated or maintained `_flow/` Markdown artifacts, including the discovery draft, product/technical baselines, progress tracker, spec requirements/design/tasks, and optional spec-local notes. Keep each artifact canonical for its own decisions, rather than creating a parallel approval registry.

## 1. Readable, modular structure

- Start with the document title and one short purpose/status line. Immediately follow with `## Index`; put the actual content after the index.
- Divide content into cohesive, named `##` sections and small `###` subsections where useful. Group related atomic items; split overly long or unrelated sections. Omit irrelevant sections rather than adding filler.
- Present each reviewable fact, scope choice, rule, decision, interface, risk, question, or task proposal as an individually identifiable item with a stable ID. Prefer short labels, bullets, and compact tables; keep detailed rationale below its item rather than embedding lengthy paragraphs in navigation.
- Preserve the canonical home for each fact. An index only links to content and mirrors its marker; it must not restate or duplicate requirements or decisions.

## 2. The visible pending-review marker

Use the literal, searchable Markdown badge `🆕 **NEW**` **beside each atomic item** whose current content has not been explicitly approved by the user/reviewer. Do not use a generic document-wide NEW badge as a substitute.

- New proposed items and newly created artifacts start with their applicable individual items marked `🆕 **NEW**`, even if an item is internally described as proposed, assumed, or open.
- If an approved item changes *materially*, mark that particular item NEW again. Mark newly added subitems independently; leave unrelated approved items unmarked. Editorial reformatting and link fixes do not invalidate approval.
- Remove NEW **only after an explicit approval of that item or an unambiguous approved group**. Approval scope must be clear; do not infer approval from silence, a passing test, code merge, completion, or a discovery status label alone.
- Keep workflow state (e.g. proposed, confirmed, open, blocked, done) separate from review state. `NEW` means **needs approval**, not necessarily recently written or not implemented.
- A resolved/superseded item retains its ID for history when required. Do not silently delete its rationale, recycle its ID, or re-mark long-approved history merely because a template changed.
- On first adopting this scheme in an existing project, honor known approvals and mark only clearly pending/new or materially revised items. If approval history is uncertain, surface the uncertainty instead of marking the entire legacy baseline NEW.

## 3. Navigable index with mirrored badges

The `## Index` contains:
1. Every substantive top-level section in document order, as a link to its Markdown heading.
2. Nested links to **individual reviewable items** with stable IDs and short descriptive labels; put `🆕 **NEW**` next to each pending item's link.
3. `🆕 **NEW**` on a *section index entry* if and only if at least one item within that section is pending approval. This aggregate badge is for scanning; individual item badges are still mandatory.

Use stable explicit item anchors so titles or badges can change without breaking links. Example **of generic structure only**:

```markdown
## Index
- [Decisions](#decisions) — 🆕 **NEW**
  - [D001 — Boundary](#d001) — 🆕 **NEW**
  - [D002 — Constraint](#d002)
- [Related documents](#related-documents)

## Decisions
<a id="d001"></a>
### D001 — Boundary 🆕 **NEW**
{{DECISION_PENDING_APPROVAL}}

<a id="d002"></a>
### D002 — Constraint
{{PREVIOUSLY_APPROVED_DECISION}}
```

For compact bullets/table rows, place the anchor and NEW badge directly in the owning bullet/cell; do not force every item into its own `###` heading. Use unique anchor IDs **within each file**; keep existing W###, R##, AC##, T### and decision IDs stable. New content needing an ID should get a clear, document-local prefix, without renumbering existing items.

## 4. Keeping the index and approvals correct

On **every** artifact edit:
1. Read the existing artifact and preserve approved content, IDs, anchors, and links.
2. Edit the smallest owning item; distinguish pending approval from implementation state.
3. Synchronize the index's section/item links and **exact NEW markers** with the body. Every pending item must be discoverable from the index; no stale index links or badges.
4. Verify every index anchor resolves, no ID collisions, sections follow a logical order, and no redundant copies of canonical content were introduced.
5. Summarize **only pending items/IDs and approval questions** when requesting review; point to the index so the reviewer can skip approved content.

Templates are starting points, not mandates for irrelevant headings. Prefer concise, stable Markdown over custom rendering or elaborate metadata.
