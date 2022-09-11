def main():
    dict = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    place_order(dict)

def place_order(dict):
    total = 0
    while True:
        try:
            item = input("Item: ").title()
            if item in dict:
                total += float(dict[item])
                print("Total $""%.2f" % total)
        except EOFError:
            print()
            break
        except ValueError:
            continue


main()