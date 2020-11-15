"""
Le but de l'exercice est de déterminer quels sont les fichiers manquants
dans la séquence des fichiers de 0001 à 0100 séparés dans les 2 dossiers
rendus_01 et rendus02 et de format 0000.jpg.
"""

import os

cur_dir = os.path.dirname(__file__)

dossier_rendu_01 = os.path.join(cur_dir, 'rendus_01')
dossier_rendu_02 = os.path.join(cur_dir, 'rendus_02')

fichiers_01 = os.listdir(dossier_rendu_01)
fichiers_02 = os.listdir(dossier_rendu_02)

# tous les fichiers attendus sont:
all_files = set(f"{i:04}.jpg" for i in range(1, 101))

# tous les fichiers présents dans les 2 dossiers
# on utilise l'union des sets créés à partir des listes des fichiers
all_present = set(fichiers_01) | set(fichiers_02)

# les fichiers manquants sont alors, au format liste triée
missing = sorted(list(all_files - all_present))

print(missing)