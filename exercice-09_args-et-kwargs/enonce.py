import os

def concatenation_chemin(*args):
    return os.path.join('C:\\', *args)


chemin_complet = concatenation_chemin('Utilisateurs', 'ThibH', 'Images')
print(chemin_complet)
