word = input('Give me some input: ')

if word.isalpha():
    print('Letters Only')
elif word.isnumeric():
    print('Numeric')
else:
    print('Mixed')