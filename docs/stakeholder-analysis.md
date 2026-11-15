# Stakeholder Analysis: Reeborg Maze

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S02 | Initial version; reviewed in RC-002, autonomous, not independent | pending |

---

## Purpose

This analysis names the people and parties who are affected by the Reeborg Maze
project or who decide about it. It gives each one a stable ID (`S01`, `S02`, ...)
that every other document uses for owners, reviewers and the RACI table. It
follows the power/interest grid: power is the ability to change what the
project delivers or whether it is accepted; interest is how much the
stakeholder cares about the result. A stakeholder is on the high side when the
level is HIGH, and on the low side when it is LOW.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Product Owner, learner and developer | Tirsvad (self-directed learning) | HIGH | HIGH | Manage Closely | Pass the exercise for every start and practise professional delivery |
| S02 | Reviewer (not yet named by S01) | Reviewer and approver of artifacts; the AI stands in for this role in autonomous mode | Tirsvad (self-directed learning) | HIGH | LOW | Keep Satisfied | Checkable criteria and an independent look at each artifact |
| S03 | Course instructor | Author of the exercise, Udemy course *100 Days of Code* | Udemy | LOW | LOW | Monitor | The exercise is solved as the course teaches it |
| S04 | Maintainer of Reeborg's world | Owner of the platform that runs the script | Reeborg's world | LOW | LOW | Monitor | The platform is used as it was designed |
| S05 | Other learners | Readers of the repository and the wiki | Public | LOW | HIGH | Keep Informed | A clear explanation they can follow and run themselves |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** S01 owns the idea, writes the prompts, reads the
  end-of-run summary and can challenge any stand-in decision.
- **Keep Satisfied (S02):** S02 decides whether an artifact is accepted, but
  reviews only when a document reaches review, so its interest is limited to
  those moments.
- **Monitor (S03, S04):** neither can change the project, and neither follows
  it. S04 matters only if the platform changes its functions; that is a risk in
  the Business Case, not a reason for closer contact.
- **Keep Informed (S05):** other learners cannot accept or reject the work, but
  they are the readers the README and the wiki are written for.

## Primary Concerns and FURPS+ Mapping

FURPS+ stands for Functionality, Usability, Reliability, Performance, Supportability, plus design, implementation, interface and physical constraints.

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | The robot reaches the goal from every start, not only the one that was tried | Functionality |
| CN-002 | S01 | The exercise result is the same in Reeborg's world and offline | Reliability |
| CN-003 | S01 | The work can be shown as planned, reviewed and accepted | Supportability |
| CN-004 | S02 | Every artifact is judged against a written checklist | Supportability |
| CN-005 | S02 | A stand-in review is never mistaken for an independent one | Reliability |
| CN-006 | S03 | The solution uses only the functions the exercise provides | Functionality |
| CN-007 | S04 | The script does not misuse the platform's functions | Constraint (design) |
| CN-008 | S05 | A newcomer can install, run and test the project from the README and the wiki | Usability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| CM-1 | Chat with S01 | Once per run, at its end | Summary of merged pull requests, review verdicts and stand-in decisions | Every gateway |
| CM-2 | Pull request on the git host | Once per gateway | Pull request description that closes its issues | Every gateway |
| CM-3 | Wiki and README | Once, at the third gateway | Published wiki and updated README | G3 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S01 wants every artifact accepted in one run, while S02 needs an independent look | S01, S02 | The AI acts as stand-in for S02, each record says `Mode: autonomous, not independent`, and the end-of-run summary lists them so S01 can challenge each one |
| S01 wants a quick prototype, while S05 needs a full explanation | S01, S05 | The wiki and README are limited to install, run, test and the algorithm; deeper design documents stay in `docs/` |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001 | O1 in [BC-001] |
| S01 | CN-002 | O2 in [BC-001] |
| S01 | CN-003 | O4 in [BC-001] |
| S02 | CN-004 | O4 in [BC-001] |
| S02 | CN-005 | O4 in [BC-001] |
| S03 | CN-006 | O2 in [BC-001] |
| S04 | CN-007 | O2 in [BC-001] |
| S05 | CN-008 | O3 in [BC-001] |

## Sign-Off

| Role | Stakeholder ID | Date | Decision |
| --- | --- | --- | --- |
| Product Owner | S01 | pending | Accepts this analysis through the acceptance of the plan |

---

[BC-001]: ./business-case.md
