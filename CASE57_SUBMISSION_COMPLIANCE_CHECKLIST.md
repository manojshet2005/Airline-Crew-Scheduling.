# Case 57 submission compliance checklist

**Status source:** `CASE57_EVIDENCE_AUDIT.md` and the per-lab evidence records.
**Current lab totals:** 16 COMPLETE, 6 PARTIAL, 3 PENDING HUMAN, 0 BLOCKED.

## Submission requirements

| Requirement | Status | Evidence / next action |
|---|---|---|
| Case 57 tasks A–E | COMPLETE | Included in the report using the official Assignment Book and actual project evidence. |
| Theory questions T1.1–T5.5 (25 total) | COMPLETE | All 25 IDs and original question text included in the report. |
| Laboratory exercises L1.1–L5.5 (25 total) | COMPLETE | All 25 IDs, status labels, evidence and limitations are included; not all labs are complete. |
| AI usage log | COMPLETE | Included as Appendix A in the final report. |
| AI disclosure statement | COMPLETE | Included as Appendix B in the final report; student signature/date remain blank for the student. |
| Original 22 screenshots individually inspected | COMPLETE | Inventory documents the demonstrated content, relevance, and suitability of each. |
| New live-UI screenshots | COMPLETE | Seven genuine Chrome screenshots saved under `CASE57_LAB_EVIDENCE/UI_UX_REDESIGN/`. |
| Functional dashboard and validator UI | COMPLETE | Flask frontend calls `validate_duty` via `/api/validate`; browser-checked on desktop and mobile. |
| Previous 13-slide PPT preserved | COMPLETE | Existing 13-slide file is retained; no PPT generation or update was performed in this continuation. |
| GitHub URL confirmed and local origin aligned | COMPLETE | Student confirmed the canonical URL; local `origin` matches it and `git ls-remote` successfully read the feature branch. |
| GitHub publication | See completion summary | Final commit and push outcome are reported in the task completion summary. No force-push is permitted. |
| Student class/section and submission date | PARTIAL | Not provided; report uses explicit placeholders. Add these details if required. |

## Lab status matrix

| Lab | Status | Missing item / exact next action |
|---|---|---|
| L1.1 | COMPLETE | — |
| L1.2 | COMPLETE | — |
| L1.3 | PARTIAL | Check the account-specific privacy settings for both AI tools and record the actual settings. |
| L1.4 | COMPLETE | — |
| L1.5 | COMPLETE | — |
| L2.1 | COMPLETE | — |
| L2.2 | COMPLETE | — |
| L2.3 | COMPLETE | — |
| L2.4 | PENDING HUMAN | Ask three actual classmates to estimate the prepared stories, record their responses, and compare them with AI estimates. |
| L2.5 | COMPLETE | — |
| L3.1 | PARTIAL | Preserve/run a complete Prompt 4 response if available and score it; do not treat incomplete generated code as executed. |
| L3.2 | COMPLETE | — |
| L3.3 | COMPLETE | — |
| L3.4 | PARTIAL | Jenkins builds #4–#6 succeeded; #6 checked out the exact two-dot GitHub URL and passed 9 tests. Build #3 was a parser/configuration failure, not the required deliberate failure. A controlled failure-and-fix demonstration remains. |
| L3.5 | COMPLETE | Compose connected the one-shot validator to healthy PostgreSQL and persisted two validation rows. Logs and a genuine terminal screenshot are in `CASE57_LAB_EVIDENCE/DOCKER/`. |
| L4.1 | COMPLETE | — |
| L4.2 | PENDING HUMAN | Review the five scenarios with a real classmate/client and capture their genuine decision and sign-off. |
| L4.3 | COMPLETE | Original fixture comparison and separate live-app Chrome check are documented; do not conflate the two. |
| L4.4 | COMPLETE | — |
| L4.5 | COMPLETE | Dashboard design values are explicitly mock; no live monitoring is claimed. |
| L5.1 | PENDING HUMAN | Have a real peer review a specified artifact/commit and record findings and reviewer confirmation. |
| L5.2 | PARTIAL | If required, run SonarQube; Pylint findings are an alternative and must not be relabeled. |
| L5.3 | PARTIAL | If the assignment requires a PR review, obtain actual review comments and test each suggestion; local AI review is not PR review. |
| L5.4 | PARTIAL | Capture reliable authoring-time measurements and SonarQube results for both implementations if required. |
| L5.5 | COMPLETE | — |

All status totals above are the pre-existing audited lab totals; the new UI work and tests are reported separately and do not retroactively alter historical lab evidence.
