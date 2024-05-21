from numb3ers import validate
import pytest


def test_numb():
    assert validate("34.46.54.3") == True
    assert validate("64.74") == False

def test_lett():
    assert validate("cat") == False


def test_lett3():
    assert validate("4.5.56.1000") == False
    assert validate("57") == False
