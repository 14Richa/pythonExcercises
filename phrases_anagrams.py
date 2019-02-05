def check(str1, str2):
	if(sorted(str1) == sorted(str2)):
		print("This string is anagram.")
	else:
		print("This string is not an anagram")
str1 = "William Shakespeare"
str2 = "I am a weakish speller"
#s = ""
#t = ""
#s = s.join(str1)
#t = t.join(str2)
check(str1, str2)