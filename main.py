import json
import requests

currency = input()

r = requests.get('http://www.floatrates.com/daily/{}.json'.format(currency.lower()))
open("currency.json", 'wb').write(r.content)
with open("currency.json", "r") as file_json:
    currency_from_json = json.load(file_json)
print(currency_from_json['usd'])
print(currency_from_json['eur'])