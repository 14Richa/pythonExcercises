
def taxi_fare(distance):
	fare = (distance * 1000)/140 * 0.25 + 4
	return fare

distance = int(raw_input())

print taxi_fare(distance)