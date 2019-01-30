bankaccount = 0
while( True ):
	inp = raw_input().split(" ")
	if inp[0] == "D":
		bankaccount = bankaccount + int(inp[1])
	if inp[0] == "W":
		bankaccount = bankaccount - int(inp[1])
	if inp[0] == "Result":
		print bankaccount
		break
	