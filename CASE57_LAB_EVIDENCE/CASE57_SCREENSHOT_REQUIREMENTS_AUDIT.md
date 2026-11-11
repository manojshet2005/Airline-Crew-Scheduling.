# Case 57 Screenshot Requirements Audit

This is a lab-by-lab check of screenshot requests recorded in the existing report/evidence audit, not a claim that every official lab requires an image. Screenshots support written/code evidence; they do not substitute for executions, analysis, or real participant input.

| Lab | Screenshot request / evidence state | Current evidence and remaining gap |
|---|---|---|
| L1.1 | Requested SDLC-diagram screenshot; **missing**. | Setup screenshots are not an SDLC diagram. |
| L1.2 | No screenshot required; written plan/table is primary. | No image needed for the planned Waterfall/Incremental comparison. |
| L1.3 | Separate screenshots of both AI-tool outputs requested; **missing**. | Existing validator screenshots do not prove paired AI outputs or privacy comparison. |
| L1.4 | No screenshot required by the lab record. | Written notes, AI extraction and classification are primary evidence. |
| L1.5 | Reuse existing test-run screenshot; **available**. | `original_22_screenshots/C57_TaskD_03_AI_Generated_Tests.png.png` shows 10 tests passing, but not prompt provenance or case-by-case analysis. |
| L2.1 | No screenshot required. | Six Agile-practice mappings are written evidence. |
| L2.2 | No screenshot required. | Sprint goal, Definition of Done and acceptance checks are written evidence. |
| L2.3 | No screenshot required. | Prioritisation tables and rationale are written evidence. |
| L2.4 | No screenshot required; genuine participant input is required. | Do not invent three classmates' estimates. |
| L2.5 | No screenshot required. | Result-linked benefits/challenges are written evidence. |
| L3.1 | Full Prompt 4 response screenshot requested for visual proof; **incomplete/cropped**. | Existing prompt/response images do not show a complete generated function; no complete code should be claimed. |
| L3.2 | A post-refactor test screenshot was requested for report evidence; **not present**. | Refactor, tests and behavior comparison are documented; unrelated Jenkins tests are not a substitute. |
| L3.3 | No screenshot required by the official lab wording. | Actual conflict, resolution and AI suggestion are preserved in `L3.3_Evidence.md`. |
| L3.4 | Jenkins dashboard, failed/successful build, stage and console evidence requested; **available with caveat**. | Figures 1–5 in `JENKINS_BUILD/`; #3 was an accidental parser failure, not the deliberate failure experiment still needed. |
| L3.5 | Compose status and app/database log screenshot requested; **available**. | Figure 6, `DOCKER/compose_live_verification.png`, shows genuine one-shot validator output, healthy DB and stored rows. |
| L4.1 | No screenshot required by the lab record. | Manual-case and seeded-defect records are written evidence; automated pytest screenshots are not manual execution. |
| L4.2 | No screenshot required; real client/classmate sign-off is required. | A screenshot cannot replace actual participation or signature. |
| L4.3 | Passing POM test screenshot requested; **available**. | `L4.3_page_object_selenium.png` and `L4.3_run_log.txt` show the genuine Chrome run; companion plain Selenium evidence is also present. |
| L4.4 | No new screenshot required. | Existing AI-test execution images can be reused; classification/accuracy explanation belongs in the written record. |
| L4.5 | No new screenshot required; existing design image is available. | `original_22_screenshots/C57_L4.5_01_Dashboard_Sketch.png.png` is a mock design, not live monitoring data. |
| L5.1 | No screenshot required; genuine peer participation is required. | Checklist/findings and an actual reviewer are required; do not invent review results. |
| L5.2 | SonarQube image requested for SonarQube proof; **missing**. | Existing Pylint/Flake8/Bandit images show those tools only, not SonarQube. |
| L5.3 | PR screenshot with AI review comments/replies requested; **missing**. | Local AI-assisted review is not an actual PR review. |
| L5.4 | Separate comparative results requested; **missing**. | Existing screenshots do not establish both versions' timing, tests and analyzer results. |
| L5.5 | `pip-licenses` output screenshot requested; **missing**. | The screenshot is not present; do not imply that this particular command was captured. |

## Genuine new screenshots in this continuation

- `JENKINS_BUILD/jenkins_dashboard.png`
- `JENKINS_BUILD/build_6_status.png`
- `JENKINS_BUILD/build_5_pipeline_stages.png`
- `JENKINS_BUILD/build_6_console_test_quality.png`
- `JENKINS_BUILD/build_6_console_success.png`
- `DOCKER/compose_live_verification.png`

`JENKINS_BUILD/build_6_pipeline_stages.png` was captured during graph loading and is intentionally excluded above as proof of rendered stage status. See `CASE57_SCREENSHOT_INVENTORY.md` for review notes on the preserved original images and older UI evidence.
