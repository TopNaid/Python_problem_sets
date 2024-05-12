import requests
import sys

try:
    try:
        if len(sys.argv) < 2:
            print("Missing Command-line argument")
            sys.exit(1)
        number = float(sys.argv[1])
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        p = response.json()
        price = p["bpi"]["USD"]["rate_float"]
        total_cost = number * price
        print(f"${total_cost:,.4f}")
    except ValueError:
        sys.exit("Input not a number")


except requests.RequestException:
    sys.exit("Error fetching data from API")


