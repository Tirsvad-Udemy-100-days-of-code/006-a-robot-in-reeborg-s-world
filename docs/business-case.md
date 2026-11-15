# Business Case: Reeborg Maze

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001], [UCD-001] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S02 | Initial version; reviewed in RC-001, autonomous, not independent | [422cb5e] |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S02 | Added CrossReference to UCD-001; reviewed in RC-017, autonomous, not independent | pending |

---

## Executive Summary

Day 6 of the Udemy course *100 Days of Code: The Complete Python Pro Bootcamp*
ends with a final exercise: a robot in Reeborg's world must find the way out of
a maze from a random start position and a random heading. The learner (S01)
has already built a working solution that follows the right wall. This project
turns that solution into a reviewed, documented and tested learning project
that follows the SQA and QC framework, so that the exercise is both passed and
used to practise professional delivery. The project is a prototype with a
single deliverable line: the solver, its offline simulator, its tests and the
documents that explain and govern them.

## Methodological and Standards Foundation

- Method: Larman, *Applying UML and Patterns* (use cases, domain model and
  system sequence diagram for the one use case), and the artifact chain of the
  SQA and QC framework mounted at `framework/`.
- Quality standard: ISO/IEC 25010:2023 characteristics tag every review
  criterion; the code is reviewed against `QC-PY-001` (Python).
- The Product Owner's language is English and the domain is education, as the
  artifact registry records.

## Problem Statement

1. The exercise only counts as passed when the robot reaches the goal from
   every possible start, but a single run in Reeborg's world shows only one
   start. The learner has no way to show that all starts work.
2. The learner's solution exists as code and a README, but no document says
   why it exists, who reviews it or what "done" means, so nothing proves that
   the work was planned, reviewed and accepted.
3. A newcomer who finds the repository cannot tell where to begin, because the
   repository has no wiki and its governance files are not tracked.

## Business Opportunity

A small, finished exercise is a safe place to practise the whole delivery
chain once: plan, document, review, test, publish. The same habits then carry
to the larger projects of the later course days. A public repository with a
clear README and wiki also helps other learners who struggle with the same
exercise.

## Objectives

| ID | Objective |
| --- | --- |
| O1 | The robot reaches the goal from every free start cell and every heading in the three provided worlds. |
| O2 | The same wall-following algorithm runs in Reeborg's world (the pasteable script) and offline (the tested function). |
| O3 | A newcomer can install, run and test the project from the README and the wiki alone. |
| O4 | The project follows the framework: the baseline documents are accepted with a `Go` review and the source code is reviewed against `QC-PY-001`. |
| O5 | The licence, AGPL-3.0-or-later, is declared in the package metadata and the framework mount and the secrets template are tracked in git. |

## Scope

### In Scope

- The right-wall-following solver, its Reeborg script and its offline
  simulator and terminal visualiser (existing code under `src/`).
- Tests for the solver on the three provided worlds (existing tests under
  `tests/`).
- The baseline documents (Business Case, Stakeholder Analysis, Project Plan,
  milestones), the dictionary, the governance and traceability documents and
  the single use case with its user story, use case diagram, domain model and
  system sequence diagram.
- The README, the wiki in English, Danish and Malay and the package metadata, including the
  licence.
- Tracking `.gitmodules` (the framework mount) and `.env.example` in git.

### Out of Scope

- Other Reeborg worlds and other course exercises.
- A graphical interface, a web service or a packaged release on the Python Package Index.
- Automated tests that drive Reeborg's website; the simulator stands in for it.
- Translations of the documents or the wiki; the Product Owner's language is
  English.
- Changing the framework; changes to it are proposed upstream.

## Expected Benefits

### Tangible Benefits

- A test suite that proves the solver for all 316 start combinations of the
  three provided worlds, repeatable with one command.
- A set of accepted documents and review records that show the project was
  planned and reviewed.
- A published wiki and a README that a newcomer can follow.

### Intangible Benefits

- Practice in planning, reviewing and documenting a small project end to end.
- Confidence that the exercise is passed for the right reason: the algorithm
  works from anywhere, not only from the one start the learner tried.
