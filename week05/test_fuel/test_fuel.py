import pytest
from fuel import convert, gauge

def main():
    test_convert()
    test_gauge()

def test_convert():
    with pytest.raises(ValueError):
        convert("three/four")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
    assert convert("1/4") == 25
    assert convert("4/4") == 100

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(25) == "25%"

if __name__ == "__main__":
    main()