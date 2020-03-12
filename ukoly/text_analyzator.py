def repeat_char(char, num_repetitions):
    return char * num_repetitions
print(repeat_char('-',80))
print('Welcome to the app. Please log in: ')
username, password = input('USERNAME: '), input('PASSWORD: ')
print(repeat_char('-',80))

registered_user = dict(bob = '123', ann = 'pass123', mike = 'password123', liz = 'pass123')

if registered_user.get(username) != password:
    print('Incorrect username or password!')
    quit()

TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

print('We have', str(len(TEXTS)), 'texts to be analyzed.')
select_number = int(input('Enter a number btw. 1 and 3 to select: '))
if select_number == 0 or select_number > 3:
    print('Incorrect number!')
    quit()
print(repeat_char('-',80))

text = TEXTS[select_number-1].split()

words = []
while text:
    word = text.pop().strip('.,')
    if word:
        words.append(word)

lowercase = 0
uppercase = 0
titlecase = 0
numeric = 0
num_summed = 0

i = 0
while i < len(words):
    if words[i].istitle():
        titlecase += 1
    elif words[i].isupper():
        uppercase += 1
    elif words[i].islower():
        lowercase += 1
    elif words[i].isnumeric():
        numeric += 1
        num_summed += float(words[i])
    i += 1

print('There are', str(len(words)), 'words in the selected text.')
print('There are', str(titlecase), 'titlecase words')
print('There are', str(uppercase), 'uppercase words')
print('There are', str(lowercase), 'lowercase words')
print('There are', str(numeric), 'numeric strings')
print(repeat_char('-',80))

counts_words = {}
i = 0
length_word = len(words[i])
counts_words[length_word] = counts_words.get(length_word, 0) + 1
lengths_words = sorted(counts_words)
while i < len(lengths_words):
    length = lengths_words[i]
    frequencies = counts_words[length]
    if len(str(length)) == 1:
        str_len = ' ' + str(length)
    else:
        str_len = str(length)
    print(str_len, '*' * frequencies, frequencies)
    i += 1

print(repeat_char('-',80))
print('If we summed all the numbers in this text we would get: ' + str(num_summed))
print(repeat_char('-',80))