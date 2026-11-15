# G2 Use Case and Code Review

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S02 | Initial version; reviewed in RC-005, autonomous, not independent | pending |

---

## Purpose

Decide whether the existing solver, the simulator and the tests are specified by an accepted use case and reviewed against the Python checklist, so that the code is accepted as the exercise solution and not only as something that happens to work.

## Deliverable

The user story, the use case diagram, the use case "Solve the maze", the domain model and the system sequence diagram, each accepted; a code review record against `QC-PY-001` with verdict `Go`; a test proving that the pasteable Reeborg script and the tested function behave the same.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | US-001, UCD-001, UC-001, DM-001 and SSD-001 each have a review record with verdict `Go` and an `Accepted` row | All five `Accepted` | Any still `Proposed` |
| 2 | The code review record against `QC-PY-001` has verdict `Go` | Verdict `Go` | `Go-with-conditions` or `No-Go` |
| 3 | `python -m pytest` passes with no failure | All tests pass, at least 316 | Any failure |
| 4 | The script-equivalence test passes for every free start of the three worlds | Test passes for all starts | Any start fails |
| 5 | Every commit under `src/` or `tests/` has a `Task: MIL-002#N` trailer | All commits carry one | A commit without a trailer |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | The baseline, the dictionary and the governance must be accepted before design documents and code changes |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1 and SC-1 | UC-001 and the tests |
| O2 and SC-2 | The script-equivalence test and the code review |
| O4 and SC-5 | The code review record |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S02 |

## Target Date

2026-11-19 — inside the Business Case constraint of 2026-11-15 to 2026-11-22.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write the user story and the use case diagram | US-001: as a learner (S01), I want the robot to reach the goal from any start, so that I pass the exercise. UCD-001 shows the learner and the one use case, with its priority (Must, from the scheme Must, Should, Could, Won't now). Review both against `QC-US-001` and `QC-UCD-001`. | Yes | US-001 |
| 2 | Write the use case Solve the maze | UC-001 in `docs/use-cases/uc-001/uc.md`, casual format: the learner starts the robot at a random cell and heading, and the robot follows the right wall to the goal. Review against `QC-UC-001`. | Yes | UC-001 |
| 3 | Write the domain model | DM-001 holds the concepts Learner, Exercise, Maze, Robot, Wall and Goal with the dictionary's terms. Review against `QC-DM-001`. | Yes | UC-001 |
| 4 | Write the system sequence diagram | SSD-001 shows the learner starting the robot and the robot's responses for UC-001. Check the diagram with `render-diagrams.sh` and review against `QC-SSD-001`. | Yes | UC-001 |
| 5 | Review the existing code against the Python checklist | Review `src/reeborg_maze/` and `tests/` against `QC-PY-001` and the Python conventions. Write one review record with a verdict and an action item for each failed criterion. | No | UC-001 |
| 6 | Resolve the code review findings | Fix every failed criterion of the code review in `src/` and `tests/`, one commit per cause with the `Task` trailer, then re-review until the verdict is `Go`. If the review finds nothing, the task closes with that statement. | No | UC-001 |
| 7 | Test that the Reeborg script behaves like the solver | Add a test that runs `reeborg_script.py` against the simulated robot for every free start and heading of the three worlds and checks that the robot reaches the goal, so the two copies of the algorithm cannot drift apart. | No | UC-001 |

---

[BC-001]: ../business-case.md
