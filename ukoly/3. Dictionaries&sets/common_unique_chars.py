string01 = 'Bratislava'
string02 = 'Budapest'

common = set(string01) & set(string02)
print('Common characters: ', str(common))
unique = set(string01) - set(string02)
print('Unique characters: ', str(unique))