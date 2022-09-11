def main():
    camel = input("camelCase: ").strip()
    print("snake_case: ",end="")
    for c in camel:
        if c.isupper() == True:
            print("_", end="")
            c = c.lower()
        print(c, end="")
    print()

main()