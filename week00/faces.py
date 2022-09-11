def main():
    str = input()
    if ":(" in str:
        str = str.split(":(")
        str = "🙁".join(str)
    if ":)" in str:
        str = str.split(":)")
        str = "🙂".join(str)
    print(str)

main()