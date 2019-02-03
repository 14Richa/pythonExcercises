binary_num = raw_input()
power = 0
n = len(binary_num)
num = 0
for i in range (n-1, -1, -1):
	num += int(binary_num[i]) * 2 ** power
	power += 1
print num

