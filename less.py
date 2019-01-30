def collatz(num):
	if(num%2==0):
		print num//2
		return num//2
	else: 
		print 3*num+1
		return 3*num+1

num = int(raw_input())

while(num!=1):
	print(num)
	num = collatz(num)

print(num)