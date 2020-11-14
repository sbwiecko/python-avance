import string

# print(string.ascii_lowercase)
print(string.ascii_lowercase.index('a'))

prenom = 'Astrid'

# A -> 1
# s -> 19
# t -> 20
# r -> 18
# i -> 9
# d -> 4

zp = zip(
    prenom,
    [string.ascii_lowercase.index(letter)+1 for letter in prenom.lower()]
)

print(list(zp))