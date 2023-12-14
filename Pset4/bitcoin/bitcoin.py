import requests
import sys

if len(sys.argv) == 2:
    val = sys.argv[1]

    try:
        val = float(val)
    except ValueError:
        sys.exit("Command-line argument is not a number")

elif len(sys.argv) == 1:
    sys.exit("Missing command-line argument")

try:
    req = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    btc_usd = req.json()["bpi"]["USD"]["rate_float"]
    converted = btc_usd * val
    print(f"${converted:,.4f}")

except requests.RequestException:
    sys.exit("Something went wrong during requests!")
