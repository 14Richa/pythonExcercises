num = int(raw_input())

if num < 2:
	print "Micro Earthquake"
elif num > 2 and num < 3:
	print "Very Minor Earthquake"
elif num > 3 and num < 4:
	print "Minor Earthquake"
elif num > 4 and num < 5:
	print "Ligth Earthquake"
elif num > 5 and num < 6 :
	print "Moderate Earthquake"
elif num > 6 and num < 7:
	print "Strong Earthquake"
elif num > 7 and num < 8:
	print "Major Earthquake"
elif num > 8 and num < 10:
	print "Great Earthquake"
elif num >= 10:
	print "Meteoric Earthquake"