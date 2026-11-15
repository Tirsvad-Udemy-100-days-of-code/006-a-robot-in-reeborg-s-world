# User Stories: Reeborg Maze

## Metadata
| Key | Value |
| --- | --- |
| ID | US-001 |
| CrossReference | [UCD-001], [UC-001], [BC-001], [MIL-001], [MIL-002], [MIL-003] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S02 | Initial version; reviewed in RC-012, autonomous, not independent | pending |

---

## Purpose and Scope

MoSCoW stands for Must, Should, Could, Won't now, the priority scheme used below. The stories of the epic "Pass the day 6 exercise", which is gateway [MIL-002]. Gateways [MIL-001] and [MIL-003] deliver documents and have no user story.

## Story List

### US-001.01 — Reach the goal from any start

**As a** learner (the actor Learner of [UCD-001]), **I want** the robot to reach the goal from any start position and heading, **so that** I pass the exercise.

**Acceptance Criteria**

- Given any free cell of the maze and any of the four headings, when the learner starts the robot, then the robot stops on the goal.
- Given the three provided mazes, when every free cell and every heading is tried, then no start fails.

| Traces to | Size | INVEST exceptions | Priority (MoSCoW) | Reason |
| --- | --- | --- | --- | --- |
| [UC-001] | fits one iteration | none | Must | It is the exercise itself; the riskiest assumption is that the method works from every start (objective O1 of [BC-001]) |

### US-001.02 — Check the solution without the website

**As a** learner (the actor Learner of [UCD-001]), **I want** to run the same solution offline and see the robot move, **so that** I can check every start quickly.

**Acceptance Criteria**

- Given a maze file and a start position, when the learner runs the solution offline, then the robot's path ends on the goal and the result is shown.
- Given the same maze and start, when the solution runs in Reeborg's world and offline, then both end on the goal.

| Traces to | Size | INVEST exceptions | Priority (MoSCoW) | Reason |
| --- | --- | --- | --- | --- |
| [UC-001] | fits one iteration | Not fully independent: it needs US-001.01 first | Should | It makes the proof of US-001.01 repeatable (objective O2 of [BC-001]) |

## INVEST Check

Both stories are Independent of the other gateways, Negotiable in how the result is shown, Valuable to the learner, Estimable from the existing code, Small enough for one iteration and Testable by the acceptance criteria. The one exception, US-001.02 needing US-001.01, is stated above.

---
[UCD-001]: ./use-case-diagram.md
[UC-001]: ./use-cases/uc-001/uc.md
[BC-001]: ./business-case.md
[MIL-001]: ./milestones/mil-001-baseline.md
[MIL-002]: ./milestones/mil-002-use-case-and-code.md
[MIL-003]: ./milestones/mil-003-wiki-and-handover.md
