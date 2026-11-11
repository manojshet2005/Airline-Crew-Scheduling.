"""Flask dashboard and API for the Case 57 duty-limit prototype."""

from math import isfinite
from flask import Flask, jsonify, render_template, request
from duty_validator import validate_duty

app = Flask(__name__)


@app.route("/")
def home():
    """Render the crew duty dashboard."""
    return render_template("dashboard.html")


@app.route("/about")
def about():
    """Describe the academic prototype."""
    return "Project: Airline Crew Scheduling | Case 57"


@app.post("/api/validate")
def validate():
    """Validate JSON duty totals with the shared domain validator."""
    payload = request.get_json()
    if not isinstance(payload, dict):
        message = "Request body must be a JSON object."
        return jsonify(valid=False, message=message), 400

    fields = ("daily", "weekly", "rest")
    values = {}
    for field in fields:
        value = payload.get(field)
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            return jsonify(
                valid=False,
                message=f"{field.title()} hours must be a finite number.",
                field=field,
            ), 400
        try:
            finite = isfinite(value)
        except OverflowError:
            finite = False
        if not finite:
            return jsonify(
                valid=False,
                message=f"{field.title()} hours must be a finite number.",
                field=field,
            ), 400
        values[field] = value

    try:
        is_valid, message = validate_duty(
            values["daily"], values["weekly"], values["rest"]
        )
    except ValueError as error:
        return jsonify(valid=False, message=str(error)), 400

    return jsonify(
        valid=is_valid,
        message=message,
        violations=[] if is_valid else [message],
    )


if __name__ == "__main__":
    app.run(debug=False)
