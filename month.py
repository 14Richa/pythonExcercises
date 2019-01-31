month = raw_input()

if month == "April" or month == "June" or month == "September" or month == "November":
	print "Days = 30"
elif month == "February":
	print "Days = 28 or 29"
else:
	print "Days = 31"
