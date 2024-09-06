from collections import defaultdict
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
	W = list(input())
	K = int(input())

	alpha_dict = defaultdict(list) # {'문자': [등장인덱스1, 등장인덱스2, ...]}
	for i in range(len(W)):
		alpha_dict[W[i]].append(i)
	
	res = []
	for idx_list in alpha_dict.values():
		if len(idx_list) >= K:
			for i in range(len(idx_list) - K + 1):
				res.append(idx_list[i+K-1] - idx_list[i] + 1)
	
	if res:
		print(min(res), max(res))
	else:
		print(-1)
