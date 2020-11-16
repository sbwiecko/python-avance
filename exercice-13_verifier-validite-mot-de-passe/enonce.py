import re

numeros_de_telephone = ['06-71-45-34-23',
                        '02-12-33-75-12',
                        '00-23-14-52-44',
                        '514-235-0293',
                        '03-52-31-56-34']

# straightforward solution
pat = r'\d{2}-\d{2}-\d{2}-\d{2}-\d{2}'

for num in numeros_de_telephone:
    validité = 'valide' if re.match(pat, num) else 'invalide'
    print(f"Le numéro {num} est {validité}")

# Le numéro 06-71-45-34-23 est valide
# Le numéro 02-12-33-75-12 est valide
# Le numéro 00-23-14-52-44 est invalide
# Le numéro 514-235-0293 est invalide
# Le numéro 03-52-31-56-34 est valide

# more 'pythonic' solution

pat = r'(\d{2}-){4}\d{2}'

for num in numeros_de_telephone:
    validité = 'valide' if re.match(pat, num) else 'invalide'
    print(f"Le numéro {num} est {validité}")
