import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    format = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s)
    if format:
        split = format.groups()
        if int(split[1]) > 12 or int(split[5]) > 12:
            raise ValueError
        start_time = transform_type(split[1], split[2], split[3])
        end_time = transform_type(split[5], split[6], split[7])
        final_time = start_time + ' to ' + end_time
        return final_time
    else:
        raise ValueError

def transform_type(hour, min, meridiem):
    update_hour = get_hour(int(hour), meridiem)
    if min == None:
        update_min = '00'
        time = f"{update_hour:02}" + ':' + update_min
    else:
        time = f"{update_hour:02}" + ':' + min
    return time

def get_hour(hour, meridiem):
    if meridiem == 'AM':
        if hour == 12:
            out_hour = 0
        else:
            out_hour = hour
    else:
        if hour == 12:
            out_hour = 12
        else:
            out_hour = hour + 12
    return out_hour

if __name__ == "__main__":
    main()