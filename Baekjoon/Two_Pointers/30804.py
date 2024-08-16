N = int(input())
fruit = list(map(int, input().split()))

counter = [0] * 10
left, right = 0, 0
kind = 0
max_count = 0

while right < N:
	if counter[fruit[right]] == 0:
		kind += 1
	counter[fruit[right]] += 1
	right += 1

	if kind > 2:
		counter[fruit[left]] -=1
		if counter[fruit[left]] == 0:
			kind -= 1
		left += 1
	
	max_count = max(max_count, right - left)

print(max_count)
