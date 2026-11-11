# Case 57 screenshot inventory

All 22 preserved original screenshots were opened and reviewed individually. The two L4.3 Selenium screenshots, seven UI screenshots, and new Jenkins/Compose captures were also reviewed. Originals remain unchanged. Suitability refers to the report and future presentation use; the PPT itself was deliberately not regenerated in this continuation.

| File | What it actually demonstrates | Relevant task/lab | Report / PPT suitability |
|---|---|---|---|
| `C57_L4.5_01_Dashboard_Sketch.png.png` | A designed monitoring dashboard with six metric cards, thresholds, actions, and mock values; not a live dashboard. | L4.5 | Suitable to illustrate a design exercise if labeled mock; not runtime evidence. |
| `C57_TaskB_01_Backlog.png.png` | GitHub Projects backlog board with four sample stories in Todo. | Task B / L2.3 | Suitable as backlog evidence; status is a captured board state only. |
| `C57_TaskC_01_Git_Log.png.png` | Terminal Git graph showing the feature branch and prior commits. | Task C / L3.3 | Suitable as Git workflow evidence; historical state, not the current final commit. |
| `C57_TaskC_01_Validator_Output.png.png` | Terminal output for one accepted, one daily-limit, and one rest-limit input. | Task C / L3.2 | Suitable as historical validator output; not proof of the new browser UI. |
| `C57_TaskC_02_PR_Merged.png.png` | GitHub pull request #7 marked merged; page says no reviews. | Task C / L3.3 | Suitable as merge evidence; **not** evidence of reviewer feedback or approval. |
| `C57_TaskC_03_Docker_Run.png.png` | `docker run --rm duty-validator:0.1 -- pytest` output with nine tests passing in one container. | Task C / L3.5 | Suitable only as historical single-container test evidence; **not** Docker Compose or database communication. |
| `C57_TaskC_04_GitHub_Files.png.png` | Repository file listing on `feature/weekly-limit`. | Task C / Git | Suitable as a historical repository snapshot; not a current remote verification. |
| `C57_TaskC_04_PR_Details.png.png` | PR description claims image build/container test, and the page shows “No reviews”. | Task C / L3.3–L3.5 | Use only as a historical PR description; claims are not independent build logs and it is not review evidence. |
| `C57_TaskD_01_Pytest.png.png` | Targeted validator suite with 10 tests passing. | Task D / L4.1 | Suitable as historical test evidence; latest expanded suite is recorded separately. |
| `C57_TaskD_02_Coverage.png.png` | Targeted test output with a 61% coverage result. | Task D / L4.1 | Suitable as historical coverage evidence; it does not represent full project coverage. |
| `C57_TaskD_03_AI_Generated_Tests.png.png` | AI-generated test set run with 10 passing cases. | Task D / L4.4 | Suitable as historical AI-test evidence; test-design accuracy is separately audited. |
| `C57_TaskE_01_Pylint.png.png` | Initial Pylint output with two findings and a score of 8.89/10. | Task E / L5.2 | Suitable as initial Pylint evidence, not SonarQube. |
| `C57_TaskE_02_Flake8.png.png` | Flake8 reports a missing final newline. | Task E / L5.2 | Suitable as historical lint evidence, not a current result. |
| `C57_TaskE_03_Bandit.png.png` | Bandit reports no issues in the then-scanned 33-line validator. | Task E / L5.2 | Suitable as historical security-scan evidence only; it does not cover the new app. |
| `C57_TaskE_04_Pylint_Final.png.png` | Pylint reports a final score of 10/10 for a prior version. | Task E / L5.2 | Suitable as historical Pylint evidence, not SonarQube or current app lint. |
| `C57_TaskE_05_Final_Unit_Tests.png.png` | Ten original validator tests pass. | Task E / L5.2 | Suitable as historical unit-test evidence; latest project suite is 36 tests. |
| `C57_TaskE_06_AI_Tests_Final.png.png` | Ten AI-generated tests pass. | Task E / L5.2/L4.4 | Suitable as historical test evidence; not the current expanded suite. |
| `L1.1_01_Tool_Versions.png.png` | Python, Git, and pip versions displayed from a separate Desktop Python directory. | Setup activity | Limited historical environment context; not proof of the current project environment. |
| `L1.1_02_Flask_Home.png.png` | Original Flask greeting page and local server request log. | Setup activity | Useful only as historical Flask setup; it is not the new dashboard. |
| `L1.1_03_Flask_Server.png.png` | Flask development-server console with a visible local debugger credential. | Setup activity | **Do not insert into report/PPT or publicly share.** Preserve original unchanged; redact only a separately authorized copy if required. |
| `L1.1_04_About_Route.png.png` | Original plain-text `/about` response. | Setup activity | Useful only as historical Flask route setup; not validator behavior. |
| `L1.1_05_Requirements.png..png` | `requirements.txt` listing in the editor. | Setup activity | Limited dependency snapshot; not proof the application was deployed. |
| `L4.3_plain_selenium.png` | Real Chrome screenshot of the local Selenium fixture in the inclusive-boundary state. | L4.3 | Suitable with the caveat that the daily-limit assertion occurred in the same run but is not shown in this captured state. |
| `L4.3_page_object_selenium.png` | Real Chrome screenshot of the same fixture in the inclusive-boundary state. | L4.3 | Suitable with the same fixture/run-log caveat; not a screenshot of the Flask dashboard. |
| `UI_UX_REDESIGN/dashboard_desktop.png` | Live Flask dashboard in Chrome at desktop width, before form submission. | UI redesign | Suitable for report and future PPT as genuine interface evidence. |
| `UI_UX_REDESIGN/dashboard_mobile.png` | Live Flask dashboard at a 390-pixel viewport, before form submission. | UI redesign | Suitable for report and future PPT as responsive-layout evidence. |
| `UI_UX_REDESIGN/validator_valid.png` | Live Flask UI showing an accepted sample schedule. | UI redesign | Suitable for report/PPT; example values are educational, not operational data. |
| `UI_UX_REDESIGN/validator_daily_violation.png` | Live Flask UI showing the exact daily-duty violation. | UI redesign | Suitable for report/PPT; genuine browser interaction. |
| `UI_UX_REDESIGN/validator_rest_violation.png` | Live Flask UI showing the exact minimum-rest violation. | UI redesign | Suitable for report/PPT; genuine browser interaction. |
| `UI_UX_REDESIGN/validator_weekly_violation.png` | Live Flask UI showing the exact rolling-week violation. | UI redesign | Suitable for report/PPT; genuine browser interaction. |
| `UI_UX_REDESIGN/validator_input_error.png` | Live Flask UI showing required-field errors and field highlighting. | UI redesign | Suitable for report/PPT; genuine browser interaction. |

