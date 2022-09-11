def main():
    time = input("What time is it? ").lower().strip()
    time = convert(time)
    if time == 1:
        print("breakfast time")
    elif time == 2:
        print("lunch time")
    elif time == 3:
        print("dinner time")

def convert(time):
    time = time.split(":")
    hour = int(time[0])
    min = int(time[1])
    if (7 == hour and 0 <= min <= 59 or hour == 8 and min == 0):
        return 1
    elif (12 == hour and 0 <= min <= 59 or hour == 13 and min == 0):
        return 2
    elif (18 == hour and 0 <= min <= 59 or hour == 19 and min == 0):
        return 3

if __name__ == "__main__":
    main()