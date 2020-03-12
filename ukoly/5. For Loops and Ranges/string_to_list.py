your_numbers = input('Hello, please write your numbers and press enter to confirm: ')
number = your_numbers.split(',')
result = []

for numb in number:
    numb = int(numb.strip())
    result.append(numb)

print('List:', result)