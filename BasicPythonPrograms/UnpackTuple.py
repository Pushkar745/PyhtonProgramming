#when we cretae a tuple , we normally assign values to it this is called packing a tuple 
fruits=("apple","banana","cherry")
(green,yellow,red)= fruits 
print(green)
print(yellow)
print(red)
#The number of variable must match the number of values in tuple if not , you must use an asterisk to collect the remeaing value as a list
#Using Asterisk 
(green, yellow ,*red)=fruits
print(green)
print(yellow)
print(red)
