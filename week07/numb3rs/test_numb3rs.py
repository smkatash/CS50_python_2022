import pytest
import re
from numb3rs import validate

def main():
    test_format()
    test_input()

def test_format():
    assert validate(r"1.2.3.4.5.6") == False
    assert validate(r"1") == False
    assert validate(r"1.2.3") == False
    assert validate(r"255-255-255-0") == False
    assert validate(r"012/255/125/0") == False
    assert validate(r"012/255/125/0") == False
    assert validate(r"255.255.255.255") == True

def test_input():
    assert validate(r"512.512.512.512") == False
    assert validate(r"512.1.1.1") == False
    assert validate(r"1.512.1.1") == False
    assert validate(r"1.1.512.1") == False
    assert validate(r"1.1.1.512") == False
    assert validate(r"127.0.0.1") == True
    assert validate(r"255.255.255.255") == True
    assert validate(r"1.2.3.1000") == False
    assert validate(r"cat") == False

if __name__ == "__main__":
    main()