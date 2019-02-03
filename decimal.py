num = int(raw_input())
binary = ""
while num > 0:
	rem = num % 2
	binary += str(rem)
	num = num // 2

#reverse(binary)
binary = binary[::-1]
print binary