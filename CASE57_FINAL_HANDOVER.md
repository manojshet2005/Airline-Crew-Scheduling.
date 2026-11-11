# Case 57 final handover

**Checked:** 11 November 2026
**Project:** `C:\Users\guest pc\Desktop\CAT2_Case57\examportal`

## Deliverables

| Deliverable | File | Verified result |
|---|---|---|
| PowerPoint | `Case57_Roll57_Manoj_FINAL.pptx` | New final deck; verified 13 slides, actual Jenkins/Compose screenshots included. Existing deck preserved. |
| Written report | `Case57_57_Manoj_FINAL.docx` | New final report; all 25 theory IDs and all 25 lab IDs verified. Existing report files preserved. |
| PDF report | `Case57_57_Manoj_FINAL.pdf` | Rendered from the final DOCX content; 31 pages. All 25 theory IDs and all 25 lab IDs verified. |

The report's Appendix A is the AI usage log. Appendix B contains the AI disclosure, eight genuine supporting screenshots, and an evidence inventory. The PDF was generated locally from the final DOCX content and visually inspected: the cover, contents, body tables, screenshots, captions, and page numbers are intact. The PDF layout may differ slightly from Microsoft Word's rendering; the text content was extracted and checked against the DOCX.

The report uses roll number **57**, student name **Manoj**, repository page `https://github.com/manojshet2005/Airline-Crew-Scheduling.`, and verified Git remote `https://github.com/manojshet2005/Airline-Crew-Scheduling..git`. Class/section and submission date are explicitly marked `[Not provided]`; the student signature and date lines remain blank for the student. The final report is the `Case57_57_Manoj_FINAL.*` copy; earlier report/PDF files were not overwritten.

## Verified project behavior

- The Flask dashboard calls the existing `duty_validator.validate_duty` function through `POST /api/validate`.
- The latest full test command, `python -B -m pytest -q -p no:cacheprovider`, completed with **36 passed**.
- Real Chrome checks covered valid input, daily/rest/weekly violations, reset, missing-field feedback, and a 390 × 844 mobile viewport. Seven genuine screenshots are in `CASE57_LAB_EVIDENCE/UI_UX_REDESIGN/`.
- Pylint on `duty_validator.py`: **10.00/10**; Flake8 on `hello.py`, `test_app.py`, and `duty_validator.py`: **no findings**; Bandit on `hello.py` and `duty_validator.py`: **no findings**. These are not SonarQube results; see L5.2 for the separate test-file findings and the unavailable SonarQube scan.
- The three displayed duty limits remain sample educational assumptions, not verified aviation regulations or a production roster approval system.
- Focused evidence checks passed: L4.2 simulated acceptance scenarios **5/5**; L5.1 simulated code checks **9/9**. The official statuses remain pending human input.

## Lab evidence status

Current official practical evidence totals are **17 COMPLETE, 5 PARTIAL, 3 PENDING HUMAN, 0 BLOCKED** across the 25 lab rows. The new final files have separate `_FINAL` names; prior report/PDF/PPT and original 22 screenshots were not overwritten.

Outstanding human-dependent work:

- **L2.4:** obtain estimates from three actual classmates and compare them with the ChatGPT estimate; the three-role Copilot simulation is not human input.
- **L4.2:** obtain genuine classmate/client review and sign-off; the fictional stakeholder role is not approval.
- **L5.1:** obtain and document a genuine peer review; role-based AI observations are not peer findings.

Infrastructure/evidence limitations:

- **L1.3:** preserved ChatGPT and Copilot outputs plus the project validator were replayed on 14 cases; all matched expected semantic classifications 14/14. Account-specific privacy settings remain unobserved.
- **L3.1:** Prompt 4 was separately retried with Copilot SDK; 12 displayed examples passed. The original ChatGPT response is still incomplete, so the lab remains partial.
- **L3.4:** Jenkins build #6 actually checked out the exact two-dot GitHub remote, installed dependencies, compiled, passed 9 tests, completed `pip check`, packaged the source archive, and finished SUCCESS. Jenkins is currently unavailable; the deliberate failing-test then corrected-success build pair was not run. A separate-branch procedure is prepared.
- **L3.5:** A real Compose run built the validator image, connected to healthy PostgreSQL and verified two persisted rows. The validator is a one-shot task; actual logs and a terminal screenshot are preserved under `CASE57_LAB_EVIDENCE/DOCKER/`.
- **L5.2:** SonarScanner, server, token and Docker daemon were unavailable; no SonarQube scan was claimed. A future scan procedure is documented.
- **L5.3:** AI-assisted local review of the actual merged PR #7 diff and verification of suggestions are documented. GitHub has zero posted review comments; local notes are not presented as posted PR feedback or human approval. This lab is complete for the official suggestion-log exercise.
- **L5.4:** project validator passed 10/10 required cases; AI reference passed 8/10. Three independent seven-round runtime benchmark logs include samples/ranges and limitations. They are microbenchmarks, not production or authoring-time measurements. SonarQube scans of both implementations remain missing.

AI simulations were separately prepared for L2.4, L4.2, and L5.1. Each was generated by one Copilot SDK assistant role-playing perspectives; none is a human participant, independent model run, client sign-off, or peer review. Focused checks recorded 5/5 L4.2 scenarios and 9/9 L5.1 checks.

## Git and publication

- Starting commit: `cc550ead6a9511b7a43011efe1d86a9a272d7dbe` on `feature/weekly-limit`.
- Existing `origin`: `https://github.com/manojshet2005/Airline-Crew-Scheduling..git`.
- The new final report and presentation are separate files; prior deliverables remain untouched. The final commit hash and remote-head comparison are included in the completion summary; no force-push is used.

## Remaining submission actions

1. Fill in class/section and submission date if required by the university.
2. Sign and date the report.
3. Perform the L3.4 controlled Jenkins failure/fix experiment when Jenkins is available.
4. Run SonarQube scans for L5.2 and both L5.4 implementations when a viable server/scanner is available.
5. Complete human-dependent labs L2.4, L4.2 and L5.1; do not fill their forms without real participation.
6. Fill in class/section and submission date if required, and sign/date the report.
