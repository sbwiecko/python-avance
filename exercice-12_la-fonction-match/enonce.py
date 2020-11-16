# %%
import re

# %%
re.match(r'[a-z]+\d{2}', 'item01')
# un ou plusieurs char minuscucles suivis de 2 char décimaux

re.match(r'[a-zA-Z]+\s\w+', 'Pierre Dupont')
# un ou plusieurs char minus ou maj suvis d'un espace et de un ou plus alphanum

re.match(r'\s+', 'pierre dupont')
# un ou plusieurs espaces -> FALSE

re.match(r'\w+', 'pierre dupont')
# un ou plusieurs alphanum, incl char min et maj
# ATTENTION ne retourne que 'pierre' car espace non inclu dans pattern

re.match(r'\w+([-+=]?)', 'pierre-dupont')
# un ou plusieurs alphanum suivi d'un group de 0 ou plus -, + ou =
# retourne 'pierre-'

re.match(r'\w+([-+=]?)', 'pierre/dupont')
# same as above, / is not included in [-+=] so only 'pierre' returned

re.match(r'\w+([-+=]+)', 'pierre/dupont')
# 1+ alphanum followed by 1+ [-+=] -> no pattern
