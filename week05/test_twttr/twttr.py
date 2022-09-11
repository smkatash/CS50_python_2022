def main():
    str = input("Input: ").strip()
    word = shorten(str)
    print(word)

def shorten(str):
    omit = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    word = ""
    for c in str:
        if c not in omit:
            word += c
    return word

if __name__ == "__main__":
    main()