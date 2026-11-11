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
- Pylint on `hello.py` and `test_app.py`: **10.00/10**; Flake8 on both: **no findings**; Bandit on `hello.py`: **no findings**.
- The three displayed duty limits remain sample educational assumptions, not verified aviation regulations or a production roster approval system.

## Lab evidence status

Current practical evidence totals are **16 COMPLETE, 6 PARTIAL, 3 PENDING HUMAN, 0 BLOCKED**. These updated counts reflect the later Jenkins and Compose executions; the preserved DOCX/PDF/PPT were not changed during this continuation.

Outstanding human-dependent work:

- **L2.4:** obtain estimates from three actual classmates and compare them with the AI estimates.
- **L4.2:** obtain genuine classmate/client review and sign-off.
- **L5.1:** obtain and document a genuine peer review.

Infrastructure/evidence limitations:

- **L3.4:** Jenkins builds #4–#6 succeeded; build #6 checked out the exact GitHub URL, installed dependencies, compiled, passed 9 tests, passed `pip check` and archived a source ZIP. Build #3 failed on a BOM/parser issue, not as a deliberate test failure; L3.4 remains partial until the controlled failure/fix is demonstrated.
- **L3.5:** A real Compose run built the validator image, connected to healthy PostgreSQL and stored validation rows. The service is a one-shot validator; actual logs and a terminal screenshot are preserved under `CASE57_LAB_EVIDENCE/DOCKER/`.
- **L5.2:** Pylint findings are not SonarQube findings.
- **L5.3:** local AI-assisted review is not an actual pull-request review.
- **L5.4:** timing and SonarQube comparison evidence remain missing.

## Git and publication

- Branch: `feature/weekly-limit`
- Existing `HEAD`: `9b9c9f0370521052a456c408c52fcd1741ba02c` (`Complete Case 57 practical work and evidence`)
- Existing `origin`: `https://github.com/manojshet2005/Airline-Crew-Scheduling..git`
- The final continuation commit and whether it was published are reported in the task completion summary; the configured remote was verified with `git ls-remote` before any push.
- `git diff --check` passed before the final staging operation.
- Jenkins build #6 and `git ls-remote` verified read access to the configured remote and `feature/weekly-limit`; the final push status is reported in the task completion summary.

## Remaining submission actions

1. Fill in class/section and submission date if required by the university.
2. Sign and date the report.
3. Complete the three human-dependent labs and any desired Jenkins, Compose, SonarQube, and timing-evidence follow-up.
4. Complete the remaining human-dependent labs and fill in any required student details.
