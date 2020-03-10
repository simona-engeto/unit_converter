# Results from previous task
candidates = ['Bruno', 'Agnes']
employees = ['Francis', 'Bruno', 'Ann', 'Jacob', 'Claire']



# Delete names from candidates
candidates.remove('Bruno')

# Print remaining candidates
print('Bruno removed from candidates: ', str(candidates))

# Repeat element
candidates = candidates * 3

# Print repeating element in list candidates
print('Repetition of Agnes in the candidate list: ', str(candidates))

# Join lists
employees = employees + candidates

# Print joined lists
print('Joined candidates and employees: ', str(employees))

# Index 2
print('On index 2 is: ', str(employees[2]))

# Find out last index and assign it to variable
last_index = len(employees) - 1

# Last index
print('On index', str(last_index), 'is: ', str(employees[last_index]))

