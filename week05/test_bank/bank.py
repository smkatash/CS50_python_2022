def main():
    greeting = input("Greeting: ").strip()
    val = str(value(greeting))
    print("$" + val)

def value(greeting):
    if greeting.startswith("Hello"):
        x = 0
    elif greeting.startswith("H"):
        x = 20
    else:
        x = 100
    return x

if __name__ == "__main__":
    main()