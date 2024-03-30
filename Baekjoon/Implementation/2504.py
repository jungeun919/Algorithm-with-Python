bracket = list(input())

stack = []
res = 0
temp = 1

for i in range(len(bracket)):
	if bracket[i] == '(':
		stack.append('(')
		temp *= 2
		
	elif bracket[i] == '[':
		stack.append('[')
		temp *= 3
		
	elif bracket[i] == ')':
		if not stack or stack[-1] != '(':
			res = 0
			break
		elif bracket[i-1] == '(':
			res += temp
			print('(:', i, res, temp)
			print('stack:', stack)
		stack.pop()
		temp //= 2
	
	elif bracket[i] == ']':
		if not stack or stack[-1] != '[':
			res = 0
			break
		elif bracket[i-1] == '[':
			res += temp
			print('[:', i, res, temp)
			print('stack:', stack)
		stack.pop()
		temp //= 3

if stack:
	res = 0

print(res)
