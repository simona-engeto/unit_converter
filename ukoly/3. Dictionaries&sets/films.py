#create dictionary
film = {}
film['name'] = 'Shawshank Redemption'
film['rating'] = 87
film['year'] = 1994
film['director'] = 'Frank Darabont'

#add a new category
film['starring'] = ['Tim Robbins', 'Morgan Freeman']
film['budget'] = 200

#remove 'budget'
del film['budget']

#nest a dict within another dict
films = {}
films['DRAMA'] = film
print(films)

#dictionary querying
print('We can currently offer: ')
print(list(films))
genre = input('What genre are you interested in? ')
print()
print('HERE IT GOES: ')
print(films[genre])

#clearing the dictionary
films.clear()
print('DATABASE HAS BEEN ERASED: ')
print(films)

