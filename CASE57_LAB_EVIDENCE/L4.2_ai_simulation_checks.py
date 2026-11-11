"""Verify the five technical outcomes used in the L4.2 AI simulation."""

from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from duty_validator import validate_duty
from hello import app


def main():
    cases = (
        ("A1 inclusive boundaries", (10, 40, 10), True, "accepted"),
        ("A2 daily violation", (10.01, 40, 12), False,
         "Daily duty limit exceeded."),
        ("A3 rest violation", (8, 40, 9.99), False,
         "Minimum rest requirement not met."),
        ("A4 weekly violation", (8, 60.01, 12), False,
         "Weekly duty limit exceeded."),
    )
    output = StringIO()
    with redirect_stdout(output):
        failures = 0
        print("L4.2 technical verification for AI-generated stakeholder simulation")
        for label, values, expected_valid, expected_message in cases:
            result = validate_duty(*values)
            actual = result[1]
            passed = result[0] is expected_valid and (
                expected_message == "accepted" or actual == expected_message
            )
            failures += not passed
            print(f"{label}: {result!r} | {'PASS' if passed else 'FAIL'}")

        with app.test_client() as client:
            response = client.post(
                "/api/validate",
                json={"daily": -1, "weekly": 40, "rest": 12},
            )
        passed = (
            response.status_code == 400
            and response.json["message"]
            == "Duty hours and rest hours cannot be negative."
        )
        failures += not passed
        print(
            "A5 negative input via Flask API: "
            f"HTTP {response.status_code}, {response.json!r} | "
            f"{'PASS' if passed else 'FAIL'}"
        )
        print(f"Scenarios: {len(cases) + 1}; passed: "
              f"{len(cases) + 1 - failures}; failed: {failures}")

    text = output.getvalue()
    log_path = Path(__file__).with_name("L4.2_ai_simulation_run.txt")
    log_path.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
