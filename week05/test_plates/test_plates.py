from plates import is_valid

def main():
    test_default()
    test_numeric()
    test_zero()
    test_whitespace()

def test_default():
    assert is_valid("blablabla") == False
    assert is_valid("A") == False
    assert is_valid("A2") == False
    assert is_valid("HH") == True
    assert is_valid("2H") == False
    assert is_valid("HHHHHH") == True

def test_numeric():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("&A5A22") == False
    assert is_valid("&.*22 ") == False
    assert is_valid("PI3.14") == False
    assert is_valid("CS50P") == False
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True

def test_zero():
    assert is_valid("AAA54") == True
    assert is_valid("AAA05") == False

def test_whitespace():
    assert is_valid(". /))((") == False
    assert is_valid(".     .") == False
    assert is_valid(" ") == False


if __name__ == "__main__":
    main()