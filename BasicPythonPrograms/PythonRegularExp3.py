from re import split

# Another
import re

#'W+' denotes Non-Alphanumeric char or group of char upon finding ','
# or whitespace ',the split(),splits the string from that point
print(split("\W+ ", "Words,Words Words"))
print(split("\W+", "Words words Words"))
# Here ':','' are not AlphaNumeric thus , #The point where splitting occurs
print(split("\W+ ", "On 12th Jan 2016 , at 11:2 "))
print(split("\d+", "On 12th JAn 2016,at 11:02 am "))
# Splitting will occurs only onec ,at '12' returned list will have length 2
print(re.split("\d+", "On 12th Jan 2016 ,at 11.02 am", 1))
print(re.split("[a-f]+", "Aey ,Boy oh boy,come here", flags=re.IGNORECASE))
print(re.split("[a-f]+", "Aey ,Boy oh boy,come here"))
