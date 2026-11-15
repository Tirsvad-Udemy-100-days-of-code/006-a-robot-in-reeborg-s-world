# Domain Dictionary: Reeborg Maze

## Metadata
| Key | Value |
| --- | --- |
| ID | DICT-001 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S02 | Initial version; reviewed in RC-007, autonomous, not independent | [422cb5e] |

---

## Purpose and Scope

Maps each Product Owner (PO) term of the education domain to its professional IT term, so that the domain model and the use case speak the learner's language and the source code speaks the programmer's. PO language: English (en), as the registry's `Languages` section states.

## Dictionary

| PO term | Language | IT term | Definition | Used as PO term in | Used as IT term in |
| --- | --- | --- | --- | --- | --- |
| Exercise | en | Assignment | The task from the course that the learner must solve, here the maze of day 6. | DM, UC, US | source code |
| Goal | en | Goal condition | The place in the maze where the robot has finished its exercise. | DM, UC, US | source code |
| Learner | en | User | The person who follows the course and runs the robot. | DM, UC, US | source code |
| Maze | en | Grid world | The fixed set of walls through which the robot must find its way. | DM, UC, US | source code |
| Robot | en | Robot | The figure that the learner's program moves through the maze. | DM, UC, US | source code |
| Start position | en | Initial state | The random cell and heading from which the robot starts. | DM, UC, US | source code |
| Wall | en | Blocked edge | A barrier between two cells that the robot cannot pass. | DM, UC, US | source code |
| Wall following | en | Right-hand rule | The method of always keeping a wall on the robot's right side until the goal is reached. | DM, UC, US | source code |

## Rules

- The Domain Model, use cases and user stories use the PO term; the Operation
  Contract, Sequence Diagram, Design Class Diagram and ERD use the IT term.
- One IT term per PO term and one PO term per IT term; no synonyms.
- Rows are in ascending order of the PO term (case-insensitive, by the
  alphabet of the PO language), so a term is found without searching.

---

[BC-001]: ./business-case.md
[SA-001]: ./stakeholder-analysis.md
[422cb5e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/006-a-robot-in-reeborg-s-world/commit/422cb5ea48b5e16adbc3ad74902614f5de08c22a
