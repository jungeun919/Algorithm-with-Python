import sys

input = sys.stdin.readline

N, K = map(int, input().split())
num = input().rstrip()

stack = []
for i in num:
    while stack and K > 0:
        if i > stack[-1]:
            stack.pop()
            K -= 1
        else:
            break
    stack.append(i)

if K > 0:
    print(''.join(stack[:-K]))
else:
    print(''.join(stack))
