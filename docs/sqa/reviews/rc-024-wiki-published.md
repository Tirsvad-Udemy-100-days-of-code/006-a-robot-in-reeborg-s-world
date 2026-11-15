# Review: the published wiki

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-024 |
| CrossReference | [WIKI], [QC-WIKI-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | S01 (Product Owner) | Initial version; reviewed in the review itself, autonomous, not independent | pending |

---

## Artifact Under Review

- Instance reviewed: [WIKI]
- Checklist used: [QC-WIKI-001], [QC-LANG-001]
- Scope: delta re-review of criterion 14 and criteria 3, 5, 9 of QC-LANG-001; reason: the wiki can be checked only after publication; earlier record: RC-023
- Language and domain: en / education (the artifact's Metadata rows)
- Language reviewer: S01 (criteria 3, 5 and 9 of QC-LANG-001 only, confirmed in chat on 2026-11-15)
- Mode: autonomous, not independent (AI as stand-in for S02)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change, not only in the repository | Pass | After the merge of PR 27, all 12 pages answered 200 on the host (`/wiki/Home`, `-da`, `-ms` and the three other pages in each language); the sidebar links resolve to the same 12 pages and the language links reach Home, Hjem and Utama. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 3 | The content (prose and table cells) is written in the stated language | Pending | Still waiting for S01 to confirm the Danish and Malay pages (English confirmed on 2026-11-15). |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pending | Still waiting for S01 to confirm the Danish and Malay pages (English confirmed on 2026-11-15). |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pending | Still waiting for S01 to confirm the Danish and Malay pages (English confirmed on 2026-11-15). |

## Overall Verdict

Go-with-conditions — criterion 14 of QC-WIKI-001 now passes on the published wiki; criteria 3, 5 and 9 of QC-LANG-001 for the Danish and Malay pages stay Pending until S01 confirms them, so the verdict of RC-023 is unchanged. Mode: autonomous, not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Confirm criteria 3, 5 and 9 of QC-LANG-001 for the Danish and Malay pages; then record a delta re-review with verdict Go | S01 | 2026-11-22 |

---

[WIKI]: ../../wiki
[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
