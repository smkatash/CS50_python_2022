import re

def main():
    print(validate(input("IPv4 Address: ").strip()))

def validate(ip):
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        nums = ip.split(".")
        for num in nums:
            if int(num) < 0 or int(num) > 255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()