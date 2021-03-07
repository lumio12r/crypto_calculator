import json
import requests

currency = input("Type currency, which you have: ")
amount = int(input("Type how many money you have: "))
other_currency = input("Type currency, which you want: ")


r = requests.get('http://www.floatrates.com/daily/{}.json'.format(currency.lower()))
open("currency.json", 'wb').write(r.content)
with open("currency.json", "r") as file_json:
    currency_from_json = json.load(file_json)
currency_rate = currency_from_json[f'{other_currency}']['rate']
money_in_other_currency = round((currency_rate * amount), 2)
print("Okay let's change {} {} into {} {}".format(amount, currency.upper(), money_in_other_currency, other_currency.upper()))
