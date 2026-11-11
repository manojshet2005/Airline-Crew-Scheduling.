# Case 57 Final Practical Evidence Index

This index maps the latest actual execution evidence. It does not replace the submitted report or presentation, which were preserved unchanged in this continuation.

## Current lab status

**16 COMPLETE, 6 PARTIAL, 3 PENDING HUMAN, 0 BLOCKED** across 25 labs. The authoritative row-by-row status and limitations are in `CASE57_EVIDENCE_AUDIT.md` and the per-lab records.

## Jenkins – L3.4

| Evidence | What it proves |
|---|---|
| `JENKINS_BUILD/build_3_console.txt` | Actual Jenkins Pipeline parser failure caused by a BOM-prefixed DSL token; not a deliberately induced test failure. |
| `JENKINS_BUILD/build_4_console.txt`–`build_6_console.txt` | Actual Jenkins logs for successful runs. Build #6 is authoritative for the current pipeline. |
| `JENKINS_BUILD/build_6_console.txt` | Exact GitHub two-dot URL, `feature/weekly-limit` checkout, install, compile, **9 passed**, `pip check`, source archive and final `SUCCESS`. |
| `JENKINS_BUILD/duty-validator-build-6.zip` | Jenkins source archive; validated ZIP containing validator, tests, requirements and Dockerfile. It is not a Docker image. |
| `JENKINS_BUILD/jenkins_dashboard.png` | Figure 1 — Jenkins job dashboard with latest successful and failed builds. |
| `JENKINS_BUILD/build_6_status.png` | Figure 2 — Successful build #6, repository/revision and source artifact. |
| `JENKINS_BUILD/build_5_pipeline_stages.png` | Figure 3 — Successful build #5 stage view; graph labels partly clipped. |
| `JENKINS_BUILD/build_6_console_test_quality.png` | Figure 4 — Build #6 pytest result and successful dependency check. |
| `JENKINS_BUILD/build_6_console_success.png` | Figure 5 — Build #6 source archive and final SUCCESS. |

`build_6_pipeline_stages.png` was captured while Jenkins was loading its graph and is not evidence of visible completed stages. The text console logs are authoritative. L3.4 remains PARTIAL because the required controlled failure-and-fix experiment was not performed.

## Docker Compose – L3.5

| Evidence | What it proves |
|---|---|
| `DOCKER/compose_execution.log` | Actual Compose run, successful image build, database readiness, validator success, row persistence and final container state. |
| `DOCKER/compose_run_evidence.txt` | Earlier actual Compose run, health check, service logs, stored row and teardown. |
| `DOCKER/compose_live_verification.png` | Figure 6 — Genuine live terminal showing container state, database connection, validator output and direct row-count query. |
| `compose.yaml`, `Dockerfile.compose`, `compose_validator_service.py` | Configuration and one-shot validator that were actually executed. |

The validator containers exit with code 0 after writing a row; PostgreSQL remains healthy. This is real Compose/database communication, not a persistent validator service or production deployment.

## Application and test evidence

- Current local full test suite: **36 passed** (20 original validator tests plus Flask route/API coverage).
- Current source checks: Pylint **10.00/10** for `duty_validator.py`; Flake8 clean on `hello.py`, `test_app.py`, `duty_validator.py`; Bandit clean on `hello.py`, `duty_validator.py`. The scoped checks and separate test-file Pylint findings are documented in `L5.2_Evidence.md`; none are SonarQube scans.
- Jenkins build #6 test suite: **9 passed** on the checked-out remote branch. These test counts are distinct and must not be combined.
- Genuine Flask/Chrome screenshots and browser run notes: `LIVE_APP_VERIFICATION/` and `UI_UX_REDESIGN/`.
- Selenium evidence: `L4.3_plain_selenium.png`, `L4.3_page_object_selenium.png`, and `L4.3_run_log.txt`.
- Original 22 screenshots remain in `original_22_screenshots/`; the per-file inventory and use limitations are in `CASE57_SCREENSHOT_INVENTORY.md`.

## Human participation still required

- L2.4: three actual classmates' planning-poker estimates.
- L4.2: genuine client/classmate acceptance review and sign-off.
- L5.1: genuine peer review findings.

Other non-human evidence limitations remain in each lab record, including L1.3 privacy comparison, incomplete ChatGPT Prompt 4 execution, L3.4 deliberate failure/fix, SonarQube, actual PR review, and L5.4 authorship/time and static-analysis comparison. L5.4's short-run runtime measurements are recorded but are not authoring-time measurements. No human input, tool output, or screenshot is fabricated.
