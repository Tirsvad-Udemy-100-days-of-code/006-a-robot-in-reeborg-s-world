# G3 Wiki and Handover

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S02 | Initial version; reviewed in RC-006, autonomous, not independent | [422cb5e] |

---

## Purpose

Decide whether the project can be handed to a newcomer: a published wiki in English, Danish and Malay, a README whose links all open, and a consistent set of documents that the framework's own checks accept.

## Deliverable

The wiki in `docs/wiki/` in English, Danish (`-da`) and Malay (`-ms`): Home, Getting Started, How It Works, Development and the sidebar, published on the git host, with a review record against `QC-WIKI-001`; the final README and traceability matrix; the end-of-run summary for S01.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `docs/wiki/` is flat and holds `Home.md`, `_Sidebar.md` and the other pages in English, with the same page set as `-da` and `-ms` files | Every page directly in the folder, three languages | A subfolder or a page missing in a language |
| 2 | The sidebar lists every page once and ends with the `Languages` section listing English, Dansk and Bahasa Melayu | Matches `QC-WIKI-001` criteria 1 to 6 | A dead link or a missing page |
| 3 | The published wiki shows the sidebar and every page, each link opens | Checked on the host after the merge | A link fails on the host |
| 4 | The review record against `QC-WIKI-001` has verdict `Go` | Verdict `Go` | `Go-with-conditions` or `No-Go` |
| 5 | `check-readme.sh`, `check-languages.sh`, `check-qc-tags.sh` and `check-editorconfig.sh` pass | All exit 0 | Any exits non-zero |
| 6 | Every row of `docs/sqa/traceability-matrix.md` names the latest `RC-*` of its artifact | No row without a record | A row without a record |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | The wiki describes the accepted use case and the reviewed code |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O3 and SC-3 | The wiki and the README |
| O4 and SC-4 | The traceability matrix and the consistency checks |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S02 |

## Target Date

2026-11-22 — the end date of the Business Case constraint.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write the wiki pages in English, Danish and Malay | Create `Home.md`, `Getting-Started.md`, `How-It-Works.md` and `Development.md` in the flat folder `docs/wiki/`, in English, plus the same pages as `-da` (Danish) and `-ms` (Malay) files, each starting with the language line. Describe install, run, tests and the wall-following algorithm for a newcomer. | No | BC-001 O3 |
| 2 | Write the wiki sidebar | Create `_Sidebar.md` as the framework defines it: the wiki title in bold, one list of the pages with Home first, and a `Languages` section last, with one line each for English, Dansk and Bahasa Melayu. | No | BC-001 O3 |
| 3 | Finish the README and the traceability matrix | Make every README link and appendix entry point at an existing document, and give every row of the traceability matrix its latest review record. | No | BC-001 O4 |
| 4 | Run the framework consistency checks | Run `check-readme.sh`, `check-languages.sh`, `check-qc-tags.sh`, `check-editorconfig.sh` and `check-plan.sh` and fix what they report in project files. | No | BC-001 O4 |
| 5 | Verify the published wiki and review it | After the merge, open the published wiki, check the sidebar and every link, and write the review record against `QC-WIKI-001` and `QC-LANG-001`. | No | BC-001 SC-3 |
| 6 | Write the end-of-run summary | List the merged pull requests, every review record with its verdict and mode, every stand-in decision and what was stopped on, for S01's challenge. | No | |

---

[BC-001]: ../business-case.md
[422cb5e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/006-a-robot-in-reeborg-s-world/commit/422cb5ea48b5e16adbc3ad74902614f5de08c22a
