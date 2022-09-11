def main():
    str = input("What is the Answer to the Great Question of Life... the Universe... and Everything? ").lower().strip()
    match str:
        case "42":
            print("Yes")
        case "forty two":
            print("Yes")
        case "forty-two":
            print("Yes")
        case other:
            print("No")

main()