"""Verify source claims used in the L5.1 AI review simulation."""

from contextlib import redirect_stdout
from io import StringIO
import math
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from duty_validator import validate_duty
from hello import app


def main():
    checks = (
        ("inclusive boundaries", (10, 60, 10), True),
        ("daily reason precedence", (11, 61, 9), False),
        ("rest reason after daily", (8, 61, 9), False),
    )
    output = StringIO()
    failures = 0
    with redirect_stdout(output):
        print("L5.1 focused checks for the AI review simulation")
        for name, values, expected_valid in checks:
            result = validate_duty(*values)
            passed = result[0] is expected_valid
            if name == "daily reason precedence":
                passed = passed and result[1] == "Daily duty limit exceeded."
            elif name == "rest reason after daily":
                passed = passed and result[1] == "Minimum rest requirement not met."
            failures += not passed
            print(f"{name}: {result!r} | {'PASS' if passed else 'FAIL'}")

        invalid_values = (
            ("boolean", True),
            ("string", "8"),
            ("NaN", math.nan),
            ("positive infinity", math.inf),
            ("negative value", -1),
        )
        for name, value in invalid_values:
            try:
                validate_duty(value, 40, 12)
            except ValueError:
                passed = True
            else:
                passed = False
            failures += not passed
            print(f"{name} rejected with ValueError: "
                  f"{'PASS' if passed else 'FAIL'}")

        print(f"Flask debug mode disabled: {not app.debug}")
        print("Focused input/precedence checks: "
              f"{len(checks) + len(invalid_values) + 1 - failures} passed; "
              f"{failures} failed.")

    text = output.getvalue()
    log_path = Path(__file__).with_name("L5.1_ai_review_checks_run.txt")
    log_path.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    if failures or app.debug:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
