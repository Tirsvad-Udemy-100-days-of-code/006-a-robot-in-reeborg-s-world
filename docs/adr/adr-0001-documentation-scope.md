# ADR-0001: Documentation scope of a prototype

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0001 |
| CrossReference | [BC-001], [PP-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S02 | Initial version; reviewed in RC-009, autonomous, not independent | [422cb5e] |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.


Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The project is a prototype of one use case: a right-wall-following solver of about 300 lines of code, no persisted data and no network. The framework's catalog offers further artifact types (KPI, BMC, BPMN, RA, OC, SD, DCD, ERD, TP, AD). The create-project skill requires a recorded reason for every skipped step. The constraints of [BC-001] limit the effort to about one week, and the plan [PP-001] has three gateways.

Options considered:

1. Write every type of the catalog for the one use case. It gives the most traceability, but several documents would have no content (an ERD for no stored data, an OC for no state-changing system operation).
2. Write only the types the use case touches and skip the rest with this record. It fits the effort and keeps every written document meaningful.

## Decision

Option 2: the project skips KPI, BMC, BPMN, RA, OC, SD, DCD, ERD, TP and AD. It writes the baseline (BC, SA, PP, MIL), DICT, GOV, TM and, for the one use case, US, UCD, UC, DM and SSD.

## Consequences

**Positive:**

- Every document that exists has content and is reviewed.
- The plan fits the one-week constraint.

**Negative:**

- There is no formal design class diagram or test plan; the code review and the tests carry that evidence.
- A second use case would need a new decision on the skipped types.

## Affected Artifacts

- [BC-001] — the scope and the success criteria assume no KPI or process model
- [PP-001] — the gateways schedule only the written types

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[422cb5e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/006-a-robot-in-reeborg-s-world/commit/422cb5ea48b5e16adbc3ad74902614f5de08c22a
