"""
Dans cet exercice, nous allons écrire 5 millions de nombres aléatoires dans un fichier 'nombres_aleatoires.txt'.
Nous utilisons pour ceci une chaîne de caractère que nous construisons au fur et à mesure de notre boucle.
Pour finir, nous écrivons cette gigantesque chaîne de caractère dans le fichier texte.

Le temps total de l'opération sur mon ordinateur avec cette méthode est d'environ 75 secondes.
Votre objectif est d'optimiser le temps d'exécution de ce script en utilisant les notions que nous avons vues
dans les parties précédentes. Il vous faudra donc utiliser un objet muable à la place de la chaîne de caractère.
"""

import os
from time import time
from random import randint

cur_dir = os.path.dirname(__file__)
fichier = os.path.join(cur_dir, 'nombres_aleatoires.txt')

a = time()

# nombre_aleatoire = ''
# for i in range(5000000):
#     nombre_aleatoire += str(randint(0, 9999))
#     nombre_aleatoire += '\n'

# with open(fichier, 'w') as f:
#     f.write(nombre_aleatoire) # -> 42.96 s

# with open(fichier, 'w') as f:
#     for i in range(5_000_000):
#         f.write(str(randint(0, 9999)) + '\n')  # -> 12.54 s

# import numpy as np
# numbers = np.random.randint(0, 9999, 5_000_000)
# with open(fichier, 'w') as f:
#     numbers.tofile(f, sep='\n', format='%s') # -> 3.86 s

def gen_numbers():
    for i in range(5_000_000):
        yield str(randint(0, 9999))

with open(fichier, 'w') as f:
    f.writelines(list(gen_numbers()))  # -> 9.84 s

b = time()

print('Temps d\'execution: {}'.format(b - a))

