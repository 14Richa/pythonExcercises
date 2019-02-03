from math import sqrt 
def func(P1,P2):
	print P1
	ans = ((int(P1[0])-int(P2[0]))**2) + ((int(P1[1])-int(P2[1]))**2)
	return sqrt(ans)


listc = []
num = int(raw_input())
for i in range (num):
	coord = raw_input().split(",")
	listc.append(coord)
print(listc)

perimeter = 0
for i in range(0,num-1):
	side_length = func(listc[i], listc[i+1])
	perimeter += side_length
side_length = func(listc[0],listc[num-1])
perimeter += side_length

print perimeter
