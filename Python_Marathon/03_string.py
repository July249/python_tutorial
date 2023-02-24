phrase = "Giraffe Academy"

print("Giraffe Academy")
print('Giraffe\nAcademy')
print("Giraffe\'s Academy")
print(phrase)
print(phrase + " is cool") # Giraffe Academy is cool
print(phrase.lower()) # giraffe academy
print(phrase.islower()) # False
print(phrase.upper()) # GIRAFFE ACADEMY
print(phrase.isupper()) # False
print(phrase.upper().isupper()) # True
print(len(phrase)) # length function
print(phrase[0]) # G
print(phrase[-1]) # y
print(phrase.index("G")) # 0
print(phrase.index("a")) # 3
print(phrase.index("Acad")) # 8
# print(phrase.index('z')) # ValueError
print(phrase.replace("Giraffe", "Elephant")) # Elephant Academy
