year = int(raw_input())

if year % 400 == 0:
	isLeap = True
elif year % 100 == 0:
	isLeap = False
elif year % 4 == 0:
	isLeap = True
else: 
	isLeap = False

if isLeap:
	print(year, "is a leap year")
else:
	print(year, "is not a leap year")