| `JENKINS_BUILD/jenkins_dashboard.png` | Actual Jenkins dashboard; build #6 is the latest success and #3 is the latest failure shown. | L3.4 | Genuine Jenkins UI evidence. |
| `JENKINS_BUILD/build_6_status.png` | Build #6 status, repository/revision and source archive. | L3.4 | Genuine successful-build evidence. |
| `JENKINS_BUILD/build_5_pipeline_stages.png` | Successful pipeline-stage graph and stage list for build #5. | L3.4 | Graph labels are partly clipped; build logs are authoritative. |
| `JENKINS_BUILD/build_6_console_test_quality.png` | Jenkins #6 test output (9 passed) and successful `pip check`. | L3.4 | Genuine console capture; remote branch suite, not the local 36-test suite. |
| `JENKINS_BUILD/build_6_console_success.png` | Jenkins #6 archive operation and final `SUCCESS`. | L3.4 | Genuine console capture. |
| `DOCKER/compose_live_verification.png` | Live terminal showing Compose container state, validator/database connection success and persisted row count. | L3.5 | Genuine capture; validator is a one-shot container and exits with code 0. |

`JENKINS_BUILD/build_6_pipeline_stages.png` is a loading-state capture and should not be used as evidence that the stage graph rendered. The original L1.1 images are Flask/setup evidence, not an SDLC diagram. The historical single-container Docker run remains separate from the newly captured Compose evidence.
