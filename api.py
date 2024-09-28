from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://api.freecurrencyapi.com/v1/"
API_KEY = "fca_live_y9PATg3ZtFnCK8fo0llN63IlaogK6hcqAowBJIs2"

printer = PrettyPrinter()

def get_currencies():
    url = f"{BASE_URL}currencies?apikey={API_KEY}"
    response = get(url).json()

    currencies = response.get('data', {})
    return currencies

def print_currencies(currencies):
    for code, details in currencies.items():
        name = details['name']
        symbol = details.get("symbol", "")
        print(f"{code} - {name} - {symbol}")

def exchange_rate(currency1, currency2):
    url = f"{BASE_URL}latest?apikey={API_KEY}&currencies={currency2}&base_currency={currency1}"
    response = get(url).json()
    
    rates = response.get('data', {})
    if not rates:
        print('Invalid currencies.')
        return None
    
    rate = rates.get(currency2)
    print(f"{currency1} -> {currency2} = {rate}")
    return rate

def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return
    
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount.")
        return

    converted_amount = rate * amount
    print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")
    return converted_amount

def main():
    currencies = get_currencies()
    print("Welcome to the currency converter!")
    print("List - lists the different currencies")
    print("Convert - convert from one currency to another")
    print("Rate - get the exchange rate of the two currencies")
    print()

    while True:
        command = input("Enter a command (q to quit): ").lower()

        if command == "q":
            break
        elif command == "list":
            print_currencies(currencies)
        elif command == "convert":
            currency1 = input("Enter a base currency: ").upper()
            amount = input(f"Enter an amount in {currency1}: ")
            currency2 = input("Enter a currency to convert to: ").upper()
            convert(currency1, currency2, amount)
        elif command == "rate":
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to convert to: ").upper()
            exchange_rate(currency1, currency2)
        else:
            print("Unrecognized command!")

main()
