# A Python program to demonstrate working of findall()
import re

# A sample text string where regular expression is searched
string = """ Hello my number is 123456789 and my friend's number is 987654321"""
# A Sample regular expressin=on to find digits
regex = "\d+"
match = re.findall(regex, string)
print(match)
