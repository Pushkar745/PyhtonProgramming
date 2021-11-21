<<<<<<< HEAD
if __name__ == '__main__':
    n = int(input())
    for x in range(1,n):
     print(x,end='')
=======
import sys
a=10
b=10 
print(id(a))
print(id(b))
c=20
d=20
e=20
print(id(c))
print(id(d))
print(id(e))
print(sys.getrefcount(a))
print(sys.getrefcount(c))
>>>>>>> a9ec4dae7c3269e11808a40e56a50235c82881a0
