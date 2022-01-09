from re import split

#'W+' denotes Non-Alphanumeric char or group of char upon finding ','
# or whitespace ',the split(),splits the string from that point
print(split("\W+ ", "Words,Words Words"))
print(split("\W+", "Words words Words"))
# Here ':','' are not AlphaNumeric thus , #The point where splitting occurs
print(split("\W+ ", "On 12th Jan 2016 , at 11:2 "))
print(split("\d+", "On 12th JAn 2016,at 11:02 am "))
