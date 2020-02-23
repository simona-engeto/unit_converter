give_number = input('Please, give me a number: ')

if give_number == '':
    print('No input provided')

else:
    deleni = len(give_number) // 2

first_half = int(give_number[:deleni])
second_half = int(give_number[deleni:])

if first_half % 2 == 0 and second_half % 2 == 0:
    print('Success')
elif first_half % 2 == 0:
    print('First')
elif second_half % 2 == 0:
    print('Second')
else:
    print('Neither')