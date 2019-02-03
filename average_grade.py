sum1 = 0
count = 0
while True:
	grade_point = raw_input()
	if grade_point == "":
		break
	sum1 += int(grade_point)
	count +=1
print (sum1/count)

