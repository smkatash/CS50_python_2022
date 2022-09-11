import pytest
from seasons import date_to_str

def test_seasons():
    assert date_to_str("525600") == "Five hundred twenty-five thousand, six hundred minutes"
    assert date_to_str("1051200") == "One million, fifty-one thousand, two hundred minutes"

if __name__ == "__main__":
    main()