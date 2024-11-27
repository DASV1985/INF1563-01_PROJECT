import requests

exchange_rates_url = 'https://v6.exchangerate-api.com/v6/de65b4f45307f78b3de4fcf0/latest/' 

print("Welcome, follow the instruction to get your curency exchange data")


base_currency = input("Enter the 3 letter base currency code: ").upper()
sec_currency = input("Enter the 3 letter secondary currency code: ").upper()
amount = float(input("Enter the amount tha you would like to exchange: "))


def get_echange_data(currency):

    url = f"{exchange_rates_url}/{currency}"
    response = requests.get(url)

    if response.status_code == 200:
        print("data successfully retrived")
        currency_data = response.json()
        return currency_data
    else:
        print("failed to retrive data")

exchange_rate = get_echange_data(base_currency)

if exchange_rate:
    exchange = exchange_rate["conversion_rates"][sec_currency]

else:
    print("data not found")

print(f"The current exchange rate for {sec_currency} is {exchange}")

exchanged_amount = amount * exchange

print(f"The amount you'll receive of {sec_currency} is {exchanged_amount}")
print(f"from {amount} {base_currency}")