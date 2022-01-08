import re

s = "Raising of devil.Pushkar "
# Without Using \
match = re.search(r".", s)
print(match)
# Using \
match = re.search(r"\.", s)
print(match)
