from plates import is_valid


def test_letters1():
    assert is_valid("Hellor") == True
    assert is_valid("Hello, world") == False

def test_letters2():
    assert is_valid("AB12A") == False

def test_letters3():
    assert is_valid("YtG567") == True

def test_letters4():
    assert is_valid("!?AB2*") == False

def test_letters5():
    assert is_valid("ab12?") == False
    assert is_valid("CS") == True

def test_letters6():
    assert is_valid("CS05") == False

def test_letters7():
    assert is_valid("AB12345") == False

def test_letters8():
    assert is_valid("343") == False

def test_letters9():
    assert is_valid("Afgf8786") == False
