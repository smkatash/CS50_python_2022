def main():
    str = input("Interpret: ").lower().strip()
    x, y, z = str.split(" ")
    x = int(x)
    z = int(z)
    if "+" in y:
        result = float(x + z)
    elif "-" in y:
        result = float(x - z)
    elif "*" in y:
        result = float(x * z)
    elif "/" in y:
        result = float(x / z)
    print(result)


main()