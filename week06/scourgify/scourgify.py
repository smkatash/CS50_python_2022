import sys
import csv

def main():
    check_arguments()
    lst = file_opener(sys.argv[1])
    create_new_file(lst)
    sys.exit(0)

def check_arguments():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        format = sys.argv[1].split(".")[-1]
        if format != "csv":
            sys.exit("Invalid format")

def file_opener(csv_file):
    lst = []
    try:
        with open(csv_file) as file:
            before = csv.DictReader(file)
            for row in before:
                lst.append(row)
        lst = modify_list(lst)
        return lst
    except FileNotFoundError:
        sys.exit(f"Could not read {csv_file}")

def modify_list(lst):
    for dict in lst:
        name = dict['name'].split(",")
        dict['first'] = name[1].strip()
        dict['last'] = name[0].strip()
        del dict['name']
    return lst

def create_new_file(lst):
    header = ['first', 'last', 'house']
    with open(sys.argv[2], 'w') as new_file:
        writer = csv.DictWriter(new_file, fieldnames=header)
        writer.writeheader()
        writer.writerows(lst)


if __name__ == "__main__":
    main()