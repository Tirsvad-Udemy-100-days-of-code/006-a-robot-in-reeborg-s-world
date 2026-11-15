# Traceability Matrix: Reeborg Maze

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | S01 (Product Owner) | Initial version, G1 state; reviewed in the Product Owner's plan acceptance, autonomous, not independent | pending |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's cross-artifact traceability success criterion is measurable. A row is added or updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | Business Case | en | education | - | [SA-001], [PP-001] | [RC-001] |
| [SA-001] | Stakeholder Analysis | en | education | [BC-001] | [BC-001], [GOV-001] | [RC-002] |
| [PP-001] | Project Plan | en | education | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003] | [RC-003] |
| [MIL-001] | Milestone | en | education | [PP-001], [BC-001] | [MIL-002] | [RC-004] |
| [MIL-002] | Milestone | en | education | [MIL-001], [BC-001] | [MIL-003] | [RC-005] |
| [MIL-003] | Milestone | en | education | [MIL-002], [BC-001] | - | [RC-006] |
| [DICT-001] | Domain Dictionary | en | education | [BC-001] | - | [RC-007] |
| [GOV-001] | Governance | en | education | [BC-001], [SA-001] | [TM-001] | [RC-008] |
| [ADR-0001] | Architecture Decision Record | - | - | [BC-001] | [PP-001] | [RC-009] |
| [TM-001] | Traceability Matrix | - | - | [BC-001] | - | none (no checklist) |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | none yet (UC-001 in MIL-002) | - | - | Gap |
| CN-002 | none yet (script-equivalence test in MIL-002) | - | - | Gap |
| CN-003 | [BC-001], [GOV-001] | [ADR-0001] | - | Covered |
| CN-004 | [GOV-001] | - | - | Covered |
| CN-005 | [GOV-001] | - | - | Covered |
| CN-006 | none yet (code review in MIL-002) | - | - | Gap |
| CN-007 | none yet (code review in MIL-002) | - | - | Gap |
| CN-008 | none yet (wiki in MIL-003) | - | - | Gap |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| 1 | none | None found | - | - | - |

---

[ADR-0001]: ../adr/adr-0001-documentation-scope.md
[BC-001]: ../business-case.md
[DICT-001]: ../dictionary.md
[GOV-001]: ./governance.md
[MIL-001]: ../milestones/mil-001-baseline.md
[MIL-002]: ../milestones/mil-002-use-case-and-code.md
[MIL-003]: ../milestones/mil-003-wiki-and-handover.md
[PP-001]: ../project-plan.md
[RC-001]: ./reviews/reviews\rc-001-business-case.md
[RC-002]: ./reviews/reviews\rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/reviews\rc-003-project-plan.md
[RC-004]: ./reviews/reviews\rc-004-mil-001-baseline.md
[RC-005]: ./reviews/reviews\rc-005-mil-002-use-case-and-code.md
[RC-006]: ./reviews/reviews\rc-006-mil-003-wiki-and-handover.md
[RC-007]: ./reviews/reviews\rc-007-dictionary.md
[RC-008]: ./reviews/reviews\rc-008-governance.md
[RC-009]: ./reviews/reviews\rc-009-adr-0001.md
[SA-001]: ../stakeholder-analysis.md
[TM-001]: ./traceability-matrix.md
