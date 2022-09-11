import sys
import inflect

p = inflect.engine()

def main():
    names = []
    while True:
            try:
                name = input("Name: ").title()
                if len(name) < 1:
                    sys.exit(0)
                names.append(name)
            except EOFError:
                output = p.join(names)
                print("\nAdieu, adieu, to " + output)
                break
            else:
                continue


main()