# list comprehension, please write a program to print the list after removing the value 24

list = [12,24,35,24,88,120,155]
list = [x for x in list if x!=24]
print list