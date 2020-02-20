# Greet the client
print('=' * 60)
print('''Welcome to the DESTINATIO,
place where people plan their trips''')
print('=' * 60)

# Offer destinations
print('We can offer you the following destinations:')
print('-' * 60)

print('''

1 - Prague  | 1000

2 - Wien    | 1100

3 - Brno    | 2000

4 - Svitavy | 1500

5 - Zlin    | 2300

6 - Ostrava | 3400

''')
print('-' * 60)

# Get input from user about destination
user_choice = int(input('Please enter the destination number to select: 3'))

# Assign variables appropriate data
DESTINATIONS = ['Prague','Wien','Brno','Svitavy','Zlin','Ostrava']
PRICES = [1000, 1100, 2000, 1500, 2300, 3400]


# Get data from variables based on user's input
destination = DESTINATIONS[user_choice-1]
price = PRICES[user_choice-1]

# Introduce registration
print('=' * 60)
print('REGISTRATION:')
print('-' * 60)
print('In order to complete your reservations, please share few details about yourself with us.')
print('-' * 60)
# Get input from user about personal data
name = input('NAME')
print('=' * 60)
surname = input('SURNAME')
print('=' * 60)
year_of_birth = input('YEAR OF BIRTH')
print('=' * 60)
email = input('EMAIL')
print('=' * 60)
password = input('PASSWORD')
print('=' * 60)

# Thank user by the input name and inform him/her about the reservation made
print('Thank you ', name)
print('We have made your reservation to ' + destination)
print('The total price is ' + str(price))
