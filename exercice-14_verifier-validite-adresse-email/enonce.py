import re

adresses_mail = ['christian_martin@gmail.com',
                 'JaiOublieLarobasegmail.com',
                 'MarieHutchinson03523@yahoo.co.uk',
                 'UnEaDreSSeMail!38BIZarre@unSiTeBizarre.com',
                 'ceciNestPasUneDresseMail']

# prefix = 1+ alphanum printable char incl [_.#!] but followed by 1+ letter/num
# dot should be not 1st nor last, and no consecutive
# domain = 1+ letter/number or dash with last portion with 2+ char
pat = r'(?P<prefix>\w+.+\w+)@(?P<domain>\w+.\w+\.[a-zA-Z]{2,})'

for address in adresses_mail:
    validite = 'valide' if re.match(pat, address) else 'invalide'
    print(f"L'adress {address} est {validite}")

# L'adresse christian_martin@gmail.com est valide
# L'adresse JaiOublieLarobasegmail.com est invalide
# L'adresse MarieHutchinson03523@yahoo.co.uk est valide
# L'adresse UnEaDreSSeMail!38BIZarre@unSiTeBizarre.com est valide
# L'adresse ceciNestPasUneDresseMail est invalide
