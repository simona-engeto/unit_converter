# Results from the previous task
candidates = ['Agnes', 'Agnes', 'Agnes']
employees = ['Francis', 'Bruno', 'Ann', 'Jacob', 'Claire', 'Agnes', 'Agnes', 'Agnes']


# Interval 2-5
print('In interval from 2 to 5 is: ', employees[2:6])

# Each 3rd
print('Every third member is: ', employees[::3])

# Save index
jacob_index = employees.index('Jacob')

# Jacob index
print('Jacob is on the index: ', jacob_index)

# Number of name Agnes
print('Number of Agnes names in the sheet: ', employees.count('Agnes'))