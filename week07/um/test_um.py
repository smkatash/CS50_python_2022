import pytest
from um import count

def main():
    test_default()
    test_count()

def test_default():
    assert count("umbrella") == 0
    assert count("album") == 0
    assert count("hm, um, number is not matching") == 1

def test_count():
    assert count("Um, thanks for the album.") == 1
    assert count("um?") == 1
    assert count("Um, thanks, um...") == 2


if __name__ == "__main__":
    main()