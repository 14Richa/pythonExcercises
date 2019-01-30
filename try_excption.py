
def addstring(str1, str2):
	try:
		return str1 + str2
	except:
		return "You sent a number"

str1 = raw_input();
str2 = raw_input();

print addstring(str1,str2)

print addstring(str1, int(str2))
