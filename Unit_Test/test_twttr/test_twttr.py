from twttr import shorten


def test_shorten():

    assert shorten("computer") == "cmptr"
    assert shorten("president") == "prsdnt"

def test_vowel():
    assert shorten("HousE") == "Hs"

def test_both():
    assert shorten("van2@.com") == "vn2@.cm"

