# Python program to demonstrate ChainMap
from collections import ChainMap
d1 = {'a': 1, 'b': 1}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
# Definig the chainmap
c = ChainMap(d1, d2, d3)
print(c)
