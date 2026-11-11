# Case 57 – Airline Crew Scheduling

This repository contains an academic prototype for checking a crew duty record against three **sample** limits. It is a small rule validator and Flask interface, not a roster generator or operational airline system.

## What it does

- Accepts daily duty hours, rolling seven-day duty hours, and rest hours.
- Calls the shared `validate_duty` function from the Flask JSON route.
- Shows the first applicable rule violation using the validator's existing order: daily, rest, then weekly.
- Rejects missing, non-numeric, Boolean, negative, NaN, infinite, and excessively large inputs at the API boundary.
- Provides a responsive dashboard with field-level input feedback, result states, and a reset action.

The educational rule assumptions are daily duty **≤ 10 hours**, rest **≥ 10 hours**, and rolling seven-day duty **≤ 60 hours**. Equality is allowed. These values have **not** been verified as aviation regulations and must not be used to approve real schedules.

The application does not calculate duty from timestamps, generate rosters, store crew data, connect to a production database, or demonstrate performance for 400 crew members. The interface is an academic prototype; Flask's development server is not suitable for production.

## Technology

- Python 3.14.7 (environment used for the recorded verification)
- Flask 3.1.3
- pytest
- Selenium with Chrome for the recorded browser checks
- HTML, CSS, and vanilla JavaScript

## Run locally

From the project root in PowerShell:

```powershell
.\venv\Scripts\python.exe hello.py
```

Open `http://127.0.0.1:5000/`. The `GET /about` route remains available.

The browser sends a JSON request to `POST /api/validate`, for example:

```json
{"daily": 8, "weekly": 42, "rest": 12}
```

A valid or rule-violating numeric schedule returns HTTP 200 with `valid`, `message`, and `violations` fields. Invalid request values return HTTP 400 with a specific message.

## Tests and checks

Run the full test suite:

```powershell
.\venv\Scripts\python.exe -B -m pytest -q -p no:cacheprovider
```

The current suite contains the original 20 validator tests and 16 Flask route/API test cases (parameterized cases included). The latest run completed with **36 passed**.

Static checks were run on the changed Python application and test files:

```powershell
.\venv\Scripts\python.exe -m pylint hello.py test_app.py
.\venv\Scripts\python.exe -m pylint duty_validator.py
.\venv\Scripts\python.exe -m flake8 hello.py test_app.py duty_validator.py
.\venv\Scripts\python.exe -m bandit -q hello.py duty_validator.py
```

Latest documented results: Pylint **10.00/10** for `duty_validator.py`; a separate Pylint run on `test_duty_validator.py` reported three style findings and **1.25/10**. Flake8 reported no findings in the three listed files, and Bandit reported no findings in the two listed Python files. These are scoped local checks, not a SonarQube scan.

The screenshots and execution notes from the live Chrome UI check are in `CASE57_LAB_EVIDENCE/UI_UX_REDESIGN/` and `UI_UX_REDESIGN_NOTES.md`.

## Project structure

```text
hello.py                         Flask page and JSON API
duty_validator.py                Shared duty rule logic
templates/dashboard.html         Dashboard and validator form
static/css/dashboard.css         Responsive visual design
static/js/validator.js           Client-side interaction and API call
test_duty_validator.py           Original validator tests
test_ai_generated.py             Original AI-generated test set
test_app.py                      Flask route and input-validation tests
Jenkinsfile                      Pipeline definition used by Jenkins builds #4-#6
compose.yaml                     Executed and verified PostgreSQL/validator stack
CASE57_LAB_EVIDENCE/             Per-lab records, screenshots, logs
```

## Practical status and limitations

Current audited official lab status: **17 COMPLETE, 5 PARTIAL, 3 PENDING HUMAN, 0 BLOCKED** (25 labs). AI-only substitute simulations are separately documented for L2.4, L4.2 and L5.1; they do not satisfy the human participation requirement. L3.4 has successful Jenkins runs but still lacks a deliberately induced failure-and-fix experiment; L3.5 has a successful one-shot Compose/database communication run.

- L2.4 still needs estimates from three actual classmates; the AI estimator roles are labeled simulations.
- L4.2 still needs genuine client/classmate review and sign-off; the fictional stakeholder simulation is not approval.
- L5.1 still needs a genuine peer review; role-based AI notes are not human findings.
- Jenkins build #6 (L3.4) checked out `https://github.com/manojshet2005/Airline-Crew-Scheduling..git` and passed 9 remote-branch tests. Build #3 failed at Pipeline DSL parsing; that was not a deliberate lab failure.
- Docker Compose (L3.5) built the validator image, connected to a healthy PostgreSQL service, and persisted validation rows. The validator exits after its one-shot task; evidence is in `CASE57_LAB_EVIDENCE/DOCKER/`.
- L5.2 records Pylint findings, not SonarQube findings. L5.3 is a local AI review of actual merged PR #7 with no GitHub comments; L5.4 records three runtime microbenchmark runs but still lacks SonarQube.

## GitHub status

The exact Git transport URL is `https://github.com/manojshet2005/Airline-Crew-Scheduling..git` (the repository name ends in a period). Jenkins build #6 successfully checked out the `feature/weekly-limit` branch. The exact remote was also verified read-only with `git ls-remote`; see the final task handover for the resulting commit and publication state. Generated report/PDF/PPT files and reference materials are kept separate from source/evidence commits.
