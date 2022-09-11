import random

def main():
    n = get_input_value()
    launch_game(n)

def get_input_value():
    while True:
        try:
            n = int(input("Level: "))
            assert n > 1
            break
        except ValueError:
            continue
        except AssertionError:
            continue
    return n

def launch_game(n):
    num = random.randrange(1, n)
    while True:
        guess = get_guess_value()
        if guess == num:
            print("Just right!")
            break
        elif num > guess:
            print("Too small!")
            continue
        elif num < guess:
            print("Too large!")
            continue

def get_guess_value():
    while True:
        try:
            n = int(input("Guess: "))
            assert n > 1
            break
        except ValueError:
            continue
        except AssertionError:
            continue
    return n

if __name__ == "__main__":
    main()