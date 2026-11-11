
import pytest
from duty_validator import validate_duty


def test_AI_01():
    assert validate_duty(0, 0, 10)[0] is True


def test_AI_02():
    assert validate_duty(10, 50, 10)[0] is True


def test_AI_03():
    assert validate_duty(10.01, 40, 12)[0] is False


def test_AI_04():
    assert validate_duty(8, 60, 10)[0] is True


def test_AI_05():
    assert validate_duty(8, 60.01, 12)[0] is False


def test_AI_06():
    assert validate_duty(8, 40, 9.99)[0] is False


def test_AI_07():
    with pytest.raises(ValueError):
        validate_duty(8, -0.1, 12)


def test_AI_08():
    with pytest.raises(ValueError):
        validate_duty(8, 40, -0.1)


def test_AI_09():
    with pytest.raises(ValueError):
        validate_duty(-0.1, 40, 12)


def test_AI_10():
    assert validate_duty(10, 60, 10)[0] is True
