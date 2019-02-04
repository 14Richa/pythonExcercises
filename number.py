

def main(num):
		if num == 1:
			s = 'st'
		elif num == 2:
			s = 'nd'
		elif num == 3:
			s = 'rd'
		else:
			s = 'th'
		return str(num) + s
    
num = int(raw_input())

print main(num)