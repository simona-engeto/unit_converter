your_number = int(input('Please enter your number: '))

result = 0

while your_number:
    result = result + your_number ** your_number
    your_number = your_number - 1

print(result)