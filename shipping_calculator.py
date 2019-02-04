def order(num_item):
	if num_item > 0:
		charges = 10 + num_item * 2
	else:
		charges = 10 
	return charges 

num_item = int(raw_input())

calculator = order(num_item)


print ("Shipping charges is" , calculator)