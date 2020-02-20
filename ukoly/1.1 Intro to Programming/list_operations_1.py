# Results from previous task
candidates = ['Bruno', 'Agnes']
employees = ['Francis', 'Bruno', 'Ann', 'Jacob', 'Claire']



# Delete names from candidates
candidates.remove('Bruno')

# Print remaining candidates
print('Bruno removed from candidates: ', candidates )

# Repeat element
candidates = candidates * 3

# Print repeating element in list candidates
print('Repetition od Agnes in the candidate list: ', candidates)

# Join lists
employees = employees + candidates

# Print joined lists
print('Joined candidates and emloyees: ', employees)

# Index 2
print('On index 2 is: ', employees[2])

# Find out last index and assign it to variable
last_index = len(employees) - 1


# Last index
print('On ', str(last_index), " index is: ", employees[last_index])

