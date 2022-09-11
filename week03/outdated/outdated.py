import re

def main():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    transform_data(months)

def transform_data(months):
    while True:
        try:
            inp = str(input("Date: ")).strip().lower()
            if "/" in inp:
                str_date = re.split("/", inp)
                if 12 >= int(str_date[0]) > 0 and 31 >= int(str_date[1]) > 0:
                    print(str_date[2], str_date[0].zfill(2), str_date[1].zfill(2), sep="-")
                    break
            elif "," in inp:
                str_date = re.split(", | ", inp)
                if str_date[0].title() in months and 31 >= int(str_date[1]) > 0:
                    index = months.index(str_date[0].title()) + 1
                    print(str_date[2], str(index).zfill(2), str_date[1].zfill(2), sep="-")
                    break
        except ValueError:
            continue


main()