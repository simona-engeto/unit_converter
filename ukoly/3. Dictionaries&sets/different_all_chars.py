string01 = 'Bratislava'
string02 = 'Budapest'

different = set(string01) ^ set(string02)
print('Different_characters: ', str(different))
all_characters = set(string01) | set(string02)
print('All characters: ', str(all_characters))