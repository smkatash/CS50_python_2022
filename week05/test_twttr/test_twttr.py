from twttr import shorten

def main():
    test_default()
    test_capital()
    test_number()

def test_default():
    assert shorten("hello world") == "hll wrld"
    assert shorten("One two three") == "n tw thr"
    assert shorten(".,/$") == ".,/$"

def test_capital():
    assert shorten("HeAdeR FilE") == "HdR Fl"

def test_number():
    assert shorten("123") == "123"

if __name__ == "__main__":
    main()