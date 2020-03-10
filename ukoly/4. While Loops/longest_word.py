words = ['Python', 'is', 'a', 'widely', 'used',

         'high-level', 'programming', 'language',

         'for', 'general-purpose', 'programming,',

         'created', 'by', 'Guido', 'van', 'Rossum',

         'and', 'first', 'released', 'in', '1991.']

longest_word = ('', 0)

while words:
    word = words.pop(0)
    if len(word) > longest_word[1]:
        longest_word = word, len(word)

print(longest_word)