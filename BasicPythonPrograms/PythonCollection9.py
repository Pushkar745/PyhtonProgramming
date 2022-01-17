#Python code to demonstrate working of append (),appendleft()
from collections import deque
#initilizing deque
de=deque([1,2,3])
#Using append() to insert element at right end
#insert 4 at the end of deque
de.append(4)
#printing modified deque
print("The deque after appending at right is :")
print(de)
#Using appendleft() to insert element at right end 
#Insert 6 at the begining deque
de.appendleft(6)
