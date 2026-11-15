# UC-001 Solve the maze

## Metadata
| Key | Value |
| --- | --- |
| ID | UC-001 |
| CrossReference | [UCD-001], [US-001], [SA-001], [DM-001], [SSD-001] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S02 | Initial version; reviewed in RC-014, autonomous, not independent | [f9581e1] |

---

**Format:** Casual

**Scope:** Reeborg Maze solution. **Level:** user-goal. **Primary actor:** Learner (as named in [UCD-001]). **Supporting actor:** Reeborg's world. **Source stories:** US-001.01 and US-001.02 in [US-001].

## Casual

The learner starts the robot at a start position in the maze: a random cell with a random heading, which the learner does not choose. The exercise is solved when the robot stops on the goal. Before the robot reaches the goal, the learner can do nothing but watch.

The robot first walks straight ahead until a wall blocks it, and then turns left, so a wall is on its right. From then on it follows the wall: when the right side is clear it turns right and moves; otherwise, when the front is clear, it moves; otherwise it turns left. This is the wall following that the course teaches. The robot stops when it stands on the goal, and the learner sees that the exercise is solved.

The learner can run the same method in two places. In Reeborg's world the website animates the robot. Offline, a copy of the maze is used and the result is shown to the learner, so the learner can try every start position in seconds.

Preconditions: the maze has a goal that is reachable along its walls, and the robot stands on a free cell. Postconditions (success guarantee): the robot stands on the goal.

Alternate flows, told informally: if the learner starts the robot already facing a wall, the first step is the left turn; if the robot starts on the goal, nothing moves. A maze with no reachable goal is outside the scope of this use case (the robot would never stop).

Business rules: the robot may use only the five questions and moves the exercise provides (move, turn left, front is clear, right is clear, at goal); a wall is never passed.

---
[UCD-001]: ../../use-case-diagram.md
[US-001]: ../../user-stories.md
[SA-001]: ../../stakeholder-analysis.md
[DM-001]: ../../domain-model.md
[SSD-001]: ./ssd.md
[f9581e1]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/006-a-robot-in-reeborg-s-world/commit/f9581e128ebea2e751df0bb20267a94301763f4b
