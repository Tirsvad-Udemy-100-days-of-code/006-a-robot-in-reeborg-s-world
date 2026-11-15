# Review: the wiki

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-023 |
| CrossReference | [WIKI], [QC-WIKI-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | S01 (Product Owner) | Initial version; reviewed in the review itself, autonomous, not independent | [1e74867] |

---

## Artifact Under Review

- Instance reviewed: [WIKI]
- Checklist used: [QC-WIKI-001], [QC-LANG-001]
- Scope: full review
- Language and domain: en, da and ms / education (wiki pages have no Metadata rows)
- Language reviewer: S01 for criteria 3, 5 and 9 of QC-LANG-001: confirmed for the English pages on 2026-11-15; Danish and Malay pages not yet confirmed
- Mode: autonomous, not independent (AI as stand-in for S02)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The wiki has a `_Sidebar.md`, because the host lists subpages only through it | Pass | `docs/wiki/_Sidebar.md` exists. |
| 2 | The sidebar starts with the wiki's title in bold, then one list of the pages in the primary language (English), `Home` first | Pass | The sidebar starts with the bold title 'Reeborg Maze', then one list of four English pages, Home first. |
| 3 | The page list holds a link to every English page of the wiki, and no link points to a page that does not exist | Pass | A link check over all 13 files found no dead link; all four English pages are in the sidebar. |
| 4 | A `**Related**` section follows the page list only when the wiki has related wikis (for example the checklists wiki for a framework wiki); each entry is a link to that wiki's Home. A wiki with nothing related has no such section | Pass | The wiki has no related wikis and the sidebar has no Related section. |
| 5 | A `**Languages**` section is the last section of the sidebar. It has one line per language, the language written in that language, linking to that language's `Home` page | Pass | The Languages section is last, with English: Home, Dansk: Hjem, Bahasa Melayu: Utama, each linking to that language's Home. |
| 6 | The sidebar does not repeat the page list per language | Pass | The page list appears once. |
| 7 | A sidebar produced by a generator carries a comment that says so and names the generator; the generator is changed, not the page | N-A | The sidebar is written by hand, not generated. |
| 8 | The wiki has a `Languages` line on each page (criterion 11), so the sidebar is not the only way to switch language | Pass | Each page has a language line. |
| 9 | Every wiki exists in English and, as a minimum, in the language the project's registry names as the PO language; further languages are added on top, never instead of English | Pass | English is the PO language; Danish and Malay are added on top. |
| 10 | Every English page has a page in each other language of the wiki: the page sets are identical | Pass | Four English pages, four `-da` pages, four `-ms` pages. |
| 11 | Every page starts with the language line, with the current language in bold and a link to the same page in each other language | Pass | Each page starts with the language line, current language in bold, links to the same page in the other two. |
| 12 | A page in a language other than English is named `<Page>-<code>.md`, with a BCP 47 code; English has no suffix | Pass | `Home-da.md` and `Home-ms.md` style names, English without suffix. |
| 13 | Code blocks, commands, file names and IDs stay in English in every language | Pass | Commands and file names are English in every language. |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change, not only in the repository | Pending | The published wiki can be checked only after the merge of this change; the check is task 5 of MIL-003 and is recorded in a delta re-review. |
| 15 | A change to the layout rules (sections, order, naming) is made in the generator or template and in this checklist's source rules together | N-A | No generator or template is changed. |
| 16 | The wiki folder (`docs/wiki/`) is flat: every page, `Home.md` and `_Sidebar.md` included, is directly in it, and languages are told apart by file name, never by a subfolder | Pass | All 13 files are directly in `docs/wiki/`. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | N-A | The wiki pages are documentation, not an artifact with Metadata rows; this criterion applies to artifacts. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | N-A | The wiki pages are documentation, not an artifact with Metadata rows; this criterion applies to artifacts. |
| 3 | The content (prose and table cells) is written in the stated language | Pending | English pages: S01 confirmed the language criteria in chat on 2026-11-15. Danish and Malay pages were written by the AI; S01 has not yet confirmed them, so these rows stay Pending. |
| 4 | The register matches the one the registry gives for the artifact type | N-A | The wiki pages are documentation, not an artifact with Metadata rows; this criterion applies to artifacts. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pending | English pages: S01 confirmed the language criteria in chat on 2026-11-15. Danish and Malay pages were written by the AI; S01 has not yet confirmed them, so these rows stay Pending. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Page and sidebar headings are in the language of the page; the sidebar structure is English as the wiki process requires. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | N-A | The wiki pages are documentation, not an artifact with Metadata rows; this criterion applies to artifacts. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | N-A | The wiki pages are documentation, not an artifact with Metadata rows; this criterion applies to artifacts. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pending | English pages: S01 confirmed the language criteria in chat on 2026-11-15. Danish and Malay pages were written by the AI; S01 has not yet confirmed them, so these rows stay Pending. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations are spelled out on first use. |

## Overall Verdict

Go-with-conditions — every Mandatory criterion that can be judged before publication passes. Two things are Pending: criterion 14 (the published wiki, checked after the merge) and criteria 3, 5 and 9 of QC-LANG-001 for the Danish and Malay pages (S01 must confirm them). A Pending criterion allows Go-with-conditions at most. Mode: autonomous, not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Check the published wiki, sidebar and every link on the host; record a delta re-review for criterion 14 | S02 (AI as stand-in) | 2026-11-16 |
| Confirm criteria 3, 5 and 9 of QC-LANG-001 for the Danish and Malay pages | S01 | 2026-11-22 |

---

[WIKI]: ../../wiki
[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[1e74867]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/006-a-robot-in-reeborg-s-world/commit/1e7486705e7656ee6aa251f7325d729d52b22694
