def length(sa,sb):
 	if len(sa) > len(sb):
 		return sa
 	else:
 	  	return sb	

s1 = raw_input()
s2 = raw_input()

print length(s1,s2)