- A repository that other learners can read and learn from.

## Strategic Alignment

The project supports the learner's goal of becoming a professional Python
developer through the course, and the habit of delivering work that is planned,
reviewed and traceable, as the framework requires.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| SC-1 | Solver reaches the goal from every free cell and heading (O1) | 316 of 316 test cases pass | `python -m pytest` in the project |
| SC-2 | Script and function share one algorithm (O2) | 0 differences in the decision order (clear right, clear front, else turn left) found in the code review | The `RC-*` of the code review |
| SC-3 | A newcomer can follow the README and wiki (O3) | The wiki has a Home page and a sidebar, and its review has a `Go` verdict | `RC-*` against `QC-WIKI-001` |
| SC-4 | Baseline documents are accepted (O4) | Each document in the registry has an `Accepted` row with a `Go` review | `docs/artifact-registry.md` and `docs/sqa/reviews/` |
| SC-5 | Source code is reviewed (O4) | 1 `RC-*` against `QC-PY-001` with verdict `Go` | `docs/sqa/reviews/` |
| SC-6 | Licence is declared and the mounts are tracked (O5) | `pyproject.toml` names `AGPL-3.0-or-later` and the licence file; `.gitmodules` and `.env.example` are in `git ls-files` | `git ls-files` and the installed package metadata |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Reeborg's website changes its functions and the pasteable script stops working | The deliverable for the course exercise breaks | The script uses only the five built-in functions the exercise names; the offline simulator mirrors them, and a test runs the pasteable script against the simulator so the two cannot drift apart |
| The AI reviews its own work, so a defect is not found | Documents or code accepted with an unseen defect | Every review record states `Mode: autonomous, not independent`; the end-of-run summary lists each one so S01 can challenge it |
| Language review of the PO-language documents cannot be done by a stand-in | Documents stay `Go-with-conditions` and `Proposed` | S01 confirms criteria 3, 5 and 9 of `QC-LANG-001`; until then the rows stay `Proposed` |
| The git host or its token is not available | Milestones and issues cannot be published | The documents are complete without issues; publishing waits for the merge workflow or for S01 |
| A secret is committed through `.env` | Credentials leak from a public repository | `.env` stays in `.gitignore`; only the placeholder file `.env.example` is tracked |

## Assumptions

- The learner (S01) is the Product Owner and the only developer.
- No person other than S01 is available to review, so S02 is a role that the
  AI fills as stand-in in autonomous mode until S01 names a person.
- The three provided test worlds represent the maze of the course exercise.
- The repository is public on the git host, so the prompt log is not committed.

## Constraints

- Python 3.13 or newer, and no runtime dependencies.
- The Reeborg script must run in Reeborg's world without imports.
- The licence is AGPL-3.0-or-later.
- The project is a prototype: the plan has three gateways over about one week,
  from 2026-11-15 to 2026-11-22.
- Nothing is written under `src/` or `tests/` before the milestone that
  contains the task is accepted with a `Go` review.

## Cost–Benefit Assessment

The assessment is qualitative: the project has no budget and no revenue, so a
monetary return cannot be calculated. The effort is the learner's own time.

| Costs | Benefits |
| --- | --- |
| About one week of part-time effort by S01 and the AI | A proven exercise solution for all starts |
| Time to read and challenge the AI's stand-in reviews | Accepted documents and a wiki that other learners can use |
| No licence or hosting cost | Practice in the full delivery chain |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Product Owner, author and developer; wants the exercise passed and the delivery chain practised |
| S02 | Reviewer of every artifact; wants objective, checkable criteria |
| S03 | Course instructor; sets the exercise and its pass condition |
| S04 | Maintainer of Reeborg's world; the platform the script runs on |
| S05 | Other learners; read the repository and the wiki |

## Recommendation

Proceed: the solution already works, the remaining effort is small, and the
project gives the learner a safe first run of the whole delivery chain.

---

[SA-001]: ./stakeholder-analysis.md
[422cb5e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/006-a-robot-in-reeborg-s-world/commit/422cb5ea48b5e16adbc3ad74902614f5de08c22a
[UCD-001]: ./use-case-diagram.md
