# Review: DM-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-015 |
| CrossReference | [DM-001], [QC-DM-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | S01 (Product Owner) | Initial version; reviewed in the review itself, autonomous, not independent | [f9581e1] |

---

## Artifact Under Review

- Instance reviewed: [DM-001]
- Checklist used: [QC-DM-001], [QC-LANG-001]
- Scope: full review
- Language and domain: en / education (the artifact's Metadata rows)
- Language reviewer: S01 (criteria 3, 5 and 9 of QC-LANG-001 only, confirmed in chat on 2026-11-15)
- Mode: autonomous, not independent (AI as stand-in for S02)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Uses ubiquitous/business language throughout; no technical or implementation jargon (e.g. no "table", "class", "pointer") | Pass | Concepts are in the learner's vocabulary; no class or storage terms outside the diagram syntax. |
| 2 | Multiplicities on associations are correct and complete (e.g. `1..*`, `0..1`) | Pass | Every association has a multiplicity. |
| 3 | No operation/method signatures shown — attributes and associations only | Pass | No operations. |
| 4 | Associations are named with an unambiguous reading direction | Pass | Each association has a verb reading direction. |
| 5 | Generalization/specialization used correctly, reflecting true "is-a" relationships, not misused for code reuse | N-A | No generalization; the Generalizations table says none. |
| 6 | Every concept traces to a noun phrase found in the use cases or glossary | Pass | Each concept appears as a noun in UC-001 and DICT-001. |
| 7 | Attributes are simple domain data (no foreign-key-like references or object pointers modeled as attributes) | Pass | Attributes are simple data (name, title, cell, side, heading). |
| 8 | The Purpose names the concerns (`CN-NNN`) the Domain Model answers and the stakeholders it serves, so its viewpoint is stated | Pass | The Purpose names CN-001, S01 and S05. |
| 9 | No technical solution names: only conceptual classes of the Product Owner's world, never a file, an environment variable, a setting source, a database, a table, an API, a service, a cache or any other mechanism | Pass | No technical solution names. |
| 10 | No empty concept: every concept has at least one attribute and at least one association | Pass | Every concept has an attribute and an association. |
| 11 | A Domain Model written for one use case reuses the concepts, attributes, associations and names of the project Domain Model, and its additions and changes are added to the project Domain Model | N-A | DM-001 is the project Domain Model; there is no earlier one to reuse. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | Metadata of DM-001 has Language en and Domain education. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is a BCP 47 code; `education` is in the registry domain list. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | S01 confirmed in chat on 2026-11-15 ('I confirm the language criteria'); the content is English throughout. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Register IT Professional English matches the registry row for the type. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | S01 confirmed in chat on 2026-11-15 ('I confirm the language criteria'); terms follow docs/dictionary.md. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Keys, headings, IDs and statuses are English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No translated twin exists beside the document. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | First version: no earlier accepted language, so no change to record. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | S01 confirmed in chat on 2026-11-15 ('I confirm the language criteria'); S01 reads English and is the Product Owner of the education exercise. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations are spelled out on first use. |

## Overall Verdict

Go — every Mandatory criterion passes; the criteria of QC-LANG-001 that need a person (3, 5, 9) were confirmed by S01 in chat on 2026-11-15. Mode: autonomous, not independent. The diagram was checked by reading, not rendered.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | - |

---

[DM-001]: ../../domain-model.md
[QC-DM-001]: ../../../framework/qc/artifacts/qc-domain-model.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[f9581e1]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/006-a-robot-in-reeborg-s-world/commit/f9581e128ebea2e751df0bb20267a94301763f4b
