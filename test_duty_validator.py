
import pytest
from duty_validator import validate_duty


def test_TC_01():
    assert validate_duty(9.5, 40, 12)[0] is True


def test_TC_02():
    assert validate_duty(10.0, 40, 12)[0] is True


def test_TC_03():
    assert validate_duty(10.5, 40, 12)[0] is False


def test_TC_04():
    assert validate_duty(10.1, 40, 12)[0] is False


def test_TC_05():
    assert validate_duty(8.0, 40, 9.5)[0] is False


def test_TC_06():
    assert validate_duty(8.0, 40, 10.0)[0] is True


def test_TC_07():
    assert validate_duty(8.0, 60.0, 12)[0] is True


def test_TC_08():
    assert validate_duty(8.0, 60.5, 12)[0] is False


def test_TC_09():
    with pytest.raises(ValueError):
        validate_duty(-1.0, 40, 12)


def test_TC_10():
    with pytest.raises(ValueError):
        validate_duty(8.0, 40, -2)
