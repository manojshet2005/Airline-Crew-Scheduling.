"""Reproduce L5.3 AI review checks against PR #7 and the current validator."""

import math
import subprocess
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from duty_validator import validate_duty as current_validator

PR_COMMIT = "80531773790cecbc22b71cc8ed4de05687d6d690"


def load_pr_validator():
    source = subprocess.run(
        ["git", "show", f"{PR_COMMIT}:duty_validator.py"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    namespace = {}
    exec(compile(source, "PR7:duty_validator.py", "exec"), namespace)
    return namespace["validate_duty"]


def outcome(function, values):
    try:
        result = function(*values)
    except Exception as error:
        return type(error).__name__
    return "accept" if result[0] else "reject: " + result[1]


def main():
    pr_validator = load_pr_validator()
    probes = (
        ("boolean", (True, 40, 12)),
        ("string", ("8", 40, 12)),
        ("NaN", (math.nan, 40, 12)),
        ("positive infinity", (math.inf, 40, 12)),
        ("valid boundary", (10, 60, 10)),
    )
    print(f"PR #7 head commit: {PR_COMMIT}")
    print("Probe | PR #7 code | Current branch code")
    for name, values in probes:
        print(
            f"{name} | {outcome(pr_validator, values)} | "
            f"{outcome(current_validator, values)}"
        )


if __name__ == "__main__":
    main()
