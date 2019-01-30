# a program which count and print the numbers of each character in a string
str = raw_input()
def char(str):
    dict = {}
    for i in str:
        keys = dict.keys()
        if i in keys:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict
print(char(str))