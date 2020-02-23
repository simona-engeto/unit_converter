my_new_dict = {'m': 12345, 'n': 32145, 'o': 54321, 'p': 23232, 'q': 43210, 'r': 13579}
maximal_value_of_key = max(my_new_dict.keys())
print('The maximal value of key is: ', maximal_value_of_key)

maximal_value = max(my_new_dict.values())

if maximal_value > my_new_dict[maximal_value_of_key]:
    del my_new_dict[maximal_value_of_key]

print(my_new_dict)