neg = []
zer = []
pos = []

line = raw_input()
while line != "":
	num = int(line)
	if num < 0:
		neg.append(num)
	elif num > 0:
		pos.append(num)
	else:
		zer.append(num)
	line = raw_input()

for x in neg:
	print(x)
for n in zer:
	print(n)
for n in pos:
	print(n)