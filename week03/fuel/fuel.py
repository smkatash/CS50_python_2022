def main():
    while True:
        value = str(input("Fraction: "))
        try:
            x, y = value.split("/")
            x = int(x)
            y = int(y)
            if x == y:
                print("F")
                break
            if x == 0:
                print("E")
                break
            if x < y:
                final = int(round(float(x / y) * 100))
                if final == 1:
                    print("E")
                    break
                elif final == 99:
                    print("F")
                    break
                else:
                    print(int(final), "%", sep="")
                    break
            continue
        except ValueError:
            continue
        except ZeroDivisionError:
            continue


main()