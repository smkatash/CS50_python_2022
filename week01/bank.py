def main():
    str = input("Bank: ").lower().strip().split()
    first_word = str[0]
    if "hello" in first_word:
        print("$0")
    elif "h" in first_word[0]:
        print("$20")
    else:
        print("$100")

main()