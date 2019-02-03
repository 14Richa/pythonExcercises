sentence = raw_input()
sentence = line.replace(" ", "")

is_palindrome = True

for i in range(0, len(sentence)):
	if sentence[i] != sentence[len(sentence) - i - 1]:
		is_palindrome = False
if is_palindrome:
	print(sentence, "is a palindrome")
else:
	print(sentence, "is not a palindrome")