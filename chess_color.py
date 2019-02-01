str1 = raw_input()

if str1[0] == "a" or str1[0] == "c" or str1[0] == "e" or str1[0] == "g":
	start = "black"
else:
	start = "white"

if int(str1[1])%2 == 0:
	if start =="white":
		ans = "black"
	else: ans = "white"
else: ans = start


print ans