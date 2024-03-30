string = list(input())

stack = []
res = 0
temp = 1

for i in range(len(string)):
	if string[i] == '(':
		temp *= 2
		stack.append('(')
	
	elif string[i] == '[':
		temp *= 3
		stack.append('[')
	
	elif string[i] == ')':
		print(stack, i)
		if not stack or stack[-1] != '(':
			res = 0
			break
		elif string[i - 1] == '(':
			res += temp
		stack.pop()
		temp //= 2
	
	elif string[i] == ']':
		print(stack, i)
		if not stack or stack[-1] != '[':
			res = 0
			break
		elif string[i - 1] == '[':
			res += temp
		stack.pop()
		temp //= 3

if stack:
	print(0)
else:
	print(res)
