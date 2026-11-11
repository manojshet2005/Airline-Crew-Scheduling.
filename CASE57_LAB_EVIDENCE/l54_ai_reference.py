"""AI-generated reference implementation for the L5.4 comparison."""


def ai_reference(d, w, r):
    values = (d, w, r)
    if any(value < 0 for value in values):
        raise ValueError("Duty hours and rest hours cannot be negative.")
    rules = (
        (d > 10, "Daily duty limit exceeded."),
        (r < 10, "Minimum rest requirement not met."),
        (w > 60, "Weekly duty limit exceeded."),
    )
    for invalid, reason in rules:
        if invalid:
            return False, reason
    return True, "Duty schedule accepted."
