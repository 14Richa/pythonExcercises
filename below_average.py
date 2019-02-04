
array =[]
count = int(raw_input())


for i in range(0,count):
	num = int(raw_input())
	array.append(num)
avg = sum(array)/count
print ("Average is" ,avg)

#count = int(raw_input())


#for below average 

for num in array:
	if num < avg:
		print("Below average is", num)
