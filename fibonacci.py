#  Fibonacci Sequence

def feb(num):
    if num == 0: return 0
    elif num == 1: return 1
    else: return feb(num-1)+feb(num-2)

num=int(raw_input())
print feb(num)
