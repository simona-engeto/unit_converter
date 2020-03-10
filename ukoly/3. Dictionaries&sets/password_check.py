data = {'user1': 'password1', 'Mark': '1234', 'Danny': 'qwert'}

username = input('Please enter username: ')
password = input('Please enter password: ')

if data.get(username) != password:
    print('Password or username is wrong')

elif data.get(username) == password:
    print('Permission granted')