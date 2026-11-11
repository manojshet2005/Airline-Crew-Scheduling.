"""Duty-limit validation for airline crew scheduling."""


def validate_duty(hours_today, hours_last_7_days, rest_hours):
    """
    Validate a crew member's duty hours against the assumed rules.

    R1: Daily duty must not exceed 10 hours.
    R2: Rest between duties must be at least 10 hours.
    R3: Duty in 7 days must not exceed 60 hours.
    R4: Negative values are invalid.
    """

    for hours in (hours_today, hours_last_7_days, rest_hours):
        if hours < 0:
            raise ValueError("Duty hours and rest hours cannot be negative.")

    if hours_today > 10:
        return False, "Daily duty limit exceeded."

    if rest_hours < 10:
        return False, "Minimum rest requirement not met."

    if hours_last_7_days > 60:
        return False, "Weekly duty limit exceeded."

    return True, "Duty schedule accepted."


if __name__ == "__main__":
    test_inputs = [
        (8, 40, 12),
        (10.5, 40, 12),
        (8, 40, 9),
        (8, 65, 12),
        (8, 60, 10),
        (8, 60.5, 12)
    ]

    for values in test_inputs:
        try:
            result = validate_duty(*values)
            print(f"Input: {values} -> {result}")
        except ValueError as error:
            print(f"Input: {values} -> Error: {error}")
