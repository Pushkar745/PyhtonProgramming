# Python program to demonstrate
# Defaultdict
from collections import defaultdict
# Defining a dict
d = defaultdict(list)
for i in range(5):
    d[i].append(i)
print("Dictionary with value as list:")
print(d)
