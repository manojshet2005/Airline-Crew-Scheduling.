"""HTTP and input-validation tests for the Flask dashboard."""

import pytest

from hello import app


@pytest.fixture(name="client")
def test_client_fixture():
    """Provide an isolated Flask test client."""
    app.config.update(TESTING=True)
    with app.test_client() as test_client:
        yield test_client


def test_dashboard_renders_validator_and_sample_rules(client):
    """Render the UI with clearly labeled sample limits."""
    response = client.get("/")

    assert response.status_code == 200
    assert b"Check a duty schedule" in response.data
    assert b"not verified aviation regulations" in response.data
    assert b'id="daily"' in response.data


def test_about_route_is_preserved(client):
    """Keep the original informational route available."""
    response = client.get("/about")

    assert response.status_code == 200
    assert b"Airline Crew Scheduling" in response.data


def test_api_accepts_inclusive_boundaries(client):
    """Accept the equality values at each sample-rule boundary."""
    response = client.post(
        "/api/validate",
        json={"daily": 10, "weekly": 60, "rest": 10},
    )

    assert response.status_code == 200
    assert response.json == {
        "valid": True,
        "message": "Duty schedule accepted.",
        "violations": [],
    }


@pytest.mark.parametrize(
    ("payload", "message"),
    [
        (
            {"daily": 10.5, "weekly": 40, "rest": 12},
            "Daily duty limit exceeded.",
        ),
        (
            {"daily": 8, "weekly": 40, "rest": 9},
            "Minimum rest requirement not met.",
        ),
        (
            {"daily": 8, "weekly": 61, "rest": 12},
            "Weekly duty limit exceeded.",
        ),
    ],
)
def test_api_returns_each_rule_violation(client, payload, message):
    """Return the domain validator's specific violation reason."""
    response = client.post("/api/validate", json=payload)

    assert response.status_code == 200
    assert response.json["valid"] is False
    assert response.json["message"] == message
    assert response.json["violations"] == [message]


def test_api_rejects_negative_input(client):
    """Return a client error for negative duty or rest values."""
    response = client.post(
        "/api/validate",
        json={"daily": -1, "weekly": 40, "rest": 12},
    )

    assert response.status_code == 400
    assert response.json["message"] == (
        "Duty hours and rest hours cannot be negative."
    )


@pytest.mark.parametrize(
    "value",
    [True, "8", None, float("nan"), float("inf"), -float("inf"), 10**1000],
)
def test_api_rejects_non_numeric_boolean_and_non_finite_input(client, value):
    """Reject booleans, coercible strings, nulls and non-finite numbers."""
    response = client.post(
        "/api/validate",
        json={"daily": value, "weekly": 40, "rest": 12},
    )

    assert response.status_code == 400
    assert response.json["field"] == "daily"
    assert response.json["message"] == "Daily hours must be a finite number."


def test_api_rejects_missing_field(client):
    """Identify a required value that is absent from the request."""
    response = client.post(
        "/api/validate",
        json={"daily": 8, "weekly": 40},
    )

    assert response.status_code == 400
    assert response.json["field"] == "rest"


def test_api_rejects_non_object_body(client):
    """Reject arrays in place of the required JSON object."""
    response = client.post("/api/validate", json=[8, 40, 12])

    assert response.status_code == 400
    assert response.json["message"] == "Request body must be a JSON object."
