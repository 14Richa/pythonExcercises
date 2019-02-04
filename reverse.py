def Reverse(lst): 
    new_lst = lst[::-1] 
    return new_lst 
      
lst = raw_input().split(",")
print(Reverse(lst)) 