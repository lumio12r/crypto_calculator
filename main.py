amount = int(input('Please, enter the number of litecoins you have: '))
cost_per_one = float(input('Please, enter the exchange rate: '))
cost_per_all = amount * cost_per_one
print("The total amount of dollars: {}".format(cost_per_all))