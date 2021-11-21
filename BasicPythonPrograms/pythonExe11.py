#Write a Program to extract each digit from an integer in the reverse order
number = 7536
print("Given number is  ",number)
while number >0:
    digit =number %10
    number =number // 10
    print(digit,end="")