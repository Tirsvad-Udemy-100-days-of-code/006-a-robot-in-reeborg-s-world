# Artifact Registry

This project's artifact state. Types, short names and `CrossReference
Candidates` come from the framework catalog
(`framework/registry/artifact-catalog.md`); this file only records where
each document lives in *this* project and the next version to use.

| Short Name | Artifact Type | Primary File | Next Available Version |
| --- | --- | --- | --- |
| BC | Business Case | docs/business-case.md | 002 |
| SA | Stakeholder Analysis | docs/stakeholder-analysis.md | 002 |
| PP | Project Plan | docs/project-plan.md | 002 |
| MIL | Milestone / Gateway | docs/milestones/*.md | 004 |
| ADR | Architecture Decision Record | docs/adr/adr-NNNN-*.md | 0002 |
| UCD | Use Case Diagram | docs/use-case-diagram.md | 002 |
| US | User Story | docs/user-stories.md | 002 |
| UC | Use Case (Brief/Casual/Fully Dressed) | docs/use-cases/uc-*/uc.md | 002 |
| DM | Domain Model | docs/domain-model.md | 002 |
| SSD | System Sequence Diagram | docs/use-cases/uc-*/ssd.md | 002 |
| DICT | Domain Dictionary (PO and IT terms) | docs/dictionary.md | 002 |
| RC | SQA Review Record | docs/sqa/reviews/rc-*.md | 023 |
| TM | Traceability Matrix | docs/sqa/traceability-matrix.md | 002 |
| GOV | Governance / ARB Workflow | docs/sqa/governance.md | 002 |

## Languages

The PO language and domain were given by the Product Owner in the first prompt
of the autonomous run (session 001): English, education. An artifact of a type
marked "Written in the PO language" exists once, in that language, under its
normal name (`business-case.md`); the `artifact` skill ("One file per
artifact") has the rule.

| Setting | Value |
| --- | --- |
| PO language | English (en) |
| PO domain | education |
| High-level register | IT Executive English |
| Technical register | IT Professional English |
| Wiki languages | en, da, ms (English is the PO language; Danish and Malay are added on top by the Product Owner; `framework/process/wiki.md`) |

Every artifact of a type marked "Yes" below states its language and domain in
its `Language` and `Domain` Metadata rows; `new-artifact.sh` fills them from
`PO language` and `PO domain`. `Language` is a BCP 47 code (`da`, `en`).
`Domain` is a value from this list; add a row to introduce a domain, so a
reviewer can see at once which professional vocabulary a document uses.

| Domain | Meaning |
| --- | --- |
| it | Software and IT |
| education | Teaching and learning, here a programming course exercise |

| Artifact types | Register | Written in the PO language |
| --- | --- | --- |
| BC, KPI, PP, MIL | IT Executive English | Yes |
| SA, BMC, BPMN, UCD, US, UC, SSD, DM, RA, GOV, DICT | IT Professional English | Yes |
| OC, SD, DCD, ERD, TP, AD, ADR, TM, RC, QC, source code | IT Professional English | No |

## Tools

Settings of the tools the framework's scripts use. Each organisation sets its own.

| Setting | Value |
| --- | --- |
| PlantUML server | <base URL of your PlantUML server, e.g. https://plantuml.example.com> |

`framework/scripts/render-diagrams.sh` reads `PlantUML server` when neither `--server`
nor the environment variable `PLANTUML_URL` is given. The diagram text is sent to that
server, so name one your organisation trusts.

## Notes

- "Next Available Version" is the zero-padded (3-digit) version to use the
  *next* time a new document of that type is created. Increment it only when
  a brand-new document is created, not when an existing document's
  `## Version History` gets a row.
- `ADR` uses 4 digits (`0001`); `RC` is sequential across all artifact types.
