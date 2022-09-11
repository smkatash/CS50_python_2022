import sys
import csv
from tabulate import tabulate

def main():
    file = check_arguments()
    table = file_opener(file)
    print(tabulate(table, headers="keys", tablefmt="grid"))

def check_arguments():
    if len(sys.argv) <= 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        csv_check = sys.argv[1].split(".")[-1]
        if csv_check != "csv":
            sys.exit("Not a CSV file")
        else:
            return sys.argv[1]

def file_opener(file):
    lst = []
    try:
        with open(file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                lst.append(row)
            return lst
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()