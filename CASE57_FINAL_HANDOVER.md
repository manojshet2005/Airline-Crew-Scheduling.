# Case 57 final handover

**Checked:** 11 November 2026
**Project:** `C:\Users\guest pc\Desktop\CAT2_Case57\examportal`

## Deliverables

| Deliverable | File | Verified result |
|---|---|---|
| PowerPoint | `Case57_Roll57_Manoj.pptx` | Existing deck preserved; 13 slides. Not regenerated or modified in this continuation. |
| Written report | `Case57_57_Manoj.docx` | Generated and saved; contains all 25 theory IDs and all 25 lab IDs. |
| PDF report | `Case57_57_Manoj.pdf` | Generated from the DOCX; 31 pages. All 25 theory IDs and all 25 lab IDs are present. |

The report's Appendix A is the AI usage log. Appendix B contains the AI disclosure, genuine supporting screenshots, and evidence inventory. The final PDF was rendered and visually inspected: the cover, contents, appendix pages, figures, captions, and page numbers are intact. An appendix orphan line was removed before the final regeneration.

The report uses roll number **57**, student name **Manoj**, and the confirmed repository URL `https://github.com/manojshet2005/Airline-Crew-Scheduling`. Class/section and submission date are explicitly marked `[Not provided]`; the student signature and date lines remain blank for the student. The final report is the `Case57_57_Manoj.*` copy; the earlier `Case57_Roll57_Manoj.docx` and `.pdf` were not overwritten.

## Verified project behavior

- The Flask dashboard calls the existing `duty_validator.validate_duty` function through `POST /api/validate`.
- The latest full test command, `python -B -m pytest -q -p no:cacheprovider`, completed with **36 passed**.
- Real Chrome checks covered valid input, daily/rest/weekly violations, reset, missing-field feedback, and a 390 × 844 mobile viewport. Seven genuine screenshots are in `CASE57_LAB_EVIDENCE/UI_UX_REDESIGN/`.
- Pylint on `duty_validator.py`: **10.00/10**; Flake8 on `hello.py`, `test_app.py`, and `duty_validator.py`: **no findings**; Bandit on `hello.py` and `duty_validator.py`: **no findings**. These are not SonarQube results; see L5.2 for the separate test-file findings and the unavailable SonarQube scan.
- The three displayed duty limits remain sample educational assumptions, not verified aviation regulations or a production roster approval system.

## Lab evidence status

Current practical evidence totals are **17 COMPLETE, 5 PARTIAL, 3 PENDING HUMAN, 0 BLOCKED** across the 25 lab rows. This continuation did not modify the existing DOCX, PDF, PPT, or original 22 screenshots.

Outstanding human-dependent work:

- **L2.4:** obtain estimates from three actual classmates and compare them with the AI estimates.
- **L4.2:** obtain genuine classmate/client review and sign-off.
- **L5.1:** obtain and document a genuine peer review.

Infrastructure/evidence limitations:

- **L1.3:** preserved ChatGPT and Copilot outputs plus the project validator were replayed on 14 cases; all matched expected semantic classifications 14/14. Account-specific privacy settings remain unobserved.
- **L3.1:** Prompt 4 was separately retried with Copilot SDK; 12 displayed examples passed. The original ChatGPT response is still incomplete, so the lab remains partial.
- **L3.4:** prior Jenkins builds #4–#6 succeeded; the current availability check found no process/listener at port 8080. The required deliberate failing-test then corrected-success build pair was not run. A separate-branch procedure is prepared.
- **L3.5:** A real Compose run built the validator image, connected to healthy PostgreSQL and stored validation rows. The service is a one-shot validator; actual logs and a terminal screenshot are preserved under `CASE57_LAB_EVIDENCE/DOCKER/`.
- **L5.2:** SonarScanner, server, token and Docker daemon were unavailable; no SonarQube scan was claimed. A future scan procedure is documented.
- **L5.3:** AI-assisted local review of merged PR #7 and verification of its suggestions are documented. GitHub has zero posted review comments; local notes are not presented as posted PR feedback or human approval. This lab is complete for the official suggestion-log exercise.
- **L5.4:** project validator passed 10/10 required cases; AI reference passed 8/10. Three independent seven-round runtime benchmark logs are included with full samples/ranges. They are microbenchmarks, not production or authoring-time measurements. SonarQube scans of both implementations remain missing.

## Git and publication

- Starting commit: `469d7087df955a706ddd3acec029a28fb6746ac9` on `feature/weekly-limit`.
- Existing `origin`: `https://github.com/manojshet2005/Airline-Crew-Scheduling..git`.
- This continuation stages only reviewed evidence and directly related status documents/scripts. The final commit hash and remote-head comparison are recorded in the completion response after verification; no force-push is used.

## Remaining submission actions

1. Fill in class/section and submission date if required by the university.
2. Sign and date the report.
3. Perform the L3.4 controlled Jenkins failure/fix experiment when Jenkins is available.
4. Run SonarQube scans for L5.2 and both L5.4 implementations when a viable server/scanner is available.
5. Complete human-dependent labs L2.4, L4.2 and L5.1; do not fill their forms without real participation.
6. Fill in class/section and submission date if required, and sign/date the report.
