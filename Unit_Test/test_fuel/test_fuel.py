from fuel import convert, gauge
import pytest


def test_convert1():
    assert convert("1/2") == 50

def test_gauge1():
    assert gauge(99) == "F"

def test_gauge2():
    assert gauge(1) == "E"

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
         convert("1/0")
         convert("5/4")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
        convert("3/2")
def test_ve():
    with pytest.raises(ValueError):
        convert("sd")
        convert("s/d")
        convert("s/50")
    with pytest.raises(ValueError):
        convert("-5/10")
        convert("5/-3")
    with pytest.raises(ValueError):
        convert("1.5/3")
        convert("5/3")
def test_input():
    assert convert('1/4') == 25 and gauge(25) == "25%"

