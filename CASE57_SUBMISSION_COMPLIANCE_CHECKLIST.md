# Case 57 submission compliance checklist

**Status source:** `CASE57_EVIDENCE_AUDIT.md` and the per-lab evidence records.
**Current lab totals:** 17 COMPLETE, 5 PARTIAL, 3 PENDING HUMAN, 0 BLOCKED.
**AI-simulation substitutes:** 3 prepared (L2.4, L4.2, L5.1); the three official statuses remain PENDING HUMAN.

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
| Previous 13-slide PPT preserved | COMPLETE | Earlier presentation remains untouched; a separate 13-slide `Case57_Roll57_Manoj_FINAL.pptx` was created and checked. |
| New final submission files | COMPLETE | `Case57_57_Manoj_FINAL.docx`, `Case57_57_Manoj_FINAL.pdf` (31 pages), and `Case57_Roll57_Manoj_FINAL.pptx` (13 slides) exist; all 25 theory IDs and 25 lab IDs are verified in DOCX/PDF. |
| GitHub URL confirmed and local origin aligned | COMPLETE | Student confirmed the canonical URL; local `origin` matches it and `git ls-remote` successfully read the feature branch. |
| GitHub publication | See completion summary | The commit hash, normal push outcome, and remote-head comparison are reported in the completion summary. No force-push is used. |
| Student class/section and submission date | PARTIAL | Not provided; report uses explicit placeholders. Add these details if required. |

## Lab status matrix

| Lab | Status | Missing item / exact next action |
|---|---|---|
| L1.1 | COMPLETE | — |
| L1.2 | COMPLETE | — |
| L1.3 | PARTIAL | Same saved ChatGPT/Copilot outputs now replay 14/14 semantic cases; account plan and privacy settings remain unobserved. |
| L1.4 | COMPLETE | — |
| L1.5 | COMPLETE | — |
| L2.1 | COMPLETE | — |
| L2.2 | COMPLETE | — |
| L2.3 | COMPLETE | — |
| L2.4 | PENDING HUMAN | AI-only estimator-role simulation is documented. Ask three actual classmates to estimate the stories; then calculate the real team median/differences and discuss the largest real gap. |
| L2.5 | COMPLETE | — |
| L3.1 | PARTIAL | Copilot SDK retry of Prompt 4 is complete and 12 examples passed. The retained ChatGPT response is still incomplete; do not attribute the Copilot retry to ChatGPT. |
| L3.2 | COMPLETE | — |
| L3.3 | COMPLETE | — |
| L3.4 | PARTIAL | Historical builds #4–#6 succeeded; current Jenkins port 8080 has no listener/process. The required controlled failure/fix pair remains unexecuted; a separate-branch procedure and availability log are prepared. |
| L3.5 | COMPLETE | Compose connected the one-shot validator to healthy PostgreSQL and persisted two validation rows. Logs and a genuine terminal screenshot are in `CASE57_LAB_EVIDENCE/DOCKER/`. |
| L4.1 | COMPLETE | — |
| L4.2 | PENDING HUMAN | AI stakeholder simulation and five technical checks are documented. A real classmate/client must review the scenarios and provide their own decision/sign-off. |
| L4.3 | COMPLETE | Original fixture comparison and separate live-app Chrome check are documented; do not conflate the two. |
| L4.4 | COMPLETE | — |
| L4.5 | COMPLETE | Dashboard design values are explicitly mock; no live monitoring is claimed. |
| L5.1 | PENDING HUMAN | Three AI reviewer-role observations are documented separately. Have a real peer review a specified artifact/commit and record genuine findings/confirmation. |
| L5.2 | PARTIAL | SonarScanner/server/token and Docker daemon are unavailable. A precise future scan procedure is recorded; Pylint is not presented as SonarQube. |
| L5.3 | COMPLETE | Actual merged PR #7 diff reviewed by Copilot SDK locally; suggestions and verification are logged. GitHub has zero posted reviews/comments; no human approval is claimed. |
| L5.4 | PARTIAL | Project validator passed 10/10, AI reference 8/10; three reproducible runtime runs are recorded. SonarQube scans of both remain outstanding. |
| L5.5 | COMPLETE | — |

Current status totals above are recalculated from all 25 authoritative lab rows: 17 COMPLETE, 5 PARTIAL, 3 PENDING HUMAN, 0 BLOCKED.
