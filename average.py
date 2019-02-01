
count = 0
sum = 0
num = 1

while num != 0:
	num = int(raw_input())
	sum = sum + num
	count += 1
if count == 0: 
	print ("Error")
else:
	print ("Average is" , sum / (count))

