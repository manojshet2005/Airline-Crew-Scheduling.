"""Re-run the preserved ChatGPT and Copilot L1.3 outputs on shared cases."""

import math
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from duty_validator import validate_duty


def chatgpt_validate_duty(hours_today, hours_last_7_days, rest_hours):
    values = (hours_today, hours_last_7_days, rest_hours)
    for value in values:
        if type(value) not in (int, float):
            raise ValueError("Inputs must be finite, non-negative numbers.")
        if isinstance(value, float) and not math.isfinite(value):
            raise ValueError("Inputs must be finite, non-negative numbers.")
        if value < 0:
            raise ValueError("Inputs must be finite, non-negative numbers.")

    if hours_today > 10:
        return False, "Daily duty exceeds 10 hours."
    if rest_hours < 10:
        return False, "Rest is below 10 hours."
    if hours_last_7_days > 60:
        return False, "Rolling 7-day duty exceeds 60 hours."
    return True, "All sample duty rules satisfied."


def copilot_validate_duty(hours_today, hours_last_7_days, rest_hours):
    values = (hours_today, hours_last_7_days, rest_hours)
    for value in values:
        if (
            type(value) not in (int, float)
            or (isinstance(value, float) and not math.isfinite(value))
            or value < 0
        ):
            raise ValueError("Inputs must be finite, non-negative numbers.")

    checks = (
        (hours_today > 10, "Daily duty exceeds 10 hours."),
        (rest_hours < 10, "Rest is below 10 hours."),
        (hours_last_7_days > 60, "Rolling 7-day duty exceeds 60 hours."),
    )
    for violated, reason in checks:
        if violated:
            return False, reason
    return True, "All sample duty rules satisfied."


CASES = (
    ("exact boundaries", (10, 60, 10)),
    ("ordinary valid", (8, 45, 12)),
    ("daily over", (10.1, 50, 12)),
    ("rest under", (8, 50, 9.9)),
    ("weekly over", (8, 60.1, 12)),
    ("daily and rest", (11, 50, 9)),
    ("rest and weekly", (8, 61, 9)),
    ("all rules", (11, 61, 9)),
    ("negative", (-1, 40, 12)),
    ("boolean", (True, 40, 12)),
    ("string", ("8", 40, 12)),
    ("NaN", (math.nan, 40, 12)),
    ("positive infinity", (8, math.inf, 12)),
    ("negative infinity", (8, 40, -math.inf)),
)


def classify(function, values):
    try:
        valid, reason = function(*values)
    except ValueError:
        return "ValueError"
    if valid:
        return "Accept"
    if reason.startswith("Daily"):
        return "Daily rejection"
    if "rest" in reason.lower():
        return "Rest rejection"
    if "week" in reason.lower() or "rolling" in reason.lower():
        return "Weekly rejection"
    return "Other rejection"


def main():
    functions = (
        ("ChatGPT", chatgpt_validate_duty),
        ("Copilot SDK", copilot_validate_duty),
        ("Project", validate_duty),
    )
    matches = {name: 0 for name, _ in functions}
    print("Case | Expected | ChatGPT | Copilot SDK | Project")
    for name, values in CASES:
        expected = classify(chatgpt_validate_duty, values)
        outcomes = [
            classify(function, values) for _, function in functions
        ]
        for (tool_name, _), outcome in zip(functions, outcomes):
            matches[tool_name] += outcome == expected
        print(
            f"{name} | {expected} | {outcomes[0]} | "
            f"{outcomes[1]} | {outcomes[2]}"
        )
    print(f"Shared cases: {len(CASES)}")
    for name, count in matches.items():
        print(f"{name} matching ChatGPT semantic outcomes: {count}/{len(CASES)}")


if __name__ == "__main__":
    main()
