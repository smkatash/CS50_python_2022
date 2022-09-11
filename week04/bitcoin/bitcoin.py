import json
import sys
import requests

def main():
    try:
        if float(sys.argv[1]):
            get_request(float(sys.argv[1]))
    except ValueError:
        sys.exit("Command-line argument is not a number")
    except IndexError:
        sys.exit("Missing command-line argument")

def get_request(amount):
    try:
        rget = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response = rget.json()
        rate = response['bpi']['USD']['rate_float']
        result = rate * amount
        print(f"${result:,.4f}")
    except requests.RequestException:
        sys.exit("RequestException")

if __name__ == "__main__":
    main()
