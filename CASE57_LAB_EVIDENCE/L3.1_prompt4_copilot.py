"""Copilot SDK retry of L3.1 Prompt 4; kept separate from app source."""

from math import isfinite


def validate_duty(
    hours_today: int | float,
    hours_last_7_days: int | float,
    rest_hours: int | float,
) -> tuple[bool, str]:
    """Apply the Case 57 sample duty rules; these are not verified law."""
    values = (hours_today, hours_last_7_days, rest_hours)
    for value in values:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError("Inputs must be finite, non-negative numbers.")
        try:
            finite = isfinite(value)
        except OverflowError:
            finite = False
        if not finite or value < 0:
            raise ValueError("Inputs must be finite, non-negative numbers.")

    rules = (
        (hours_today > 10, "Daily duty exceeds 10 hours."),
        (rest_hours < 10, "Rest is below 10 hours."),
        (hours_last_7_days > 60, "Rolling 7-day duty exceeds 60 hours."),
    )
    for violated, reason in rules:
        if violated:
            return False, reason
    return True, "All sample duty rules satisfied."


if __name__ == "__main__":
    cases = (
        (10, 60, 10),
        (8, 45, 12),
        (10.1, 50, 12),
        (8, 50, 9.9),
        (8, 60.1, 12),
        (11, 50, 9),
        (8, 61, 9),
        (-1, 40, 12),
        (True, 40, 12),
        ("8", 40, 12),
        (float("nan"), 40, 12),
        (8, float("inf"), 12),
    )
    for values in cases:
        try:
            print(f"{values!r} -> {validate_duty(*values)}")
        except ValueError as error:
            print(f"{values!r} -> ValueError: {error}")
