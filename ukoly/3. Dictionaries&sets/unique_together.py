str1 = 'New York'
str2 = 'Yorkshire'

unique_together = set(str1) ^ set(str2)
print(list(unique_together))