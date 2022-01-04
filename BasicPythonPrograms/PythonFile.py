file = open('Pushkar.txt', 'r')
# This will print every line one by one in the file
for each in file:
    print(each)
# Python code to illustrate read() mode
print(file.read())
print(file.read(5))
