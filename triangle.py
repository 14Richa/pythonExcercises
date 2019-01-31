s1 = int(raw_input())
s2 = int(raw_input())
s3 = int(raw_input())

if s1 == s2 and s2 == s3:
	print "Equilateral"
elif s1 == s2 or s2 == s3 or s3 == s1:
	print "Isoceles"
else:
	print "Scalene"