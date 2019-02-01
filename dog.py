human_year = int(raw_input())
if human_year <= 2:
	dog_year = 10.5 * human_year
else:
	dog_year = 10.5*2 + 4 * (human_year-2)

print dog_year