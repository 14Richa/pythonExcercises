# a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No"

str = raw_input()
if str=="yes" or str=="YES" or str=="Yes":
    print "Yes"
else:
    print "No"