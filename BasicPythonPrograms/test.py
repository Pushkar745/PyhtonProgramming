import random
a=range(1,20)
print(random.randrange(1,20))
for i in range(1,20):
    print(i) 
    for j in a:
        print(i+j,end=", ")