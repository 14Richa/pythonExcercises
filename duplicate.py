#  a program to print this list after removing all duplicate values with original order reserved

def Remove(duplicate): 
    final = [] 
    for num in duplicate: 
        if num not in final: 
            final.append(num) 
    return final 
       
#duplicate = raw_input()
duplicate = [int(x) for x in raw_input().split(",")]
print(duplicate)
#print(duplicate)
print(Remove(duplicate))