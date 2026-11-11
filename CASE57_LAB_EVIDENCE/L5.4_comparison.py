"""Reproducible L5.4 comparison of the project and AI reference validators."""

import math
from pathlib import Path
import platform
import statistics
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from duty_validator import validate_duty as project_validator
from l54_ai_reference import ai_reference


CASES = (
    ("exact boundaries", (10, 60, 10), "accept"),
    ("typical valid", (8, 40, 12), "accept"),
    ("daily violation", (10.01, 40, 12), "daily"),
    ("rest violation", (8, 40, 9.99), "rest"),
    ("weekly violation", (8, 60.01, 12), "weekly"),
    ("daily before rest", (11, 40, 9), "daily"),
    ("rest before weekly", (8, 61, 9), "rest"),
    ("negative input", (-1, 40, 12), "ValueError"),
    ("boolean input", (True, 40, 12), "ValueError"),
    ("NaN input", (math.nan, 40, 12), "ValueError"),
)
EXTRA_CASES = (
    ("string input", ("8", 40, 12), "ValueError"),
    ("positive infinity", (8, math.inf, 12), "ValueError"),
)


def classify(function, values):
    try:
        valid, reason = function(*values)
    except ValueError:
        return "ValueError"
    except TypeError:
        return "TypeError"
    if valid:
        return "accept"
    if reason.lower().startswith("daily"):
        return "daily"
    if "rest" in reason.lower():
        return "rest"
    if "week" in reason.lower():
        return "weekly"
    return "other rejection"


def measure(function, cases, repeats, rounds):
    for _ in range(1000):
        for values in cases:
            function(*values)
    samples = []
    for _ in range(rounds):
        start = time.perf_counter_ns()
        for _ in range(repeats):
            for values in cases:
                function(*values)
        elapsed = time.perf_counter_ns() - start
        samples.append(elapsed / (repeats * len(cases)))
    return samples


def main():
    functions = (
        ("project", project_validator),
        ("AI reference", ai_reference),
    )
    matching = {name: 0 for name, _ in functions}
    print("Required ten shared behavior cases")
    print("Case | Expected | Project | AI reference")
    for name, values, expected in CASES:
        project = classify(project_validator, values)
        ai = classify(ai_reference, values)
        matching["project"] += project == expected
        matching["AI reference"] += ai == expected
        print(f"{name} | {expected} | {project} | {ai}")
    print(f"Required cases: {len(CASES)}")
    for name in matching:
        print(f"{name} matching expected outcomes: {matching[name]}/{len(CASES)}")
    for name, values, expected in EXTRA_CASES:
        project = classify(project_validator, values)
        ai = classify(ai_reference, values)
        print(f"Supplementary {name} | {expected} | {project} | {ai}")

    valid_cases = tuple(
        values for _, values, expected in CASES if expected == "accept"
    )
    repeats = 20_000
    rounds = 7
    print(
        "Benchmark: perf_counter_ns; warm-up=1000 invocations/case/tool; "
        f"rounds={rounds}; repeats={repeats}; valid cases/round="
        f"{len(valid_cases)}; calls/tool/round={repeats * len(valid_cases)}"
    )
    results = {}
    for round_index in range(rounds):
        ordered = functions if round_index % 2 == 0 else functions[::-1]
        for name, function in ordered:
            results.setdefault(name, []).append(
                measure(function, valid_cases, repeats, 1)[0]
            )
    for name in ("project", "AI reference"):
        samples = results[name]
        print(
            f"{name}: samples ns/call="
            + ", ".join(f"{sample:.1f}" for sample in samples)
        )
        print(
            f"{name}: sample range ns/call="
            f"{min(samples):.1f}-{max(samples):.1f}"
        )
        print(
            f"{name}: median ns/call={statistics.median(samples):.1f}; "
            f"median ms/20k-repeats over {len(valid_cases)} valid cases="
            f"{statistics.median(samples) * repeats * len(valid_cases) / 1e6:.3f}"
        )
    project_median = statistics.median(results["project"])
    ai_median = statistics.median(results["AI reference"])
    delta_pct = (ai_median - project_median) / project_median * 100
    print(f"AI-reference median vs project: {delta_pct:+.2f}% (positive is slower)")
    print(
        f"Python: {sys.version.split()[0]}; OS: {platform.platform()}; "
        f"CPU: {platform.processor() or 'not reported'}"
    )


if __name__ == "__main__":
    main()
