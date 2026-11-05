
import pytest
from duty_validator import validate_duty


def test_valid_schedule():
    assert validate_duty(8, 40, 12)[0] is True


def test_daily_limit_exceeded():
    assert validate_duty(10.5, 40, 12)[0] is False


def test_minimum_rest_not_met():
    assert validate_duty(8, 40, 9)[0] is False


def test_weekly_limit_exceeded():
    assert validate_duty(8, 65, 12)[0] is False


def test_daily_limit_boundary():
    assert validate_duty(10, 40, 10)[0] is True


def test_weekly_limit_boundary():
    assert validate_duty(8, 60, 10)[0] is True


def test_negative_daily_hours():
    with pytest.raises(ValueError):
        validate_duty(-1, 40, 12)


def test_negative_weekly_hours():
    with pytest.raises(ValueError):
        validate_duty(8, -1, 12)


def test_negative_rest_hours():
    with pytest.raises(ValueError):
        validate_duty(8, 40, -1)
