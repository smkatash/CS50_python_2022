import sys

def main():
    filename = check_arguments()
    syntax = filename.split(".")[-1]
    if "py" == syntax:
        lines = file_opener(filename)
    else:
        sys.exit("Not a Python file")
    print(lines)

def check_arguments():
    if len(sys.argv) <= 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        filename = sys.argv[1]
        return filename

def file_opener(filename):
    counter = 0
    try:
        with open(filename) as file:
            lines = file.read().splitlines()
            counter = len(lines)
            for line in lines:
                update_line = line.rstrip().strip().split('\n')
                for word in update_line:
                    if len(word) < 1:
                        counter -= 1
                    elif len(word) > 0 and word.startswith("#"):
                        counter -= 1
        return  counter
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()