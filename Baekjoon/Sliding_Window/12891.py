S, P = map(int, input().split()) # 총 길이, 부분 길이
word = list(input())
A, C, G, T = map(int, input().split()) # 각 문자의 최소 포함 개수

def check_valid():
	if curr_dict['A'] < A:
		return False
	if curr_dict['C'] < C:
		return False
	if curr_dict['G'] < G:
		return False
	if curr_dict['T'] < T:
		return False
	return True

curr_dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
count = 0

for i in range(P): # 초기 윈도우
	curr_dict[word[i]] += 1
if check_valid() == True:
	count += 1

for i in range(P, S):
	curr_dict[word[i - P]] -= 1
	curr_dict[word[i]] += 1
	if check_valid() == True:
		count += 1

print(count)
