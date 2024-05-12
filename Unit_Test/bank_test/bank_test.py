from bank import value


def test_hello():
    assert value("Hello") == 0

def test_hey():
    assert value("Hey") == 20

def test_what_up():
    assert value("what's Up") == 100


