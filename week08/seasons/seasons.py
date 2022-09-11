import sys
import datetime
from datetime import date
import inflect

p = inflect.engine()

def main():
    get_date = input("Date of Birth: ")
    valid_date = validate_date(get_date)
    difference_days = get_difference_min(valid_date)
    days_in_words = date_to_str(difference_days)
    print(days_in_words)

def validate_date(input_date):
    try:
        construct_date = date.fromisoformat(input_date)
        return construct_date
    except ValueError:
        sys.exit("Invalid date")

def get_difference_min(valid_date):
    today = date.today()
    days_to_min = today - valid_date
    return days_to_min.days * 24 * 60

def date_to_str(date):
    output = p.number_to_words(date, andword="")
    return output.capitalize() + " minutes"

if __name__ == "__main__":
    main()