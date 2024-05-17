import requests


def convert_currency(amount, from_currency, to_currency):
    try:
        # Get the latest exchange rates from Fixer-API
        api_key = "API KEY"
        response = requests.get(
            f"https://data.fixer.io/api/latest?access_key={api_key}&base={from_currency}&symbols={to_currency}")

        # Parse the JSON response
        data = response.json()

        # Check if the API request was successful
        if not data["success"]:
            return f"Error: {data['error']['info']}"

        # Get the exchange rate for the desired currency
        rate = data["rates"].get(to_currency)

        # Check if the desired currency is supported
        if rate is None:
            return f"Error: {to_currency} is not a supported currency"

        # Calculate the converted amount
        converted_amount = amount * rate
        return converted_amount

    except requests.exceptions.RequestException as e:
        # Handle API request errors
        return f"Error: {e}"

    except Exception as e:
        # Handle any other errors
        return f"Error: {e}"


# Get user input
amount = float(input("Enter the amount: "))
from_currency = input("Enter the original currency: ").upper()
to_currency = input("Enter the desired currency: ").upper()

result = convert_currency(amount, from_currency, to_currency)

if "Error" in result:
    print(result)
else:
    print(f"{amount} {from_currency} is equal to {result} {to_currency}")
