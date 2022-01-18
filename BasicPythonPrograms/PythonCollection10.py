#Python code to demonstrate working of pop() and popleft()
from collections import deque
de=deque([5,8,2,4,1,3,5])
de.pop()
print("The deque after deleting from right is : ")
print(de)
#deletes 5 from the left end of deque
de.popleft()
print("the deque after deleting from left is :")
print(de)
