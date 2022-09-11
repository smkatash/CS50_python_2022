def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    fuel = gauge(percentage)
    print(fuel)

def convert(fraction):
    while True:
        try:
            values = fraction.split('/')
            x = int(values[0])
            y = int(values[1])
            fraction = (x / y) * 100
            if x > y:
                fraction = input("Fraction: ")
            return int(fraction)
        except ValueError:
            raise ValueError
        except ZeroDivisionError:
            raise ZeroDivisionError

def gauge(percentage):
    if percentage == 75:
        return "75%"
    elif percentage >= 50 and percentage <= 74:
        return "50%"
    elif percentage >= 25 and percentage <= 49:
        return "25%"
    elif percentage >= 76 and percentage <= 100:
        return "F"
    elif percentage >= 0 and percentage <= 24:
        return "E"

if __name__ == "__main__":
    main()