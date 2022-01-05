# Python program to demonstrate writing to file
# Opeing a file
file1 = open('PushkarNew.txt', 'w')
l = ["This is Mumbai \n", "This is Paris \n", "This is Londaon \n "]
s = "Hello\n"
# Writing a string to file
file1.write(s)
# Writing multiple string at a time
file1.writelines(l)
# Closing File
file1.close()
# Checking if the data is written to file or not
file1 = open('PushkarNew.txt', 'r')
print(file1.read())
file1.close()
