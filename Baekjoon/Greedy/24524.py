S = input()
T = input()

counter = [0] * len(T) # i번쨰까지 완성된 문자 개수

for s in S:
	if s in T:
		if s == T[0]:
			counter[0] += 1
		else: # 첫번쨰 문자가 아닐 경우
			idx = T.find(s) # 없을 경우 -1 리턴
			if idx != -1:
				if counter[idx - 1] > 0:
					counter[idx - 1] -= 1
					counter[idx] += 1

print(counter[-1])
