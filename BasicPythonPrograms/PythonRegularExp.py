import re

s = "Pushkar sudhir baviskar Manasi"
match = re.search(r"Pushkar", s)
print("start IndexL", match.start())
print("End Index:", match.end())
