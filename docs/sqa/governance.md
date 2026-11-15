# Governance: Reeborg Maze

## Metadata
| Key | Value |
| --- | --- |
| ID | GOV-001 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S02 | Initial version; reviewed in RC-008, autonomous, not independent | pending |

---

## Purpose

Defines how this project applies Quality Criteria (QC) checklists to real
artifact instances, producing Software Quality Assurance (SQA) Review Records and Go/No-Go decisions. It serves objective O4 of [BC-001], that the baseline documents and the code are reviewed, and it relies on the traceability matrix [TM-001] and the review process `framework/process/review-checklist-process.md`.

## Architecture Review Board (ARB) Review Workflow

1. **Submission** — the artifact owner submits an instance for review,
   identifying its type's QC checklist (`framework/qc/*/qc-*.md`).
2. **QC Checklist Review** — the assigned reviewer (see RACI) applies the
   checklist criterion by criterion.
3. **Review Record** — the reviewer documents the outcome as an SQA Review
   Record (`RC-*` under `docs/sqa/reviews/`).
4. **Go/No-Go Decision** — the Accountable role for the artifact category
   decides; contested or cross-cutting cases escalate to the ARB Chair.
5. **Sign-off** — on **Go**, the artifact's `## Version History` gets an
   `Accepted` row (the previous row becomes `Deprecated`). On **Go-with-conditions**, status stays `Proposed` until
   the Action Items are closed. On **No-Go**, the artifact returns to its
   owner.
6. **Traceability Update** — the reviewer updates the Traceability Matrix with the
   instance and its `RC-*` reference.

## RACI by Artifact Category

Every cell holds stakeholder IDs from [SA-001], never role names. S02 has no
named person yet; in autonomous mode the AI is the stand-in for S02, and S01
is the named alternate who may review any artifact the AI authored.

| Artifact Category | Responsible (runs the review) | Accountable (Go/No-Go owner) | Consulted | Informed |
| --- | --- | --- | --- | --- |
| Strategic (Stakeholder Analysis, Business Case) | S02 | S01 | S05 | S03 |
| Process/Business (Project Plan, Milestones/Gateways) | S02 | S01 | S05 | S03 |
| Requirements (Use Case Diagram, User Story, Use Case) | S02 | S01 | S05 | S03 |
| Modeling/Design (Domain Model, SSD, Domain Dictionary, ADR) | S02 | S01 | S05 | S03 |
| Source code (Python) and tests | S02 | S01 | S05 | S04 |
| Wiki and README | S02 | S01 | S05 | S03 |
| Governance and traceability (GOV, TM) | S02 | S01 | S05 | S03 |

Cross-cutting escalations and disputed verdicts are Accountable to the ARB
Chair (S01), overriding the category-level Accountable role.

## Escalation Rules

- A **No-Go** verdict, or any disagreement between the Responsible reviewer
  and the category's Accountable owner, escalates to the ARB Chair.
- A reviewer may not review an instance they authored. The one exception is
  autonomous mode: the AI may act as stand-in for a reviewer or an Accountable
  role, recorded as `AI as stand-in for <S-ID>` and `Mode: autonomous, not
  independent`; the Product Owner's acceptance of the plan is the
  authorisation for it.
- Repeated No-Go verdicts (2 or more) on the same artifact type trigger a
  review of the corresponding `QC-*` checklist itself.

## Blocking Findings, Risk Exceptions and Pending Criteria

- A blocking finding, a `Fail` on a Mandatory criterion or an open security finding rated High or Critical, gives `No-Go`; `Go-with-conditions` is allowed only for findings that do not block.
- A risk exception lets a blocking finding pass for a limited time. It names the finding, the owner (S01), the approver (S01, who is neither the author of the finding nor its owner when a person other than S01 exists; until then S01 decides and the record says so), an expiry date and the compensating controls. An expired exception is blocking again. The AI stand-in never approves a risk exception.
- A criterion that only a person can confirm stays `Pending` until S01 confirms it; the author's own assessment, a stand-in's or an AI author's, never closes it.

## Cadence

- Reviews are triggered per artifact instance as it is produced or revised.
- QC checklists belong to the framework and are reviewed there; this project does not change them.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[TM-001]: ./traceability-matrix.md
