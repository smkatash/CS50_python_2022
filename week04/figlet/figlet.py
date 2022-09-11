import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    if len(sys.argv) == 1:
        try:
            call_random(sys.argv, figlet)
        except:
            sys.exit("Invalid usage")
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "-font"):
        try:
            call_fonts(sys.argv, figlet)
        except:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

def call_random(argv, figlet):
    word = str(input("Input: ")).strip()
    f = random.choice(figlet.getFonts())
    figlet.setFont(font=f)
    print(figlet.renderText(word))


def call_fonts(argv, figlet):
    word = str(input("Input: ")).strip()
    figlet.getFonts()
    figlet.setFont(font=argv[2])
    print(figlet.renderText(word))

if __name__ == "__main__":
    main()
