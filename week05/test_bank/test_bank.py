from bank import value

def test_default():
    assert value("Hello, sir!") == 0
    assert value("Hello") == 0
    assert value("How are you?") == 20
    assert value("Hi") == 20

def test_fail():
    assert value("What's up?") == 100
    assert value("100$") == 100
    assert value("./0") == 100