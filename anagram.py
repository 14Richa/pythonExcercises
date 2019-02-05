def check(str1, str2):
	if(sorted(str1) == sorted(str2)):
		print("This string is anagram.")
	else:
		print("This string is not an anagram")
str1 = raw_input()
str2 = raw_input()
check(str1, str2)