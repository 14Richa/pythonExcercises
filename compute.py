

def func(num):
    if num==0:
        return 0
    else:
        return func(num-1)+100

num=int(raw_input())
print func(num)
