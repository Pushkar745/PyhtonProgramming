list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1+list2
print(list3)
# Another way to join two list is by appending all the items from list 2 in list 1
for x in list2:
    list1.append(x)
print(list1)
# another method is extend()
list1.extend(list2)
print(list1)
