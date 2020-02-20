# Prices
mercedes    = 150
rolls_royce = '400'
extra_cost = int(input("Price your extra_cost: "))

#Calculate
price_two_mercedes = mercedes * 2
price_mercedes_rolls_royce = mercedes + int(rolls_royce)
price_two_rolls_royce_extra_cost = int(rolls_royce) * 2 + 2 * extra_cost
price_mercedes_extra_cost = mercedes + extra_cost

#Print
print('Price for two mercedes is ', price_two_mercedes, ' ', 'USD')
print('Price for mercedes and rolls royce is ', price_mercedes_rolls_royce, ' ', 'USD')
print('Price for two rolls roys with extra cost is ', price_two_rolls_royce_extra_cost, ' ', 'USD')
print('Price for mercedes with extra cost is ', price_mercedes_extra_cost, ' ', 'USD')