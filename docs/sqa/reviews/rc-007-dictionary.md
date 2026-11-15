# Review: DICT-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-007 |
| CrossReference | [DICT-001], [QC-DICT-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | S01 (Product Owner) | Initial version; reviewed in the review itself, autonomous, not independent | pending |

---

## Artifact Under Review

- Instance reviewed: [DICT-001]
- Checklist used: [QC-DICT-001], [QC-LANG-001]
- Scope: full review
- Language and domain: en / education (the artifact's Metadata rows)
- Language reviewer: S01 (criteria 3, 5 and 9 of QC-LANG-001 only, confirmed in chat on 2026-11-15)
- Mode: autonomous, not independent (AI as stand-in for S02)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Every row has a PO term, its language, an IT term and a definition | Pass | All eight rows have PO term, language, IT term and definition. |
| 2 | Each PO term maps to exactly one IT term and the reverse (no synonyms) | Pass | Eight PO terms map to eight distinct IT terms and back. |
| 3 | Every Domain Model concept has a row, and the Domain Model uses its PO term | N-A | No Domain Model exists yet (DM-001 is a task of MIL-002); criterion rechecked as a delta re-review when DM-001 is reviewed. |
| 4 | The Operation Contracts, Sequence Diagrams, Design Class Diagrams and ERD use the IT term, not the PO term | N-A | No OC, SD, DCD or ERD exists; ADR-0001 skips them. Source code uses the IT terms. |
| 5 | Definitions are written in the PO language and are one sentence | Pass | Each definition is one English sentence. |
| 6 | "Used as PO term in" and "Used as IT term in" name artifact types that exist in the project | N-A | The columns name US, UC and DM, which are created in MIL-002; rechecked with criterion 3. |
| 7 | The dictionary's `Language` and `Domain` rows, and the language of every row, match the PO language and domain in the project registry | Pass | Language en and Domain education match the registry. |
| 8 | The dictionary rows are in ascending order of the PO term (case-insensitive, by the alphabet of the PO language) | Pass | Rows are in ascending order: Exercise, Goal, Learner, Maze, Robot, Start position, Wall, Wall following. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | Metadata of DICT-001 has Language en and Domain education. |
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

Go — every Mandatory criterion passes; the criteria of QC-LANG-001 that need a person (3, 5, 9) were confirmed by S01 in chat. Mode: autonomous, not independent. Criteria 3, 4 and 6 are N-A because their subject does not exist yet.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Delta re-review of criteria 3 and 6 when DM-001, UC-001 and US-001 exist | S02 (AI as stand-in) | 2026-11-19 |

---

[DICT-001]: ../../dictionary.md
[QC-DICT-001]: ../../../framework/qc/artifacts/qc-dictionary.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
