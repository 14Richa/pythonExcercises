grade = raw_input()
grade = grade.upper()



if grade == "A+" or grade == "A":
	grade_point = "A"
elif grade == "A-":
	grade_point = "A_minus"
elif grade == "B+":
	grade_point = "B_plus"
elif grade == "B":
	grade_point = "B"
elif grade == "B-":
	grade_point = "B_minus"
elif grade == "C+":
	grade_point = "C_plus"
elif grade == "C":
	grade_point = "C"
elif grade == "C-":
	grade_point = "C_minus"
elif grade == "D+":
	grade_point = "D_plus"
elif grade == "D":
	grade_point = "D"
elif grade == "F":
	grade_point == "F"
else:
	grade_point == "INVALID" 

if grade_point == "INVALID":
	print ("This is not a valid grade")
else:
	print (grade_point)



