# a program that reads an integer from the user. Then your program should
#display a message indicating whether the integer is even or odd.

num = int(raw_input())


if num % 2 == 0:
	print "Number is even."
else: 
	print "Number is odd."