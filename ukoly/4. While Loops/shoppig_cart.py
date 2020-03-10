item1 = float(input('Enter the price: '))
item2 = float(input('Enter the price: '))
item3 = float(input('Enter the price: '))

shopping_cart = []
shopping_cart.append(item1)
shopping_cart.append(item2)
shopping_cart.append(item3)

shopping_cart = []
repeat = True

while repeat:
    item = float(input('Enter the price: '))
    shopping_cart.append(item)
    answer = input('Press enter to continue or "q" to quit: ')
    if answer == 'q':
        repeat = False

i = 0
repeat = True

while repeat:
    index = i % len(shopping_cart)
    print(shopping_cart[index])
    answer = input('Press enter to continue or "q" to quit: ')
    if answer == 'q':
        repeat = False
    else:
        i = i + 1

total_price = 0
i = 0
while i < len(shopping_cart):
    total_price = total_price + shopping_cart[i]
    i = i + 1
print('Cart: ', str(shopping_cart))
print('Total price is: ', str(total_price))


