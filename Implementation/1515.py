input_str = input()

n = 0

while True:
	n += 1

	num_str = str(n)
	while len(num_str) > 0 and len(input_str) > 0:
		if num_str[0] == input_str[0]:
			input_str = input_str[1:]
		num_str = num_str[1:]

	if input_str == '':
		print(n)
		break
