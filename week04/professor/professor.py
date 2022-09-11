import random

def main():
    level = get_level()
    var = 0
    score = 0
    counter = 0
    for var in range(10):
        var -= 1
        x = generate_integer(level)
        y = generate_integer(level)
        try:
            check = x + y
            result = int(input(f"{x} + {y} = "))
            if result == check:
                score += 1
            while result != check:
                print("EEE")
                counter += 1
                result = int(input(f"{x} + {y} = "))
                if counter >= 2:
                    print("EEE")
                    print(f"{x} + {y} = {check}")
                    counter = 0
                    break
            continue
        except ValueError:
            print("EEE")
            continue
    print("Score: " + str(score))

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            assert 1 <= level < 4
            return level
        except ValueError:
            continue
        except AssertionError:
            continue

def generate_integer(level):
    try:
        if level == 1:
            num = random.randint(0, 9)
        elif level == 2:
            num = random.randint(10, 99)
        elif level == 3:
            num = random.randint(100, 999)
        return num
    except:
        raise ValueError

if __name__ == "__main__":
    main()