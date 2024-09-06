w_len, s_len = map(int, input().split()) # 단어 길이, 추출할 길이
W = list(input()) # 찾을 단어
S = list(input()) # 내용

W_dict = {}
S_dict = {}

for i in range(w_len):
	if W[i] in W_dict:
		W_dict[W[i]] += 1
	else:
		W_dict[W[i]] = 1

start = 0
count = 0

for i in range(s_len):
	if S[i] in S_dict:
		S_dict[S[i]] += 1
	else:
		S_dict[S[i]] = 1
	
	if i >= w_len - 1:
		if W_dict == S_dict:
			count += 1
		
		if S[start] in S_dict:
			S_dict[S[start]] -= 1
			if S_dict[S[start]] == 0:
				del S_dict[S[start]]
		start += 1

print(count)
