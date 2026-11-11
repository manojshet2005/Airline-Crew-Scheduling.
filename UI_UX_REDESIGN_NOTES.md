# Case 57 UI/UX redesign notes

## Scope and implementation

The saved project previously had only a Flask greeting page and an `/about` route. The existing `duty_validator.py` was retained as the single source of rule logic. The dashboard now calls that validator through a Flask JSON endpoint; no parallel copy of the duty rules was added.

- `hello.py` now renders the dashboard and exposes `POST /api/validate`.
- `templates/dashboard.html` contains the responsive crew-duty interface, accessible inputs, sample-rule caveat, and result panel.
- `static/css/dashboard.css` implements the navy/teal visual system, rule cards, spacing, status colors, and tablet/mobile layouts.
- `static/js/validator.js` handles input feedback, asynchronous validation, success/violation/error states, and reset.
- `test_app.py` covers page/routes, rule boundaries and reasons, and invalid input handling.

The dashboard deliberately does not show fabricated operational metrics, roster data, live alerts, or database status. It stores no crew data and is not a production-ready airline interface.

## Input and response behavior

The route calls `validate_duty` for valid finite numeric values. It rejects missing fields, strings, Booleans, nulls, negative values, NaN, positive/negative infinity, and numbers too large for the finite-number check. Business-rule rejections preserve the validator's exact first reason. Missing or invalid request values return HTTP 400; valid and rule-violating numeric schedules return HTTP 200.

The three displayed limits (daily ≤ 10 hours, rest ≥ 10 hours, rolling seven-day ≤ 60 hours) are sample educational assumptions, not verified aviation regulations.

## Verification actually performed

- Full pytest suite: **36 passed**.
- Real Chrome run against the live Flask app: valid schedule, daily violation, rest violation, weekly violation, reset, and missing-field error.
- Mobile viewport: 390 × 844; the page fit without horizontal overflow and the validator action remained available.
- Pylint: **10.00/10** on `hello.py`, `test_app.py`, and `duty_validator.py` (separate invocations).
- Flake8: **no findings** on `hello.py`, `test_app.py`, and `duty_validator.py`.
- Bandit: **no findings** on `hello.py` and `duty_validator.py`.
- Seven genuine screenshots were saved in `CASE57_LAB_EVIDENCE/UI_UX_REDESIGN/`.

The original L4.3 plain/POM Selenium screenshots are still from their local fixture. The newer screenshots document a separate run against the live Flask dashboard; neither set changes the historical lab status audit.
