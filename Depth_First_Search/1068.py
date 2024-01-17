import sys

input = sys.stdin.readline

n = int(input())
parent_node = list(map(int, input().split()))
del_node = int(input())

def dfs(del_node):
	parent_node[del_node] = -2

	for i in range(n):
		if parent_node[i] == del_node:
			dfs(i)

dfs(del_node)

count = 0
for i in range(n):
	if parent_node[i] != -2 and i not in parent_node:
		count += 1
print(count)
