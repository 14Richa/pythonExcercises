

def month_day(month):
	if month == "January" or month == "May" or month == "March" or month == "July" or month == "August" or month == "October" or month == "December":
		return 31
	elif month == "September" or month == "April" or month == "June" or month == "November":
		return 30 
    #return month

month = raw_input()

a = month_day(month)
print a