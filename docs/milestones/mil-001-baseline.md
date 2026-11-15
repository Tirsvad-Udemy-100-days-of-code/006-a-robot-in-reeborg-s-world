# G1 Baseline and Repository Hygiene

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001], [US-001] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S02 | Initial version; reviewed in RC-004, autonomous, not independent | [422cb5e] |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S02 | Added CrossReference to US-001; reviewed in RC-019, autonomous, not independent | [f9581e1] |

---

## Purpose

Decide whether the project has the documents and the repository hygiene it needs before any further work starts: an accepted Business Case, Stakeholder Analysis, Project Plan and milestones, the governance and dictionary that the reviews rely on, and a repository whose mounts, secrets template, licence and README are in order.

## Deliverable

The accepted baseline: Business Case, Stakeholder Analysis, Project Plan, the three milestone documents, the dictionary, the governance document, the traceability matrix and the decision record on documentation scope, each with a review record. The repository tracks `.gitmodules` and `.env.example`, `pyproject.toml` carries the licence metadata, and the README follows the framework template.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Every baseline document has a review record with verdict `Go` and an `Accepted` Version History row | Every row of the three documents and the registered baseline files is `Accepted` | Any row still `Proposed` |
| 2 | `git ls-files` lists `.gitmodules`, `framework` and `.env.example`, and `.env` is ignored | All three listed, `git check-ignore .env` succeeds | A file missing, or `.env` not ignored |
| 3 | `pyproject.toml` names `AGPL-3.0-or-later` as the licence expression and `LICENSE` as the licence file, and the installed metadata shows both | Metadata shows `License-Expression: AGPL-3.0-or-later` | Either missing |
| 4 | `bash framework/scripts/check-readme.sh` and `bash framework/scripts/check-editorconfig.sh` pass | Both exit 0 | Either exits non-zero |
| 5 | `bash framework/scripts/sync-project.sh` (dry run) lists all three milestones with their tasks | Output lists MIL-001, MIL-002 and MIL-003 | A milestone or a task row missing |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | First gateway of the project |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O4 and SC-4 | Baseline documents accepted |
| O5 and SC-6 | Licence declared and mounts tracked |
| O3 | README follows the framework template |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S02 |

## Target Date

2026-11-16 — inside the Business Case constraint of 2026-11-15 to 2026-11-22.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Track the framework mount and the secrets template | The framework mount (`.gitmodules` and the `framework` link) is staged and `.env.example` is untracked. Commit both so a clone gets the framework and a placeholder file for the credentials, and confirm that `.env` itself stays ignored. | No | BC-001 O5 |
| 2 | Add the licence metadata to pyproject.toml | `pyproject.toml` already names the licence expression and the licence file. Complete the metadata with the authors, keywords and classifiers that Python Enhancement Proposal 639 allows (no licence classifier), and check the result with the installed package metadata. | No | BC-001 SC-6 |
| 3 | Ignore the AI prompt log and record the session | The repository is public, so `docs/ai-prompts/` goes into `.gitignore`. Keep the session's prompts in `docs/ai-prompts/session-001/prompts.md` as the framework's prompt-log process says. | No | |
| 4 | Add the root editorconfig | Create `.editorconfig` from `framework/templates/editorconfig/baseline.editorconfig` and check it with `check-editorconfig.sh`. | No | |
| 5 | Review and accept the Business Case and the Stakeholder Analysis | Review BC-001 against `QC-BC-001` and `QC-LANG-001`, SA-001 against `QC-SA-001` and `QC-LANG-001`. Write one review record each and set the rows to `Accepted` on a `Go`. | No | BC-001, SA-001 |
| 6 | Write the dictionary | Record the Product Owner's education terms (learner, exercise, maze, goal, wall) next to their IT terms, in `docs/dictionary.md`, and review it against `QC-DICT-001`. | No | BC-001 |
| 7 | Write the governance and the traceability matrix | Fill the RACI of `docs/sqa/governance.md` with S01 and S02, set the escalation rules, and create `docs/sqa/traceability-matrix.md` with a row for every artifact. Review the governance against `QC-GOV-001`. | No | BC-001, SA-001 |
| 8 | Record the documentation scope in an ADR | ADR-0001 records which artifact types a prototype of one use case skips (KPI, BMC, BPMN, RA, OC, SD, DCD, ERD, TP, AD) and why, as the create-project skill requires for a skip. | No | BC-001 |
| 9 | Fill the README from the framework template | Replace the template placeholders in the README with the project's real text, restore the setup and run instructions of the previous README, and keep the appendix of project documents without the lines for AGENTS.md, the framework README and the framework changelog, because the framework is private and a reader of the public repository cannot open them. Check with `check-readme.sh`. | No | BC-001 O3 |
| 10 | Review and accept the Project Plan and the milestones | The Project Plan has no checklist, so S01 accepts it as Product Owner. Review each milestone against `QC-MIL-001` and set the rows to `Accepted` on a `Go`. | No | PP-001 |
| 11 | Install the git hooks and enable the plan gate | Run `install-git-hooks.sh --enable-plan-gate` so a commit under `src/` or `tests/` needs a `Task: MIL-NNN#N` trailer. | No | |

---

[BC-001]: ../business-case.md
[422cb5e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/006-a-robot-in-reeborg-s-world/commit/422cb5ea48b5e16adbc3ad74902614f5de08c22a
[US-001]: ../user-stories.md
[f9581e1]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/006-a-robot-in-reeborg-s-world/commit/f9581e128ebea2e751df0bb20267a94301763f4b
