coordinates = (4, 5)
# coordinates[1] = 10 # TypeError: 'tuple' object does not support item assignment

print(coordinates) # (4, 5)
print(coordinates[0]) # 4
print(coordinates[1]) # 5

list = [(4, 5), (6, 7), (80, 34)]
list[1] = (66, 77)
print(list) # [(4, 5), (66, 77), (80, 34)]
print(list[1][0]) # 66
