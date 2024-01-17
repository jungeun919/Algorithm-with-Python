str = input()

reverse_str = ""
idx = 0

while idx < len(str):
	if str[idx] == '<':
		start_idx = idx
		idx += 1
		while idx < len(str) and str[idx] != '>':
			idx += 1
		idx += 1
		reverse_str += str[start_idx:idx]
	
	elif str[idx].isalnum(): # 소문자 또는 숫자
		start_idx = idx
		while idx < len(str) and str[idx].isalnum():
			idx += 1
		reverse_word = (str[start_idx:idx])[::-1]
		reverse_str += reverse_word
	
	else: # 공백
		reverse_str += ' '
		idx += 1

print(reverse_str)
