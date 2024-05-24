from seasons import minutes
import pytest


def test_minutes1():
    with pytest.raises(SystemExit):
        minutes("rat")
    with pytest.raises(SystemExit):
        minutes("2022-june-02")


def test_minutes2():
    assert minutes("1999-12-31") == "Twelve million, eight hundred twenty-eight thousand, nine hundred sixty minutes"
    assert minutes("2022-09-08") == "Eight hundred ninety-five thousand, six hundred eighty minutes"
