# Review: US-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-012 |
| CrossReference | [US-001], [QC-US-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | S01 (Product Owner) | Initial version; reviewed in the review itself, autonomous, not independent | pending |

---

## Artifact Under Review

- Instance reviewed: [US-001]
- Checklist used: [QC-US-001], [QC-LANG-001]
- Scope: full review
- Language and domain: en / education (the artifact's Metadata rows)
- Language reviewer: S01 (criteria 3, 5 and 9 of QC-LANG-001 only, confirmed in chat on 2026-11-15)
- Mode: autonomous, not independent (AI as stand-in for S02)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Follows INVEST criteria (Independent, Negotiable, Valuable, Estimable, Small, Testable) | Pass | Two stories with a goal and a benefit; each is small and testable; US-001.02 depends on US-001.01, flagged as an exception. |
| 2 | Written in "As a / I want / So that" form | Pass | Both use As a / I want / so that. |
| 3 | Clear, testable acceptance criteria are included | Pass | Given/When/Then criteria for each. |
| 4 | Traceable to a use case or epic | Pass | Each traces to UC-001. |
| 5 | Story is sized to fit within a single iteration | Pass | Both fit one iteration. |
| 6 | Story statement avoids technical implementation detail | Pass | No class, file or technology names except 'maze file' as the learner's own material. |
| 7 | Role named in the story matches an actor defined in the Use Case Diagram | Pass | The role Learner is the actor of UCD-001. |
| 8 | A story with more than one actor goal is split into use cases, one per actor goal, and each use case names the story it comes from | Pass | Each story has one actor goal. |
| 9 | The story has a priority (MoSCoW: Must, Should, Could, Won't now) with the reason beside it | Pass | Each has a MoSCoW priority (Must, Should) with a reason. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | Metadata of US-001 has Language en and Domain education. |
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

Go — every Mandatory criterion passes; the criteria of QC-LANG-001 that need a person (3, 5, 9) were confirmed by S01 in chat on 2026-11-15. Mode: autonomous, not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | - |

---

[US-001]: ../../user-stories.md
[QC-US-001]: ../../../framework/qc/artifacts/qc-user-story.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
